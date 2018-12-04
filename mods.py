""" Modules of Standard algorithm functions for the SDD course.

This script will contain functions to all of the standard
algorithims listed in the course specs for the HSC SDD course.
"""

__author__ = "Pedro Oste"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "pedro.oste@education.nsw.com.au"
__status__ = "Prototype, Development or Production"

""" revision notes:


"""

#include statements



def loadArray(thisArray):
    """appeneds data into an array.
        
        prompt the user to add data to the existing array
    
    Args:
        thisArray: the array to which the data will be added
    Returns:
        the modified array
    Raises:
        none
    """
    outArray = thisArray[:]
    value = input("please entere some data or enter 'xxx' to quit ")
    
    while value != 'xxx':
        outArray.append(value)
        value = input("please entere some data or enter 'xxx' to quit ")
    print("there are now {} items loaded into the array".format(len(thisArray)))
    return outArray
    


def printArrayContents(thisArray):
    """prints the contents within the array

    a much longer description of the really amazing stuff this function does and how it does it.

    Args:
        thisArray: the array to be printed
        
    Returns:
        none        
    Raises:
        none        
        """
    i = 0 #start at zero in python
    while i < len(thisArray):
        print(thisArray[i], end = ' ')
        i = i + 1
    print(' ')



def sumArrayContents(thisArray):
    """Sums the contents of the array

    Args:
        thisArray: The array that the contents will be added together        arg2: the second argument required by the function.
        
    Returns:
        total: sum of the array

    Raises:
        TypeError.
    """
    i = 0
    total = 0
    while i < len(thisArray):
        try: 
            total = total + eval(thisArray[i])
            i = i + 1
            
        except TypeError:
            print("you a dummie")
            total = None
            
    print("the sum of the array is {}".format(total))
    return total
    

def findMax(thisArray):
    """Finds the maximum within the array.

    Based off the psuedocode boi.

    Args:
        thisArray: this is the array that will be used to find the maximum
    Returns:
        the maximum and where to find the maximum within the array.

    Raises:
        
    """
    maxIndex = 1
    i = 1
    max = ''
    while i < len(thisArray):
        if thisArray[i] > max:
            max = thisArray[i]
            maxIndex = i
        i = i + 1
    print('The highest value is {} at position {}'.format(max,maxIndex))
    pass










class SampleClass(object):
    """Summary of class here.

    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""





#copy
def function_name(arg1, arg2, other_silly_variable=None):
    """Does something amazing.

    a much longer description of the really amazing stuff this function does and how it does it.

    Args:
        arg1: the first argument required by the function.
        arg2: the second argument required by the function.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        description of the stuff that is returned by the function.

    Raises:
        AnError: An error occurred running this function.
    """
    pass

