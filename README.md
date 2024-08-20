Project Title:
Background
Agriculture is the main economic activity in Rwanda with 70% of the population engaged in the sector, and around 72% of the working population employed in agriculture. The period for cultivation can be divided into the first cultivable season (from September to January) and the second cultivable season (from February to June). In the marshlands, where water is abundant, there is also a third agricultural season for the cultivation of rice and vegetables (FAO,2024).

The agricultural sector accounts for 33% of the national GDP . In general, Rwanda’s GDP has been growing at the rate of 7% since 2014. Tea and coffee are the major exports while plantains, cassava, potatoes, sweet potatoes, maize and beans are the most productive crops. Rwanda exports dry beans, potatoes, maize, rice, cassava flour, maize flour, poultry and live animals within Eastern Africa.

Challenges
Due to the strong link between agriculture and poverty, the challenges in the agriculture sector are also drivers of rural poverty. Despite remarkable improvements over recent years, the agricultural sector in Rwanda still faces many challenges but the one of challenges is improper crops choosing according to the soil features and rainfall.

The crop advisory system employs modern farming methods that leverage soil characteristics, types, crop yield data, and weather conditions to advise farmers on the most suitable crops to cultivate for enhanced yield and profitability. This approach aims to minimize crop failures and empower farmers to make well-informed decisions about their farming strategies.

In light of the current agrarian crisis, there is a pressing need for improved recommendation systems that can significantly mitigate the crisis by empowering farmers to make informed decisions before embarking on crop cultivation activities.

Goal
To provide farmers with recommendations on the best crops to cultivate, considering multiple parameters, thereby aiding them in making informed decisions prior to planting.

ML Task type: Classification

Objective: The objective of the model is to predict the most suitable crop to be cultivated based on various input parameters such as levels of Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH level, and Rainfall. This prediction helps in providing advisory recommendations to farmers, aiming to optimize crop yield and ensure sustainable agricultural practices.

Description: In a classification task for a crop advisory system, the model learns from historical data where the features (N, P, K, Temperature, Humidity, pH, Rainfall) are used to predict the class label (crop type) of the data instances. The model uses this learned relationship to classify new, unseen data into one of several predefined crop categories. This assists farmers in making informed decisions about which crop(s) are likely to thrive best under given environmental conditions, thereby maximizing productivity and profitability while minimizing risks such as crop failure or suboptimal yields.

# Importing libraries

from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
import warnings
warnings.filterwarnings('ignore')
The dataset
The dataset used in this project is composed usefull features affecting the yield of the crop, those features are: Nitrogen, Phosphorous, Pottasium and pH values of the soil. Also, it also contains the humidity, temperature and rainfall required for a particular crop. The dataset retrieved from kaggle.

the following line codes describe more information of dataset like columms number, size, datatype
