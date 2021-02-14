"""
Joshua Wren
26 January 2021
Factorial Calculator
"""

# A program to calculate the factorial of a given input.


def getNaturalNumInput():
    # Does user want to try again?
    didQuit = input(
        "Hit enter to start, type anything else to quit: ")
    if didQuit != '':
        return "Quit"
    else:
        isInputBad = True
        try:
            inputNaturalNum = int(
                input("Enter a natural number: "))
            if int(inputNaturalNum):
                return inputNaturalNum
        except ValueError:
            print("That was not a natural number.\n")
            isInputBad = False
            # restart function
            return getNaturalNumInput()


def main():
    print("\n***** Factorial Calculator *****")
    print("\nThis program finds the solution for an input factorial.")
    print("{Example: User enters 5; Expected output = 120}\n")

    checkNum = getNaturalNumInput()
    if isinstance(checkNum, int):
        factor = checkNum
        solution = 1

        while factor > 1:
            solution *= factor
            factor -= 1

        print(f"The solution of {checkNum}! is {solution}.")
        return main()
    else:
        return "***** End of Program *****"


if __name__ == '__main__':
    main()
