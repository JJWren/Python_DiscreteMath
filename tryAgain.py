def tryAgain():
    trueFalse = False
    while trueFalse == False:
        tryAgain = input("Enter 'y' to try again, 'n' to quit program: ")
        if tryAgain == 'y':
            return True
        elif tryAgain == 'n':
            return False


boolVal = tryAgain()
print(boolVal)
