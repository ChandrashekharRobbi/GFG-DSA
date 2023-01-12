import pyperclip as pypc
def convertinotlink(s):
    print(s)
    print(f"7. [{s}](#{s.replace(' ','-')})")
    print(f"#### {s}")
    pypc.copy(f"#### {s}")
    
def linuxconvertinotlink(s):
    print(s)
    print(f"7. [{s}](#{s.replace(' ','-')})")
    print(f"#### {s}")
    # pypc.copy(f"#### {s}")
