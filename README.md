# Un Minuto Pitch

## Author

[**Ian Wanarua**]()

## Description

This is a python-flask application that allows users to post one minute pitches and also allows other users who have signed up to comment and upvote or downvote a pitch. It also allows a person to signup to be able to access the functionalities of the application.

## Technologies Used

* Flask
* Html
* Css
* Bootstrap
* python3.8
* Heroku

## Requirements

This program requires python3.+ installed, so as to run. A guide on how to install python on various platforms can be found [here](https://www.python.org/)

## Setup/Installation

To get the code..

1. Cloning the repository:
  ```bash
  https://github.com/Ianwanarua/pitches.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd pitches
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python3.8 manage.py server
  ```
5. Testing the application
  ```bash
  python3.8 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.