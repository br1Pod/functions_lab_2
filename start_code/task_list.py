tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def task_check_list(list, done):
    task_list = []
    for task in list:
        if task['completed'] == done:
            task_list.append(task['description'])
    print(task_list)


def task_description(list):
    task_list = []
    for task in list:
        task_list.append(task['description'])
    print(task_list)


def duration_list(list, time):
    task_list = []
    for task in list:
        if task['time_taken'] >= time:
            task_list.append(task['description'])
    print(task_list)

def task_description_print(list, description):
    for task in list:
        if task['description'] == description:
            print(task)


def update_task(list, description, toggle):
    for task in list:
        if task['description'] == description:
            task['completed'] = toggle
            print('Task updated!')

def new_task(list):
    description = input('What is your task: ')
    
    while True:
        complete = input('is it complete? yes or no: ').lower()
        if complete == 'yes' or complete == 'no':
            if complete == 'yes':
                complete = True
            elif complete == 'no':
                complete = False
            break
        else:
            print('Please try again')
   
    time_taken = int(input('How long will it take: '))
    new_task = { "description": description, "completed": complete, "time_taken": time_taken}
    list.append(new_task)


# #1
# task_check_list(tasks, False)
# print('-'*25)
# #2
# task_check_list(tasks, True)
# print('-'*25)
# #3
# task_description(tasks)
# print('-'*25)
# #4
# duration_list(tasks, 15)
# print('-'*25)
# #5
# task_description_print(tasks, 'Walk Dog')
# print('-'*25)
# #6
# update_task(tasks, 'Feed Cat', True)
# print(tasks)
# print('-'*25)
# #7
# new_task(tasks, new_task)
# print(tasks)
# print('-'*25)
# #8
def menu_display():
    print("Menu:")
    print("1: Display All Tasks")
    print("2: Display Uncompleted Tasks")
    print("3: Display Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")

def menu():
    menu_display()
    while True:
        user_input = input('Enter your choice').lower()
        if user_input == '1':
            task_description(tasks)
        elif user_input == '2':
            task_check_list(tasks, False)
        elif user_input == '3':
            task_check_list(tasks, True) 
        elif user_input == '4':
            update_task(tasks, 'Feed Cat', True)
        elif user_input == '5':
            duration_list(tasks, 15)
        elif user_input == '6':
            task_description_print(tasks, 'Walk Dog')
        elif user_input == '7':
            new_task(tasks)
        elif user_input == 'm':
            menu_display()
        elif user_input == 'q':
            quit()
        else:
            print('Sorry that does not compute!')
            

menu()