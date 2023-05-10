tasks = []

while True:
    user_choice = input('Type add, show, edit, complete or exit: ')
    user_choice = user_choice.strip()

    if user_choice == 'add':
        task = input('Enter a Task: ') + '\n'

        with open('tasklist.txt', 'r') as file:
            tasks = file.readlines()

        tasks.append(task)

        with open('tasklist.txt', 'w') as file:
            file.writelines(tasks)

    elif user_choice == 'show':
        try:
            with open('tasklist.txt', 'r') as file:
                tasks = file.readlines()

            for index, item in enumerate(tasks):
                if not item.strip():
                    continue
                row = f"{index + 1}.{item.strip().title()}"
                print(row)
        except FileNotFoundError:
            print('Error: File not found')

    elif user_choice == 'edit':
        while True:
            try:
                with open('tasklist.txt', 'r') as file:
                    tasks = file.readlines()

                number = int(input('Item Number to Edit: '))
                number = number - 1

                if number < 0 or number >= len(tasks):
                    print("Invalid input. Enter a valid number.")
                    continue

                new_task = input('Enter New Task: ')
                tasks[number] = new_task + '\n'

                with open("tasklist.txt", 'w') as file:
                    file.writelines(tasks)

                print("Task updated successfully.")
                break

            except ValueError:
                print("Invalid input. Enter a valid number.")
                continue

    elif user_choice == 'complete':
        while True:
            try:
                number = int(input('Task Number to Complete: '))

                with open('tasklist.txt', 'r') as file:
                    tasks = file.readlines()

                index = number -1

                if index < 0 or index >= len(tasks) or not tasks[index].strip():
                    print("Invalid input. Enter a valid number.")
                    continue

                completed_task = tasks[index].strip('\n')
                tasks.pop(index)

                with open('tasklist.txt', 'w') as file:
                    file.writelines(tasks)

                print(f'---Task {number}: {completed_task.title()} has been completed.---')
                break

            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

    elif user_choice == 'exit':
        print('---Program successfully closed---')
        break
    else:
        print('Invalid Command')
    elif user_choice == 'exit':
        print('---Program successfully closed---')
        break
    else:
        print('Invalid Command')
