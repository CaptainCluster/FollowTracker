# ***FollowTracker***

**FollowTracker** stores a GitHub url in **usernames.txt** file, and will then use that stored url to scrape
the follower data of that user. After the data has been successfully scraped, it will be saved into a **JSON** 
file, from where it can be retrieved and written into an **Excel** file (.xlsx). As of 9th of February 2024, 
the user will interact with the program via a **GUI** created with Tkinter, a more user-friendly solution than
the **terminal**.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

📚Dependencies
---
**The program will need multiple different libraries in order to work! Make sure you have installed all
the dependencies before using this program!**

⬇️ To quickly install the **dependencies**, run this command:

```pip install -r requirements.txt```

On top of that, **tkinter** is used. If you use a Debian-based Linux distro, you can install it with
the following command:


```sudo apt install python3-tk```

After the dependencies have been installed, you should be good to go. 👍

🚯Before you scrape
---
This program receives its data through the **GitHub API**. This application was made for **research** purposes,
and to help users figure out how their followership has developed. Please do not use the application for any
**malicious** purposes, such as spamming.

[Read the GitHub Acceptance Use Policy by clicking this!](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies)

🔧 Tools
---
The program comes with a tool for archiving follower data. This tool of preservation protects the data from being
overwritten. You can use the tool by executing **archiver.py**. It copies the data from **followerdata.json** and
then copies that data into another JSON file that has a name not being used.
