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
    

