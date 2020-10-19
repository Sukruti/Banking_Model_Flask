# Bank Customer Churn Prediction: 

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [Bug / Feature Request](#bug---feature-request)
  * [Future scope of project](#future-scope)


## Demo
 * Home Screen :
![HomeScreen](https://user-images.githubusercontent.com/6366237/96409048-4b731580-1202-11eb-9b1b-eedcae591b60.PNG)
 * File Output
![File_Output](https://user-images.githubusercontent.com/6366237/96408866-fdf6a880-1201-11eb-9a68-c5ced877595b.PNG)
 * Data Entry Output
![Individual Entry](https://user-images.githubusercontent.com/6366237/96409317-b45a8d80-1202-11eb-8de0-52f17bd486b2.PNG)



## Overview
This is a Flask web app which predicts customer attrition from a bank data.


## Installation
The Code is written in Python 3.6.10. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Directory Tree 
```
├── static 
│   ├── css
├── template
│   ├── home.html
│   ├── complete.html
├── testdata
│   ├── RIA_Bank_test
├── Procfile
├── README.md
├── app.py
├── RandomForestAlgo.ipynb
├── random_forest_regression_model.pkl
├── requirements.txt
├── RIA_ML_Data_Set.xlsx
```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) 


## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an [issue]

## Future Scope

* Use multiple Algorithms
* Optimize Flask app.py
* Front-End 
