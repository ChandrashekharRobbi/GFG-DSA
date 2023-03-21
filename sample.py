from IPython.display import display, Javascript

# Define an array to store references to executed cells
executed_cells = []

# Execute a cell and store its reference
def execute_cell(index):
    display(Javascript('IPython.notebook.execute_cells([' + str(index) + '])'))
    cell = get_ipython().user_ns['_']
    executed_cells.append(cell)

# Delete all executed cells
def delete_executed_cells():
    for cell in executed_cells:
        cell.parent.delete_cell(cell.index)
    # Clear the array of executed cells
    executed_cells = []
    

def delete_cell():
    display(Javascript('''
        var cell_index = IPython.notebook.get_selected_index();
        var prev = cell_index - 1;
        IPython.notebook.select(prev);
        
        console.log("yeah it is update");
        IPython.notebook.kernel.execute("prev = " + prev);
    '''))
    prev = get_ipython().user_ns['prev']
    print(f"The previous cell index was {prev}.")
    
    
#     def delete_cell():
#     display(Javascript('''
#         var cell_index = IPython.notebook.get_selected_index();
#         var prev = cell_index - 1;
#         IPython.notebook.delete_cell(prev);
#     '''))