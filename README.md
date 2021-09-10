# Planetly task

This API is used to work with a database with the historical temperatures of the cities in the world from [Kaggle's dataset](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data?select=GlobalLandTemperaturesByCity.csv) This task took me aproximately 4.5hours to finish.

## Pre-requirements

In this API the following steps are needed to make it work:

- Download dataset
- Read DB_Creation.txt to set-up the database with postgreSQL
- Fork the project
- Pull the files
- Install docker container
- Install requirements.txt
- Run the app.py script
- Enjoy.

## Explanation of the code

The brief explanation of the API and the answer to the questions in the task can be found [here](https://docs.google.com/document/d/1y5SdWOuzvM-tFvmXV0oagp8_BsMroYBtHLgBw4-w0jM/edit?usp=sharing)

## Problems and future improvements
The main problem that I faced during this task was with Flask and the many forms that I was creating for each step of the menu thinking in the user experience, this took me more time that I was expecting as I had to be very careful with the creation of the .html pages.
Also, I had problems with the syntax for the queries, as I've tried different libraries and this also may me delayed a bit.
At the end everything was solved. 

For future improvements:
- I would conduct a Performance test to check if it's fast enough when the query involves to much data otherwise to try different architectures
- Create a function to add several entries at once, maybe with an custom CSV file uploaded
- Create a function to delete data
- create a function to compare data by multiple tables
- improve the aesthetics of the API by using bootstrap or something similar


## Versions and updates
[Version 1.0](https://github.com/maxrojass/planetly-task): Uploaded first version. automated.
