#create class attendance counter

#ask user to input how many students are in the class
#ask the user to input the names of each student based on the number of students in the class. 
def counter():
    class_list = []
    students = int(input('How many students are in your class: '))
    for student in range(students):
        name = (input(f'Student #{student + 1} name?: '))
        class_list.append(name)

#verify that the class list is correct. If the class list is wrong, end the program.
#If the class list is correct then continue with program. This might be a little tricky.
#You should probably use google to figure it out. If you're still stuck, ask for help.     
    list_check = input(('Is this class list correct: ' + ', '.join(class_list) + '\nEnter y/n: '))
    if list_check == 'n':
        return ('Class list wrong, start again')
    elif list_check == 'y':
        print()

#initalize 4 variables. 2 variables are needed to keep count of the number of students present and absent.
#2 more variables are needed to create a list of student names that are present and absent
    count_present = 0
    present_list = []
    count_absent = 0
    absent_list = []

#iterate through number and names of students and use user input to record if student is present or absent
#if user input is equal to y then record student as present and add their name to the present list
#if user input is equal to n then record student as absent and add their name to the absent list
    for item in class_list:
        attendance = input(f'Is {item} present? (y/n): ')
        if attendance == 'y':
            count_present += 1
            present_list.append(item)
        elif attendance == 'n':
            count_absent += 1
            absent_list.append(item)
        else:
            "Invalid input"
            return

#print the number of students present and absent        
#print the names of students present and absent
    print('Students present: ', count_present)
    print('Student names: ', ', '.join(present_list))
    print('Students absent: ', count_absent)
    print('Student names: ', ', '.join(absent_list))
    return

#run your program
if __name__ == "__main__":
    counter()

