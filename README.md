# Python Projects

This repository showcases a collection of projects developed using Python, the Django framework and Tkinter. Additionally, it contains Artificial Intelligence and Machine Learning projects using Python.

## Projects

### [Webpage Generator Project](https://github.com/zsuzsannamangu/Python-Projects/tree/master/Python-Projects/WebPage_Generator)
- **Description:** This program can automatically create a basic HTML web page and display the text that the user inputted into the text field.
- **Technologies Used:** Python, Tkinter

### [File Transfer Project](https://github.com/zsuzsannamangu/Python-Projects/tree/master/Python-Projects/File_Transfer_Assignment)
- **Description:** With this program, you can move files from one folder to another with the click of a button.
- **Technologies Used:**  Python, Tkinter and the shutil module for moving files.

### [Checkbook Project](https://github.com/zsuzsannamangu/Python-Projects/tree/master/Python-Projects/Checkbook_Project)
- **Description:** This is an application for keeping track of various bank accounts. The user can create an account, add a transaction (withdrawal or deposit), see their bank account balance and all transactions that apply to it.
- **Technologies Used:**  Python, Django

### [Timeseries Prediction Project](https://github.com/zsuzsannamangu/Python-Projects/tree/master/Python-Projects/AI-Projects/Timeseries_Prediction)
- **Description:** This application predicts and visualizes daily temperatures using time series prediction, which involves forecasting future values based on historical data 
patterns by identifying trends, reoccurance, regularity, and other patterns. 
- **Technologies Used:**  Python and the following libraries: for data manipulation: pandas, for forecasting: Prophet, and for data visualization: matplotlib and plotly.

### [Sentiment Analysis Project](https://github.com/zsuzsannamangu/Python-Projects/tree/master/Python-Projects/Sentiment_Analysis)
- **Description:** Sentiment Analysis is a subfield of Natural Language Processing (NLP) that involves determining the emotional tone behind a body of text. This application analyzes text data to extract subjective information and classifies text as positive or negative.
- **Technologies Used:**  Python and the following libraries: for data manipulation: pandas, for text processing: re, to build and evaluate a machine learning model: Scikit-Learn, to preprocess text data: NLTK, and for GUI: Flask

## Support and contact details

_Feel free to contact me at zsuzsannamangu[at]gmail.com with any questions._

## Technologies Used

_Python, Django, Tkinter, pandas, Prophet, matplotlib, plotly, NLTK, Flask, Scikit_Learn, re_

### License

*MIT*

Copyright (c) 2024 **_Zsuzsanna Mangu_**


# _Doctor Lookup_

#### _The application helps find a doctor by services or doctor's name, 06/28/2019_

#### By _**Zsuzsanna Mangu**_

## Description

_A website where users may enter a medical issue (ie: “sore throat”) into a form, submit it, and receive a list of doctors in Portland who can treat their medical issue. It uses the BetterDoctor API to retrieve information._

## Setup/Installation Requirements

* _Install Node.js and its corresponding package manager (npm) from Node's website_
* _Confirm that Node and npm are in place by checking the versions -> run $ node -v then $ npm -v_
* _Clone the repository_
* _Visit the BetterDoctor API site at https://developer.betterdoctor.com/ and get an API key_
* _Create your own local file with your own API key with the same filename and location_
* _Navigate to root directory_
* _Place your API key in an .env file at the top level of your directory and include .env in .gitignore_
* _Install all required packages locally by running $ npm install in the command line_
* _Run $ npm run build to bundle code_
* _To check the application in the browser run $ npm run start_

## Configuration/dependencies

  * _webpack_ - Webpack is a module bundler that runs by loading assets such as plugins
  * _webpack-cli_ - this package allows us to use Webpack from the command line
  * _webpack-dev-server_ - to set up a live development server so our our code automatically rebundled and reloaded
  * _eslint and eslint loader_ - to check for errors and typos (we need the loader as well to use the linter with Webpack)
  * _uglifyjs-webpack-plugin_ - to minify our code to the bare minimum so our page loads faster
  * _clean-webpack-plugin_ - to clean up our dist folder as it's getting cluttered
  * _css-loader and style-loader_ - to transform our CSS into JavaScript code so Webpack can bundle it
  * _jquery, popper.js and bootstrap_- to develop the front end of our application
  * _html-webpack-plugin_ - to use Webpack to generate HTML files
  * _jasmine-core and Jasmine_ - Jasmine is a JavaScript testing framework to write tests
  * _Karma_ - to run tests wrote with Jasmine
  * _Babel_ - to fit all browsers, we compile code from ES6 to older versions with Babel
  * _dotenv-webpack plugin_ - to make our environmental variables (.env) available inside our application

## Specs

| Behavior | Input | Output |
| ------------- |:-------------:| -----:|
| A user should be able to enter a medical issue to receive a list of doctors in the Portland area that fit the search query. | rash | 1. Dr. Samantha Srmith, 760 N Height Ave., 503-333-3434, dermatologist, samsrmithdr.com, accepting new patients; 2. ... |
| A user should be able to to enter a name to receive a list of doctors in the Portland area that fit the search query. | Samantha Srmith | Dr. Samantha Srmith, 760 N Height Ave., 503-333-3434, dermatologist, samsrmithdr.com, accepting new patients |
| If the API call results in an error, the application should return a notification that states what the error is. | bad API call | Error: Bad Request |
| If the query response doesn't include any doctors, the application should return a notification that states that no doctors meet the criteria. | Samantha Srmithhh | No doctors meet your criteria. |

## Objectives

* Application correctly makes an API call and parses data from the API response.
* The application handles errors when the API call doesn't return a 200 OK status.
* Dependencies are managed with npm.
* Webpack is used to lint, bundle, and process code.

## Support and contact details

_Feel free to contact me at zsuzsannamangu[at]gmail.com with any questions._

## Technologies Used

_Javascript, Webpack, Jasmine and Karma for testing, BetterDoctor API_

### License

*MIT*

Copyright (c) 2019 **_Zsuzsanna Mangu_**
