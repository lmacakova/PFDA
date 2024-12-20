# pfda.assessment
## Author: Lucia Macakova
## Programming for Data Analytics - Assignment tasks

### About: 
### About: 
This is my solution for assignment tasks in the module Programming for Data Analytics. I am the only contributor.

I worked with modules pandas[^1], numpy[^2], matplotlib[^3] and seaborn[^4].

##### Assignment 2 - Weather
Task: With data from weatherreadings.csv, plot the temperature over time (column "dryBulbTemperature_Celsius").

Solution: I converted string objects of 'reportStartDateTime' column into datetime series, and than I made this series the index of my dataframe, timestamped in ISO8061 format[^5]. With these steps, I could make a plot, where ticks on axis x mean the exact time instant. I set and formatted ticks with tools of matplotlib.dates[^6].

##### Assignment 3 - Domains
Task: To create a pie chart of people's email domains from data of people-1000.csv. 

Solution: After loading, viewing, and checking dataframe, I created new column 'domains' from data in column 'email' with function string()[^7], counted values, and made a plot.

##### Assignment 5 - Risk
Task: Write a program that simulates 1000 individual battle rounds in the Risk game (3 attackers vs 2 defenders)[^8] and plots the result. One battle round is one shake of the attacker and defender dice. 
More information about the Risk game is in assignment5.risk.ipynb 

Solution: I created the function battle_round(), with which I simulated 1000 rounds of battle and plotted results.

##### Assignment 6 - Knock Airport Weather
Task: With data from hly4935.csv file create a plot of:
- The temperature
- The mean temperature each day
- The mean temperature for each month
- The wind speed
- The rolling wind speed over 24 hours
- The max wind speed for each day
- The monthly mean of the daily max wind speeds

There could be a need to correct missing values.

<<<<<<< HEAD
Solution: I checked missing cells, replaced ' ' with NaN, and refilled cells with values from previous cells. I used function fillna()[^9]. I converted string objects of 'date' column into datetime series. Than I made this series the index of my dataframe. I converted string values in 'wdsp' column into integer values. I made plots using functions resample()[^10] and rolling()[^11]. function.

### Resources:
[^1]    https://pandas.pydata.org/docs/index.html
[^2]    https://numpy.org/doc/stable/index.html 
[^3]    https://matplotlib.org/stable/
[^4]    https://seaborn.pydata.org/index.html
[^5]    https://en.wikipedia.org/wiki/ISO_8601
[^6]    https://matplotlib.org/stable/api/dates_api.html
[^7]    https://www.geeksforgeeks.org/python-str-function/
[^8]    https://www.ultraboardgames.com/risk/game-rules.php
[^9]    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html
[^10]   https://www.geeksforgeeks.org/python-pandas-dataframe-resample/
[^11]   https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html
=======
#### Solutions:
The Solutions are described in steps in jupyter notebooks for the particular tasks.


### Resources:
1.  https://pandas.pydata.org/docs/index.html
2.  https://numpy.org/doc/stable/index.html 
3.  https://matplotlib.org/stable/
4.  ttps://seaborn.pydata.org/index.html
5.  https://www.w3schools.com/python/default.asp
6.  https://en.wikipedia.org/wiki/ISO_8601
7.  https://www.ultraboardgames.com/risk/game-rules.php
8.  https://www.geeksforgeeks.org/python-pandas-dataframe-resample
9.  https://en.wikipedia.org/wiki/Moving_average
>>>>>>> 0ab2852450d55ed5ae6d915b4a7d6f7b82759d61





### Contact:
Lucia Macakova
email: G00439449@atu.ie
