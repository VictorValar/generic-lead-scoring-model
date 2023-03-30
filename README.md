# Generic Lead Scoring Model
## About
`glsm` is a user-friendly Python package that simplifies the process of building lead scoring models. It supports both predictive and non-predictive models, providing flexibility and ease of use.

The goal of the lead score is to provide a qualification metric for comparison between leads. It is based on product interest and company interaction data.

### Predictive Model
Soon!
### Non-predictive Model

| Name | Description |  |
|------------ |------------|------------|
Weight| Feature weight   that represents the relative importance of each feature | $ {w} $
Points| Assigned points of each feature | ${p}$
Normalized weight | Weights unit vector normalization | $${\hat{w}} = \frac{w_n}{\sqrt{\sum\limits^{n}_{i=0}w_i^2}}$$
Lead score | A weighted sum of assigned points for each feature, where the feature weights are normalized to form a unit vector. | $$\lambda = \sum_{i=1}^n {\hat{w}_i}{p_i}$$

***
## Disclaimer
This library is in active development. Suggestions and contributions are welcome.
## Installation
### Requirements
-
Can be installed using pip:
```bash
pip install
```
***
# Understanding the Models
There are two ways for you to understand the proposed models:

1. Through the [Google Sheets simulator](https://docs.google.com/spreadsheets/d/1ESEtcjno36ZLW5XMEoHqLKHjiZMkrZeIECcrcgFxHzA/edit?usp=sharing) (Non-predictive only)
2. Reading the following sections
## Predictive Model
Soon!

***
## Non-predictive Model

This model and the following set of rules are a suggestion to get you started. You can use them as a starting point and adapt them to your business needs.
The library is flexible enough to allow you to use your own assumptions and  rules.


The non-predictive model has the following characteristics:
1. It avoids the use of predictive algorithms, which can be data-intensive and require significant computational power and technical expertise to operate effectively.
2. It uses relative feature weights, meaning that the inclusion of a new feature won't change the weights of the existing ones. This can simplify the implementation and interpretation of the model.
3. It provides a score that ranges from 0 to 100 points, with 50 being the minimum threshold for lead qualification. The score reflects the current objectives and scenarios of the company, allowing for comparisons of lead performance over time.

###  Weight (${w}$):
Feature weight is a value between 0 and 1 that multiplies the points assigned to each feature. It is used to differentiate the importance of each feature.


### Normalized Weight (${\hat{w}}$):
The model needs to be flexible and adaptable to accommodate changes in the business environment. Sometime after the model is built, the company may change its focus or process. In this case, features may need to be added or removed.

The normalized weight is a unit vector that is used to scale data in a way that preserves the relative relationships between the features when new features are added.

    The basic idea is to transform the data such that the magnitude of the vector formed by the features is equal to 1. This ensures that each feature is scaled proportionally to the others, so the relative relationships between them is preserved when new features are added.


#### Unit vector nomalization:
$$
\hat{w_n} = \frac{w_n}{|w|}
$$
#### Feature vector magnitude:
$$
|w| = \sqrt{\sum\limits^{n}_{i=0}w_i^2}
$$

#### Normalized weight vector:

$$
\hat{w_n} = \frac{w_n}{\sqrt{\sum\limits^{n}_{i=0}w_i^2}}
$$


### Points (${p}$):
Assigned points per feature is the score assigned to each option of a feature. 50 shloud  assigned to the option that represents the minimum viable for the lead to be considered qualified.

$$
0  \leq p \geq 100
$$

### Lead Score ($\lambda$):
Lead score is the sum of the normalized weight of each feature multiplied by the points assined to each feature.


$$
\lambda = \sum_{i=1}^n {\hat{w}_i}{p_i} = ({\hat{w}_1}{p_1})+({\hat{w}_2}{p_2})+({\hat{w}_3}{p_3})...({\hat{w}_n}{p_n})
$$

### Features ($f_1$,$f_2$,$f_3$ ... $f_n$)
Features are a set of characteristics assigned to each lead. If you have difficulties finding out which features to add, start by adding relevant lead form or CRM fields as features.

Each feature has points associated with it, which are assigned to each option of the feature. The points assigned to each option are relative to the minimum viable option for the lead to be considered qualified (50 points).

You should first define the features and their options, then assign 50 points to the minimum viable option for the lead to be considered qualified. The remaining points should be distributed among the other options in a way that reflects the relative importance of each option.

In this way if $\lambda \geq 50$ the lead is considered qualified.

Remember that this is a suggestion, you can assign the points as you see fit and as your business requires. You may want to use negative points to penalize leads that do not meet certain criteria for example. It is generally easier to work with positive points, but it is up to you.

#### Example:
| Monthly Website Users | Points|
|------------ | ------------|
Up to 50k | 30
50k - 100k | 50 (ICP)
100k - 200k | 80
More than 200k | 100

***



