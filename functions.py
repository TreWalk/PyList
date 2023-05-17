import PySimpleGUI as sg

def get_tasks(filepath):
    with open(filepath, 'r') as f:
        tasks = f.readlines()
    return tasks

def write_tasks(filepath, tasks):
    with open(filepath, 'w') as f:
        f.writelines(tasks)

filepath = 'tasklist.txt'

# Function to clean task list
def clean_tasks(filepath):
    # Get the tasks from the file
    tasks = get_tasks(filepath)

    # Remove empty tasks
    tasks = [task for task in tasks if task.strip()]

    # Write the cleaned tasks back to the file
    write_tasks(filepath, tasks)

# Function to complete a task
def complete_task(filepath):  # add filepath as a parameter
    tasks = get_tasks(filepath)
    if not tasks:  # if the task list is empty
        sg.popup('No tasks to complete.', 'Please try again.')
        return tasks

    while True:
        try:
            number = int(sg.popup_get_text('Task Number to Complete:', 'Complete Task'))
            index = number - 1

            if index < 0 or index >= len(tasks) or not tasks[index].strip():
                sg.popup('Invalid input. Enter a valid number.', 'Please try again.')
                continue

            completed_task = tasks[index].strip('\n')
            tasks.pop(index)
            write_tasks(filepath, tasks)

            sg.popup(f'Task {number}: {completed_task.title()} has been completed.', 'Task Completed')
            break

        except ValueError:
            sg.popup('Invalid input. Please enter a valid number.', 'Please try again.')
            continue

    return tasks

