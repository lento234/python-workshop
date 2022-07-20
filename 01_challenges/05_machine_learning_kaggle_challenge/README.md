# Machine learning kaggle challenge

You can compete with an active ML challenge at kaggle and win:

* 1st Place - $40,000
* 2nd Place - $30,000
* 3rd Place - $20,000
* 4th Place - $10,000

Note: Pay attention to the deadline.

## Description

You will participate in kaggle challenge ([Americal Express - Default Prediction](https://www.kaggle.com/competitions/amex-default-prediction/overview). Note:

* **August 17, 2022**: Entry Deadline. You must accept the competition rules before this date in order to compete.
* **August 17, 2022**: Team Merger Deadline. This is the last day participants may join or merge teams.
* **August 24, 2022**: Final Submission Deadline.

Whether out at a restaurant or buying tickets to a concert, modern life counts on the convenience of a credit card to make daily purchases. It saves us from carrying large amounts of cash and also can advance a full purchase that can be paid over time. How do card issuers know we’ll pay back what we charge? That’s a complex problem with many existing solutions—and even more potential improvements, to be explored in this competition.

Credit default prediction is central to managing risk in a consumer lending business. Credit default prediction allows lenders to optimize lending decisions, which leads to a better customer experience and sound business economics. Current models exist to help manage risk. But it's possible to create better models that can outperform those currently in use.

American Express is a globally integrated payments company. The largest payment card issuer in the world, they provide customers with access to products, insights, and experiences that enrich lives and build business success.

In this competition, you’ll apply your machine learning skills to predict credit default. Specifically, you will leverage an industrial scale data set to build a machine learning model that challenges the current model in production. Training, validation, and testing datasets include time-series behavioral data and anonymized customer profile information. You're free to explore any technique to create the most powerful model, from creating features to using the data in a more organic way within a model.

If successful, you'll help create a better customer experience for cardholders by making it easier to be approved for a credit card. Top solutions could challenge the credit default prediction model used by the world's largest payment card issuer—earning you cash prizes, the opportunity to interview with American Express, and potentially a rewarding new career.

## Evaluation

The evaluation metric, $M$, for this competition is the mean of two measures of rank ordering: Normalized Gini Coefficient, $G$, and default rate captured at 4%, $D$.

$$
M = 0.5 \cdot (G+D)
$$

The default rate captured at 4% is the percentage of the positive labels (defaults) captured within the highest-ranked 4% of the predictions, and represents a Sensitivity/Recall statistic.

For both of the sub-metrics $G$ and $D$, the negative labels are given a weight of 20 to adjust for downsampling.

This metric has a maximum value of 1.0.

Python code for calculating this metric can be found in [this Notebook](https://www.kaggle.com/code/inversion/amex-competition-metric-python).

## Challenge

1. Join the kaggle [competition](https://www.kaggle.com/competitions/amex-default-prediction/overview).

2. Use ML to predict the `target` variable for each `customer_ID` in the test set.

3. Upload the prediction using the following format:

```
customer_ID,prediction
00000469ba...,0.01
00001bf2e7...,0.22
0000210045...,0.98
etc.
```

4. Your uploaded file and code will be evaluated using the evaulation metric $M$.

4. See you score on the [leaderboard](https://www.kaggle.com/competitions/amex-default-prediction/leaderboard).
