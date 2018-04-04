import threading


class Loader:


    def __init__(self):
        self.activeThreads = []

    def loadQueue(self, *funcs_with_args):
        # Create The Thread, Start It And Add It To The List
        loaderThread = Loader.LThread(funcs_with_args)
        loaderThread.start()
        self.activeThreads.append(loaderThread)

    def waitForAll(self):
        for activeThread in self.activeThreads:
            activeThread.join()


    class LThread(threading.Thread):

        def __init__(self, funcsWithArgs):
            threading.Thread.__init__(self)
            self.funcsWithArgs = funcsWithArgs

        def run(self):
            # nameOfFunc, Param1, Param2, ..., ParamN
            for functionWithArgs in self.funcsWithArgs:
                functionWithArgs[0](*functionWithArgs[1:])
