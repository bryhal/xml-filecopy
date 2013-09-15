import win32service
import win32serviceutil
import win32event

class PySvc(win32serviceutil.ServiceFramework):
    # you can NET START/STOP the service by the following name
    _svc_name_ = "xml_file_copy"
    # this text shows up as the service name in the Service
    # Control Manager (SCM)
    _svc_display_name_ = "OLP - OPS File copier"
    # this text shows up as the description in the SCM
    _svc_description_ = "Copies PDF files from OPS to OLP servers"
    
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        # create an event to listen for stop requests on
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
    
    # core logic of the service   
    def SvcDoRun(self):
        import servicemanager
        
        f = open('test.dat', 'w+')
        rc = None
        
        # if the stop event hasn't been fired keep looping
        while rc != win32event.WAIT_OBJECT_0:
            #f.write('TEST DATA\n') # example
            #f.flush() # example
            
            ###### stuff we want to do here ##################
            
            
            
            ##################################################
            
            # block for 5 seconds and listen for a stop event
            rc = win32event.WaitForSingleObject(self.hWaitStop, 5000)
            
        #f.write('SHUTTING DOWN\n') # example
        #f.close() #example
    
    # called when we're being shut down    
    def SvcStop(self):
        # tell the SCM we're shutting down
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # fire the stop event
        win32event.SetEvent(self.hWaitStop)
        
if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PySvc)
