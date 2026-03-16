import json

tasks = []

def enter(task):
    tasks.append({"task":task , "status":False})

def display():
    if len(tasks) == 0:
        print("No tasks available.")
        return
    for i,j in enumerate(tasks):
        if j["status"] == True:
            state = "Completed"
        else:
            state = "Pending"
        print(f"{i+1}. {j['task']} : {state}")
    
def complete():
    pending = []  #notes the indices of pending tasks in tasks[]

    for i,j in enumerate(tasks):
        if j["status"]==False:
            pending.append(i)
            print(f"{len(pending)}. {j['task']}")

    if len(pending)==0:
        print("No pending tasks")
        return

    choice = int(input("Choose a task to complete (Enter 0 to exit): "))
    
    if choice == 0:
        return 
    if choice<1 or choice>len(pending):
        print("Out of bounds!")
        return
    
    real_index = pending[choice-1]
    tasks[real_index]["status"] = True

def delete():
    pending = []

    for i,j in enumerate(tasks):
        if j["status"] == False:
            pending.append(i)
            print(f"{len(pending)}. {j['task']}")

    if len(pending)==0:
        print("No pending tasks")
        return

    choice = int(input("Select task to delete (Enter 0 to exit): "))

    if choice == 0:
        return
    if choice<1 or choice>len(pending):
        print("Out of bounds!")
        return
    
    real_index = pending[choice-1]
    tasks.pop(real_index)
    print("Task deleted")

def empty():
    confirm = input("Delete all tasks? (y/n): ")

    if confirm.lower() == "y":
        tasks.clear()
        print("All tasks cleared.")
    else:
        print("Operation cancelled.")

def load(): #loading data from json file
    try:
        with open("data.json","r") as f:
            data = json.load(f)
            tasks.extend(data)
    except:
        pass

def save(): #saving data into json file
    with open("data.json","w") as f:
        json.dump(tasks,f)