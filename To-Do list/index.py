#enter tasks
#task completed
#delete task
#print task

import functions as fn
import json

# load tasks at startup
fn.load()

while True:
    print("\nPress 1 -> Add Task")
    print("Press 2 -> Completed Task")
    print("Press 3 -> Delete Task")
    print("Press 4 -> Print Tasks")
    print("Press 5 -> Delete All Tasks")
    print("Press 0 -> Exit")

    n = int(input("Enter a number: "))
    if n==1:
        a = input("Enter the task: ")
        fn.enter(a)
        fn.save()
    
    elif n==2:
        fn.complete()
        fn.save()

    elif n==3:
        fn.delete()
        fn.save()

    elif n==4:
        fn.display()

    elif n==5:
        fn.empty()
        fn.save()

    elif n==0:
        break

    else:
        print("Invalid input. Enter a number between 0 and 4!")