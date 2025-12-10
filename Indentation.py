#    INDENTATION

"""In Python, Indentation is used to define blocks of code. It tells the Python interpreter that a group of statements belongs to a specific block. 
All statements with the same level of indentation are considered part of the same block. 
Indentation is achieved using whitespace (spaces or tabs) at the beginning of each line. The most common convention is to use 4 spaces or a tab, per level of indentation.
"""

print("I have no Indentation ")
    print("I have tab Indentation ")



"""first print statement has no indentation, so it is correctly executed.
second print statement has tab indentation, but it doesn't belong to a new block of code. 
Python expects the indentation level to be consistent within the same block. This inconsistency causes an IndentationError.
"""
