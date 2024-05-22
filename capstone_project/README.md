<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# Capstone Project - An Automated System for Accident Severity

> Author: Irfan Muzafar
---

## Overview

Firstly, we conduct initial findings on traffic accidents in Singapore. Then, our various models try to classify images into five severity types: Fire, Minor, Moderate, No Accident and Severe. Afterwhich, we evaluate the performance of each model using accuracy and loss and choose our best model. Then, we apply regularization methods to reduce overfitting. By leveraging machine learning algorithms on data collected from roboflow, our classifier seeks to better capture the five classes, some of which may be difficult to detect. This is so that various authorities can automate their deployment services when an accident happens.

## Problem Statement

How can we develop an automated system capable of analysing images from traffic cameras or phone cameras to classify accidents into five severity classes accurately?

## Python Version and Libraries

- Python 3.8 or above
- Pandas 
- Numpy
- Matplotlib
- Seaborn
- OS
- Scikit-learn 
- Tensorflow 
- Keras
- Transformers

## Datasets

- [Singstat Road Traffic Accident Casualties, Annual](https://tablebuilder.singstat.gov.sg/table/TS/M651281)
- [Car Crash Severity Detection](https://universe.roboflow.com/ansonlau1325-gmail-com/car-crash-severity-detection/dataset/13)

## Data Collection, Cleaning and EDA

This project uses the Pandas library to read the CSV file `Singstat Road Traffic Accident Casualties, Annual`. The data collected is then processed to remove some columns, ensuring that only meaningful data is used for analysis. Various histograms, bar charts and boxplots were plotted. Also, this project uses the OS library to read folders and image files downloaded from `Car Crash Severity Detection`, generating a dataframe with file paths and labels.

## Modelling

The model was trained using a labeled dataset, with the data split into training and testing subsets. During the project's exploratory phase, a self-trained Convolutional Neural Network (CNN) model and three pre-trained models (MobileNetV2, VGG19 and EfficientNetB4) were used to predict the class of each image.

**Baseline Models**
| Model | Train Accuracy | Test Accuracy | Train Loss | Test Loss |
| --------------- | --------------- | --------------- | --------------- | --------------- |
| CNN    | 0.9923    | 0.6626    | 0.0696 | 1.6319 |
| MobileNetV2 | 0.9392 | 0.8098 | 0.2255 | 0.5140 |
| VGG19 | 0.7710 | 0.6687 | 0.5937 | 0.8421 |
| EfficientNetB4 | 0.2881 | 0.4601 | 3.9087 | 5.2880 |

**Accuracy** was selected as the primary metric for evaluation as it is easy to understand and interpret. It is the ratio of correctly predicted instances to the total number of instances.

Balancing accuracy, loss and extent of overfitting, we have chosen MobileNetV2 to be our best model. From here, we proceed with applying regularization to our best model.

| Model | Train Accuracy | Test Accuracy | Train Loss | Test Loss |
| --------------- | --------------- | --------------- | --------------- | --------------- |
| Base MobileNetV2 | 0.9392 | 0.8098 | 0.2255 | 0.5140 |
| MobileNetV2 with regularization | 0.8339 | 0.8221 | 0.4457 | 0.5072 |

## Extra: Zero-Shot Image Classification
We also explored using Zero-Shot Image Classification on some images from our test dataset.

## Classification
After training and optimising our image classification model, we ran a prediction across our test dataset (containing 100 images) to capture:

- **Correct Classifications: 65 images**<br>
    - Predictions equal to True Labels

- **Wrong Classifications: 35 images**<br>
    - Predictions different from True Labels

Most of these wrong predictions come from true labels of Minor and Moderate.

## Learnings
Limitations:
- Inaccuracy in some classes.
- Unclear definitions for minor, moderate and severe accidents.
- Deeper analysis cannot be done without number of injuries and speed before collision.

Recommendations:
- Use data augmentation to generalise and expand dataset.
- Relate severity of accidents to injuries suffered.
- Use dashcams for severity analysis

## Conclusion

We conducted analysis on accidents in Singapore and accident image classification using various models with the aim of automating process and enabling prompt responses from emergency rescue team and towing services.

Despite some limitations above that eventually posed as a barrier to reach our goal, we believe that there is still value in creating an accurate multi-class image predictor to identify different severity of accidents for immediate response from various services. Other agencies or authorities like vehicle insurance companies and the Traffic Police may benefit from our severity classifier.

---