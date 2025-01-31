import TaskManagerCLI.TaskManagerCLI as tm

if __name__ == '__main__':
    TM = tm.AppController()
    endpoints = TM.Endpoints
    tasks = endpoints.LinkedList
    tasks.append("Clean room 1")
    tasks.append("Clean room 2")
    tasks.insert("Clean room 3", "Clean room 2")
    tasks.to_string()
    print()
    tasks.remove("Clean room 1")
    tasks.to_string()

