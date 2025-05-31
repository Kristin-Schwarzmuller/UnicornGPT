from datetime import datetime


def log_time():
    """
    Logs the current date and time to a file named with today's date.
    The file is stored in the './data/' directory.
    """
    today = datetime.today().strftime("%Y%m%d")
    now = datetime.now()
    with open(f"./data/{today}_time.txt", "a") as f:
        f.write(f"{now}\n")
