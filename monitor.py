import psutil
import time
from datetime import datetime

LOG_FILE = "logs/system.log"

def write_log(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

for i in range(5):

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    message = (
        f"{datetime.now()} | "
        f"CPU:{cpu}% "
        f"MEM:{memory}% "
        f"DISK:{disk}%"
    )

    print(message)

    write_log(message)

    if cpu > 80:
        write_log("ALERT: CPU HIGH")

    time.sleep(10)