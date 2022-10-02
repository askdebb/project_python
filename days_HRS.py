#changing days to hours program
#By Christopher W. Debrah
#This program accepts number of days and coverts to hours


def days_hrs():
    your_input = input("Enter the number of days: ")


    try:
        days = int(your_input)
        do_the_maths = days * 24
        print("You Entered {} days".format(your_input))
        print("{} day(s) in hours is {} in hours.".format(your_input,do_the_maths))
    except ValueError:
        print("You entered an invalid input")
        days_hrs()
days_hrs()