import re
import os
import time
import random
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# for a safer side git pull before any other operation
os.popen("git pull")


class Watcher:
    # set the Path of the directory to monitor
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
        def checkForName(event):
            # to extract specific file name from the event path
            if '~' in event:
                value = event.split("~")[-1]
            else:
                value = event.split("\\")[-1]
            # to check which value gets printed
            return value
        
        def findPatternOfFunction(value):
            diff_output = subprocess.check_output(['git', 'diff', f'{value}']).decode()
            # this is the pattern to find def function present in it or not
            pattern = r"def\s+(\w+)\("
            # Use re.search() to find the first match of the pattern in the input string
            return re.findall(pattern, diff_output)
        
        def commit_message_find(pre_msg, match, s, count):
            if match:
                return f"{random.choice(pre_msg)} {match[-1]} function",0
                # else select random from s and change the value of commit_message
            else:
                count += 1
                print(f"count {count}")
                return None,count
                if count == 10:
                    count = 0
                    return random.choice(s),count

        
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event - %s." % event.src_path)
            

        elif event.event_type == 'modified':
            count = 0
            # Taken any action here when a file is modified.
            print("Received modified event - %s." % event.src_path)
            value = checkForName(event.src_path)
            print(value)
            # if the file is not Untitled then only perform operations
            if value != 'Untitled.ipynb':
                # get all the possible values such that it can related to changes
                s = ["changes", "update", "modification"]
                # pre_msg for commit messagfe
                pre_msg = ["Added Some Code to","Modified","Changes in "]
                # it returns the output of what all changes we have done to the file
                match = findPatternOfFunction(value)
                # set initial value to None
                commit_message = None
                # if a match is found then change the commit_message with the function name
                commit_message,count = commit_message_find(pre_msg, match, s, count)
                # print the commit message to see in terminal
                print(f"commit message is '{commit_message}'")
                # now git add the file
                os.popen(f'git add "{value}"')
                # time.sleep so that there will be no load at once at cmd
                time.sleep(1)
                time.sleep(1)
                # git commit along with message
                if commit_message != None:
                    os.popen(f'git commit -m "{commit_message}"')
                else:
                    pass
                time.sleep(1)
                # finally git push 🥳
                os.popen("git push")
                # os.popen("^C")
                # this timer such that it will again see in after 10 seconds
                time.sleep(10)
            # if not untitled then send message
            else:
                print(f"{value} is common so it wouldn't be added Rename it to add")

            

if __name__ == '__main__':
    w = Watcher()
    w.run()