import os

def desktop():
    pass

def get_usernames():
    users_list = os.listdir(path="C:/Users")
    usernames = []
    for item in users_list:
        if item != "Public" and item != "All Users" and item != "Default User" and item != "Default" and item != "desktop.ini":
            print(item)
            usernames.append(item)
    return usernames

def inspect_user(username):
    user_directory = "C:/Users/" + username
    dir_content = os.listdir(path=user_directory)
    for file in dir_content:
        file_segmented = file.split('.')
        if len(file_segmented) != 1:
            if file_segmented[1] == "exe":
                print("del " + user_directory.replace('/', '\\') + "\\" + file)
                os.system("del " + user_directory.replace('/', '\\') + "\\" + file)
    desktop_user_directory = user_directory + "/Desktop"
    desktop_content = os.listdir(path=desktop_user_directory)
    for item in desktop_content:
        filename_splited = item.split(".")
        if len(filename_splited) != 1:
            if filename_splited[1] == "exe":
                os.system("del " + desktop_user_directory.replace('/', '\\') + "\\" + item)
                print("Executable file deleted succesfully")

def inspact_users_files(usernames):
    for user in usernames:
        inspect_user(user)

def main():
    usernames = get_usernames()
    inspact_users_files(usernames)

if __name__ == '__main__':
    main()