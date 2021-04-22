#Optimized version of Main Program
#to calculate count of steps to reach 1
#Graph Plot for those sequence of numbers

import math
from matplotlib import pyplot as plt

def Cm(n, steps):
    n = int(n)
    steps +=1
    #Check if n is power of 2
    if(n & (n-1)) == 0:
        #if power of 2 then logn base 2 is the remaining steps
        return steps + math.log(n, 2)
    #Check if n is even
    elif n % 2 == 0:
        #Find if n/2 is power of 2
        return Cm(n/2, steps)
    else:
        #If n is odd check if (m*3+1) is power of 2
        return Cm(n * 3 + 1, steps)

x_axis = []
y_axis = []

def main():
    for i in range(10000):
        #As i starts from 0. So, i+1
        n = i + 1
        steps = 0
        Cm(n, steps)
        print("For Number: ", n)
        print("Total number of steps to reach 1: ", Cm(n, steps))
        x_axis.append(i + 1)
        y = Cm(n, steps)
        y_axis.append(y)
    #Plotting graph
    plt.scatter(x_axis, y_axis)
    plt.xlabel("Numbers")
    plt.ylabel("Number of Steps")
    plt.title("Plot of Number of Steps")
    plt.show()

if __name__ == "__main__":
    main()

