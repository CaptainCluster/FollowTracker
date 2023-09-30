#Asking the user what profile they want to follow. The username  will be added to the url. 
#The url will then be stored into the username.txt file.

def askProfileName():
    urlStart = "https://github.com/" #All we have to do is add the username to the end to get a valid url

    username = input("Type your GitHub username over here: ")

    url = urlStart + username

    usernameFile = open("src/username.txt", "w", encoding="utf-8")
    usernameFile.write(url)

    usernameFile.close()
