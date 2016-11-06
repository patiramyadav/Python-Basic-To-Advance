'''
Created on Oct 27, 2016 4:59:47 PM

@author: Pati Ram Yadav

@Path: C:\JavaDev\Eclipse Mars.2 (4.5.2)\plugins\org.python.pydev_5.2.0.201608171824\pysrc\pydevd.py

@Module: new_vs_init.new_vs_init_method

'''
class A(object):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)
        
#         print("Inside the __new__ method", self, args, kwargs)
#         return "new"
    def __init__(self):
        pass
    def my_fxl(self):
        print("aasldf")
    
if __name__ == "__main__":
    a = A()
    a.my_fxl()
    print(a)
    b = A()
    b.my_fxl()
    print(b)
