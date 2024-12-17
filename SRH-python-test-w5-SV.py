# Big Data Programming: Pyhton Module Test
# Instructions ...
# Please consider good style & naming while developing the code when necessary,
#  such as Docstring, linting, etc. it is considered in the grading process!
# Use this file for the solution only. Jupyter notebook(.ipynb) not acceptable!
# Push the solution to a remote repo of name "SRH-Python-Test", and send me the link of the repo as DM
#  on Ms Teams for assessment.
# The duration of this test is 1 hour.

# Q1: What is the main difference between the list and Tuple?
# A1: List is mutable and Tuple is immutable. Also, tuple is ordered.


# Q2: why should list indexing be used Python?
# A2: The list is not ordered, and index can help us track, add and delete elements in the list using the specific index value.


# Q3: You have two lists (string_list, values_list) below. Write a function of
#  a name count_car. The function returns a dictionary.
#  The expected return of the function should print out this dictionary:
#  {'Audi_Q5': 2, 'Honda_civic': 4, 'Mercedes_200E': 5, 'BMW_720': 7, 'VW_passat': 2}
string_list = ['Audi_Q5', 'Honda_civic', 'Mercedes_200E', 'Honda_civic',
               'BMW_720', 'VW_passat']

value_list = [2, 4, 5, 7, 2]

# Creating the dictionary function
def count_car(string_list,value_list): 
        new_dict = {string_list[i]: value_list[i] for i in range(len(string_list))}
        return new_dict
        


# Q4: Write a function of a name double_even_numbers. The function squares the
#  even numbers only. Also, the function leaves the first element of the input
#  as is without getting squared regardless being even or odd number.
#  The function has one argument which is a numpy array of 100 elements of
#  integer type between 0-10.
#  The function returns an array. Use list comprehension in your answer.

import numpy as np
np_arr  = np.random.randint(0,10,size = (100,1))

# Creating the square fucntion 
def double_even_numbers(np_arr):
    for i in range(len(1,np_arr)):
        if(i%2 == 0):
            sqd_arr = [i*i]
    return sqd_arr
        

# Q5: Read "movies.csv" file, a file is provided. Create a function
#  returns only table of elements before 2000 with score 7 and above, then save
#  the elements in a new csv file with a name "dest_csv". 

import csv

#Defining both input and output files
input_file = "/Users/gautamchugh/Downloads/movies.csv"
output_file = "/Users/gautamchugh/Downloads/dest_csv.csv"

with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
     open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Copy desired row from the input file to the output file
    for row in reader:
        if(row["year"] < '2000' && row["score"] >= '7'):
            writer.writerow(row)

print(f"Desired cells have been copied from {input_file} to {output_file}.")


# Q6: Write a function of a name div_func. It returns the divsion of elements
#  in a list in reversed order. The function should pass the two lists below
#  without errors.

import random
random.seed(42)
short_list = [1, 0, 2, 2, 20]
long_list = [random.randrange(0, 10, 1) for i in range(15)]

def div_func(list):
    div_list = [i/i for i in range(len(list),0)]
