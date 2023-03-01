'''
Title: Assignment07
Desc: Script that shows pickling and exception handling features of Python
Changelog:
FChen14, 02/27/2023, Created File
'''
import pickle
# Data #
# For declaring variables #
number = []
# Processing #
class Processing:
    "Processing Tasks"

    def pickle_number(number):
        """ To pickle the user input into file
        :param number: (list) with data
        """
        with open("number.pickle", "wb") as f: # kind of like a try-except block to try to dump data
            pickle.dump(number, f)

    def unpickle_number():
        """ To unpickle data from file
        :return: data from pickle file
        """
        with open("number.pickle", "rb") as f: # kind of like a try-except block to load data
            pickled_number = pickle.load(f)
        return pickled_number
# Presentation #
class IO:
    "Performs Input and Output tasks"
    def main():
        "Asks user for input and outputs unpickled data of their input"
        while True:
            try:
                user_number = input("Please enter your favorite number (type 'exit' to quit): ") # gathers input

                if user_number.lower() == "exit": # users can exit
                    break
                else:
                    user_number = int(user_number) # turns input into an int
                    number.append(user_number)
                    break
            except ValueError:
                print("Invalid input: please enter a numeric value only\n") # pops up if they put in anything but numbers
            except:
                print("An unexpected error has occurred!\n") # to catch any other unexpected error
        Processing.pickle_number(number)
        print("Favorite number has been pickled to number.pickle\n") # let's users know their input was pickled

        try:
            unpickled_number = Processing.unpickle_number()
            print("Your favorite number unpickled is:", unpickled_number, "\n") # pulls out the pickled number from the file
        except FileNotFoundError:
            print("Error: number.pickle couldn't be found!!!\n") # incase the file isn't found
        except UnpicklingError:
            print("Error: invalid pickle data\n") # in case data couldn't be unpickled
        print("Thank you for your time!")
# Main Body of Script #
IO.main()

