import TaskManagerCLI.Endpoints as Endpoints
#import Service
import os


class AppController:
    def __init__(self):
        os.getcwd()
        self.Endpoints = Endpoints.Endpoints(self)
        #self.Service = Service.Service(self)


