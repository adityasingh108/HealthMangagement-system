''''
Author : Aditya kumar singh
'''
from datetime import datetime  # import time module


def log(s):
    """ This function Logging the data of person  in a
    Text file .
 """
    if s == 1:  # if for aadi press 1 logging the data
        # ask aadi to log the data for food and exercise
        try:
            aadi_input = int(input("1 for food\n2 for exercise\n:>"))
        except:
            print("Error! Enter only numbers")
            exit()  # program exit
        if aadi_input == 1:  # if press the 1 Logging the data in a file
            with open("aadi_food.txt", "a") as file_object:
                content = input("")
                file_object.write(f"{content} time{datetime.now()}\n")
                file_object.close()
        elif aadi_input == 2:  # if press the 1 Logging the data in a file
            with open("aadi_exercise.txt", "a") as file_object:
                content = input("")
                file_object.write(f"{content} time{datetime.now()}\n")
                file_object.close()
    elif s == 2:
        # ask mitthu to log the data for food and exercise
        try:
            mithu_input = int(input("1 for food\n2 for exercise\n:>"))
        except:
            print("Error! Enter only numbers")
            exit()  # program exit
        if mithu_input == 1:  # if press the 1 Logging the data in a file
            with open("mithu_food.txt", "a") as file_object:
                content = input()
                file_object.write(f"{content} time{datetime.now()}\n")
                file_object.close()
        elif mithu_input == 2:  # if press the 1 Logging the data in a file
            with open("mithu_exercise.txt", "a") as file_object:
                content = input("")
                file_object.write(f"{content} time{datetime.now()}\n")
                file_object.close()
    elif s == 3:
        # ask shubendu  to log the data for food and exercise
        try:
            subendu_input = int(input("1 for food\n2 for exercise\n:>"))
        except:
            print("Error! Enter only numbers")
            exit()  # program exit
        if subendu_input == 1:  # if press 1 logg the data in the text file
            with open("subendu_food.txt", "a") as file_object:  # create a empty .txt file
                content = input()
                file_object.write(f"{content} time{datetime.now()}\n")
                file_object.close()
        elif subendu_input == 2:  # if press 2 logg the data for exercise
            # create a file in a folder where the program runs
            with open("subendu_exercise.txt", "a") as file_object:
                content = input("")
                file_object.write(f"{content} time{datetime.now()}\n")
                file_object.close()


def retrive(r):
    '''This function 
    retrive the Data  from a file '''
    if r == 1:
        try:
            aadi_input = int(input("1 for food\n2 for exercise\n:>"))
        except:
            print("Error! Enter only numbers")
            exit()  # program exit
        if aadi_input == 1:  # if press the 1 tretrive the  Logging the data  from a  file
            with open("aadi_food.txt", 'r') as file_object:
                for line in file_object:
                    print(line, end="")
        elif aadi_input == 2:  # if press the 2 retrive the logging data from  a file
            with open("aadi_exercise.txt", "r") as file_object:
                for line in file_object:
                    print(line, end="")
    if r == 2:
        try:
            mithu_input = int(input("1 for food\n2 for exercise\n:>"))
        except:
            print("Error! Enter only numbers")
            exit()  # program exit
        if mithu_input == 1:  # if press the 1 tretrive the  Logging the data  from a  file
            with open("mithu_food.txt", 'r') as file_object:
                for line in file_object:
                    print(line, end="")
        elif mithu_input == 2:  # if press the 2 retrive the logging data from  a file
            with open("mithu_exercise.txt", "r") as file_object:
                for line in file_object:
                    print(line, end="")
    if r == 3:
        try:
            subendu_input = int(input("1 for food\n2 for exercise\n:>"))
        except:
            print("Error! Enter only numbers")
            exit()  # program exit

        if subendu_input == 1:  # if press the 1 tretrive the  Logging the data  from a  file
            with open("subendu_food.txt", 'r') as file_object:
                for line in file_object:
                    print(line, end="")
        elif subendu_input == 2:  # if press the 2 retrive the logging data from  a file
            with open("subendu_exercise.txt", "r") as file_object:
                for line in file_object:
                    print(line, end="")


if __name__ == "__main__":
    while True:
        # a= input("Enter stop to Quit program")
        try:
            a = int(input("1 for Log the data \n0 for retrive the Data\n:>"))
        except:
            print("Error! Enter only numbers")
            exit()  # program exit
        try:
            if a == 1:
                b = int(input("1 for Aadi\n2 for Mithu\n3 for Subendu\n:>"))
                log(b)
            elif a == 0:
                b = int(input("1 for Aadi\n2 for Mithu\n3 for Subendu\n:>"))
                retrive(b)
        except:
            print("Error ! ,You cant't retrive the data ")
                    
        print("Press q to quit and c to continue \n:>")  # stooping the program  fro user input 
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"): 
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue