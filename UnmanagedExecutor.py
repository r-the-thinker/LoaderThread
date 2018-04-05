import threading


class UnmanagedExecutor:


    def __init__(self):
        self.activeThreads = []

    def execChain(self, *funcs_with_args):
        # Create The Thread, Start It And Add It To The List
        loaderThread = Executor.ExecutorThread(list(funcs_with_args))
        loaderThread.start()
        self.activeThreads.append(loaderThread)

    def waitForAll(self):

        # Waits Until Everyone is finished
        for activeThread in self.activeThreads:
            activeThread.join()

    def isFinished(self):
        for activeThread in self.activeThreads:
            if activeThread.isAlive():
                return False
        return True

    class ExecutorThread(threading.Thread):

        def __init__(self, funcsWithArgs):
            threading.Thread.__init__(self)
            self.funcsWithArgs = funcsWithArgs

        def run(self):
            # nameOfFunc, Param1, Param2, ..., ParamN
            while not len(self.funcsWithArgs) == 0:
                functionWithArgs = self.funcsWithArgs.pop(0)
                functionWithArgs[0](*functionWithArgs[1:])
