# DataAnalysisPython
Analyzing US Health Insurance Data using Python

In this project I will try to find out the relations between different parameters and health insurance, using matplot, scipy, csv
I will be extracting the data from a scv file and then I will use matplot and scipy to look at the relations between parameters. 

I extracted the data from the csv file and formatted the data into a compatible dictionary.

Afterwards I started experimenting with some plotting of the numeric parameters.
This resulted in the following outcomes:
- the greater the age, the greater the costs (in 4 visible lines, lower limit is most clear)

- When looking at the (bmi, charges)-graph you can see that there appears to be a upper limit line y = ax + b where a > 0 
    (the greater the bmi, the greater the chance of greater charges)
    FACTS --> All people with charges>60000 have BMI>30

When experimenting with the non numeric parameters, the scatter plot show some discoveries:
- At first sight there appears to be no connection between sex and charges
- There appears to be a great connection between smokers en non-smokers when looking at their (age, charges)-graph 
- This connection also appears at their (bmi, charges)-graph

There is Lots of room for further exploring these connections, or sorting per age group, or making different chart types
- I started this as a small project with the focus on extracting the data, so I will stop at this point.
- Maybe I will finish this gradually over the time to come, but it won't be my main priority.

It was a very fun project to execute en the first time I was really struggling with Python (mostly data extraction)
