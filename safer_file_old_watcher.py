import os
import time
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

os.popen("git pull")


class Watcher:
    DIRECTORY_TO_WATCH = "C:\GFG_DataScience\DSA"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event - %s." % event.src_path)
            os.popen('git add .\img')
            time.sleep(1)
            time.sleep(1)
            if '~' in event.src_path:
                value = event.src_path.split("~")[-1]
            else:
                value = event.src_path.split("\\")[-1]
            print("created")
            os.popen(f"git commit -m Created {value}")
            time.sleep(1)
            os.popen("git push")
            

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print("Received modified event - %s." % event.src_path)
            # event_name = event.src_path.split("~")
            # print("Event Name",event_name[-1])
#             value = "Problem Solving.ipynb"
#             value2 = event.src_path.split("~")[-1]

            if '~' in event.src_path:
                value = event.src_path.split("~")[-1]
            else:
                value = event.src_path.split("\\")[-1]
            print(value)
#             print("Experiment name:" , value2)
            if value != 'Untitled.ipynb':
                print("GIt adding for: ", value)
            else:
                print(f"{value} is common so it wouldn't be added Rename it to add")
            if value != 'Untitled.ipynb':
                os.popen(f'git add "{value}"')
                time.sleep(1)
                time.sleep(1)
                s = ["changes", "update", "modification"]
                os.popen(f"git commit -m {random.choice(s)}")
                time.sleep(1)
                os.popen("git push")
                # os.popen("^C")
                time.sleep(10)

            

if __name__ == '__main__':
    w = Watcher()
    w.run()