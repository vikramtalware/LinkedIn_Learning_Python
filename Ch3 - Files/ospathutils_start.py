#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    print(os.name)
    
    # Check for item existence and type
    print("Item exists: ", path.exists("textfile.txt"))
    print("Is item a file: ", path.isfile("textfile.txt"))
    print("Is item a dir: ", path.isdir("textfile.txt"))
    
    # Work with file paths
    print("Item's Path: ", path.realpath("textfile.txt"))
    print("Item's Path and name: ", path.split(path.realpath("textfile.txt")))
    
    # Get the modification time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
    
    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been", td, "since the file was modified.")
    print("Or",td.total_seconds(),"seconds")

  
if __name__ == "__main__":
    main()