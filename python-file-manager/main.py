from pathlib import Path
import os


# list all files and folders

def list_files_and_folders():
    #List all files and folders in current directory
    try:
        path = Path('.')
        items = list(path.glob('*'))
        print("\n--- All Files & Folders ---")
        for i, item in enumerate(items):
            if item.is_file():
                print(f"{i+1} : {item} (FILE)")
            else:
                print(f"{i+1} : {item} (FOLDER)")
        print()
    except Exception as err:
        print(f"An error occurred as {err}")
        


#create a new file
def createfile():
    try:
        list_files_and_folders()
        name = input("Please tell your file name: ")
        p = Path(name)

        # Check if file already exists
        if not p.exists():
            with open(p, "w") as fs:
                data = input("What you want to write in this file: ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY")
        else:
            print("This file already exists")
    except Exception as err:
        print(f"An error occurred as {err}")


# Read a file
def readfile():
    try:
        list_files_and_folders()
        name = input("Please enter file name you want to read: ")
        p = Path(name)

        # Check if file exists
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print(data)
            print("FILE READ SUCCESSFULLY")
        else:
            print("File does not Exist")
    except Exception as err:
        print(f"An Error occurred as {err}")


# Update a file
def updatefile():
    try:
        list_files_and_folders()
        name = input("Which file you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():

             # Update options
            print("Press 1 for changing the name of your file")
            print("Press 2 for overwriting the data of your file")
            print("Press 3 for appending some content in your file")

            res = int(input("Select what update you want: "))
             # Rename file
            if res == 1:
                name2 = input("Enter new file name: ")
                p2 = Path(name2)
                p.rename(p2)
                print("File name changed successfully")
                
             # Replace file content
            elif res == 2:
                with open(p,'w') as fs:
                    data = input("Enter the Data: ")
                    fs.write(data)
                print("File Updated Successfully")

             # Add new content
            elif res == 3:
                with open(p,'a') as fs:
                    data = input("Enter the Data: ")
                    fs.write("\n" + data)
                print("File Updated Successfully")

            else:
                print("Invalid Option")
        
        else:
            print("File does not exist")
    except Exception as err:
        print(f"An Exception Occurred {err}")


# Delete a file

def deletefile():
    try:
        list_files_and_folders()
        name = input("Please enter file name you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(name)
            print("File Deleted Successfully")
        else:
            print("No such file exist")
    except Exception as err:
        print(f"An error occurred as {err}")



# Create a new folder
def createfolder():
  
    try:
        list_files_and_folders()
        name = input("Please tell your folder name: ")
        p = Path(name)
        if not p.exists():
            p.mkdir()
            print("FOLDER CREATED SUCCESSFULLY")
        else:
            print("This folder already exists")
    except Exception as err:
        print(f"An error occurred as {err}")


# Delete an empty folder
def deletefolder():
   
    try:
        list_files_and_folders()
        name = input("Please enter folder name you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_dir():
            # Check if folder is empty
            if not list(p.iterdir()):
                p.rmdir()  
                print("Folder Deleted Successfully")
            else:
                print("Folder is not empty! Only empty folders can be deleted.")
        else:
            print("No such folder exist")
    except Exception as err:
        print(f"An error occurred as {err}")



# Rename a folder
def renamefolder():
    
    try:
        list_files_and_folders()
        oldname = input("Enter current folder name: ")
        p = Path(oldname)
        if p.exists() and p.is_dir():
            newname = input("Enter new folder name: ")
            p2 = Path(newname)
            p.rename(p2)
            print("Folder renamed successfully")
        else:
            print("Folder does not exist")
    except Exception as err:
        print(f"An error occurred as {err}")




# Main menu
while True:
    print("\n" + "="*50)
    print(" FILE & FOLDER MANAGEMENT SYSTEM ")
    print("="*50)
    print("Press 1 for list files and folders")
    print("FILE OPERATIONS:")
    print("Press 2 for Creating a file")
    print("Press 3 for Reading a file")
    print("Press 4 for Updating a file")
    print("Press 5 for Deleting a file")
    print("\nFOLDER OPERATIONS:")
    print("Press 6 for Creating a folder")
    print("Press 7 for Deleting a folder (empty only)")
    print("Press 8 for Renaming a folder")
    print("\nPress 9 for Exiting")
    print("="*50)

    try:
        check = int(input("Please tell your response: "))

         # Execute selected option
        if check == 1:
            list_files_and_folders()
            
        elif check == 2:
            createfile()
            
        elif check == 3:
            readfile()
            
        elif check == 4:
            updatefile()
            
        elif check == 5:
            deletefile()
            
        elif check == 6:
            createfolder()
            
        elif check == 7:
            deletefolder()
            
        elif check == 8:
            renamefolder()
            
        elif check == 9:
            print("Exiting program... Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1-9")

       # Handle invalid input      
    except ValueError:
        print("Please enter a valid number!")