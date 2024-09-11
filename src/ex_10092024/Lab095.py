import os
from os import listdir

print(os.name)
print(os.getcwd())
os.chdir(r"C:\Users\win10\PycharmProjects\pythonProject_pyATB4x\src")
print(os.getcwd())


for file in os.listdir("."):
    print(file)

# os.rmdir("new_dir")
# os.rmdir("new_dirt")

full_path=os.path.join(r"C:\Users\win10\PycharmProjects\pythonProject_pyATB4x\src\ex_10092024", "example.txt")
print(full_path)

print(os.path.exists("example.txt"))


