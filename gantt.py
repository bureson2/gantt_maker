import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def create_gantt_chart(tasks):
    # Prepare data for the chart
    task_names = []
    starts = []
    ends = []

    for task in tasks:
        task_names.append(task['name'])
        starts.append(task['start'])
        ends.append(task['end'])

    # Create the chart
    fig, ax = plt.subplots(figsize=(10, len(tasks)))

    ax.barh(task_names, mdates.date2num(ends) - mdates.date2num(starts), left=mdates.date2num(starts), align='center')
    ax.xaxis_date()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

def add_task(tasks):
    name = input("Enter the task name: ")
    start = datetime.strptime(input("Enter the start date (dd-mm-yyyy): "), "%d-%m-%Y")
    end = datetime.strptime(input("Enter the end date (dd-mm-yyyy): "), "%d-%m-%Y")
    tasks.append({"name": name, "start": start, "end": end})

def remove_task(tasks):
    name = input("Enter the task name to remove: ")
    tasks[:] = [task for task in tasks if task['name'] != name]

if __name__ == "__main__":
    tasks = [
        {"name": "Work 1", "start": datetime(2023, 11, 1), "end": datetime(2023, 11, 5)},
    ]

    while True:
        print("\nMenu:")
        print("1. Display Gantt chart")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_gantt_chart(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")
