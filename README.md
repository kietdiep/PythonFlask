# Workout Sharing Web App using Flask

## Overview
* This is a simple web application that allows users to share their workout routines with their peers. 

### Questions

1. What does this app do?
2. Give the command [go to] "pick a genre/category"
3. Give the command "Change screen Mode" 
4. More command and functionalities to come... 

### Prerequisites
* You need to create an account and get an API key in the MovieDatabase Api [Follow the link -> ](https://developers.themoviedb.org/3)

### Functionality

* It allows the user to click on a specific Genre and the app fetches movies according to that Genre. 
* Once the user clicks on a specific movie, the app will display information about the movie, from reviews to the cast. And according to the specific movie clicked the User will be able to see recommended movies that are similar to the clicked one. 
* You can also ask the app 

### Images
![Image](src/Img/darkmode.png)
![Image](src/Img/lightmode.png )
![Image](src/Img/infolight.png )
![Image](src/Img/infodark.png )

### Technologies
* To build this app the latest versions of Python, CSS, HTML, and Flask were used

- Flask_SQLAlchemy==2.5.1
- Flask==2.0.1
- itsdangerous==2.0.1
- Flask_WTF==0.15.1
- WTForms==2.3.3
- Flask_Mail==0.9.1
- Flask_Bcrypt==0.7.1
- Flask_Login==0.5.0
- Pillow==8.3.1
- secrets==1.0.2


### Installing 
* Clone the Repo and run 'pip install -r requirements.txt'
* After all libraries are installed, you can run with 'python run.py' 

