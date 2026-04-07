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

         print("---- MENU OPTIONS ----\n\n1. Enter 'Delete' to delete the tasks\n" \
         "2. Enter 'Add' to add more tasks")
         print("")

         self.option = input("Enter from the above menu = ").capitalize()

    # Delete tasks & update the file
    def delete_tasks(self):
        print("")  # spacing
        
        # Ask user if they want to delete
        tempdelete =input("Write 'Delete' if you want to remove tasks.\n---> ").capitalize()
        print("")  # spacing

        # If yes, start deletion loop
        if tempdelete == "Delete":
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

         tempadd_more = input("Write 'Add' to add more tasks = ").capitalize()
         

         if tempadd_more=="Add":

            super().task_inputed()

            with open("tasks.json","w") as taskfile:
                json.dump(self.tasks,taskfile,indent=4)

            super().initial_tasks_print()

    def update_status(self):
         print("")

         tempstatus=input("Enter 'Update status' to update task's status to 'Complete' = ").capitalize()
         print("")

         if tempstatus=="Update status":
            for i in range(len(self.tasks)):

                number_status=int(input("Enter the task's number of which status you want to change('100' to end) = "))
                print("")

                if number_status!=100:
                 self.tasks[number_status-1]["status"]= "Completed"
                else:
                    break

                super().initial_tasks_file()
                super().initial_tasks_print()
                 
            
# Create the manager instance and run the app
manager=tasks_manager()
manager.task_inputed()          # Input tasks
manager.initial_tasks_file()    # Save tasks to file
manager.initial_tasks_print()   # Print all tasks
manager.update_status()