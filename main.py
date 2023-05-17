from functions import clean_tasks, filepath
from gui import start_gui

def main():
    clean_tasks(filepath)
    start_gui()

if __name__ == "__main__":
    main()
