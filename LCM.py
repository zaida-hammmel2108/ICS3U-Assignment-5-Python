#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Nov 2022
# This program determines the lowest common multiple

# code from https://www.javatpoint.com/python-find-lcm
def main(num1, num2):
    # selecting the greater number  
    if num1 > num2:  
        greater = num1  

    else:  
        greater = num2  
    while(True):  
        if((greater % num1 == 0) and (greater % num2 == 0)):  
            lcm = greater  
            break  
        greater += 1  
    return lcm    
  
# taking input from users  
user_num1 = int(input("Enter first number: "))  
user_num2 = int(input("Enter second number: "))  
# printing the result for the users  
print("The L.C.M. of", user_num1,"and", user_num2,"is", main(user_num1, user_num2))  


if __name__ == "__main__":
    main(user_num1, user_num2)
