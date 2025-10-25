import argparse
import logging
import os
from utils import add_task, list_tasks, delete_task
from dotenv import load_dotenv

load_dotenv()

TODO_FILE = os.getenv("TODO_FILE", "tasks.txt")

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(description="Simple CLI To-Do App")
parser.add_argument("command", choices=["add", "list", "delete"])
parser.add_argument("task", nargs="?", help="Task id")

args = parser.parse_args()

if args.command == "add" and args.task:
    add_task(TODO_FILE, args.task)
elif args.command == "list":
    list_tasks(TODO_FILE)
elif args.command == "delete" and args.task:
    delete_task(TODO_FILE, int(args.task))
else:
    logging.error("Invalid Entry")
