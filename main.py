import TaskManagerCLI.TaskManagerCLI as tm

if __name__ == '__main__':
    TM = tm.AppController()
    endpoints = TM.Endpoints
    service = TM.Service
    service.add_task("Create Task Manager CLI")
    service.add_task("Be proud of myself for acomplishing this")
    service.add_task("test")
    service.mark_task("test", 1)
    service.update_task("test", "new name")
    service.mark_task("new name", 2)
    endpoints.LinkedList.to_string()
    service.delete_task("new name")
    endpoints.LinkedList.to_string()
