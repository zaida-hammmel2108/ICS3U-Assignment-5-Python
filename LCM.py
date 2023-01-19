#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Dec 2022
# This program calculates the LCM of two integers

import math


def main():

    # input

    integer1 = input("Enter your first number: ")
    integer2 = input("\nEnter your second number: ")

    # process & output

    try:
        integer1_int = int(integer1)
        integer2_int = int(integer2)

        if integer1_int > integer2_int:
            greater = integer1_int
        else:
            greater = integer2_int
        while True:
            if (greater % integer1_int == 0) and (greater % integer2_int == 0):
                lcm = greater
                break
            greater += 1
        print("\nThe L.C.M. of", integer1, "and", integer2, "is", lcm)

    except Exception:
        print("\nInvalid Integer.")


if __name__ == "__main__":
    main()
