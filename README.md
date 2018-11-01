# LoopTimer
Timer in threading package of Python is just one time timer.
This class LoopTimer is inherited from threading.Timer.
The run() function is modified. And will loop until cancel() is called.
Due to thread in Python can't be re-started, another thread should be started if you need a new timer.
Please refer to code.
