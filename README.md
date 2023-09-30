# FollowTracker
*Saves the usernames and names of the GitHub followers that follow a selected URL.*

📰Basics
---
This program stores a GitHub url in **usernames.txt** file and then will read the line, stored in it, every 
time the this program is executed. **BeautifulSoup** and **Requests** are used to scrape the data. After 
the data has been successfully scraped, it will be saved into a **JSON** file, from where it can be retrieved
and written into an **Excel** file (.xlsx).

📚Dependencies
---
**The program will need multiple different libraries in order to work! Make sure you have installed all
the dependencies before using this program!**

💻 For scraping data:

```pip install beautifulsoup4```
```pip install requests```

✍️ For writing data into an Excel file:

```pip install openpyxl```

After these have been installed, you should be good to go. 👍

📣Notable "issues"
---
* Some GitHub users have not defined a **Name** for their account. This is taken into account and handled as
  an exception. There's a placeholder created for these instances when writing the Excel file.
