from django.http import *
from django.contrib.auth.models import User
import threading
from django.db import *
import time

''' Q1 Is this Async or Sync signal . It will call the signal synchronously
signals are synchrnous by default this
function creates a new user every time on the sync route
'''
def sync(request):
    print("Caller before create")
    User.objects.create(username=f"sync_{int(time.time())}")
    print("Caller after create")
    return HttpResponse(f"Sync proof {int(time.time())}")

# Q2 trigger
'''calls the signal in the same thread as caller thread
 trigger thefunctions syncs and threads  prints the thread current number'''
def thread(request):
    print("Caller thread:", threading.current_thread().name)
    User.objects.create(username=f"thread_{int(time.time())}")
    return HttpResponse(f"Thread proof threading.current_thread().name: {threading.current_thread().name}")

# Q3: Same Transaction
def roll(request):
    try:
        with transaction.atomic():
            User.objects.create(username=f"user_{int(time.time())}")
            raise Exception("Rollback")
    except:
        pass
    return HttpResponse("Rolled back, not saved time or user  now is because of integrity of user authentication unique constaraint " + str(int(time.time())))
