# Project: Rohlik Sales Forecasting Challenge
### Author: Lucia Macakova

As a student of the [Atlantic Technical University](https://www.atu.ie/) in the program [Higher Diplomma in Science and Data Analytics](https://www.gmit.ie/higher-diploma-in-science-in-computing-in-data-analytics), in the year 2024/2025, I decided to try kaggle competition [Rohlik Sale Forecasting Challenge](https://www.kaggle.com/competitions/rohlik-sales-forecasting-challenge-v2/overview) as a project for the module Programming for Data Analytics,

I am the only contributor to this project.

### Task: Predicting sales values for each warehouse 

Predicting sales values is essential for planning, supplying chains, delivery logistics and inventory management. With accurate forecast, businesses can minimaze waste of resources and volume of unnecessary work-related tasks.

###  Data:

-   sales_train.csv - training set containing the historical sales data for given date and inventory with selected features described below
-   sales_test.csv - full testing set
-   inventory.csv - additional information about inventory like its product (same products across all warehouses share same product unique id and name, but have different unique id)
-   solution.csv - full submission file in the correct format
-   calendar.csv - calendar containing data about holidays or warehouse specific events, some columns are already in the train data but there are additional rows in this file for dates where some warehouses could be closed due to public holiday or Sunday (and therefore they are not in the train set)

Columns for sales_train.csv and sales_test.csv

-   unique_id - unique id for inventory
-   date - date
-   warehouse - warehouse name
-   total_orders - historical orders for selected Rohlik warehouse known also for test set as a part of this challenge
sales 
-   Target value, sales volume (either in pcs or kg) adjusted by availability. The sales with lower availability than 1 are already adjusted to full potential sales by Rohlik internal logic. There might be missing dates both in train and test for a given inventory due to various reasons. This column is missing in test.csv as it is target variable.
-   sell_price_main - sell price
-   availability - proportion of the day that the inventory was available to customers. The inventory doesn't need to be available at all times. A value of 1 means it was available for the entire day. This column is missing in test.csv as it is not known at the moment of making the prediction.
-   type_0_discount, type_1_discount, … - Rohlik is running different types of promo sale actions, these show the percentage of the original price during promo ((original price - current_price) / original_price). Multiple discounts with different type can be run at the same time, but always the highest possible discount among these types is used for sales. Negative discount value should be interpreted as no discount.

Columns for inventory.csv

-   unique_id - inventory id for a single keeping unit
product_unique_id 
-   product id, inventory in each warehouse has the same product unique id (same products across all warehouses has the same product id, but different unique id)
-   name - inventory id for a single keeping unit
L1_category_name, L2_category_name, … - name of the internal category, the higher the number, the more granular information is present
-   warehouse - warehouse name

Columns for calendar.csv

-   warehouse - warehouse name
-   date - date
-   holiday_name - name of public holiday if any
holiday - 0/1 indicating the presence of holidays
-   shops_closed - public holiday with most of the shops or large part of shops closed
-   winter_school_holidays
-   school_holidays

Columns for test_weights.csv

-   unique_id - inventory id for a single keeping unit
-   weight - weight used for final metric computation[^1]

### Solution:

In project.ipynb notebook. I decided to use neural network prediction[^2] with mean absolute error as measurement.

### Contact:
Lucia Macakova

email: G00439449@atu.ie

### Resources:
[^1]: https://www.kaggle.com/competitions/rohlik-sales-forecasting-challenge-v2/data
[^2]: https://www.kaggle.com/code/ezeanyi/predicting-future-sales-with-neural-networks#LSTM
[^3]: https://en.wikipedia.org/wiki/Mean_absolute_error