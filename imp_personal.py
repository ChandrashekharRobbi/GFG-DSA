import pyperclip as pypc
from IPython.display import display, Javascript
import time
class MyFunction:
    '''
    This function is generated by Chandrashekhar Robbi
    This function can create the markdown and comment by justing entering your message by calling new function
    It has also additional features like as you enter the message and run the cell the comment is automatically gets copied in your clipboard
    the default value for comment is 4 i.e 4*#
    You can change the value by taking whatever number you want
    it has functions like 
    new(string) -> For creating new comment, markdown
    printArr() -> to print the content of the arr
    removeLastelement() -> remove the last element from the list
    removeByUsingIndex(x) -> remove by using index
    makeNullArr() -> to make empty list
    '''
    def __init__(self):
        self.arr = []
        print("I am changed")
        
    def delete_cell(self):
        display(Javascript('''
            var cell_index = LastCell.prev_cell;
            IPython.notebook.delete_cell(cell_index);
        '''))
        
    def new(self, s, h=4):
        hash = "#"*h
        comment = f"1. [{s}](#{s.replace(' ','-')})"
        markdown = f"{hash} {s}"
        if comment not in self.arr:
            pypc.copy(markdown)
            self.arr.append(comment)
            print("Successfully added to the comment list")
            time.sleep(5)
            self.delete_cell()
        else:
            print('It is already in the list')
            
    def printArr(self):
        for i in self.arr:
            print(i)  
            
    def removeLastelement(self):
        self.arr.pop()  
        
    def removeByUsingIndex(self, x):
        self.arr.pop(x)
        
    def makeNullArr(self):
        self.arr = []
        
