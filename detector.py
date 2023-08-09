#By Darkly Steamgear
#08/09/2023

#This is a basic script that will search through a given directory for mcreator mods. it uses python's zipfile mods to pythonically search for these mods.
import zipfile
import os
from fnmatch import fnmatch

#Globals, saves all mod names to an array called mcreatorMods
CREATOR_DIR = "net/mcreator"
mcreatorMods = []

#The main method of the script that searches through all of the mods in the user specified folder
def find_mcreator_mods(moddir):
    for file in os.listdir(moddir):
        os.chdir(moddir)
        if fnmatch(file, "*.jar"):
            jarfile = zipfile.ZipFile(file, "r")
            ismcreator = any(mdir.startswith(CREATOR_DIR.rstrip("/")) for mdir in jarfile.namelist())
            jarfile.close()
            if ismcreator:
                mcreatorMods.append(file)
                print("mcreator mod found: " + file)

if __name__ == "__main__":
    directory = input("Please specify the directory you want to search for mcreator mods in: ")
    find_mcreator_mods(directory)
