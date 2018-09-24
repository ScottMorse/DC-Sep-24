
class ToDo:

    _tasks = []
    
    @classmethod
    def tasks(self):
        ToDo._tasks.sort(key=lambda task: task.priority,reverse=True)
        return ToDo._tasks
    
    @classmethod
    def add_task(self,task):
        if not isinstance(task, Task):
            raise ValueError("Not a Task object in argument.")
        ToDo._tasks.append(task)

    @classmethod
    def view_tasks(self):
        print(ToDo.tasks())
    
    @classmethod
    def clear_all_tasks(self):
        check = input("Are you sure? (y/n)")
        if check != 'y':
            return
        ToDo._tasks = []
    
    @classmethod
    def mark_as_complete(self,task):
        if task not in ToDo.tasks():
            print('Task not found.')
            return
        del ToDo._tasks[self._tasks.index(task)]

class Task:

    def __init__(self,title,priority=0):
        if not isinstance(title, str):
            raise ValueError('Task title must be a string.')
        if not isinstance(priority, int):
            raise ValueError('Priority must be an integer.')
        if priority < 0:
            raise ValueError('Priority must be a positive number or 0.')
            
        self._title = title
        self._priority = priority
        ToDo.add_task(self)
    
    @property
    def title(self):
        return self._title
    
    @property
    def priority(self):
        return self._priority

    def __repr__(self):
        return self.title
