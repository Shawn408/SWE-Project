# Milestone Project 1

## Main Code Files
1. App.py
2. TMDB.py
3. Wiki.py

## Design Files
1. Index.html, Login.html, Signup.html
2. Style.css, Login.css, Signup.css

## Technologies
The technologies used in this project are a long list. First, I needed to download flask, requests, python-dotenv, flask-login, and flask-sqalchemy which were essential for the project. Flask was used to create the web app, and requests made the TMDB and Wikipedia API calls. Python-dotenv was used to find the .env file, which holds the API key from TMDB, and load it to the TMDB file so the API calls can be accessed properly. Flask-Login was used for the login and authentication of the user. Flash-SQAlchmey is used for the creation and usuage of the database produced in heroku. The other technologies used were HTML and CSS. The HTML and CSS were used to create the web app's design. HTML set up the variables passed from app.py to the file. CSS was used to style the web app as I added a 3D pop design for the movie titles when you hover over them. The link between appy.py and the HTML and CSS files was through Jinja2. Heroku was used to make a web app that can be accessed anywhere. There were two files needed for the upload of app.py to Heroku. These were requirements.txt and Procfile. Requirements.txt was used to install the requirements for the app. Procfile was used to tell Heroku what to do with the app.

## Setup
- You will need to install flask, requests, and python-dotenv in your WSL terminal if you are using Windows or use the terminal provided in Mac. I installed them using pip3 install flask, requirements, python-dotenv, flask-login, flask-sqlachemy. Install them individually, not together, as shown as that was just an example of what command to use. 
- You will also need to acquire an API key from TMDB. This can be freely obtained by making an account then you into account settings. In the API tab, you will need to fill out all information like name, the reason for the API, and a site. I used www.example.com as a fill-in for the site location. After you have acquired the API key, you will need to add it to the .env file. Since we will not hard code the API key as anyone can access it, we will need to add it to the .env file. Use the os library to open the .env file and add the API key to the file. You variable the same you will in the heroku file. Then use the key to access the get movie API for the TMDB.py file.
- Now make the WIKI.py file. This is the file that will be used to access the Wikipedia API. You will not need an API key for this file. Setup the parameters specified in the Wikipedia API to make the wiki URL link.
- Make a database using heroku. This is the database that will be used to store the user's information in one table and will be used to store movie reviews with ratings in another table.
- Make an app.py file. This is the file that will be used to access the TMDB API and WIKI API. You will need to import both Flask and render_template from the flask. You will also need to import the TMDB and Wiki files. Setup the app route for the login page which will how you will login in to get into the webpage. Setup the app route for signup page where you must signup to have your username be added to the Account database. Setup the app route to use the two functions from the TMDB and Wiki files. Then in render_template, you initialize the TMDB and Wiki variables with the index.html. Then you render the template.
- Make an index.html, login.html, signup.html files. This is the file that will be used to create the web app's design.
- Make a style.css, login.css, signup.css files. This is the file that will be used to style the web app.
- Make requirements.txt, where you will add all the libraries you are using except the os library as that is part of the python standard library. So you will need to add the flask, requests, python-dotenv, flask-login, flask-sqlachemmy, psycopg2 libraries without the import part.
- Make Procfile.txt, where you will add the command to run the app.py file. This is the command that will be used to run the app.py file. 

## Heroku
https://serene-anchorage-71808.herokuapp.com/

## Implementation Difference
The implementation between execution and planning was pretty similar for this project. The only difference was that I had to maybe have a different way of rerouting the login to signup if the account username does not exist in the database. I did not have to do this for the signup page because I was using the flask-login library to handle the login. So I setup a simple signup page that will check if the username exists in the database. If it does, then it will redirect to the login page. If it does not, then it will add the username to the database and redirect to the login page.

## Techincal Issues
1. The most technical issue was the Wifi network. The school wifi network was not working correctly. I would run the app locally, which caused a long loading screen which was not what I wanted. I used my hotspot to connect to the app with better speed. This was very troublesome as I was on campus most of the time the last two weeks. My home network was fine when it came to load up the app locally. Heroku, fortunately, was not affected by the school wifi issue; hence the app loaded better. So my thoery is that the wifi network on campus must have a issue with producing webpages which are not avabilable on the internet as they are locally produced through VS Code.
2. The other technical issue was figuring out how to properly route the login to signup if username not existing or the login to main page then the signup to login page once username was added. The issue was I had never learned how flask-login worked hence it was a issue. The documents on it were not also as helpful, but I was able to research more online and found couple of videos and documents. I was able to figure out the signup was not adding to the database correctly so I restructured the app route for signup which was able to finally add the username to the database. Then the pathway worked perfectly.

## Bonus
1. I added a logout function which lets user logout of the web app. The login page will appear everytime you go to web app but if you want to logout, you can click the logout link under the row of links.
2. I added a placeholder feature to the movie id form. This way the person does not need to have to worry about the movie id. The movie id will be automatically generated for the user.