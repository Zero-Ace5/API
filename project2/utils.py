import logging


def add_task(file, task):
    with open(file, "a") as f:
        f.write(task + '\n')
    logging.info(f"Added task: {task}")


def list_tasks(file):
    try:
        with open(file) as f:
            tasks = f.readlines()
            if not tasks:
                logging.info("No Tasks Added")
            for idx, t in enumerate(tasks, 1):
                print(f"{idx}. {t.strip()}")
    except FileNotFoundError:
        logging.info("Task file unavailable")


def delete_task(file, task_id):
    try:
        with open(file) as f:
            tasks = f.readlines()
        if 0 < task_id <= len(tasks):
            removed = tasks.pop(task_id-1)
            with open(file, "w") as f:
                f.writelines(tasks)
            logging.info(f"Deleted: {removed.strip()}")
        else:
            logging.error("Task ID not valid")
    except FileNotFoundError:
        logging.info("Task file unavailable")
