def average():
    '''This function when called will ask for the 3 test score inputs and then calculate the average score.'''
    score1 = float(input("Enter your first test score: "))
    score2 = float(input("Enter your second test score: "))
    score3 = float(input("Enter your third test score: "))
    avg_total = float(score1 + score2 + score3) / 3
    return avg_total

if __name__ == '__main__':
    '''This is the man function that is ran when we start the program'''
    firstname = input("Please enter your first name: ")
    lastname = input("Please enter your last name: ")
    age = input("Please enter your age: ")
    answer = average() # this statement calls the average function and will prompt the user for input

    print(lastname + ', ' + firstname + ". Age: " + age + ". Average test score:\t" + str(answer))
    # the print statement will show all input by the user on one line
