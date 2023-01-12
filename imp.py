import pyperclip as pypc
def convertinotlink(s):
    desc = None
    print(s)
    print(f"7. [{s}](#{s.replace(' ','-')})")
    print(f"#### {s}")
    pypc.copy(f"#### {s}")