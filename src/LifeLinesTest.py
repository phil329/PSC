# -*- coding: utf-8 -*-
"""
------------------------------------------------------------
    Software:   PyCharm
    File Name:    LifeLinesTest
    Description:   
  
    Author:  Phil
    Email:  furuoo@163.com
    Date:   2021/2/26 14:21
    Version:  3.8.1
"""
# --------------------------------------------------------------
#    Document Description:Test code for survival analysis in python
#
# --------------------------------------------------------------

from lifelines.datasets import load_waltons
from lifelines import KaplanMeierFitter
from lifelines.utils import median_survival_times


df = load_waltons()
print(df.head(5), '\n')
print(df['T'].min(), df['T'].max(), '\n')
print(df['E'].value_counts(), '\n')
print(df['group'].value_counts(), '\n')

'''
The data have three columns, where T stands for min(T, C), and where T is the time of death 
and C is the observation cutoff time.E represents whether "death" was observed, 
1 means it was observed and 0 means it was not  observed, i.e. the censored data in the survival analysis,
7 in total.Group represents the presence or absence of virus, miR-137 represents the presence of virus,
 and control represents the absence of virus.Control represents the absence of the virus, 
 i.e. the control group. According to the statistics, there were 34 people with miR-137 virus 
 and 129 people without it.
'''

# Use this data to take the Kaplan Meier model from the fitted survival analysis
# (a model dedicated to estimating survival functions) and plot survival curves for the entire population.
kmf = KaplanMeierFitter()
kmf.fit(df['T'], event_observed=df['E'])
kmf.plot_survival_function()
median_ = kmf.median_survival_time_
median_confidence_interval_ = median_survival_times(kmf.confidence_interval_)
print(median_confidence_interval_)


'''
The solid blue line in the figure shows the survival curve, and the light blue band represents 
the 95% confidence interval. As time increases, the survival probability S(t) gets smaller, 
which is certain, while the 95% confidence interval for t at S(t) = 0.5 is [53, 58]. 
This is not the focus of our attention, we really want to focus on the difference 
between the survival curves of the experimental group (presence of virus) 
and the control group (absence of virus). Therefore, we need to observe the survival curves 
in groups equal to "miR-137" and "control", respectively:
'''


groups = df['group']
ix = (groups == 'miR-137')

kmf.fit(df['T'][ix], df['E'][ix], label='miR-137')
ax = kmf.plot()
treatment_median_confidence_interval_ = median_survival_times(kmf.confidence_interval_)
print("95% confidence interval of survival time corresponding to 50% survival of virus with miR-137:'\n'", treatment_median_confidence_interval_, '\n')

kmf.fit(df['T'][~ix], df['E'][~ix], label='control')
# Share a canvas
ax = kmf.plot(ax=ax)

control_median_confidence_interval_ = median_survival_times(kmf.confidence_interval_)
print("95% confidence interval of survival time corresponding to 50% survival of viruses not bearing miR-137:'\n'", control_median_confidence_interval_)


'''
It can be seen that the survival curve of the virus with miR-137 is below the control group. 
It indicates that its mean survival time is significantly smaller than that of the control group. 
Also the survival time 95% confidence interval corresponding to 50% survival of virus with miR-137 is [19,29], 
and the corresponding control group is [56,60]. The difference is large 
and this method can be applied in scenarios such as analyzing user churn, 
for example, if we have implemented some epidemic prevention activities for a group of people, 
we can analyze whether our activities are effective in this way.
'''

print('--------------------------------------------------------------------------------------------')


'''
II. cox regression
This model uses survival outcome and survival time as the response variables, 
allows simultaneous analysis of the effects of numerous factors on survival, 
enables analysis of information with truncated survival times, and does not require 
estimation of the type of survival distribution of the information.

Hypothesis testing for regression models usually uses likelihood ratio tests, Wald tests, 
and score tests, and their test statistics all obey a chi-square distribution. 
The degrees of freedom are the number of independent variables to be tested in the model. 
In general, the estimation of Cox regression coefficients and hypothesis testing of the model
are computationally intensive and usually require the use of a computer to perform the corresponding calculations.

Usually survival time is associated with multiple factors, 
so we are faced with multidimensional data. 
A more complex data set is used below. 
The first step is still to import and use the example data.

'''

from lifelines.datasets import load_regression_dataset
from lifelines import CoxPHFitter


regression_dataset = load_regression_dataset()

print(regression_dataset.head(5))
print('----------------------------------------')
print(regression_dataset['E'].value_counts())

'''
Where T represents min(T, C), where T is the time of death and C is the observation cut-off time.
E represents whether "death" was observed, 1 means it was observed, 0 means it was not observed, i.e.
"censored" data in survival analysis, and the total number of censored data is var1, var2, and var3 
represent the variables of our relationship, 
which can be dummy variables for whether the experimental group, a user's channel path, 
or a user's own attributes. We use this data for Cox regression
'''

cph = CoxPHFitter()
cph.fit(regression_dataset, 'T', event_col='E')
cph.print_summary()
print("\ncph.params_ :\n",cph.params_)

'''
From the results, we consider var1 and var3 to be significant at 5% level of significance. 
It is considered that the higher the level of var1, the higher the value of the risk function of the user, i.e., 
the shorter the survival time (cox regression models the risk function, 
which is the opposite of the death acceleration model, which models the survival time, 
and the two models have opposite signs of the parameters). 
Similarly, the higher the var3 level, the higher the value of the user's risk function.
'''
