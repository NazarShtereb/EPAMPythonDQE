# Homework 1 "Python Basics"
import random


rlist =  [random.randrange(0, 1000, 1) for i in range(100)] # create list of 100 random numbers from 0 to 1000
    
n = len(rlist)  # create a variable with the list length value
for j in range(n - 1, 0, -1):  # going through every number of the list, starting from the end, with step -1
    for i in range(j):
        if rlist[i] > rlist[i + 1]:  # if first number is bigger than second number, then
            rlist[i], rlist[i + 1] = rlist[i + 1], rlist[i]  # rearrange them
print(f'A list of numbers: \n {rlist}\n')  # print the list

even = []  # create a blank list for even numbers
odd = []  # create a blank list for odd numbers
    
for i in rlist: even.append(i) if not(i%2) else odd.append(i)  # append even number to even list, odd to odd list

data = [odd,even] # prepare data structures to output results in one loop
names = ["odd","even"] # prepare data structures to output results in one loop
for i in range(len(data)): # loop on data
    try: 
        average = " {:.2f}".format(sum(data[i])/len(data[i])) # calculate average and convert result to string
    except ZeroDivisionError:  # if divide on zero throws an error
        average = "Calculation error" # prepare string in case on division error
    print(f'An avg of {names[i]} numbers: {average} \n')  # calculating an average for the list of even numbers
