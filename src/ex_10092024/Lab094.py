#file
import os

try:
    file=open("example.txt", "r")
    print(file.read())

except FileNotFoundError as fnfe:
    print("file not found, fix the path/create a file")

finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)