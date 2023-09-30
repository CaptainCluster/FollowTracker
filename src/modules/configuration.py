#If no GitHub user url has been written in username.txt, 
#it'll be defined and writ
def askProfileName():
    urlStart = "https://github.com/"
    username = input("Type your GitHub username over here: ")
    url = urlStart + username #https://github.com/[username]
    
    #Writing the url to the .txt file so that it can be read before scraping
    usernameFile = open("src/username.txt", "w", encoding="utf-8")
    usernameFile.write(url)

    usernameFile.close()
