from functions import register_user,login_user,save_task, view_incomplete_tasks, view_task_details, completed_deleted
def main_menu(user_id):
    # while True:
        print("****************************")
        print("1. ADD TASK")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        # try:
        choice =(input("Enter your choice:"))

        if choice == '1':
            title = input("Task Title: ")
            details = input("Task Details: ")
            deadline = input("Deadline (DD-mm-YYYY): ")
            save_task(title, details, deadline, user_id)
        elif choice == '2':
            view_incomplete_tasks(user_id)
            if view_incomplete_tasks is not True:
                try:
                    task_id=int(input("Enter Task id to view: "))
                    view_task_details(task_id,user_id)
                except ValueError:
                    print("Enter integer value")
        elif choice == '3':
            view_incomplete_tasks()
            try:
                task_id=int(input("Enter Task id to Mark Completed: "))
                completed_deleted(task_id,user_id)
            except ValueError:
                print("Enter Integer Value")
        else:
            print("Invalid Choice")

        # except ValueError:
        #     print("Enter integer value")

def login_menu():
    from functions import register_user, login_user
    print("1. Login")
    print("2. Register")
    choice = input("Choose an Option")
    if choice == '1':
        username = input("Username:")
        password = input("Password:")
        return login_user(username, password)
    elif choice == '2':
        username = input("Username:")
        password = input("Password:")
        register_user(username,password)
        return login_menu()
    else :
        print("Invalid choice")
        return login_menu


