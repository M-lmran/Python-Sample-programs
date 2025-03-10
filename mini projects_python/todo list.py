# def todo_list(user,todo):
task = []
print("Assalamu alaikum , how may i help you?")
while True:
    print('\n1. Add Task')
    print('2. Delete Task')
    print("3. View Task")
    print("4. Exit")
    user = int(input("\nEnter The Number :  "))
    
    
    try:
        

        if user == 1:
            todo = input("enter your task :  ")
            task.append(todo)
            
        elif user == 2:
            todo_ = input("enter your previous task to remove")
            task.remove(todo_)
            
        elif user == 3:
            for i in task:
                print("\n",i)
        elif user == 4:
            print("Thank you for using me")
            break
    except:
        print("please enter the number in integer")

# a = int(input("please enter number as displayed above: "))
# b = input("please enter a task in the form of list:  ") 
# print(todo_list(a,b))
            
