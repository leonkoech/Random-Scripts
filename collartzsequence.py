# collatz sequencec
# Write a function named collatz() that has one parameter named number. If
# number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.
# Then write a program that lets the user type in an integer and that keeps
# calling collatz() on that number until the function returns the value 1. 

def collatz(number):
    if number%2 == 0:
        # number is even
        print (number//2)
        return number //2
    else:
        # number is odd
        print (3*number+1)
        return 3*number+1
def main():
    try:
        c=int(input('enter a number:\n'))
    except ValueError:
           print('oops! that is not an integer')
           main()
           
    if collatz(c)>1:
        main()
    else:
        exit()
if __name__=='__main__':
    main()