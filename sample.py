from IPython.display import display, Javascript

# Define an array to store references to executed cells
executed_cells = []

# Execute a cell and store its reference

    

from IPython.display import display, Javascript

def delete_cell():
    display(Javascript('''
        var cell_index = IPython.notebook.get_selected_index();
        var prev = cell_index - 1;
        IPython.notebook.delete_cell(cell_index);
        console.log("Cell deleted");
        IPython.notebook.kernel.execute("prev = " + prev);
    '''))
    prev = get_ipython().user_ns['prev']
    print("Previous cell index:", prev)

    
    
#     def delete_cell():
#     display(Javascript('''
#         var cell_index = IPython.notebook.get_selected_index();
#         var prev = cell_index - 1;
#         IPython.notebook.delete_cell(prev);
#     '''))