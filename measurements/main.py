
def measurement_KG_G():
    user_input = input("Enter your number to convert: ")

    try:
        number_to_process = float(user_input)
        print("Choose to covert to KG (Kilograms) or G(Grams)")
        another_user_input = input("For KG press 1, G press 2: ")


    except:
        print("You entered a number with letters or only letter(s) which is '{}'.Try again".format(user_input))
        measurement_KG_G()


measurement_KG_G()