

from IPython.display import display, Javascript

z_val = []
from IPython.display import display, Javascript

def delete_cell():
    display(Javascript('''
        var cell_index = IPython.notebook.get_selected_index();
        var prev = cell_index - 1;
        IPython.notebook.focus_cell();
        console.log(prev);
        IPython.notebook.kernel.execute("prev = " + prev, 
                                         { iopub: { output: function(data) { console.log(data); }}});
        console.log(prev);
    '''))
    try:
        prev = get_ipython().user_ns['prev']
        print("Previous cell index:", prev)
        print(prev)
        z_val.append(prev)
        print(z_val)
    except KeyError:
        print("Failed to retrieve previous cell index")


def delete_all():
    for i in sorted(z_val, reverse=True):
        display(Javascript('''
            var cell_index = IPython.notebook.get_selected_index();
            var prev = cell_index - 1;
            IPython.notebook.delete_cell({});
            console.log("Cell deleted");
            IPython.notebook.kernel.execute("prev = " + prev, 
                                             {{ iopub: {{ output: function(data) {{ console.log(data); }}}}}});   
        '''.format(i)))
   
    print(len(z_val), "cells deleted")
    del z_val
