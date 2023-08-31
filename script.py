import os
import boto3
from datetime import datetime, timedelta
import time

# AWS credentials
AWS_ACCESS_KEY = 'AKIAU2MEWKYKTNSO77KL'
AWS_SECRET_KEY = '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'

# S3 bucket details
BUCKET_NAME = 'automatebackups'
BACKUP_FOLDER = 'backups'

# Local folder to back up
LOCAL_FOLDER = '/Users/PRINCESSSADIYA/Downloads/backups/script.py.zip'

# Interval between backups (in seconds)
BACKUP_INTERVAL = 24 * 60 * 60  # 24 hours


def upload_to_s3(local_path, s3_path):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
    s3.upload_file(local_path, BUCKET_NAME, s3_path)

def backup_files(local_path):
    # Extract the file name from the full local path
    file_name = os.path.basename(local_path)
    
    # Timestamp for backup file
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_filename = f'Backup_{timestamp}_{file_name}'
    backup_path = os.path.join(BACKUP_FOLDER, backup_filename)

    # Upload the local file to S3
    upload_to_s3(local_path, backup_path)

def main():
    while True:
        try:
            backup_files('/Users/PRINCESSSADIYA/Downloads/backups/script.py.zip')
            print("Backup successful.")
        except Exception as e:
            print(f"Backup failed: {e}")
        
        time.sleep(BACKUP_INTERVAL)

if __name__ == '__main__':
    main()