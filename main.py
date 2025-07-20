from ui import login_menu,main_menu

def main():
    user_id = login_menu()
    if user_id:
        main_menu(user_id)

if __name__ == "__main__":
    main()
