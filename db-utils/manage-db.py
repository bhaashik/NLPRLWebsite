# NLPRLMain/db_utils/manage_db.py

import os
import subprocess
import shutil
from datetime import datetime
from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent.parent
BASE_DIR = Path(__file__).resolve().parent.parent

# Update this mapping according to routers
APP_TO_DB = {
    'default': 'db.sqlite3',
    # 'events': 'db_events.sqlite3',
    # 'faculties': 'db_faculties.sqlite3',
    # 'projects': 'db_projects.sqlite3',
    # 'courses': 'db_courses.sqlite3',
    # Add other apps here
}

DB_DIR = BASE_DIR
BACKUP_DIR = BASE_DIR / 'backups'

os.makedirs(BACKUP_DIR, exist_ok=True)

def create_blank_db():
    """Create blank db files if missing."""
    for db_name in APP_TO_DB.values():
        db_path = DB_DIR / db_name
        if not db_path.exists():
            print(f"Creating blank database: {db_name}")
            open(db_path, 'a').close()
    print("✔️ All databases checked or created.")

def backup_before_reset():
    """Backup all databases before reset."""
    backup_dir = BASE_DIR / "backups" / datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create a new backup folder with timestamp
    backup_dir.mkdir(parents=True, exist_ok=True)

    # Loop through all databases and copy them to the backup folder
    db_files = list(BASE_DIR.glob("*.sqlite3"))
    for db_file in db_files:
        shutil.copy(db_file, backup_dir)
        print(f"✅ Backed up {db_file.name} to {backup_dir}")

    print("🛑 Backup completed before reset.")


# def reset_all_databases():
#     """Delete all database files and create blank ones."""
#     confirm = input("⚠️ Are you sure you want to RESET all databases? (yes/no): ")
#     if confirm.lower() == 'yes':
#         for db_name in APP_TO_DB.values():
#             db_path = DB_DIR / db_name
#             if db_path.exists():
#                 print(f"Deleting {db_name}...")
#                 db_path.unlink()
#         create_blank_db()
#         print("✅ Reset done.")
#     else:
#         print("❌ Cancelled reset.")

def reset_all_databases():
    """Backup before reset, then reset all databases."""
    backup_before_reset()  # Backup first!

    db_files = list(BASE_DIR.glob("*.sqlite3"))

    for db_file in db_files:
        try:
            db_file.unlink()  # Delete the database file
            print(f"🔴 Deleted {db_file.name}")
        except FileNotFoundError:
            print(f"❌ {db_file.name} not found!")

    # Run migrations to re-create empty databases
    migrate_all_apps()  # Migrate all apps again

    print("✅ Databases reset successfully.")

def backup_all_databases():
    """Backup all databases to backups/ folder."""
    for db_name in APP_TO_DB.values():
        src = DB_DIR / db_name
        dest = BACKUP_DIR / db_name
        if src.exists():
            shutil.copy2(src, dest)
            print(f"🔄 Backup created for {db_name}")
    print("✅ All databases backed up.")

def restore_all_databases():
    """Restore all databases from backups/ folder."""
    confirm = input("⚠️ Are you sure you want to RESTORE all databases from backup? (yes/no): ")
    if confirm.lower() == 'yes':
        for db_name in APP_TO_DB.values():
            backup_file = BACKUP_DIR / db_name
            db_path = DB_DIR / db_name
            if backup_file.exists():
                shutil.copy2(backup_file, db_path)
                print(f"🔄 Restored {db_name}")
        print("✅ All databases restored from backup.")
    else:
        print("❌ Cancelled restore.")

def list_databases():
    """Show the list of databases."""
    print("\n📂 Current databases:")
    for db_name in APP_TO_DB.values():
        db_path = DB_DIR / db_name
        status = "✅ Exists" if db_path.exists() else "❌ Missing"
        print(f" - {db_name}: {status}")

def migrate_all_apps():
    """Run makemigrations and migrate for all apps."""
    print("🔄 Running makemigrations...")
    subprocess.call(["python", BASE_DIR / "manage.py", "makemigrations"])

    print("🔄 Running migrate...")
    subprocess.call(["python", BASE_DIR / "manage.py", "migrate"])

    print("✅ All apps migrated successfully.")

def backup_all_databases():
    """Backup all databases manually."""
    backup_dir = BASE_DIR / "backups" / datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_dir.mkdir(parents=True, exist_ok=True)

    db_files = list(BASE_DIR.glob("*.sqlite3"))
    for db_file in db_files:
        shutil.copy(db_file, backup_dir)
        print(f"✅ Backed up {db_file.name} to {backup_dir}")

    print("📦 All databases backed up successfully.")


# Quick CLI interface
if __name__ == "__main__":
    # print("""
    # ==== DATABASE MANAGEMENT UTILITY ====
    # 1. Create blank db files
    # 2. Reset all databases
    # 3. Backup all databases
    # 4. Restore databases from backup
    # 5. List databases
    # 0. Exit
    # """)
    # choice = input("Enter your choice: ").strip()
    # if choice == '1':
    #     create_blank_db()
    # elif choice == '2':
    #     reset_all_databases()
    # elif choice == '3':
    #     backup_all_databases()
    # elif choice == '4':
    #     restore_all_databases()
    # elif choice == '5':
    #     list_databases()
    # else:
    #     print("Bye!")
    # print("""
    # ==== DATABASE MANAGEMENT UTILITY ====
    # 1. Create blank db files
    # 2. Reset all databases
    # 3. Backup all databases
    # 4. Restore databases from backup
    # 5. List databases
    # 6. Run makemigrations and migrate (for all apps)
    # 0. Exit
    # """)
    # choice = input("Enter your choice: ").strip()
    # if choice == '1':
    #     create_blank_db()
    # elif choice == '2':
    #     reset_all_databases()
    # elif choice == '3':
    #     backup_all_databases()
    # elif choice == '4':
    #     restore_all_databases()
    # elif choice == '5':
    #     list_databases()
    # elif choice == '6':
    #     migrate_all_apps()
    # else:
    #     print("Bye!")

    # Quick CLI interface

    if __name__ == "__main__":

        print("BASE_DIR: {}".format(BASE_DIR))

        print("\n")

        print("""
        ==== DATABASE MANAGEMENT UTILITY ====
        1. Create blank db files
        2. Safe reset (Backup before reset)
        3. Backup all databases
        4. Restore databases from backup
        5. List databases
        6. Run makemigrations and migrate (for all apps)
        0. Exit
        """)
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            create_blank_db()
        elif choice == '2':
            reset_all_databases()  # Safe reset
        elif choice == '3':
            backup_all_databases()
        elif choice == '4':
            restore_all_databases()
        elif choice == '5':
            list_databases()
        elif choice == '6':
            migrate_all_apps()
        else:
            print("Bye!")
