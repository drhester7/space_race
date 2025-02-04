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

        self.tasks[name] = {
            "name": name,
            "description": description,
            "start_time": None,
            "end_time": None,
            "elapsed_time": None
        }
        save_json(self.task_file, self.tasks)
        print(f"Task '{name}' initialized.")

    def calculate_elapsed(self, name):
        task = self.tasks.get(name)
        start_time = datetime.fromisoformat(task["start_time"])
        end_time = datetime.fromisoformat(task["end_time"])
        return str(end_time - start_time)

    def start_research(self, name):
        task = self.tasks.get(name)
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