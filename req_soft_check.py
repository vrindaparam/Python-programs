import os

def soft_check(filepath):
   
    if os.path.isfile(filepath):
        print("Required software is installed")
    else:
        print("Software is not installed")


filepath = input("Enter the filepath of the software")
#filepath = "/usr/bin/customapp"
soft_check(filepath)
