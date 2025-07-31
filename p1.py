# importing the module
import sys
# this function will be the first to run as soon as the main function executes
def initial_phonebook():
    rows, cols=int(input("Please enter initial number of contacts:")), 5
    
# We are collecting the initial number of contacts the user wants to have in the

# phonebook already. User may also enter 0 if he doesn't wish to enter any.
    phone_book = []
    print("phone_book")
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):"% (i+1))
        print("NOTE: * indicates mandatory feilds")
        print("........................................")
        temp = []
        for j in range(cols):
            # We have taken the conditions for values of j only for the personalized fields
            # such as name, number, e-mail id, dob, category etc
            if j == 0:
                temp.append(str(input("Enter name*:")))
                # We need to check if the user has left the name empty as its mentioned that

                # name & number are mandatory fields.

                # So implement a condition to check as below.
                if temp[j] == "" or temp[j] == "":
                     temp.append(int(input("Enter number*:")))
                     # We do not need to check if user has entered the number because int automatically

                    # takes care of it. Int value cannot accept a blank as that counts as a string.

                    # So process automatically exits without us using the sys package.
