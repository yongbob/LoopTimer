import threading
import time

class LoopTimer(threading.Timer):
    '''Call a function after a specified number of seconds:
            t = LoopTimer(30.0, f, args=[], kwargs={})
            t.start()
            t.cancel()     # stop the timer's action if it's still waiting
    '''
    def __init__(self, interval, function, *args, **kwargs):
        threading.Timer.__init__(self,interval, function, args, kwargs)
        
    def run(self):
        while True:
            self.finished.wait(self.interval)
            if self.finished.is_set():
                self.finished.set()
                break
            self.function(*self.args, **self.kwargs)

if __name__ == '__main__': 
 
 
    def fun_timer(*args,**kwargs):
        print('The current number of threads is: %s' % threading.active_count())
        print('thread name:',threading.current_thread())
        print(*args)
    
    t1 = LoopTimer(2,fun_timer,'=== first timer')
    t1.start()
    time.sleep(5)
    t1.cancel()

    t2= LoopTimer(1,fun_timer,'~~~second timer')
    t2.start()
    time.sleep(5)
    t2.cancel()
    print("end")
