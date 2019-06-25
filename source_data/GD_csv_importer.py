'''
 For project to be more portable, option for downloading data is implemented
 For storing data in cloud google drive is used.
 As this specific data is imported from Kaggle, we could have used native Kaggle API
 As this API allows downloads. But for more general use we will direclty connect to the
 Google Drive.
'''

import time

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Authenticate
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

# Mount the Drive
drive = GoogleDrive(gauth)

# Files are located at : BI_Projects -> World_Bank_Indexes
# As objects are accessed by IDs first we will display all of them
main_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

for file1 in main_list:

    if 'BI_Projects' in file1['title']:

        BI_Project = drive.ListFile({'q': f"'{file1['id']}' in parents and trashed=false"}).GetList()

        for file2 in BI_Project:

            if 'World_Bank_Indexes' in file2['title']:

                World_Bank_Indexes = drive.ListFile({'q': f"'{file2['id']}' in parents and trashed=false"}).GetList()

                for file3 in World_Bank_Indexes:
                    if '.csv' in file3['title']:
                        start = time.time()
                        file3.GetContentFile(file3['title'])
                        end = time.time()

                        print(f"file {file3['title']} was downloaded in {end - start} seconds")
