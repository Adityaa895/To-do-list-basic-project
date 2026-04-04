class task_initial:
    def __init__(self):
        self.tasks=[]  # List to store all tasks

        # Words to make prompts more fun: first, second, etc.
        self.numbersword = [
            "first", "second", "third", "fourth", "fifth",
            "sixth", "seventh", "eighth", "ninth", "tenth",
            "eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth"
        ]

    def task_inputed(self):
            print(" ")
        # Counter for numbering tasks
            n=0

        # Temp variable to hold user input
            temptasks=""

        # Keep asking tasks until user types "Exist"
            while temptasks !="Exist":

            # Prompt with numbered task
                temptasks=input(f"Enter your {self.numbersword[n]} task ('Exist' to end) = ").capitalize()
            
            # Add task to the list if not exiting
                if temptasks!= "Exist":
                    self.tasks.append(temptasks)
                n=n+1  # Move to next number word

            print(" ")  # Just some spacing

    def initial_tasks_file(self):         
        # Save tasks to a file
        with open("tasks.txt","a") as taskfile:
            for i in range(len(self.tasks)):
                taskfile.write(f"{i+1}. {self.tasks[i]}\n")  # Numbered in file

    def initial_tasks_print(self):
        # Print all tasks nicely
        for i in range(len(self.tasks)):
            print(f"{i+1}. {self.tasks[i]}.")

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
                    super().initial_tasks_print()
                    
                    print("")

# Create the manager instance and run the app
manager=tasks_manager()
manager.task_inputed()          # Input tasks
manager.initial_tasks_file()    # Save tasks to file
manager.initial_tasks_print()   # Print all tasks
manager.delete_tasks()          # Delete if needed