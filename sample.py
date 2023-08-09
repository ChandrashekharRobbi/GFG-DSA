from IPython.display import Markdown
from IPython.core.getipython import get_ipython

def on_markdown_change(cell):
    print("Markdown content changed!")
    display(Markdown(cell.value))

for cell in get_ipython().notebook.cells:
    if cell.cell_type == 'markdown':
        cell.events.on_change(on_markdown_change)