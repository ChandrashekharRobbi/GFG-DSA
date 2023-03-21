

from IPython.display import display, Javascript

def delete_cell():
    display(Javascript('''
        var cell_index = IPython.notebook.get_selected_index();
        var prev = cell_index - 1;
        console.log("Cell deleted");
        IPython.notebook.kernel.execute("prev = " + prev, 
                                         { iopub: { output: function(data) { console.log(data); }}});   
    '''))
    try:
        prev = get_ipython().user_ns['prev']
        time.sleep(10)
        print("Previous cell index:", prev)
    except KeyError:
        print("Failed to retrieve previous cell index")


# def delete_cell():
#     display(Javascript('''
#         var cell_index = IPython.notebook.get_selected_index();
#         var prev = cell_index - 1;
#         IPython.notebook.delete_cell(cell_index);
#         console.log("Cell deleted");
#         IPython.notebook.kernel.execute("prev = " + prev, 
#                                          { iopub: { output: function(data) { console.log(data); }}});   
#     '''))
#     try:
#         prev = get_ipython().user_ns['prev']
#         time.sleep(10)
#         print("Previous cell index:", prev)
#     except KeyError:
#         print("Failed to retrieve previous cell index")