import datetime

"""
This program defines a function login() and then takes username and password from the user.
It checks if they match with any of the username and password pairs stored in a file 
called 'user.txt' and if match found call display_menu() function using using for loop. 
If no match is found it prints a message saying the username or password was incorrect 
and decrements the variable attempts by 1. If variable attempts is greater than 0, it 
calls the login() function again. Otherwise it prints a message saying the user has 
used up all their attempts to login and exits the program.
"""
def login():
    global username
    username = input('Please enter your user name: ')
    password = input('Please enter your password: ')
    user_read = open('user.txt', 'r')
    attempts = 3
    user_data = user_read.read().splitlines()
    match = False
    for user in user_data:
        if user.split(",")[0] == username and user.split(",")[1] == password:
            match = True
            display_menu()
    if not match:
        print('Your user name or password was incorrect. Please try again.')
        attempts = attempts - 1
        if attempts > 0:
            login()
        else:
            print('You have used up all your attempts to login. Exiting program.')


"""
This program defines a function display_menu() that displays a menu of options to the user and prompts 
them to make a selection. It uses a while loop and the value of display_menu variable to keep displaying 
the menu until the user selects for example option 'e' to exit the menu and the program.
"""
def display_menu():
    display_menu = True
    while display_menu == True:
        menu = input('''Welcome back! Select one of the following options below:
        r - register a user
        a - add a task
        va - view all tasks
        vm - view my tasks
        st - statistics
        e - exit
        : ''').lower()
        if menu == 'r':
            register_user()
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all_tasks()
        elif menu == 'vm':
            view_my_tasks()
        elif menu == 'st':
            view_statistics()
        elif menu == 'e':
            display_menu = False
            print('Goodbye!')
            exit()


"""
This program defines a function register_user() that allows the user to register. It first checks if the current 
user is admin, if yes, it prompts the user to enter a new username and password, and then prompts the user to 
confirm the password. If the password and password confirmation match, it opens the "users.txt" file in append 
mode, writes the new username and password to the file and closes it and prints a message that the new user has 
been registered. If the password and password confirmation do not match, it prints a message asking the user to 
try again. If the current user is not admin, it prints a message that only admin can register new users.
"""
def register_user():
    if username == 'admin':
        new_username = input('Please enter the user name of the person you want to register: ')
        new_password = input('Please enter the password of the person you want to register: ')
        new_password_confirm = input('Please confirm the password: ')
        if new_password == new_password_confirm:
            user_write = open('user.txt', 'a')
            user_write.write(new_username + ',' + new_password_confirm + '\n')
            user_write.close()
            print(new_username + ' has been registered!')
        else:
            print('Passwords do not match, please try again!')
    else:
        print('Only admin can register new users!')


"""
This section defines a function add_task() that allows the user to add a task to a file called "task.txt" by taking
inputs of the username, title, description, due_date and the current_date, and task status. It then uses a while loop 
and asks the user to enter information for the task. The task status is being checked if it is 'yes' or 'no' and if 
it's 'yes', then it's modified to 'Yes' if it's 'no' it's modified to 'No'. It then opens the "task.txt" file in 
append mode, writes the task information to the file and closes it. The function then prints a message saying the 
task was added successfully, and asks the user if they want to add another task, if the user enters 'no' the while 
loop breaks and exits.
"""
def add_task():
    while True:
        username = input('Please enter the username of the person the task is assigned to: ')
        title = input('Please enter the title of the task: ')
        description = input('Please enter a description of the task: ')
        due_date = input('Please enter the due date of the task (YYYY-MM-DD): ')
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        task_status = input('Has the task been completed? (yes/no)')
        if task_status.lower() == "yes":
            task_status = "Yes"
        else:
            task_status = "No"
        task_write = open('tasks.txt', 'a')
        task_write.write(username + ',' + title + ',' + description + ',' + due_date + ',' + current_date + ',' + task_status + '\n')
        task_write.close()
        print('Task successfully added!')
        again = input("Do you want to add another task? (yes/no) ")
        if again.lower() == "no":
            break


"""
This program defines a function called "view_all_tasks()". It firstly checks if username is admin, otherwise it
prints only the admin user is authorised to view all tasks.Then opens a file called 'tasks.txt' in read mode. It 
reads all the lines from the file, and assigns them to a variable called "tasks". It then iterates over the 
"tasks" variable and for each task, it splits the task string by the comma and assigns the resulting list to 
a variable called "task_info". It then prints the different parts of the task such as "Assigned To", "Title", 
"Description", "Due Date", "Creation Date", and "Completed" by accessing the index of the "task_info" list.
"""
def view_all_tasks():
    if username == 'admin':
        task_file = open('tasks.txt', 'r')
        tasks = task_file.readlines()
        task_file.close()
        for task in tasks:
            task_info = task.strip().split(',')
            print('——————————————————————————\n')
            print("Assigned To: ", task_info[0])
            print("Title: ", task_info[1])
            print("Description: ", task_info[2])
            print("Due Date: ", task_info[3])
            print("Creation Date: ", task_info[4])
            print("Completed: ", task_info[5])
            print()
            print('——————————————————————————\n')
    else:
        print("Only the admin user is authorised to view all tasks.")


"""
This code defines a function called "view_my_tasks()" which opens a file called 'tasks.txt' in read mode and reads 
all the lines from the file. It then iterates over the tasks and for each task, it splits the task string and 
assigns the list to a variable called "task_info". It then checks if the first element in task_info which is 
"Assigned To" is equal to variable called "username". If it's true, it append the task_info to task_list variable. 
After iterating over all the tasks, it checks if task_list variable is empty or not. If it's empty, it means there 
is no task found and prints "No task found for user: ", followed by the user's name. Otherwise, it iterates over
task_list variable and for each task, it prints the different parts of the task e.g "Title", "Description" etc. 
"""
def view_my_tasks():
    task_list = []
    with open("tasks.txt", "r") as task_file:
        tasks = task_file.readlines()
    for task in tasks:
        task_info = task.strip().split(',')
        if task_info[0] == username:
            task_list.append(task_info)
    if not task_list:
        print("No task found for user: ", username)
    else:
        for i, task in enumerate(task_list, start=1):
            print('——————————————————————————\n')
            print("Task {}".format(i))
            print("Title: {}".format(task[1]))
            print("Description: {}".format(task[2]))
            print("Due Date: {}".format(task[3]))
            print("Creation Date: {}".format(task[4]))
            print("Completed: {}".format(task[5]))
            print()
            print('——————————————————————————\n')


"""
This program defines a function called "view_statistics()" which opens two files: "tasks.txt" and "user.txt" in read 
mode. First it checks whether username is admin and it reads all the lines from each file, counts the number of lines 
and assigns the count to the variable "line_count". It then prints the number of tasks and the number of users by using
the line count variable. If username is not admin, it prints an error message. At the end of the function the login()
function is called. 
"""
def view_statistics():
    if username == 'admin':
        with open("tasks.txt") as f:
            lines = f.readlines()
            line_count = len(lines)
            print("Number of tasks:", line_count)
        with open("user.txt") as f:
            lines = f.readlines()
            line_count = len(lines)
            print("Number of users:", line_count)
    else:
        print("Only the admin user is authorised to view task statistics.")


login()
