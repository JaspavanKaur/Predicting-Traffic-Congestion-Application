# Predicting Traffic Congestion Application
 ## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Additional Files](#additional-files)
* [Troubleshooting](#troubleshooting)

## General info
This project is a simple web application that predicts if there would be low, medium or high traffic congestion using real-time weather forecasting data from OpenWeatherMap API. It is a prototype for "Code for Cities: Environmental Sustainability and Resiliency", a hackathon held by SMU AntHill and Surbana Jurong, which aims to solve environmental and sustainability issues in Singapore using data analytics/science.

The predictions are tested using various classification and neural network models such as SVM, Random Forest, K-NN, etc. If you would like to know more on what models we used to test and train, you can take a look [here](models/Code_for_cities_Team_Bzbz.ipynb). In this website, we decided to use Random Forest for our predictions.
	
## Technologies
Project is created with:
* Python: 3.8
* HTML: 5
* Vue.js: 3.0
* Bootstrap: 4
	
## Setup
To run this project, install it locally using python:


1. Run traffic-congestion-api.py and weather-api.py files in api folder. Ensure that they are run in different cmd terminals.
```
cd api
python traffic-congestion-api.py
```
```
cd api
python weather-api.py
```


2. Run app.py
```
cd ..
python app.py
```


3. Ctrl + click on the localhost link. You should see the front page as seen below

https://user-images.githubusercontent.com/66090549/129002517-aadbe9f0-3fc0-4758-9aba-84d53c1d91fe.mp4

## Additional Files
* [Round 1: Proposal Submission [PDF file]](https://github.com/dian-farah/Predicting-Traffic-Congestion-Application/files/6967225/Code.for.cities_.Prediction.of.road.congestion.by.Bzbz.pdf)
* [Round 2: Prototype Pitch Submission [PDF file]](https://github.com/dian-farah/Predicting-Traffic-Congestion-Application/files/6967232/Prediction.of.Traffic.Congestion.Phase.2._.Team.Bzbz.pdf)

## Troubleshooting
If you are unable to run the .py files, it may be due to certain python packages that you have not installed. You can follow [this link](https://www.youtube.com/watch?v=paRXeLurjE4) on how to install python packages into VSCode.
