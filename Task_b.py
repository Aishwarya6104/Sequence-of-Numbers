#Main Program for sequence of numbers in range[1, 10000]
# to calculate count of steps to reach 1


from matplotlib import pyplot as plt

def Cm(n):
    steps = 1

    while n > 1:
        #If n is even
        if n % 2 == 0:
            n = (n / 2)
            steps = steps + 1
        #If n is odd
        elif n % 2 == 1:
            n = (3 * n + 1)
            steps += 1
    return steps

x_axis = []
y_axis = []

def main():
    for i in range(10000):
        #As i starts from 0. So, i+1
        n = i + 1
        steps = Cm(n)
        print("For Number: ", n)
        print("Total number of steps to reach 1: ", str(steps))
        x_axis.append(i+1)
        y = Cm(n)
        y_axis.append(y)
    #Plotting graph
    plt.scatter(x_axis, y_axis)
    plt.xlabel("Numbers")
    plt.ylabel("Number of Steps")
    plt.title("Plot of Number of Steps")
    plt.show()

if __name__ == "__main__":
    main()





