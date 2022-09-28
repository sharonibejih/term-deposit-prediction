# Term Deposit Prediction

A term deposit is a cash investment held at a financial institution. Your money is invested for an agreed rate of interest over a fixed amount of time, or term. The bank has various outreach plans to sell term deposits to their customers such as email marketing, advertisements, telephonic marketing, and digital marketing.

### Business Problem:
Telephonic marketing campaigns still remain one of the most effective ways to reach out to people. However, they require huge investment as large call centers are hired to actually execute these campaigns. Hence, it is crucial to identify the customers most likely to patronize term deposits beforehand so that they can be specifically targeted via call.

### Approach
#### Data:
The [data](https://www.kaggle.com/datasets/prakharrathi25/banking-dataset-marketing-targets) used for this project is related to direct marketing campaigns (phone calls) of a Portuguese banking institution. The classification goal is to predict if the client will subscribe to a term deposit or not.

#### Model:
The `XGBoost` algorithm was adopted for this task. The resulting model has an `f1-score of 0.76`. `MlFlow` was used for the experiment tracking.

#### Deployment:
The data preprocessing and model is packaged and deployed as a `Flask` API web service.



