# Python code​​​​​​‌​‌‌​​​​‌​​​​​‌​​‌​‌​​​‌​ below
# Use print("messages...") to debug your solution.

show_expected_result = True
show_hints = True

import os
from os import path

def file_info():
    t_bytes = 0
    folder = "deps"
    files = os.listdir(folder)
    for i in files:
        if path.isfile(folder + "/" + i) and i.endswith(".txt"):
            filesize = path.getsize(folder + "/" + i)
            t_bytes += filesize
    return t_bytes
