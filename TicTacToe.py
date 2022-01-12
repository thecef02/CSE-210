# Cristian Fernandez - CSE 210 -
# TIC TAC TOE Game. Week 02
dict = {7:" ",8:" ",9:" ",
        4:" ",5:" ",6:" ",
        1:" ",2:" ",3:" "}
numChoosed = 0

class c:  # to give color to the text
    red =     '\033[91m'
    green =   '\033[92m'
    yellow =  '\033[93m'
    blue =    '\033[94m'
    blink  =  '\033[6m'
    reverse = '\033[7m'
    end =     '\033[0m'

def get_int(prompt, min, max):
    """Prompt the user for an integer, verify that it is
    between min and max inclusive, and return the integer.
    """
    num = None
    while num is None:
        try:
            text = input(prompt)
            prospect = int(text)
            if prospect < min:
                print(f"Invalid input: number must be {min} or greater.")
            elif prospect > max:
                print(f"Invalid input: number must be {max} or less.")
            else:
                num = prospect
        except ValueError as val_err:
            print(f"Invalid integer: {text}. Please try again.")
    return num

def checkForWin():
    # Check all the posible conbinations for a winner.

    #check the diagonals
    if (dict[7] == dict[5]) and (dict[7] == dict[3]) and dict[7] != " " and dict[5] != " " and dict[3] != " ":
        return True
    elif (dict[9] == dict[5]) and (dict[9] == dict[1]) and dict[9] != " " and dict[5] != " " and dict[1] != " ":
        return True
    
    #check the horizontal convinations
    elif (dict[7] == dict[8]) and (dict[7] == dict[9]) and dict[7] != " " and dict[8] != " " and dict[9] != " ":
        return True
    elif (dict[4] == dict[5]) and (dict[4] == dict[6]) and dict[4] != " " and dict[5] != " " and dict[6] != " ":
        return True
    elif (dict[1] == dict[2]) and (dict[1] == dict[3]) and dict[1] != " " and dict[2] != " " and dict[3] != " ":
        return True

    #check the vertical convinations
    elif (dict[7] == dict[4]) and (dict[7] == dict[1]) and dict[7] != " " and dict[4] != " " and dict[1] != " ":
        return True
    elif (dict[8] == dict[5]) and (dict[8] == dict[2]) and dict[8] != " " and dict[5] != " " and dict[2] != " ":
        return True
    elif (dict[9] == dict[6]) and (dict[9] == dict[3]) and dict[9] != " " and dict[6] != " " and dict[3] != " ":
        return True


    else:
        return False

def getColorToLine(whatLine):
    # determine what set of item from the dictionary will be used and set the correct color to the choosen symbol (X or O)
    counter = 0
    if whatLine == 1:
        counter = 7
    elif whatLine == 2:
        counter = 4
    else:
        counter = 1

    fullBuildLine = ""    
    for i in range(counter,counter+3):
        buildLine = c.yellow if dict[i] == "X" else c.blue
        fullBuildLine = fullBuildLine + buildLine + dict[i] + c.end + " │ "
    fullBuildLine = fullBuildLine[:-3]
    return fullBuildLine

def drawScreen():
    #this will refresh the screen with the right color for each player
    cls() 
    print(f"{c.red}        ╔═══════════════════╗{c.end}")
    print(f"        {c.red}║{c.end} {c.reverse} TIC - TAC - TOE {c.end} {c.red}║{c.end}")
    print(f"{c.red}        ╚═══════════════════╝{c.end}")
    print(f"{c.green}        By Cristian Fernandez{c.end}")
    print("\n")
    print("   7 │ 8 │ 9      =      " + getColorToLine(1))
    print("  ───┼───┼───           ───┼───┼───")
    print("   4 │ 5 │ 6      =      " + getColorToLine(2))
    print("  ───┼───┼───           ───┼───┼───")
    print("   1 │ 2 │ 3      =      " + getColorToLine(3))
    print ("\n\n")

def printWinnerBanner(turn):
    #We have a winner so we selebrate.
    print(f"{c.red}    ╔═══════════════════════════════╗{c.end}")
    print(f"    {c.red}║{c.end} {c.reverse}{turn}{c.end} is the winner of this game. {c.red}║{c.end}")
    print(f"    {c.red}╚═══════════════════════════════╝{c.end}")

def clearDict():
    for each_i in dict:
        dict[each_i] = " "

def main():
    oneMoreTime = "Y"
    while oneMoreTime == "Y": 
        clearDict()
        drawScreen()
        for i in range(9):
            val = "0"
            turn = "X" if (i % 2) == 0 else "O"
            print (f'  It is the turn for {turn}')
            while val != " ":
                numChoosed = get_int(f"  Enter the number where you want to place the {turn} ",1,9)
                val = dict[numChoosed]
            dict[numChoosed] = turn
            drawScreen()
            if checkForWin():
                # print winner
                printWinnerBanner(turn)
                break
        
        oneMoreTime = input("\nDo you want to play again? Y/N ").upper()

def cls():
    # clear the screen (black)
    print(chr(27) + '[2J')

if __name__ == '__main__':
    main()


