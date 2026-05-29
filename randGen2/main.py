from os import listdir, path


Location = "../../../Downloads/" # Target
Files = list() # Files in Target
Name = None # Name
Extension = "" # Extension

Files = [path.splitext(x)[0] for x in listdir(Location) if path.isfile(path.join(Location, x))]
print(Files)
