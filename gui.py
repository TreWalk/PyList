import PySimpleGUI as sg
from functions import get_tasks, write_tasks, filepath, complete_task

def start_gui():
    # GUI Layout Definition
    label = sg.Text("Welcome to PyList", font=("Arial", 20))
    input_box = sg.InputText(tooltip="Enter Task", key="Task")
    button_spacer1 = sg.Text("", size=(10, 5))
    button_spacer2 = sg.Text("", size=(10, 1))
    add_button = sg.Button("ADD", size=(10, 1), key="ADD")
    complete_button = sg.Button("COMPLETE", size=(10, 1), key="Complete")
    tasks = get_tasks(filepath)
    list_box_values = [f"{i + 1}. {task.title()}" for i, task in enumerate(tasks)]
    list_box = sg.Listbox(values=list_box_values, enable_events=True, key='tasks', size=(45, 30))
    edit_button = sg.Button("EDIT", size=(10, 1), key="Edit", disabled=True)  # Disabled initially

    # Create Window
    layout = [
        [
            sg.Column(
                [
                    [label],
                    [button_spacer2],
                    [sg.Text("Enter a Task:")],
                    [input_box],
                    [sg.Text("Your Tasks:")],
                    [list_box],
                ],
                element_justification="left",
            ),
            sg.Column(
                [
                    [button_spacer1],
                    [add_button],
                    [complete_button],
                    [edit_button],
                ],
                element_justification="right",
                vertical_alignment="top",
            ),
        ]
    ]

    window = sg.Window('PyList 1.0', layout, element_justification='right')

    # Main Event Loop
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == "tasks":
            window["Edit"].update(disabled=False)

            selected_task_str = values["tasks"][0]
            selected_task_text = selected_task_str.split('. ')[1].strip()
            window["Task"].update(selected_task_text)

        if event == "ADD":
            task = values["Task"].strip()

            if task:
                tasks.append(task + "\n")
                write_tasks(filepath, tasks)

                window["Task"].update("")

                list_box_values = [f"{i + 1}. {task.title()}" for i, task in enumerate(tasks)]
                window["tasks"].update(values=list_box_values)
            else:
                sg.popup('Task field cannot be empty.', 'Please enter a task.')

        elif event == "Edit":
            if values["tasks"]:
                selected_task_str = values["tasks"][0]
                selected_task_index = int(selected_task_str.split('.')[0]) - 1

                new_task = values["Task"] + "\n"

                tasks[selected_task_index] = new_task
                write_tasks(filepath, tasks)

                list_box_values = [f"{i + 1}. {task.title()}" for i, task in enumerate(tasks)]
                window["tasks"].update(values=list_box_values)

                window["Task"].update("")
                window["Edit"].update(disabled=True)

            else:
                sg.popup('No task selected.', 'Please select a task to edit.')

        elif event == "Complete":
            tasks = complete_task(filepath)
            list_box_values = [f"{i + 1}. {task.title()}" for i, task in enumerate(tasks)]
            window["tasks"].update(values=list_box_values)

    window.close()


