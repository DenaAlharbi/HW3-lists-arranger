# create a list of numbers from 1 to 9 in random order


# The initial list of numbers.
listOfNumbers = [3, 2, 4, 1, 9, 5, 8, 6, 7]
# The list printed without any changes.
print(listOfNumbers)


# A while loop to iterate over the inner loop until the list is sorted.
while listOfNumbers != sorted(listOfNumbers):  # The sorted() makes the list ordered ascending from 1 to 9.

    # The j variable is in order to be able to get into the loop.
    j = 0
    while j < len(listOfNumbers):  # The len() is used to determine the value of the index in the list.
        listOfNumbers[j] -= 1  # This line updates the value of the numbers in the list and decreases them by one
        # each time it goes through.
        if listOfNumbers[j] == 0:  # if this condition is met the number will be removed using the pop().
            listOfNumbers.pop(j)  # j refers to the index of that number inside the list.
        # if the condition is not met the index will increase by one.
        else:
            j += 1
    # The append() will add a 9 each time at the end of the list.
    listOfNumbers.append(9)
    # The print statement is here in order to showcase the development of the list during each loop.
    print(listOfNumbers)
