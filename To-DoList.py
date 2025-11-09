todo_list = []
 
print( 'welcome to do list')
print('1. Add task')
print('2. View tasks')
print('3. Remove task')
print('4. Exit')

while True:
     choice = input('Enter your choice (1-4):')
     
     if choice =='1':
         task = input('Enter the task :')
         todo_list.append(task)
         print('task added')
         
     elif choice == '2':
         print('your tasks:')
         for i, task in enumerate(todo_list,1):
             print(f"{i}. {task}")
             
     elif choice =='3':
         task_num = int(input('Enter task number to remove:'))
         if 0 < task_num <= len(todo_list):
             removed_task = todo_list.pop(task_num - 1)
             print(f'Remove: {removed_task}')
             
         else:
             print('invalid task number')
             
     elif choice == '4':
              print('good bye')
              break
     else:
         print('invalid choice. please enter 1-4')

             
             
             
             
         