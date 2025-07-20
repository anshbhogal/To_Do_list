from models import Task, session, User
import datetime

def register_user(username, password):
    if session.query(User).filter_by(username=username).first():
        print("Username already exists")
        return None
    user = User(username=username, password=password)
    session.add(user)
    session.commit()
    print("Registration successful")
    return user.id

def login_user(username, password):
    user = session.query(User).filter_by(username=username, password=password).first()
    if user:
        print(f"welcome, {username}!")
        return user.id
    else :
        print("Invalid Credentials..")
        return None
    
def save_task(title, details, deadline_str, user_id):
    deadline = datetime.datetime.strptime(deadline_str, "%d-%m-%Y").date()
    task = Task(title=title, details=details, deadline=deadline, user_id=user_id)
    session.add(task)
    session.commit()
    print("Task saved successfully.")

def view_incomplete_tasks(user_id):
    tasks = session.query(Task).filter_by(user_id=user_id).all()
    if not tasks:
        print("No Tasks Found")
        return True
    else:
        for task in tasks:
            print(task)

def view_task_details(id,user_id):
    task_id = session.query(Task).filter_by(id=id, user_id=user_id).first()
    if task_id:
        print(f"\nTitle:{task_id.title}\nDetails:{task_id.details}\nDeadline:{task_id.deadline}")
    else:
        print("Task not found")

def completed_deleted(id,user_id):
    task_id = session.query(Task).filter_by(id=id, user_id=user_id).first()
    if task_id:
        session.delete(task_id)
        session.commit()
        print("Task Marked Completed")
    else:
        print("Task not found")