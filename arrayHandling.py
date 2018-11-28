""" Short, one line description of the module ending with a period.
A longer description of the module with details that may help the user or anybody
reviewing the code later. make sure you outline in detail what the module does and how it can be used.
"""

__author__ = "Pedro oste"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "pedro.oste@education.nsw.com.au"
__status__ = "Prototype, Development or Production"


""" revision notes:


"""

#include statements
from mods import *

#other setup stuff


#now the real stuff we came here for
def main():
    newArray = []
    loadArray(newArray)
    printArrayContents(newArray)
    arraySum = sumArrayContents(newArray)
    
    anotherArray = ['a','b','c']
    loadArray(anotherArray)
    printArrayContents(anotherArray)
    

if __name__ == '__main__':
    main()    

        


    