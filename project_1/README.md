# Project 1: Exploring climate data of Singapore

### Problem Statement

Weather affects daily activities of Singapore population, hence it is worth analysing weather data to identify trends. I am working as a Data Analyst for some F&B businesses. In this project, we will analyse how and when weather changes affect online F&B businesses. For example, on rainy days, do online F&B sales proportion go up?

The ideal outcome is to provide the F&B businesses with relevant information to manage resources as rainy conditions and temperature fluctuates in different parts of the year.

### Datasets

|Feature|Type|Dataset|Description|
|---|---|---|---|
|maximum_rainfall_in_a_day|float|rainfall-monthly-highest-daily-total| The highest rainfall in a day for each month in mm|
|no_of_rainy_days|integer|rainfall-monthly-number-of-rain-days|Number of rainy days in each month| 
|total_rainfall|float|rainfall-monthly-total|Total rainfall in mm| 
|mean_rh|float|relative-humidity-monthly-mean|Mean relative humidity in percentage|
|wet_bulb_temperature|float|wet-bulb-temperature-hourly|Mean wet bulb temperature of each month (converted from wet bulb temperature hourly)|
|mean_temp|float|surface-air-temperature-monthly-mean|Mean surface air temperature of each month|
|online_f&b_sales_proportion|float|online-fnb-sales-proportion_cleaned|Percentage of online F&B sales to total F&B sales| 

#### Brief Summary of Analysis

- Used groupby function to calculate the mean of values for Jan2019, Jan2020, Jan2021 and Jan2022. Same for the other months of the year. This is for the Line Graph below.

- Plotted a Line Graph: Over a year (Jan-Dec), very similar trends observed between number of rainy days and online F&B sales proportion. Correlation value is 0.493. More rainy days are also expected in June and November. 

- Plotted a Bar Graph: Spike in the number of online F&B sales proportion from March 2020 to April 2020.

- Correlation Matrix and Scatter Plot for Before Circuit Breaker: As max rainfall in a day increases, online F&B sales proportion increase slightly. Correlation value is 0.179.

- Correlation Matrix and Scatter Plots for During Circuit Breaker: There was a strong correlation (0.754 and 0.692) between wet-bulb/surface-air temperature and online F&B sales proportion (But external factor, Circuit Breaker, should be considered). 

- Correlation Matrix and Scatter Plot for After Circuit Breaker: As total rainfall and maximum rainfall in a day rises, there was a moderate rise in online F&B sales proportion. Correlation values are 0.545 and 0.533

### Conclusions and Recommendations

Based on our data, it is likely that rainy days will boost online F&B sales proportion. Thus, more resources such as containers for packing food and delivery riders can be prepared as well. Additionally, the F&B businesses can ensure that the online order application system is able to handle an increase in the amount of orders.

For future research purposes, we might want to use the data for online F&B sales "numbers" instead of "proportion" to see if weather changes affect online F&B sales numbers. Also, a longer timeframe, instead of just 2019 to 2022, can be used for future analysis. This is so that we have a better interpretation of the trends throughout a year.