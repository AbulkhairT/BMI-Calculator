"""
Abulkhair Turmakhanov
Class: CS 521 - Fall 2022
Date: December 7th, 2022
Homework Problem # Final Project
Description of Problem (just a 1-2 line summary!):
This code takes inputs, analyzes it and returns an output to a user.
"""

#This is the class bmi_finder which has all attributes

class bmi_finder():
    def __init__ (self, weight, height, breakfast, lunch, dinner):
        self.weight = weight
        self.height = height
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner

#try block and a function which calculates BMI

    def get_bmi(self, weight, height):
        try:
            return self.weight/(self.height*self.height)
        except ZeroDivisionError:
            print('Do not divide by zero')
            exit()

    def caloriefinder(self, breakfast, lunch, dinner):
            return (self.breakfast + self.lunch + self.dinner)

    def __hiddengem(self, __hidden):
        self.__hidden = __hidden
        print('This is the private method being printed')

    def __repr__(self):
        return f'bmi_finder(weight={self.weight}, height={self.height})'
