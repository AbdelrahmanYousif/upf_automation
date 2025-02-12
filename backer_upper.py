import shutil
from datetime import datetime

source = "C:/Users/abdor/OneDrive/Dokument/Upf_automation/source/folder"
destination = "C:/Users/abdor/OneDrive/Dokument/Upf_automation/backups/backup"

def backup_files():
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    target = f"{destination}_{timestamp}"
    shutil.copytree(source, target, dirs_exist_ok=True)

if __name__== "__main__":
    backup_files()