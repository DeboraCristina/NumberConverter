import pyperclip as pc
from sys import argv

if len(argv) >= 2:
    pc.copy(argv[1])
