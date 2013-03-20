'''
Created on 2012-11-8

@author: huangchong
'''
from apscheduler.scheduler import Scheduler
import datetime
import logging 
'''
    Singleton
'''
class JzScheduler(Scheduler): 
    
    def __init__(self):
        Scheduler.__init__(self, daemonic=False)
        
    
    @staticmethod  
    def instance():    
        if not hasattr(JzScheduler, "_instance"):  
            with JzScheduler._instance_lock:  
                if not hasattr(JzScheduler, "_instance"):  
                    # New instance after double check  
                    JzScheduler._instance = JzScheduler()  
        return JzScheduler._instance  
  
    @staticmethod  
    def initialized():  
        """Returns true if the singleton instance has been created."""  
        return hasattr(JzScheduler, "_instance") 
    

    
# def job_function():    
#     print " [x] Requesting"
#     print 'set_bandwidth_job start at ', datetime.datetime.now()
# 
# def job_function2():    
#     print " [x] Requesting 2"
#     print 'set_bandwidth_job start at ', datetime.datetime.now()
#     
# if __name__ == '__main__':
#     sche = JzScheduler()
#     sche.add_interval_job(job_function,seconds=0)
#     sche.start()
#         
#         
# @sche.interval_schedule(seconds=1)
# def bandwidth_job():
#         job_function()         
        
        