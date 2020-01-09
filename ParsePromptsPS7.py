from interPretr import interPretr
from pathlib import Path

def parseAndExecute(cl):
    tokenizedCommands = []
    
    tokenizedCommands = [token.strip() for token in cl.split(':')]
    
    numOfTokens =  len(tokenizedCommands)

    invalidCommand = False

    if(numOfTokens > 0):
        command = tokenizedCommands[0]

        if((numOfTokens == 1) & (command == "showMinList")):
            ip.showAll()
        elif((numOfTokens == 2) & (command == "searchLanguage")):
            ip.displayCandidates(tokenizedCommands[1])
        elif(numOfTokens == 3):
            if(command=="DirectTranslate"):
                ip.findDirectTranslator(tokenizedCommands[1], tokenizedCommands[2])
            elif(command == "TransRelation"):
                ip.findTransRelation(tokenizedCommands[1], tokenizedCommands[2])
            else:
                invalidCommand = True
        else:
            invalidCommand = True
        
    if(invalidCommand):
        with open("output.txt", "a") as outputFile:
            print(f"\nInvalid Command : {commandLine}\n", file=outputFile)
            print(f"{help}", file=outputFile)
    

ip=interPretr()
    #readPromptsFile()


print("abc")
with open("promptsPS7.txt", "r") as promptFile:
    for commandLine in promptFile:
        print("readprompts", commandLine)
        parseAndExecute(commandLine)

ip.readApplications('inputfile.txt')

Path("outputPS7.txt").touch()
    
help = """
Supported List of Commands : 
==========================
showMinList
searchLanguage: Hindi
DirectTranslate: English : Malayalam
TransRelation: English : Malayalam
"""

#def readPromptsFile():