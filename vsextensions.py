import os

# this script deletes obsolete vscode extensions. Tested on Ubuntu. Just put copy this file into home/.vscode/extensions
# then run it as root (sudo su && python3 vsextensions.py) and it will remove irrelevant vscode extensions. 
# my vscode wasn't deleting the old extensions. And I did not have time to delete individual ones.
# good luck

def Convert(string): 
    # function to turn a string to a list
    li = list(string.split(",")) 
    return li 
def deleteitems(itemlist):
    # function to iterate over the items in the items passed as parameters 
    # and delete them
    for item in itemlist:
        os.system('sudo rm -r {}'.format(item))
       
def openfilecontents(nameoffile):
    # this function opens the file you want and reads it. In my case it is .obsolete which has a dictionary
    # of the folders that are obsolete
    f= open(nameoffile,"r")
    if f.mode == 'r':
        contents =f.read()
        mydict=contents
        # replacing
        mydict=contents.replace(':true','').replace('{','').replace('}','').replace('"','')
    f.close()
    return mydict
def main():
    
    myItemList=openfilecontents('.obsolete')
    finaldict=Convert(myItemList)
    deleteitems(finaldict)
    
if __name__=='__main__':
    main()
