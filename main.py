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
        with open("tasks.json","a") as taskfile:
            for i, task in enumerate(self.tasks):
                taskfile.write(f"{self.numbersword[i]} task -->\n")
                taskfile.write(f"\n")
                taskfile.write(f"Title : {task['title']}\n")
                taskfile.write(f"Schedule date : {task['schedule date']}\n")
                taskfile.write(f"Status : {task['status']}\n")
                taskfile.write(f"\n"*2)

    def initial_tasks_print(self):
        print("Your tasks list ----->")
        # Print all tasks nicely
        for i, task in enumerate(self.tasks):
                print(f"{self.numbersword[i]} task -->")
                print("")
                print(f"Title : {task['title']}")
                print(f"Schedule date : {task['schedule date']}")
                print(f"Status : {task['status']}")
                print("\n"*2)

class tasks_manager(task_initial):
    # Delete tasks & update the file
    def delete_tasks(self):
        print("")  # spacing
        
        # Ask user if they want to delete
        tempdelete =input("Write 'delete' if you want to remove tasks.\n---> ").lower()
        print("")  # spacing

        # If yes, start deletion loop
        if tempdelete == "delete":
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

                    # Update file with remaining tasks
                    with open("tasks.txt","w") as taskfile:
                        for i in range(len(self.tasks)):
                            taskfile.write(f"{i+1}. {self.tasks[i]}\n")  # save updated tasks
                    
                    # Show current tasks after deletion
                    print("Updated tasks list ---->")
                    print("")
                    super().initial_tasks_print()
                    
                    print("")

# Create the manager instance and run the app
manager=tasks_manager()
manager.task_inputed()          # Input tasks
manager.initial_tasks_file()    # Save tasks to file
manager.initial_tasks_print()   # Print all tasks
manager.delete_tasks()          # Delete if needed