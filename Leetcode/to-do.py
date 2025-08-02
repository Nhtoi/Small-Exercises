import sys

class Entry():
    tasks = []
    def __init__(self, title, date, description, dueDate, isDone):
        self.title = title
        self.date = date
        self.description = description
        self.dueDate = dueDate
        self.isDone = isDone
        Entry.tasks.append(self)
    
    def __str__(self):
        return f"Entry: Title: {self.title} Date: {self.date} Description: {self.description} Due Date: {self.dueDate} Finished: {self.isDone}"

    def CreateEntry():
        goAgain = "y"
        while goAgain == "Y" or goAgain == "y":
            title = input("Give your Task a Title: ")
            date = input("Give your Task a date: ")
            description = input("Give your Task a Description: ")
            dueDate = input("Give your Task a Due Date: ")
            isDone = "False"
            entry = Entry(title, date, description, dueDate, isDone)
            goAgain = input("Would you like to make another entry: (Y/N): ")
            print("Entry Created Successfully")
        main() 

def DisplayEntries():
    if Entry.tasks:
        for task in Entry.tasks:
            print(task)
    else:
        print("No Tasks To Display At the Moment") 
        main() 
    print("Diplayed all Tasks")  
    main()  

def EditTask():
    toedit = []
    if not Entry.tasks:
        print("Nothing to Edit, Create some Tasks First!")
        main() 
    else:
        for task in Entry.tasks:
            print(task.title)
            toedit.append(task.title)
        edit = input("What task would you like to Edit? ")
        while edit not in toedit:
            print("Invalid Choice, Choose From The Available List: ")
            print(toedit)
            edit = input("What task would you like to Edit? ")
        for task in Entry.tasks:
            if task.title == edit:
                    task.title = input("Give your Task a New Title: ")
                    task.date = input("Give your Task a New date: ")
                    task.description = input("Give your Task a New Description: ")
                    task.dueDate = input("Give your Task a New Due Date: ")
                    task.isDone = input("Are you Finished With your Task?: (Y/N) ")
                    task.isDone.lower()
                    print(task.isDone)
                    while task.isDone != "y" and task.isDone != "n" and task.isDone != True and task.isDone != False:
                        if task.isDone == "y":
                            task.isDone = True
                        elif task.isDone == "n":
                            task.isDone = False
                        task.isDone = input("Invalid Task is Done Choice either (Y/N): ")
                    print("Entry Edited Successfully")
                    main() 

def DeleteTask():
    todelete = []
    if not Entry.tasks:
        print("Nothing to Delete, Create some Tasks First!")
        main() 
    else:
        for task in Entry.tasks:
            print(task.title)
            todelete.append(task.title)
        delete = input("What task would you like to delete? ")
        while delete not in todelete:
            print("Invalid Choice, Choose From The Available List: ")
            print(todelete)
            delete = input("What task would you like to delete? ")
        for task in Entry.tasks:
            if task.title == delete:
                Entry.tasks.remove(task)
                print("Task Deleted Sucessfully")
                main()

def main():
    print("-=+Main Menu+=-\n")
    print("Choose from the Following Options:\n \n" \
    "1. Create a Task \n" \
    "2. Delete a Task \n" \
    "3. Display all Tasks \n" \
    "4. Edit a Task \n" \
    "If you want to Exit type 'Exit'")
    choice = input("Make a Choice: ")
    Controller(choice.lower())
            
def Controller(choice):
    options = ["1","2","3","4","exit"]
    if choice not in options:
        print("Invalid Input Try Again")
        main()
    else:
        if choice == "1":
            Entry.CreateEntry()
        elif choice == "2":
            DeleteTask()
        elif choice == "3":
            DisplayEntries()
        elif choice == "4":
            EditTask()
        elif choice == "exit":
            return 0

    
if __name__ == '__main__':
    sys.exit(main())