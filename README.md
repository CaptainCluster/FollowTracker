# ***FollowTracker***

📰Basics
---
**FollowTracker** stores a GitHub url in **usernames.txt** file, and will then use that stored url to scrape
the follower data of that user. After the data has been successfully scraped, it will be saved into a **JSON** 
file, from where it can be retrieved and written into an **Excel** file (.xlsx). As of 9th of February 2024, 
the user will interact with the program via a **GUI** created with Tkinter, a more user-friendly solution than
the **terminal**.

📚Dependencies
---
**The program will need multiple different libraries in order to work! Make sure you have installed all
the dependencies before using this program!**

⬇️ To quickly install the **dependencies**, run this command:

```pip install -r requirements.txt```

After the dependencies have been installed, you should be good to go. 👍

📣Notable "issues"
---
* Some GitHub users have not defined a **Name** for their account. This is taken into account and handled as
  an exception. There's a placeholder created for these instances when writing the Excel file.

🚯Before you scrape
---
This program only scrapes data that has been, willingly, made **public** by GitHub users. It is **not** built in
a way that encourages malicious actions, like spam. It is, instead, built for **research** purposes to help its
users figure out how the followership of a selected profile has developed.

[Read the GitHub Acceptance Use Policy by clicking this!](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies)

🔧 Tools
---
The program comes with a tool for archiving follower data. This tool of preservation protects the data from being
overwritten. You can use the tool by executing **archiver.py**. It copies the data from **followerdata.json** and
then copies that data into another JSON file that has a name not being used.
