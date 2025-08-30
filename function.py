from database import engine,metadata_obj,get_connection
import models
from crud import created_tasks,get_tasks,delete_tasks,update_task,change_task_status
from datetime import datetime
metadata_obj.create_all(engine)

def add_tasks():
    title = input("task yozing: ")
    description = input("description: ")
    due_date_text = input("(yyyy-mm-d | hh-mm):")
    due_date = datetime.strptime(due_date_text, "%Y-%m-%d | %H-%M")

    created_tasks(get_connection(),title, description=description,due_date=due_date)

def show_task():
    result = get_tasks(get_connection())

    for row in result:
        print(row)

def remove_tasks():
    task_id = int(input("Task_id: "))
    delete_tasks(get_connection(),task_id)

def edit_task():
    task_id = int(input("Task_id: "))
    update_task(get_connection(),task_id , title="Edit task")


def mark_task():
    mark = int(input("task_id: "))
    change_task_status(get_connection(),mark)