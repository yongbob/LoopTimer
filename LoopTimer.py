import threading
import time
count = 0
class LoopTimer(threading.Timer):
    '''Call a function after a specified number of seconds:
            t = LoopTimer(30.0, f, args=[], kwargs={})
            t.start()
            t.cancel()     # stop the timer's action if it's still waiting
    '''
    def __init__(self, interval, function, *args, **kwargs):
        threading.Timer.__init__(self,interval, function, args, kwargs)
        self.start_time=time.time()
        self.__resume = threading.Event()
        self.__resume.set()
        
    def pause(self):
        self.__resume.clear()
    
    def resume(self):
        self.__resume.set()
    def stop(self):
        self.__resume.set()
        super().cancel()
        
    def run(self):
        while True:
            print("timer: ",time.time()-self.start_time)
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)
            global count
            count =count + 1
            print(count)
            if not self.__resume.is_set():
                self.__resume.wait()
            if self.finished.is_set():
                self.finished.set()
                break

   
if __name__ == '__main__': 
 
    def sayhello(a):
        print("hello: "+str(a))

    def fun_timer(*args,**kwargs):
        for each in args[0]:
            sayhello(each)
              
  
    seed1=[]
    for i in range(3):
        seed1.append(i)
        
    t1 = LoopTimer(1,fun_timer,seed1)
    t1.start()
    
    time.sleep(5)
    print("pause=====")
    t1.pause()
    time.sleep(3)
    print("resume===")
    t1.resume()
    time.sleep(5)
    t1.stop()
    
    
    print("end")
 

