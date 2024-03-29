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
To install the application, clone this repository to your local machine. After you have successfully cloned this repository to your local machine, proceed to the OpenAi API Key Setup part.
### **OpenAI API Key Setup**
To use the AI-powered feature in this application, you will need to obtain an OpenAI API key and insert it into the openai_api.py file. 

**Follow these steps to set up your OpenAI API key:**

**1**. Visit the OpenAI website and create an account.

**2**. Once you have an account, navigate to the API tokens page in the OpenAI documentation and generate an API key.

**3**. Copy the API key and paste it into the openai.apy file at line 7 in the following line of code:

`self.api_key = "INSERT_YOUR_API_KEY_HERE"`

**4**. Replace `INSERT_YOUR_API_KEY_HERE` with your actual API key.

**5**. Start the Flask server by running the command `python app.py` in your terminal.

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