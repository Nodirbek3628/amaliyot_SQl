from function import add_tasks,show_task,edit_task,remove_tasks,mark_task

def main():
     while True:
        print(
            "==== Menu ====\n"
            "1. TASK yaratish\n"
            "2. TASK ko'rish\n"
            "3. TASK yangilash\n"
            "4. TASK holatini o'zgartirish\n"
            "5. TASK o'chirish\n"
            "6. Dasturdan chiqish"
        )
        choice = input(">> ")

        if choice == "1":
            add_tasks()
        elif choice == "2":
            show_task()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            mark_task()
        elif choice == "5":
            remove_tasks()
        elif choice == "6":
            break
        else:
            print("Menudagi raqamlardan birini tanlang")
             



if __name__ == "__main__":
    main()