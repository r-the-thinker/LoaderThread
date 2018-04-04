# LoaderThread
Just something to so save time when wanting to execute functions in the background.
<br/>
<br/>
loadQueue start's a new thread evey time 


```python

def func1():
  print("Func1")
def func2(name, age):
  print(name, "is", age, "years old.")
def funcTime(delay):
  time.sleep(delay)
  
 
loader = Loader()
loader.loadQueue((func1,), (func2, "Toasty", 20), (funcTime, 3))
loader.loadQueue((funcTime, 10))
 
loader.waitForAll()
 
print("Finished Loading All")

```
