#By Darkly Steamgear
#08/09/2023
import math
#This is a basic script that will search through a given directory for mcreator mods. it uses python's zipfile mods to pythonically search for these mods.
import zipfile
import os
from fnmatch import fnmatch
import webbrowser

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
    #Search for every file in the mods folder directory
    for file in os.listdir(moddir):
        #Booleans instantiated to be set later on in the code for determining MCreator status
        isdefinetlymcreator = False
        isprobablymcreator = False
        #Change the directory to the mod directory for easier file manipulation
        os.chdir(moddir)
        #Checks if the file it is currently looking at is a jar file
        if fnmatch(file, "*.jar"):
            #Instantiate loacal variables within this section of the function
            jarfile = zipfile.ZipFile(file, "r")
            prob = 0
            #Checks through for any directory with net/mcreator inside of the jar file.
            isdefinetlymcreator = any(mdir.startswith(CREATOR_DIR.rstrip("/")) for mdir in jarfile.namelist())
            #If it is not 100% MCreator mod, begin looping through and checking for certain cases that all
            #mods made with MCreator have. You can't hide from this tool
            if not isdefinetlymcreator:
                for mdir in jarfile.namelist():
                    #In the case where a mod has a class named mcreator, but not the net/mcreator directory.
                    if mdir.find("mcreator") >= 1:
                        prob = prob + 10
                        isdefinetlymcreator = True
                        break
                    #ModElement, Element, Variables$ are known classnames of MCreator mods, which will be flagged
                    #And given points to the probability score for a mod to be made with MCreator
                    #Since there are some mods that are not made with mcreator
                    #That may have these class names
                    #A mod needs 3 points before it is considered possibly mcreator
                    #Since MCreator mods have 6 classes with the above stated names.
                    if mdir.find("Elements") and mdir.find("ModElement") >= 1:
                        prob = prob + 1
                        print("Possible mcreator class found in modfile: " + file + " class: " + mdir)
                    if mdir.find("Variables$") >= 1:
                        prob = prob + 1
                        print("Possible mcreator class found in modfile: " + file + " class: " + mdir)
            if prob >= 3:
                isprobablymcreator = True
            if prob >= 7:
                isdefinetlymcreator = True
            jarfile.close()
            #If it is a definite MCreator mod, add it to the list of mcreator mods, and print it to the console.
            if isdefinetlymcreator:
                mcreatorMods.append(file)
                #This line is for the basic fancy console GUI I have created. basically for caluculating where the lines should go
                #To make the boxes neat
                mostCharsA = len(file) if mostCharsA < len(file) else mostCharsA
                print("MCreator mod found: " + file)
            # Else if it is probably an mcreator mod, create a probability and append the file to the possible list
            elif isprobablymcreator:
                possibleMcreatorMods.append(file)
                #This line is for the basic fancy console GUI I have created. basically for caluculating where the lines should go
                #To make the boxes neat
                mostCharsB = len(file) if mostCharsB < len(file) else mostCharsB
                possibleMcreatorModsprob.append(prob/6.10)
                print("possible mcreator mod found: " + file)
    print("-----------------------------------------------------------\n")
    #If there are no flagged mods, YOU BALLIN!!!
    if not mcreatorMods and not possibleMcreatorMods:
        print("FINAL VERDICT:")
        print("No MCreator mods found, you are certified free of MCreator lag :D")
        webbrowser.open("https://youtu.be/UeFTkveHajE?t=18")
        return
    else:
        #Sets the number of characters that the boxes for the console GUI should have.
        mostChars = mostCharsB if mostCharsA < mostCharsB else mostCharsA
        #This finds the whitespace for the console GUI to make it look neater
        print(find_whitespace(int(mostChars / 2) + 2, "equal") + "RESULTS" + find_whitespace(
            int(mostChars / 2) + 3, "equal"))
        #Console GUI output to show you all definitive mcreator mods
        if mcreatorMods:
            print("+" + find_whitespace(mostCharsA+5, "line") + "+")
            print("|Mods 100% made with MCreator" + find_whitespace(mostCharsA-28+5,"empty")+"|\n"
                  "|" + find_whitespace(mostCharsA+5,"plus") + "|")
            i = 0
            #For every mod that is a stupid mcreator mod, print them out and add the appropriate character
            #To make a neat looking console GUI
            for stupidmod in mcreatorMods:
                number = i + 1
                subtractor = len(str(number))
                stupidsize = len(stupidmod) - 2 + subtractor
                print("| " +str(number) + ") " +stupidmod + find_whitespace(mostCharsA-stupidsize,"empty")+"|")
                i=i+1
            print("+" + find_whitespace(mostCharsA+5, "line") + "+\n")
            print("+" + find_whitespace(mostCharsB+5, "line") + "+")
        #Console GUI output to show you all possible mcreator mods with their probabilities for being mcreator
        if possibleMcreatorMods:
            print("|Mods that are probably made with MCreator" + find_whitespace(mostCharsB-41+5,"empty") + "|\n"
                  "|" + find_whitespace(mostCharsB+5,"line") + "|")
            i = 0
            #For every mod that is a stupid possible mcreator mod, print them out and add the appropriate character
            #To make a neat looking console GUI
            for stupidmod in possibleMcreatorMods:
                number = i+1
                subtractor = len(str(number - 1))
                stupidsize = len(stupidmod) -2 + subtractor
                print ("| " + str(number) + ") " + stupidmod + find_whitespace(mostCharsB-stupidsize,"empty") + "| CHANCE: "+str(round(possibleMcreatorModsprob[i] * 100)) + "%")
                i=i+ 1
            print("+" + find_whitespace(mostCharsB+5,"line") + "+\n")
        #Final verdict statements. these will determine the fate of your modpack and judge you accordingly.
        print("TOTAL OF " +str(len(possibleMcreatorMods) + len(mcreatorMods)) +  " POSSIBLE MCREATOR MODS\n")
        print("FINAL VERDICT:")
        if len(possibleMcreatorMods) + len(mcreatorMods) >= 16:
            print("You really need to rethink your life choices. That's just, A LOT OF MCREATOR MODS. stop it. get some help. Nobody is going to want to play this PC killer.")
            webbrowser.open("https://www.youtube.com/watch?v=l60MnDJklnM")
        elif 8 < (len(possibleMcreatorMods) + len(mcreatorMods)) <= 15:
            print("Make sure to read the descriptions and comments on the mods you are adding. You have too many MCreator mods installed, and you will have preformance issues.")
            webbrowser.open("https://www.youtube.com/watch?v=5W-J6iPyZmM")
        elif 3 < (len(possibleMcreatorMods) + len(mcreatorMods)) <= 8:
            print("That's quite a few potential MCreator mods. Think about what you want to remove.")
            webbrowser.open("https://www.youtube.com/watch?v=HAoQdrwFK8U")
        elif 1 < (len(possibleMcreatorMods) + len(mcreatorMods)) <= 3:
            print("You have a few potential MCreator mods. please note that they more often then not cause preformance issues.")
            webbrowser.open("https://www.youtube.com/watch?v=LISrjmodGSE")
        elif (len(possibleMcreatorMods) + len(mcreatorMods)) == 1:
            print("You have one MCreator mod. It may be the sole cause of your preformance issues. Try to remove it if you are having issues.")
            webbrowser.open("https://www.youtube.com/watch?v=KnhXwlFeRP8")

        print("=" + find_whitespace(mostChars, "equal") + "=\n")
        #This is your redemption. it will delete each mcreator mod it found based on your go ahead.
        deleteMods = False
        deletePossibleMods = False
        if mcreatorMods:
            deleteMods = True if "Y" in input("Delete MCreator mods from your mods list? (You will be prompted for each mod). You have " + str(len(mcreatorMods)) + " MCreator mods. y/n: ").upper() else False
        if possibleMcreatorMods:
            deletePossibleMods = True if "Y" in input("Delete Possible MCreator mods from your mods list? (You will be prompted for each mod). You have " + str(len(possibleMcreatorMods)) + " Possible MCreator mods. y/n: ").upper() else False
        #Added some subtractor value to cheat instead of messing with the array I already have.I should have used classes instead of just trying to write this all in one giant blob.
        #Because there is no self in single method python scripts, only globals
        #My Code OCD is not handling this very well. but it just works and that's good enough for me.
        sub = 0
        if deleteMods:
            mcreatorNew = mcreatorMods
            for file in mcreatorMods:
                deleteMod = True if "Y" in input("Delete " + file + "? y/n: ").upper() else False
                if deleteMod:
                    os.remove(file)
                    sub = sub + 1
                    print("MCreator mod " + file + " has been deleted.")
                else:
                    print("MCreator mod " + file + " was not deleted.")
        j = 0
        if deletePossibleMods:
            for file in possibleMcreatorMods:
                deleteMod = True if "Y" in input("Delete " + file + "? It has a " +str(round(possibleMcreatorModsprob[j] * 100)) + "% chance of being MCreator. y/n: ").upper() else False
                if deleteMod:
                    os.remove(file)
                    print("Possible MCreator mod " + file + " has been deleted.")
                    sub = sub + 1
                else:
                    print("Possible MCreator mod " + file + " was not deleted.")
                j = j + 1
        #The ultimate verdict after being prompted to remove mcreator mods
        print("+" + find_whitespace(mostCharsB + 5, "line") + "+\n")
        print("ULTIMATE VERDICT:")
        if len(possibleMcreatorMods) + len(mcreatorMods) - sub >= 16:
            print("YOU  NEED TO LET GO. YOU HAVE A PROBLEM. At this point, you're doing this on purpose. Stop it, get some help.")
            webbrowser.open("https://www.youtube.com/watch?v=xhV_GMslNkc")
        elif 8 < (len(possibleMcreatorMods) + len(mcreatorMods))- sub <= 15:
            print("...Removing only a few of these types of mods is not going to help you. You really should run this again.")
            webbrowser.open("https://www.youtube.com/watch?v=NzishIREebw")
        elif 3 < (len(possibleMcreatorMods) + len(mcreatorMods))- sub <= 8:
            print("I hope you know what you're doing.")
            webbrowser.open("https://www.youtube.com/watch?v=0vEfDtV1MQU")
        elif 1 < (len(possibleMcreatorMods) + len(mcreatorMods))- sub <= 3:
            print("Better... Let's hope!")
            webbrowser.open("https://www.youtube.com/watch?v=yDSNJr__OiQ")
        elif (len(possibleMcreatorMods) + len(mcreatorMods))- sub == 1:
            print("Good job, this might just work now.")
            webbrowser.open("https://www.youtube.com/watch?v=aAwaxTGnkSk")
        else:
            print("YOU HAVE BEEN FREED OF MCREATOR WOO!!!")
            webbrowser.open("https://www.youtube.com/watch?v=CBEvfZu4HE4")

#A function to help create lines for the console GUI. takes the amount of whitespace, and the type of whitespace you want to create for said line
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
