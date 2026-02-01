Answer 
Q1: By default are Django signals executed synchronously or asynchronously?
Answer: Yes Django signals are executed synchronously by default.
 the caller waits until the signal handler finishes before continuing.

Q2: Do Django signals run in the same thread as the caller?
Answer: Yes, by default signals run in the same thread as the caller.
The handler executes in the same thread context where the signal was sent.

Q3: By default do Django signals run in the same database transaction as the caller?
Answer: Yes, signals run in the same database transaction as the caller by default.
If the caller’s transaction is rolled back, any changes made inside the signal handler are also rolled back. the db transactions prevents from commiting incomplete transactions. 


RectangleQ2
     Rectangle.py file has the Custom Class in Python for getting the length and width  of rectangle. initialie the instane and iterate the obj. 


inside the sub folder there are:


sub
   RectangleQ2
     Rectangle.py
   accu
     accu - urls.py
     siggnal- app.py , views.py, signals.py, models.py
    db.sqlite3
    manage.py
