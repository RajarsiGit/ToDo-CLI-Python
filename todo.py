import os
import sys
import datetime

now = datetime.datetime.now()

todo_file = os.getcwd() + '\\todo.txt'
done_file = os.getcwd() + '\\done.txt'

if len(sys.argv) <= 1 or (len(sys.argv)==2 and sys.argv[1]=='help'):
    strbuf = '''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics'''
    sys.stdout.buffer.write(strbuf.encode())

elif len(sys.argv)==2:
    if sys.argv[1]=='ls':
        try:
            with open(todo_file, 'r') as todo:
                todo_task = todo.readlines()
            if len(todo_task) < 1:
                sys.stdout.buffer.write('There are no pending todos!'.encode())
                exit()
            for i, item in zip(range(len(todo_task), 0, -1), reversed(todo_task)):
                strbuf = '[' + str(i) + '] ' + item
                sys.stdout.buffer.write(strbuf.encode())
        except Exception as e:
            sys.stdout.buffer.write('There are no pending todos!'.encode())

    elif sys.argv[1]=='report':
        with open(todo_file, 'r') as todo:
            todo_task = todo.readlines()
        with open(done_file, 'r') as done:
            done_task = done.readlines()
        strbuf = str(now.strftime("%Y-%m-%d")) + ' Pending : ' + str(len(todo_task)) + ' Completed : ' + str(len(done_task))
        sys.stdout.buffer.write(strbuf.encode())
    
    elif sys.argv[1]=='add':
        sys.stdout.buffer.write('Error: Missing todo string. Nothing added!\n'.encode())

    elif sys.argv[1]=='del':
        sys.stdout.buffer.write('Error: Missing NUMBER for deleting todo.\n'.encode())

    elif sys.argv[1]=='done':
        sys.stdout.buffer.write('Error: Missing NUMBER for marking todo as done.\n'.encode())

elif len(sys.argv)==3:
    if sys.argv[1]=='add':
        with open(todo_file, 'a') as todo:
            todo.write(sys.argv[2] + '\n')
        strbuf = 'Added todo: "' + sys.argv[2] + '"'
        sys.stdout.buffer.write(strbuf.encode())

    elif sys.argv[1]=='del':
        with open(todo_file, 'r') as todo:
            todo_task = todo.readlines()
            if int(sys.argv[2]) > len(todo_task):
                strbuf = 'Error: todo #' + sys.argv[2] + ' does not exist. Nothing deleted.'
                sys.stdout.buffer.write(strbuf.encode())
                exit()
            elif int(sys.argv[2]) < 1:
                strbuf = 'Error: todo #' + sys.argv[2] + ' does not exist. Nothing deleted.'
                sys.stdout.buffer.write(strbuf.encode())
                exit()
            todo_task.pop(int(sys.argv[2]) - 1)
            with open(todo_file, 'w') as todo:
                todo.writelines(todo_task)
        strbuf = 'Deleted todo #' + sys.argv[2]
        sys.stdout.buffer.write(strbuf.encode())

    elif sys.argv[1]=='done':
        with open(todo_file, 'r') as todo:
            todo_task = todo.readlines()
            if int(sys.argv[2]) > len(todo_task):
                strbuf = 'Error: todo #' + sys.argv[2] + ' does not exist.'
                sys.stdout.buffer.write(strbuf.encode())
                exit()
            elif int(sys.argv[2]) < 1:
                strbuf = 'Error: todo #' + sys.argv[2] + ' does not exist.'
                sys.stdout.buffer.write(strbuf.encode())
                exit()
            with open(done_file, 'a') as done:
                done.writelines('x ' + now.strftime("%Y-%m-%d") + ' ' + todo_task[int(sys.argv[2]) - 1])
            todo_task.pop(int(sys.argv[2]) - 1)
            with open(todo_file, 'w') as todo:
                todo.writelines(todo_task)
        strbuf = 'Marked todo #' + sys.argv[2] + ' as done.'
        sys.stdout.buffer.write(strbuf.encode())
