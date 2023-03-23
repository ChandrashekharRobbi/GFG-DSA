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
        print("Note that after executing new function your next cell will automatically converted to markdown cell :)")
        
    def delete_cell_prev(self):
        display(Javascript('''
            var cell_index = IPython.notebook.get_selected_index();
            var prev = cell_index - 1;
            IPython.notebook.delete_cell(prev);
        '''))
        
    def delete_cell_curr(self):
        display(Javascript('''
            var cell_index = IPython.notebook.get_selected_index();
            IPython.notebook.delete_cell(cell_index);
        '''))
        
    def to_markdown(self):
        display(Javascript('''
            IPython.notebook.insert_cell_below();
            IPython.notebook.to_markdown();
        '''))
        
    def new(self, s="default", h=4, delete=False):
        hash = "#"*h
        comment = f"1. [{s}](#{s.replace(' ','-')})"
        markdown = f"{hash} {s}"
        if comment not in self.arr:
            pypc.copy(markdown)
            self.arr.append(comment)
            print("Successfully added to the comment list")
        if delete:
            self.delete_cell_prev()
#             self.to_markdown()
#             time.sleep(1)
        else:
            print('It is already in the list')
            self.to_markdown()
#             time.sleep(1)
#             self.delete_cell_prev()
            
    def printArr(self):
        for i in self.arr:
            print(i) 
        time.sleep(5)
        self.delete_cell_curr()
            
    def removeLastelement(self):
        self.arr.pop() 
        time.sleep(3)
        self.delete_cell_prev()
        
    def removeByUsingIndex(self, x):
        self.arr.pop(x)
        time.sleep(3)
        self.delete_cell_prev()
        
    def makeNullArr(self):
        self.arr = []
        time.sleep(1)
        self.delete_cell_prev()
        
