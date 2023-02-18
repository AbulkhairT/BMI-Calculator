"""
Abulkhair Turmakhanov
Class: CS 521 - Fall 2022
Date: December 7th, 2022
Homework Problem # Final Project
Description of Problem (just a 1-2 line summary!):
This code takes inputs, analyzes it and returns an output to a user.
"""

#Importing class
from Class import *

# Unit test
if __name__ == "__main__":
    while True:
        p = bmi_finder( 80 , 1.70, 200, 300, 300)
        print('Welcome user! Please enter your weight and height')
        weight = int(input('What is your weight in killograms? '))
        height = float(input('What is your height in meters? '))
        breakfast = int(input('How many calories you '
                              'consumed for breakfast? '))
        lunch = int(input('How many calories you '
                          'consumed for lunch? '))
        dinner = int(input('How many calories you '
                           'consumed for dinner? '))
        result = bmi_finder(weight, height, breakfast, lunch, dinner)
        final = result.get_bmi(weight, height)
        final_another = result.caloriefinder(breakfast, lunch, dinner)
        print('your BMI is -', final)


        if final > 30:
            print('Your BMI doesnt look great, change something')
        else:
            print('Your BMI is great!')


        print('your total calories intake is -', final_another)

        if final_another > 2401:
            print('Your calorie intake is high, decrease it to maintain'
                  ' same weight')
        elif final_another <=2400 and final_another >= 1800:
            print('This is a healthy calorie intake, keep it up!')
        else:
            print('This is too little, please try to increase your calories')


        try:
            with open('test.txt', 'w') as f:
                for i in range(final_another):
                    f.write(str(final_another))
                    f.write('\n')
                    break
        except:
            print("test.txt couldn't open")

        q = []

        for i in range(int(final)):
            if final not in q:
                q.append(final)
            else:
                None

        print(q,'- this is the users BMI in a list form')
        print(p.__repr__(), '- this is where we access repr')
        print(p._bmi_finder__hiddengem(1))

        print('End of the program, but do not worry we are going to '
              'start over!')
    else:
        print('Something is not working here'
