#create class attendance counter

#ask user to input how many students are in the class 
def counter():
    students = int(input('How many students are in your class: '))

#iterate through number of students and have user input if student is present or absent
    count_present = 0
    count_absent = 0

    for student in range(students):
        present = input('Is student #' + str(student + 1) + ' present? (y/n): ')
        if present == 'y':
            count_present += 1
        elif present == 'n':
            count_absent += 1
        else:
            "Invalid input"
            return
        
    print('Students present: ', count_present)
    print('Students absent: ', count_absent)
    return

if __name__ == "__main__":
    counter()
