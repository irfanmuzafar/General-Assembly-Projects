<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# Project 3 - Classifying Grab's Customer Feedback into Ride Hailing and Delivery

> Authors: Irfan Muzafar, Ng Wei, Lim Zheng Gang
---

## Overview

This project aims to classify user reviews of the Grab app into two distinct services: delivery (GrabFood) and ride-hailing (Grab). By leveraging machine learning algorithms on data collected from the Reddit subreddits of Uber and UberEats, this classifier seeks to simplify the process of segregating service-specific feedback without manual interpretation.

## Persona

Greg, a 30-year-old product manager, oversees the product feature pipeline for the year 2024. He's been tasked by his boss to draft a proposal for enhancing customer experience in Grab Delivery service. However, Greg finds himself stretched thin as he devotes most of his time to sorting and classifying numerous reviews on the Grab app store, aiming to extract actionable insights. What he urgently requires is an efficient classifier that can swiftly distinguish between Delivery and Ride Hailing reviews, allowing him to prioritize improvements in customer experience.

## Problem Statement

How can we distinguish between customer feedback related to Grab's ride-hailing and delivery services fast and accurately?

## Python Version and Libraries

- Python 3.8 or above
- PRAW (Python Reddit API Wrapper)
- Scikit-learn
- Pandas
- Numpy
- Scipy
- Nltk
- Gensim
- Transformers

## Data Collection, Cleaning and EDA

This project uses the PRAW library to scrape user reviews from specific subreddits related to Uber and UberEats. The data collected is then processed to remove irrelevant content, ensuring that only meaningful text is used for classification. 1,2,3-gram frequency analysis bar-charts were plotted.

## Preprocessing and Modelling

During the project's exploratory phase, two transformers (CountVectorizer and TF-IDF) and three estimators (Multinomial Naive Bayes, KNN, and Logistic Regression) were tested with the use of Pipeline and GridSearchCV for optimization. The best performance was achieved using a combination of CountVectorizer and Multinomial Naive Bayes.

- **Transformer**: CountVectorizer was employed to convert text data into a matrix of token counts.
- **Estimator**: Multinomial Naive Bayes, chosen for its efficacy in binary classification tasks.

## Evaluation

### Model Training and Result

The model was trained using a labeled dataset, with the data split into training and testing subsets.

| Classifier           | CountVectorizer | TF-IDF  |
|----------------------|-----------------|---------|
| Multinomial Naive Bayes | train 85%, test 77% | train 94%, test 78% |
| K-Nearest Neighbors  | train 69%, test 67% | train 61%, test 57% |
| Logistic Regression  | train 86%, test 76% | train 89%, test 77% |

**Accuracy** was selected as the primary metric for evaluation because correctly identifying whether a review pertains to delivery or ride-hailing is crucial for our analysis.

### Model Selection  

Countvectorizer and Multinomial Naive Bayes model is selected since we are selecting model with the highest accuracy. We are unable to select the model that uses TF-IDF vectorizer as the discrepency between test score and train score is too huge. This indicates strongly that the model will perform badly on test or unseen data. This is especially important in our case of evaluating reviews on app store.  

Multinomial Naives Bayes model is also preferred due to its lower computational complexity. 


## Conclusion

In response to the problem statement regarding the need to effectively differentiate between customer feedback concerning Grab's ride-hailing and delivery services, we have conducted model evaluation and exploratory data analysis (EDA). Our findings have led us to select a count-vectorized multinomial Naive Bayes model, which achieved an accuracy score of 77.5% on test data. Moving forward, we intend to validate our model using real app reviews from the Google Play Store. This validation process will help us determine the suitability of our model for accurately addressing the identified problem. We managed to achieve an accuracy score of 82.37% (better than our initial test score of 77.7%).   

## Recommendations

The results is promising but we should also recognize that the model is not perfect. The below can help to improve the experience of our end users:

1. Discover better training data that can gives us better prediction. This can be done by scrapping for more localized content such as hardware zone since there are fundamental linguistic differences between countries Uber operate in vs SouthEast Asia.  
  
2. Similar to subreddit, app review comments contains uninformative reviews such as "i like him" which can be filtered out prior to classification. This will also ensure our end users get better quality data for analysis. One of the next steps can be to develop a classifier to identify such cases. 

3. Recommend implementing a classifier capable of detecting not only binary discrete results but also multiple discrete outcomes. This enhanced classifier would not only differentiate between ride-hailing and delivery services but also consider overall app performance. By incorporating this multi-class classification approach, we can provide more comprehensive insights into customer feedback, enabling Grab to address specific issues related to each service while simultaneously improving overall app functionality and user experience. Additionally, deploying advanced natural language processing techniques could further refine the classifier's accuracy and effectiveness in handling diverse customer feedback scenarios.

All in all, even though this model is not perfect, an accuracy score of 77.7% against our initial baseline model that only predicts the majority with an accuracy of 52.4% is a good step towards helping our target audience (the product managers) automate the classification process. 