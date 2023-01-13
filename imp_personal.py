import pyperclip as pypc
import time
def convertinotlink(s):
    print(s)
    comment = f"7. [{s}](#{s.replace(' ','-')})"
    markdown = f"#### {s}"
    print(comment)
    print(markdown)
    
    pypc.copy(comment)
    
    time.sleep(0.5)
    pypc.copy(f"#### {s}")
    
def linuxconvertinotlink(s):
    print(s)
    print(f"7. [{s}](#{s.replace(' ','-')})")
    print(f"#### {s}")

