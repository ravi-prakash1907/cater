## importing modules
from shareBox import server as sender
from shareBox import client as receiver

######################

class cater():
    def __init__(self, menuOption=""):
        ###
        self.__mainMenu = "\n Menu\n"+"-"*6+"\n\n1. Send Files! \n2. Receive Files!"+menuOption
        self.choice = self.__menu__()
    
    ## main menu
    def __menu__(self):
        print(self.__mainMenu)
        ch = input("\nEnter your choice: ")    
        return ch

    ## mainApp
    def cater(self):
        ## making host to share files
        if self.choice == '1':
            Sender = sender.server()
            print("\n"+"-"*20+"\n")
            Sender.server()
            return True
        ## making client to get files
        elif self.choice == '2':
            Receiver = receiver.client()
            print("\n"+"-"*20+"\n")
            Receiver.client()
            return True
        ## invalid input
        else:
            print("\n"+"-"*20+"\n")
            return False
        
        ## if ran at least once
        flag = False

######################
def app():
    flag = True
    firstRun = True
    addOnMenu = ''

    while flag:
        ## creating an instance
        caterApp = cater(addOnMenu)
        ## sharing the files
        flag = caterApp.cater()

        ## adding exit choice in menu
        if flag and firstRun:
            firstRun = False
        if firstRun is False:
            addOnMenu = "\n*  Any other key to exit!!"
        
        ## deleting current instence on Secreat Share App
        del(caterApp)
    
    ## exit prompt
    if firstRun:
        print("\nSomething went wrong!!\nApp terminated unexpectedly!!")
    else:
        print("\nThanks for using 'cater'!\n")
