"""
Joshua Wren
07 February 2021
Permutations Calculator
"""

# A program to calculate the total permutations
# given a total number of items and a set size.
# -------------------------------------------------------------------------
# Example: Given a 50-song list, and a desired outcome of a 10-song list,
# The total possible permutations is: 50!/40! {n!/(n-r)!}

from math import factorial


def getTwoNumInput():
    numList = []
    while len(numList) < 2:
        try:
            checkNum = int(input("Enter an integer greater than 0: "))

            if isinstance(checkNum, int):
                if checkNum > 0:
                    numList.append(checkNum)
                else:
                    print("Unacceptable input.\n")
            else:
                print("Unacceptable input.\n")
        except ValueError:
            print("Unacceptable input.\n")
    return numList


def tryAgain():
    trueFalse = False
    while trueFalse == False:
        tryAgain = input("Enter 'y' to try again, 'n' to quit program: ")
        if tryAgain == 'y':
            return True
        elif tryAgain == 'n':
            return False


def main():
    print("\n***** Permutations Calculator *****")
    print("\nThis program finds the total number of permutations given two inputs,")
    print("such that: n!/(n-r)!")

    print("Numbers entered will calculate the smallest input from the greatest.")
    checkNums = getTwoNumInput()
    # order list from greatest to least
    if checkNums[0] < checkNums[1]:
        temp = checkNums[0]
        checkNums[0] = checkNums[1]
        checkNums[1] = temp

    diff = checkNums[0] - checkNums[1]
    solution = int(factorial(checkNums[0])/factorial(diff))

    print(
        f"Total permutations of set size {checkNums[1]} out of set size {checkNums[0]}: {solution}\n")

    print("Would you like to try another permutation?")
    yesNo = tryAgain()
    if yesNo == True:
        return main()
    else:
        return print("\n***** End of Program *****")


if __name__ == '__main__':
    main()
