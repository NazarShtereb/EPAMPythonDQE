# Homework 1 "Python Basics"
import random


rlist = []  # create a blank list

for i in range(100):  # create for loop with 100 iterations
    rlist.append(random.randrange(0, 1000, 1))  # add random numbers in range 0 - 1000
n = len(rlist)  # create a variable with the list length value
for n in range(len(rlist) - 1, 0, -1):  # going through every number of the list, starting from the end, with step -1
    for i in range(n):
        if rlist[i] > rlist[i + 1]:  # if first number is bigger than second number, then
            rlist[i], rlist[i + 1] = rlist[i + 1], rlist[i]  # rearrange them
print(f'A list of numbers: {rlist}')  # print the list

even = []  # create a blank list for even numbers
odd = []  # create a blank list for odd numbers

for i in rlist:  # loop through an every element in the list of all elements
    if (i % 2) == 0:
        even.append(i)  # check if the number is even. If it is even then add it to the even list
    else:
        odd.append(i)  # if not, so it is odd, then add it to the odd list
try:
    print(
        f'An avg of even numbers: {sum(even) / len(even):.2f}')  # calculating an average for the list of even numbers
    print(
        f'An avg of odd numbers: {sum(odd) / len(odd):.2f}')  # calculating an average for the list of odd numbers
except ZeroDivisionError:  # if divide on zero throws an error
    print("Calculation error")
