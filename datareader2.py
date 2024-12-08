sys.path.append('/home/alku8270/Documents/ASTR 340/astr3400/py_mesa_reader')
import mesa_reader as m

class datareader:
    
    def __init__(self,path):
        self.path=path
        
    def get_data(self,lognum):
        if lognum==0:
            logsZAMS=m.MesaData(file_name=self.path+f'LOGS/history.data')
            
        else:
            logsZAMS=m.MesaData(file_name=self.path+f'LOGS/profile{lognum}.data')
            
        return logsZAMS
    
    def plot_data(self,var1,var2,plt_typ,lognum=1):
        '''
        This function does all the plotting and data gathering.
        
        Inputs:
        **ALL MUST BE IN STRINGS**
        var1=x variable
        var2=y variable
        plt_typ=type of plot (normal,loglog,semilogx,semilogy)
        lognum= which log files you wish to use (use 0 for history file)
        
        Example:
        plot_data('zone','logT','normal',lognum=2)
        logZAMS=self.get_data(lognum)
        '''
        
        logsZAMS=self.get_data(lognum)
        
        if data_typ=='individual':
            x=logsZAMS.data(var1)
            y=logsZAMS.data(var2)
            
            if plt_typ=='normal':
                plt.plot(x,y)
                plt.xlabel(var1)
                plt.ylabel(var2)
            
            elif plt_typ=='loglog':
                plt.loglog(x,y)
                plt.xlabel(var1)
                plt.ylabel(var2)
            
            elif plt_typ=='semilogx':
                plt.semilogx(x,y)
                plt.xlabel(var1)
                plt.ylabel(var2)
        
            elif plt_typ=='semilogy':
                plt.semilogy(x,y)
                plt.xlabel(var1)
                plt.ylabel(var2)
                
            else:
                print('Unsupported plot type')
            