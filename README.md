# Game-Buddy
Your own Steam Store buddy; ready to help you find your next favorite game!
GAME BUDDY

Link to the Game Buddy project: Game-Buddy Github

~Requires languages:
Python

~Required libraries:
Requests
Beautifulsoup
Time
Json
Urljoin
urlparse
xml.etree

~CAUTION: games.json is a large file. Opening it may slow your computer while it is loading in, or crash your web browser. 

~How to download:
The only file you will need to make it run is the gamebuddy.html. If you are using Visual Studio Code to open the file, you can use the Live Server VSC extension to open the project in your web browser.

Installation steps:
1) Download the file from the Game Buddy Github page
2) Open the file in Visual Studio Code. If you do not have VSC here is a link.
3) From there you will want to add Live Server as an extension. The extension ID for Live Server is “ritwickdey.LiveServer”. Here is a link to the extension as well..
4) After downloading the extension, if you right click the gamebuddy.html file in the Explorer tab it will give you the option ‘Open with Liver Server”. Click that option.
5) From there, the site will open in your browser. Welcome to Game Buddy.


~The other files were programs used to create this project. Here is a summary of each:
-gamebuddy.html is the actual delivered project. It is an html file that when opened will show the finished results of Game Buddy.
-games.json holds all the game data for this project in json format. It contains  5,596 games total. Under each game is data about: its URL, title, release date, rating, on sale status, original price, sale price (if any).
-Scrpper2 is a python program we used to scrape the data contained in the games,json file from the Steam store. It is called scrpper2 because it can’t be a program without some typos, and it was not our first attempt at a scraper program. 
-sitemap.py is also a python program that was used to crawl through the steam store to collect the URLs for its site. The URLs were saved in the following file, steamsitemap.xml
-steamsitemap.xml is the sitemap that contains all the URLs from which we scraped the game data from.
-urls.json is a json file storing all the URLs from the sitemap. It wasn’t needed in the end but was part of the process so we included it.

We hope you enjoy Game Buddy as much as we enjoyed making it!
Sincerely,
Kaylynn, Kaitlyn, Taylor, and Ayesha
