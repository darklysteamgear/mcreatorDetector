#By Darkly Steamgear
#08/09/2023
import math
#This is a basic script that will search through a given directory for mcreator mods. it uses python's zipfile mods to pythonically search for these mods.
import zipfile
import os
from fnmatch import fnmatch

#Globals, saves all mod names to an array called mcreatorMods
CREATOR_DIR = "net/mcreator"
mcreatorMods = []
possibleMcreatorModsprob = []
possibleMcreatorMods = []
mostCharsA = 28
mostCharsB = 41


#The main method of the script that searches through all of the mods in the user specified folder
def find_mcreator_mods(moddir):
    global mostCharsA
    global mostCharsB
    print("\n----------------------------LOG----------------------------")
    for file in os.listdir(moddir):
        isdefinetlymcreator = False
        isprobablymcreator = False
        os.chdir(moddir)
        if fnmatch(file, "*.jar"):
            jarfile = zipfile.ZipFile(file, "r")
            prob = 0
            isdefinetlymcreator = any(mdir.startswith(CREATOR_DIR.rstrip("/")) for mdir in jarfile.namelist())
            if not isdefinetlymcreator:
                for mdir in jarfile.namelist():
                    if mdir.find("Elements") and mdir.find("ModElement") >= 1:
                        prob += 1
                        print("Possible mcreator class found in modfile: " + file + " class: " + mdir)
                    if mdir.find("Variables$") >= 1:
                        prob += 1
                        print("Possible mcreator class found in modfile: " + file + " class: " + mdir)
            if prob >= 3:
                isprobablymcreator = True
            jarfile.close()
            if isdefinetlymcreator:
                mcreatorMods.append(file)
                mostCharsA = len(file) if mostCharsA < len(file) else mostCharsA
                print("mcreator mod found: " + file)
            elif isprobablymcreator:
                possibleMcreatorMods.append(file)
                mostCharsB = len(file) if mostCharsB < len(file) else mostCharsB
                possibleMcreatorModsprob.append(prob/6.10)
                print("possible mcreator mod found: " + file)
    print("-----------------------------------------------------------\n")
    if not mcreatorMods and not possibleMcreatorMods:
        print("FINAL VERDICT:")
        print("No MCreator mods found, you are certified free of MCreator lag :D")
        return
    else:
        mostChars = mostCharsB if mostCharsA < mostCharsB else mostCharsA
        print(find_whitespace(int(mostChars / 2) - 2, "equal") + "RESULTS" + find_whitespace(
            int(mostChars / 2) - 3, "equal"))
        if mcreatorMods:
            print("+" + find_whitespace(mostCharsA, "line") + "+")
            print("|Mods 100% made with MCreator" + find_whitespace(mostCharsA-28,"empty")+"|\n"
                  "|" + find_whitespace(mostCharsA,"plus") + "|")
            i = 0
            for stupidmod in mcreatorMods:
                stupidsize = len(stupidmod) + 4
                print("| " +str(i + 1) + ") " +stupidmod + find_whitespace(mostCharsA-stupidsize,"empty")+"|")
                i=+1
            print("|" + find_whitespace(mostCharsA, "line") + "|\n")
            print("+" + find_whitespace(mostCharsB, "line") + "+")
        if possibleMcreatorMods:
            print("|Mods that are probably made with MCreator" + find_whitespace(mostCharsB-41,"empty") + "|\n"
                  "|" + find_whitespace(mostCharsB,"line") + "|")
            i = 0
            for stupidmod in possibleMcreatorMods:
                stupidsize = len(stupidmod) + 4
                print ("| " + str(i + 1) + ") " + stupidmod + find_whitespace(mostCharsB-stupidsize,"empty") + "| CHANCE: "+str(round(possibleMcreatorModsprob[i] * 100)) + "%")
                i=+ 1
            print("+" + find_whitespace(mostCharsB,"line") + "+\n")
            print("TOTAL OF " +str(len(possibleMcreatorMods) + len(mcreatorMods)) +  " POSSIBLE MCREATOR MODS\n")
            print("FINAL VERDICT:")
            if len(possibleMcreatorMods) + len(mcreatorMods) >= 16:
                print("You really need to rethink your life choices. That's just, A LOT OF MCREATOR MODS. stop it. get some help. Nobody is going to want to play this PC killer. https://www.youtube.com/watch?v=l60MnDJklnM")
            elif 8 < (len(possibleMcreatorMods) + len(mcreatorMods)) <= 15:
                print("Make sure to read the descriptions and comments on the mods you are adding. You have too many MCreator mods installed, and you will have preformance issues.")
            elif 3 < (len(possibleMcreatorMods) + len(mcreatorMods)) <= 8:
                print("That's quite a few potential MCreator mods. Think about what you want to remove.")
            elif 1 < (len(possibleMcreatorMods) + len(mcreatorMods)) <= 3:
                print("You have a few potential MCreator mods. please note that they more often then not cause preformance issues.")
            elif (len(possibleMcreatorMods) + len(mcreatorMods)) == 1:
                print("You have one MCreator mod. It may be the sole cause of your preformance issues. Try to remove it if you are having issues.")


        print("=" + find_whitespace(mostChars, "equal") + "=\n")

def find_whitespace(whitespace, type):
    result = ""
    if type == "line":
        for i in range(0,whitespace):
            result += "-"
    elif type == "empty":
        for i in range(0,whitespace):
            result += " "
    elif type == "plus":
        for i in range(0,whitespace):
            result += "+"
    elif type == "equal":
        for i in range(0,whitespace):
            result += "="
    return result

if __name__ == "__main__":
    directory = input("Please specify the directory you want to search for mcreator mods in: ")
    find_mcreator_mods(directory)
