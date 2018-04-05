# LoaderThread
Just something to so save time when wanting to execute functions in the background.
<br/>
<br/>
loadQueue start's a new thread evey time 


```python

from UnmanagedExecutor import*
import time

def funcTime(delay):
    time.sleep(delay)
def funcPrint(text):
    print(text)

l = Executor()

l.execChain((funcTime, 10), (funcPrint, "Keyboard"))
l.execChain((funcTime, 1), (funcPrint, "Mouse"))
l.waitForAll()

```

# Example Use

```python
ue = UnmanagedExecutor()
ue.execChain( (updateMainCamera,), (updateSceneCamera, preferences) )
ue.execChain( (updatePhysics,), (updateSystem,) )
ue.waitForAll()

```
