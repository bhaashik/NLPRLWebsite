#!/bin/bash

# Name of backup file
DATE=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR=backups
DB_FILE=db.sqlite3
DUMP_FILE=$BACKUP_DIR/db_backup_$DATE.json

# Create backup directory if not exists
mkdir -p $BACKUP_DIR

echo "Backing up database..."
cp $DB_FILE $BACKUP_DIR/db_backup_$DATE.sqlite3

echo "Dumping data..."
python manage.py dumpdata --natural-primary --natural-foreign > $DUMP_FILE

echo "Backup completed: $BACKUP_DIR"
