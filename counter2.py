#create class attendance counter

#ask user to input how many students are in the class 
def counter():
    class_list = []
    students = int(input('How many students are in your class: '))
    for student in range(students):
        name = (input(f'Student #{student + 1} name?: '))
        class_list.append(name)
    
    list_check = input(('Is this class list correct (y/n):  ', class_list))
    if list_check == 'n':
        return ('Woops, rerun the program and start again')
    elif list_check == 'y':
        print()
#iterate through number of students and have user input if student is present or absent
    count_present = 0
    present_list = []
    count_absent = 0
    absent_list = []

    for item in class_list:
        attendance = input(f'Is {item} present? (y/n): ')
        if attendance == 'y':
            count_present += 1
            present_list.append(class_list)
        elif attendance == 'n':
            count_absent += 1
            absent_list.append(class_list)
        else:
            "Invalid input"
            return
        
    print('Students present: ', count_present)
    print('Student names: ', present_list)
    print('Students absent: ', count_absent)
    print('Student names: ', absent_list)
    return

if __name__ == "__main__":
    counter()

