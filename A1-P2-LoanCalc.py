#Program 2 – Weekly Loan Calculator
#Develop a short term loan calculator program as a console application 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # setting var to 0 for clean numbers
    loanAmount      = 0
    interestRate    = 0
    numOfYears      = 0

    print("Weekly Loan Calculator")

    # getting input from the user for Loan Amount, Instrst Rate, and Number of Years, Includes error handling for false values.
    while True: # <--- setting up loop to catch if user enters values that are not numbers
        try: 
            loanAmount = float(input("\nEnter the amount of loan: "))
            break # <--- the loop will exit if the input is valid
        except ValueError: # <--- prints error message if non number is entered
            print("Invlid input. Please enter a valid number for 'the amount of loan'.")

    while True:
        try:
            interestRate = float(input("Enter the interest rate (%): "))
            break
        except ValueError:
            print("Invlid input. Please enter a valid number for 'interest rate (%)'.")

    while True:
        try:
            numOfYears = float(input("Enter the number of years: "))
            break
        except ValueError:
            print("Invlid input. Please enter a valid number for 'number of years'.")

    # Calcs from the user input for weekly payment amount
    i = interestRate / 5200 # <--- weekly interest rate ( useing i to store it as a new variable in memory)
    weeks = 52 * numOfYears # <--- calc the num of weeks for the load period 
    weeklyPayment = (i / (1 - (1 + i) ** -weeks)) * loanAmount # <--- we raise the weekly interest rate to the power of weeks ( - becuase we are calculating the inverse of compouning )

    # printing the output to the user of entered values
    print(f"\nThe weekly payment will be: ${weeklyPayment:.2f}")

    # YOUR CODE ENDS HERE

main()