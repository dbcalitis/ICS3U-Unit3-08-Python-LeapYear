#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Sept 2021
# This program is a leap year checker


def main():
    # This function checks if the year given by the user is a leap year or not
    # input
    user_year = input("Please enter the year: ")

    try:
        # process & output
        user_year = int(user_year)
        if user_year % 4 == 0:
            if user_year % 100 == 0:
                if user_year % 400 == 0:
                    print("{0} is a leap year.".format(user_year))
                else:
                    print("{0} is not a leap year.".format(user_year))
            else:
                print("{0} is a leap year.".format(user_year))
        else:
            print("{0} is not a leap year.".format(user_year))
    except Exception:
        print("Invalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
