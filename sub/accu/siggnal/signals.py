import time
from threading import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Q1: Sync vs Async more time more delay in response of the sync and thread page
@receiver(post_save, sender=User)
def syncs(sender, instance, **kwargs):
    print("Signal start")
    time.sleep(8)# simulate long processing time
    print("Signal end")

# Q2: Same Thread
@receiver(post_save, sender=User)
def threads(sender, instance, **kwargs):
    print("Signal thread:", current_thread().name)
