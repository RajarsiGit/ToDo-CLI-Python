import os
import sys
import datetime

TODO_FILE = os.path.join(os.getcwd(), 'todo.txt')
DONE_FILE = os.path.join(os.getcwd(), 'done.txt')

USAGE = '''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics'''


def read_todos():
    try:
        with open(TODO_FILE, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return []


def write_todos(tasks):
    with open(TODO_FILE, 'w') as f:
        f.writelines(tasks)


def read_done():
    try:
        with open(DONE_FILE, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return []


def validate_number(n_str, tasks, action):
    try:
        n = int(n_str)
    except ValueError:
        print(f'Error: todo #{n_str} does not exist. {action}')
        return None
    if n < 1 or n > len(tasks):
        print(f'Error: todo #{n_str} does not exist. {action}')
        return None
    return n


def cmd_help():
    print(USAGE)


def cmd_ls():
    tasks = read_todos()
    if not tasks:
        print('There are no pending todos!')
        return
    for i, task in zip(range(len(tasks), 0, -1), reversed(tasks)):
        print(f'[{i}] {task.rstrip()}')


def cmd_add(text):
    with open(TODO_FILE, 'a') as f:
        f.write(text + '\n')
    print(f'Added todo: "{text}"')


def cmd_del(n_str):
    tasks = read_todos()
    n = validate_number(n_str, tasks, 'Nothing deleted.')
    if n is None:
        return
    tasks.pop(n - 1)
    write_todos(tasks)
    print(f'Deleted todo #{n_str}')


def cmd_done(n_str):
    tasks = read_todos()
    n = validate_number(n_str, tasks, '')
    if n is None:
        return
    today = datetime.date.today().strftime('%Y-%m-%d')
    with open(DONE_FILE, 'a') as f:
        f.write(f'x {today} {tasks[n - 1].rstrip()}\n')
    tasks.pop(n - 1)
    write_todos(tasks)
    print(f'Marked todo #{n_str} as done.')


def cmd_report():
    today = datetime.date.today().strftime('%Y-%m-%d')
    pending = len(read_todos())
    completed = len(read_done())
    print(f'{today} Pending : {pending} Completed : {completed}')


def main():
    args = sys.argv[1:]

    if not args or args[0] == 'help':
        cmd_help()
    elif args[0] == 'ls':
        cmd_ls()
    elif args[0] == 'add':
        if len(args) < 2:
            print('Error: Missing todo string. Nothing added!')
        else:
            cmd_add(args[1])
    elif args[0] == 'del':
        if len(args) < 2:
            print('Error: Missing NUMBER for deleting todo.')
        else:
            cmd_del(args[1])
    elif args[0] == 'done':
        if len(args) < 2:
            print('Error: Missing NUMBER for marking todo as done.')
        else:
            cmd_done(args[1])
    elif args[0] == 'report':
        cmd_report()


if __name__ == '__main__':
    main()
