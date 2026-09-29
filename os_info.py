import datetime
import getpass
import json
import os
import platform
import shutil
import socket
import sys

# 1. Определяем ОС
if sys.platform.startswith("linux"):
    os_name = "Linux"
elif sys.platform == "darwin":
    os_name = "macOS"
elif sys.platform == "win32":
    os_name = "Windows"
else:
    os_name = "Unknown"

# 2. Собираем параметры
if os_name == "Windows":
    disk_path = os.environ.get("SystemDrive", "C:") + "\\"
else:
    disk_path = "/"
disk = shutil.disk_usage(disk_path)
gb = 1024 ** 3

info = {
    "os_name": os_name,
    "os_release": platform.release(),
    "os_version": platform.version(),
    "architecture": platform.machine(),
    "cpu_count": os.cpu_count(),
    "disk_total_gb": round(disk.total / gb, 2),
    "disk_free_gb": round(disk.free / gb, 2),
    "hostname": socket.gethostname(),
    "username": getpass.getuser(),
    "home_dir": os.path.expanduser("~"),
    "python_version": platform.python_version(),
    "collected_at": datetime.datetime.now().isoformat(timespec="seconds"),
}

# 3. Записываем результат в JSON
with open("os_info.json", "w", encoding="utf-8") as f:
    json.dump(info, f, ensure_ascii=False, indent=4)

print("ОС:", os_name)
print("Результат сохранён в os_info.json")
