# History Game
## Overview

Welcome to the History Game, a web application that lets you play a fun and educational game about world history. This README file provides some basic information on how to install and use the application.

## Requirements

To use this application, you will need to have Python 3.10.6 installed on your computer, along with the following Python packages:

Flask 2.2.2

Flask-SQLAlchemy 3.0.3

openai 0.26.5

bcrypt 4.0.1

requests 2.28.2

selenium 4.8.3

## Installation
To install the application, simply clone this repository to your local machine and navigate to the root directory of the project in your terminal. Then, run the following command to start the Flask server:

`python app.py`

After that, you should be able to access the application by navigating to the following URL in your web browser:

`http://127.0.0.1:5000`

## Usage

Once you have the application running, you can start playing the History Game by following the on-screen instructions. The game consists of multiple choice questions about world history.

## Testing
Selenium tests are located in the selenium_tests directory, with separate files for authentication and selecting time period. 

To run the tests, you'll need to add the path to your local installation of Google Chrome Driver to the PATH environment service variable. Once this is done, you can run the individual python files to run the selenium tests.

To run the Selenium tests, you will need to install the Selenium package and a compatible web driver. Then, run each test file individually using the following command:

`python authentication_tests.py`

`python select_period_tests.py`


Note that the Selenium tests require an active internet connection and the application to be running.