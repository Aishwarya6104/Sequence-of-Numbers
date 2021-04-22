#Program for just 1 number to calculate count of steps to reach 1
#For example, I considered the number n = 10

def Cm(n):
    print("For Number: ", n)
    steps = 1
    while (n > 1):
        if n % 2 == 0:
            n = (n / 2)
            steps = steps + 1
            print(str(n) + " : " + str(steps))
        elif n % 2 == 1:
            n = (3 * n + 1)
            steps = steps + 1
            print(str(n) + " : " + str(steps))
    return steps


def main():
    n = 10
    steps = Cm(n)

    print("Total number of steps to reach 1: ", str(steps))

if __name__ == "__main__":
    main()