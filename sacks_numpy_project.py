# -*- coding: utf-8 -*-

"""
Goal 1: Make 2 arrays
Goal 2: Try 5 methods of your choice:
    1. Use trigonometric functions
    2. Find Min and Max
    3. Find the mean and standard deviation of each array
    4. Use the mean and sttandard deviation to calculate the z-score for each array
    5. Multiply z_x_2 by 2, then combine the two z-scored arrays 
    into one array with a shape of 8x4 and ordered smallest to largest
Goal 3: Create an output directory (if needed)
Goal 4: Save some output to output 
Goal 5: Read file back in from output directory
Goal 6: Use argparse to add command-line arguments to code
"""

#Load in Packages/Modules
import os, shutil
import numpy as np
import pickle
import argparse

#Function for making a new directory if need be: 
def make_dir(dirname, clean=False):
    """
    Make a directory if it does not exist.
    Use clean=True to clobber the existing directory.
    """
    if clean == True:
        shutil.rmtree(dirname, ignore_errors=True)
        os.mkdir(dirname)
    else:
        try:
            os.mkdir(dirname)
        except OSError:
            pass # assume OSError was raised because directory already exists

## make sure the output directory exists
this_dir = os.path.abspath('.').split('/')[-1]
this_parent = os.path.abspath('.').split('/')[-1]
out_dir = this_parent + '_output/'
print('Creating ' + out_dir + ', if needed')
make_dir(out_dir)

parser = argparse.ArgumentParser()
parser.add_argument('-begin', '--integer_begin', default=1, type=int)
parser.add_argument('-int', '--integer_int', default=1, type=int)

args = parser.parse_args()

print("\nvariables defined as...")
print("\nbeginning = ", args.integer_begin)
print("end =", args.integer_begin+31*args.integer_int)
print("interval =", args.integer_int)


x = np.array(np.arange(args.integer_begin, args.integer_begin+32*args.integer_int, args.integer_int))
print("\nStarting array:")
print(x) 

x_1 = np.array(x[::2].reshape(4,4))
print("\narray x_1")
print(x_1)

x_2 = np.array(x[1::2].reshape(4,4))
print("\narray x_2")
print(x_2)

print("\nGoal 1: Use trigonometric functions")
print("\nsin of x_1")
print(np.sin(x_1))
print("\ncos of x_2")
print(np.cos(x_2))

print("\nGoal 2: Find min and max of each array")
print("\nx_1:")
print("max =", np.max(x_1))
print("min = ", np.min(x_1))

print("\nx_2:")
print("max =", np.max(x_2))
print("min = ", np.min(x_2))

print("\nGoal Goal 3: Find the mean of each array")
mean_x_1 = np.mean(x_1)
sd_x_1 = np.std(x_1)
mean_x_2 = np.mean(x_2)
sd_x_2 = np.std(x_2)
print("\nx_1 mean and standard deviation:")
print(mean_x_1, ",", sd_x_1)
print("\nx_2 mean and standard deviation:")
print(mean_x_2, ",", sd_x_2)

print("\nGoal 4: Find the z-score of each number in the array")
z_x_1 = (x_1 - mean_x_1)/sd_x_1
z_x_2 = (x_2 - mean_x_2)/sd_x_2
print("\nx_1:")
print(z_x_1)
print("\nx_2:")
print(z_x_2)

print("\nGoal 5: Multiply z_x_2 by 2, then combine the two z-scored arrays into one array with a shape of 8x4 and ordered smallest to largest")
z_x_2_2 = z_x_2*2
x_big = (np.concatenate((z_x_2_2, z_x_1), axis=0))
x_big_flat = np.sort(x_big.reshape(1,32))
x_final = x_big_flat = x_big_flat.reshape(8,4)
print(x_final)

#Export x_final as a pickle file
out_fn = this_parent + '_output/' + 'x_final.p'
pickle.dump(x_final, open(out_fn, "wb"))

#Read in x_final pickle file
x_final_new = pickle.load(open(out_fn, 'rb'))
print("\nread in pickle file:") 
print(x_final_new)









