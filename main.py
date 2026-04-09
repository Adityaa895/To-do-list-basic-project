import json

class task_initial:
    def __init__(self):
        self.tasks=[]  # List to store all tasks

        # Words to make prompts more fun: first, second, etc.
        self.numbersword = [
            "First", "Second", "Third", "Fourth", "Fifth",
            "Sixth", "Seventh", "Eighth", "Ninth", "Tenth",
            "Eleventh", "Twelfth", "Thirteenth", "Fourteenth", "Fifteenth"
        ]

    def task_inputed(self):
            print(" ")
        # Counter for numbering tasks
            n=0

            check=""

        # Keep asking tasks until user types "Exist"
            while check !="Exit":
                    temptasks={}
                    
                    temptasks["title"]= input(f"Enter your {self.numbersword[n].lower()} task = ").capitalize()
                    temptasks["schedule date"] = input(f"Enter your {self.numbersword[n].lower()} task schedule date = ")
                    temptasks["status"] = "Pending"
                    n=n+1

                    print("")
                    self.tasks.append(temptasks)


                    check=input("Enter 'Exit' to end = ").capitalize()
                    print("")
                        
            print(" ")  # Just some spacing

    def initial_tasks_file(self):         
        # Save tasks to a file
        with open("tasks.json","w") as taskfile:
            json.dump(self.tasks,taskfile,indent=4)

    def initial_tasks_print(self):
        print("Your tasks list ----->")
        print("")
        # Print all tasks nicely
        for i, task in enumerate(self.tasks):
                print(f"{self.numbersword[i]} task -->")
                print("")
                print(f"Title : {task['title']}")
                print(f"Schedule date : {task['schedule date']}")
                print(f"Status : {task['status']}")
                print("\n"*2)

class tasks_manager(task_initial):

    def menu_option(self):
         print("")

         print("<------ MENU OPTIONS ------>\n\n1. Enter 'Delete' to delete the tasks\n" \
         "2. Enter 'Add' to add more tasks\n3. Enter 'Update status' to update task's status completed\n" \
         "3. Enter 'Pending' to view pending tasks\n4. Enter 'Edit' to edit tasks")
         print("")

    # Delete tasks & update the file
    def delete_tasks(self):
        print("")  # spacing
    
        for i in range(len(self.tasks)):
             # Ask which task to delete, 100 to quit
             index_delete=int(input("Enter the number of task you want to delete ('100' to end) = "))
             print("")

             if index_delete == 100:
                 break
             else:
                 # Remove chosen task (adjusting for 0-index)
                self.tasks.pop(index_delete-1)

                print(" ")  # spacing

                super().initial_tasks_file()
                    # Show current tasks after deletion
                print("Updated tasks list ---->")
                print("")
                super().initial_tasks_print()
                    
                print("")

    def add_more_tasks(self):
         temptasks=[]
         print("")
         
         super().task_inputed()

         with open("tasks.json","w") as taskfile:
            json.dump(self.tasks,taskfile,indent=4)

         super().initial_tasks_print()

    def update_status(self):
         print("")

         tempnumber=int(input("Enter the task's number of which status you want to change = "))-1
         print("")

         if 0<=tempnumber<len(self.tasks):
             self.tasks[tempnumber]["status"]= "Completed"
         else:
             print("Invalid task's number!!")

         super().initial_tasks_file()
         super().initial_tasks_print()

    def display_pending(self):
        print("")
        print("List of pending tasks ---->")

        pending_count = 0

        for task in self.tasks:
            if task["status"] == "Pending":
                print(f"{self.numbersword[pending_count]} task -->")
                print(f"Title : {task['title']}")
                print(f"Schedule date : {task['schedule date']}")
                print(f"Status : {task['status']}\n")
                pending_count += 1

    def update_title(self):
        print("")

        tempnumber=int(input("Enter the number of the task you want to edit = "))-1
        print("")

        if 0<=tempnumber<len(self.tasks):

            new_title=input("Enter your new task's title = ").capitalize()
            self.tasks[tempnumber]["title"]=new_title

            super().initial_tasks_file()
            super().initial_tasks_print()

        else:
            print("Invalid task's number")

    def update_schedule(self):
        print("")

        tempnumber=int(input("Enter the number of the task you want to edit = "))-1
        print("")

        if 0<=tempnumber<len(self.tasks):

            new_schedule=input("Enter your new task's schedule date = ")
            self.tasks[tempnumber]["schedule date"] = new_schedule

            super().initial_tasks_file()
            super().initial_tasks_print()

        else:
            print("Invalid task's number")
                 
    def edit_task(self):
        print("")
        check=""

        while check!="Exit":

            print("<------ Task edit options ------>\n1. Enter 'Title' to edit title\n" \
            "2. Enter 'Date' to edit schedule date\n3. Enter 'Status' to update status\n ")

            tempoption=input("Enter from the above edit options = ").capitalize()

            if tempoption=="Title":
                self.update_title()
            elif tempoption == "Date":
                self.update_schedule()
            elif tempoption =="Status":
                self.update_status()
            else:
                print("Please enter from the given options!")

            check=input("Enter 'Exit' to end tasks editing = ").capitalize()
            print("")

# Create the manager instance and run the app
manager=tasks_manager()
manager.task_inputed()          # Input tasks
manager.initial_tasks_file()    # Save tasks to file
manager.initial_tasks_print() 

while True:
    manager.menu_option()

    option = input("Enter from the above menu = ").capitalize()

    if option=="Delete":
        manager.delete_tasks()
    elif option =="Add":
        manager.add_more_tasks()
    elif option == "Pending":
        manager.display_pending()
    elif option == "Edit":
        manager.edit_task()
    else:
        print("Please enter from the menu options.")