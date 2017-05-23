"""
This file may contain utility functionalities to the extend you will need it
123456789012345678901234567890123456789012345678901234567890123456789012
"""
def my_input_float(var):
    """
    This function is for validation of entering a float value
    """
    while True:
        try:
            variable = float(input("Please enter "+ var +": "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    return variable

def my_input_int(var):
    """
    This function is for validation of entering a float value
    """
    while True:
        try:
            variable = int(input("Please enter "+ var +": "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    return variable