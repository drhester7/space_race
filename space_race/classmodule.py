from datetime import datetime
from .funcmodule import load_json
from .funcmodule import save_json
import json


class tech_class():
    def __init__(self, config):
        self.task_file = config['space_race']['tasks_file']
        self.tasks = load_json(self.task_file)

    def init_tech(self, name, description):
        if name in self.tasks:
            print(f"Task '{name}' already exists.")
            return

        print(f'Initializing task {name}...')
        self.tasks[name] = {
            "name": name,
            "description": description,
            "start_time": None,
            "end_time": None,
            "elapsed_time": None
        }
        save_json(self.task_file, self.tasks)

    def calculate_elapsed(self, name):
        task = self.tasks.get(name)
        start_time = datetime.fromisoformat(task["start_time"])
        end_time = datetime.fromisoformat(task["end_time"])
        return str(end_time - start_time)

    def start_research(self, name = None):
        if not name:
            name = self.get_default()

        task = self.tasks.get(name)
        if not task:
            self.init_tech(name, "")
            task = self.tasks.get(name)
        
        print(f'Starting research on {name}...')
        task["start_time"] = datetime.now().isoformat()
        save_json(self.task_file, self.tasks)

    def halt_research(self, name):
        task = self.tasks.get(name)
        task["end_time"] = datetime.now().isoformat()
        task["elapsed_time"] = self.calculate_elapsed(name)
        self.calculate_elapsed(name)
        save_json(self.task_file, self.tasks)
        json_string = json.dumps(task, indent=4)
        print(json_string)

    def delete_reasearch(self, name):
        task = self.tasks.get(name)
        if not task:
            print(f"Task '{name}' does not exist.")
            return

        del self.tasks[name]
        save_json(self.task_file, self.tasks)
        print(f"Task '{name}' deleted.")

    def set_default(self, name):
        task = self.tasks.get(name)
        if not task:
            print(f"Task '{name}' does not exist.")
            return
        for task in self.tasks:
            self.tasks[task]["default"] = False
        self.tasks[name]["default"] = True
        save_json(self.task_file, self.tasks)
        print(f"Task '{name}' set as default.")

    def get_default(self):
        for task in self.tasks:
                if self.tasks[task]["default"]:
                    name = self.tasks[task]["name"]
                    break
        return name