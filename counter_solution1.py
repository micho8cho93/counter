#create class attendance counter

#ask user to input how many students are in the class, remember that input() will read numbers as strings.
# How can we convert the input to an integer? 
def counter():
    students = int(input('How many students are in your class: '))

#initialize two variables. 1) to keep count of students present and 2) to keep count of students absent
    count_present = 0
    count_absent = 0

#iterate through number of students and have user input if student is present or absent
#remember that for loops do not naturally work with integers, how can you iterate through a RANGE of numbers?
    for student in range(students):
        present = input('Is student #' + str(student + 1) + ' present? (y/n): ')
        if present == 'y':
            count_present += 1
        elif present == 'n':
            count_absent += 1
        else:
            print('Invalid input')
            return

#print the number of students present and absent        
    print('Students present: ', count_present)
    print('Students absent: ', count_absent)
    return

#run your program
if __name__ == "__main__":
    counter()
