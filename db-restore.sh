#!/bin/bash

# Directory where backups are stored
BACKUP_DIR=backups

echo "Restoring database..."

# Delete old database
rm db.sqlite3

# Create a new empty database
python manage.py migrate

# Find the latest backup JSON file
LATEST_JSON=$(ls -t $BACKUP_DIR/db_backup_*.json | head -1)

echo "Loading data from $LATEST_JSON"
python manage.py loaddata $LATEST_JSON

echo "Restore completed."
