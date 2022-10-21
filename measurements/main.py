
from measurement_funcs import *


def measurement_KG_G():
    user_input = input("Enter your number to convert: ")

    try:
        number_to_process = float(user_input)
        print(number_to_process)

        def manipulation():
            print("Choose to covert to KG (Kilograms) or G(Grams)")
            another_user_input = input("For KG press 1, G press 2: ")

            if another_user_input == '1':
                processing = kg(number_to_process)
                print("{} grams will be {} kilograms.".format(
                    number_to_process, processing))
            elif another_user_input == '2':
                processing = g(number_to_process)
                print("{} kilograms will be {} grams.".format(
                    number_to_process, processing))
            else:
                print("Invalid input")
                print("Try again...")
                print("\n")

                manipulation()
        manipulation()
    except:
        print("You entered a number with letters or only letter(s) which is '{}'.Try again".format(
            user_input))
        measurement_KG_G()


measurement_KG_G()
