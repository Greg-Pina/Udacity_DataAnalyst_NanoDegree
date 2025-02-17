# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
In this project, you will develop a classification model on publicly available Census Bureau data. You will also write code to monitor the model performance on various data slices. Then, you will deploy your model using the FastAPI package.

## Intended Use
The model is intended for use in applications requiring classification of income levels based on census data. It is not suitable for financial or legal decision-making or any other use where high accuracy is critical.

## Training Data
The model was trained on the Census Income dataset, also known as the Adult dataset, which was donated on 4/30/1996. The dataset consists of 48,842 instances and 14 features. The data was extracted from the 1994 Census database using the following conditions: ((AAGE>16) && (AGI>100) && (AFNLWGT>1)&& (HRSWK>0)). The prediction task is to determine whether a person makes over $50K a year. The dataset contains both categorical and integer features and has missing values.

## Evaluation Data
The model was evaluated on a separate dataset of 2,000 instances that were not seen during training. This dataset was also manually labeled and represents a diverse set of categories.

## Metrics
The model's performance was evaluated using accuracy, precision, recall, and F1 score. The results are as follows:
- Overall Precision: 0.7385
- Overall Recall: 0.6346
- Overall F1 Score: 0.6826

### Performance on Slices
The model's performance on different slices of the data is as follows:

#### Workclass
- `?`: Precision: 0.6923 | Recall: 0.4286 | F1: 0.5294
- `Federal-gov`: Precision: 0.7681 | Recall: 0.7571 | F1: 0.7626
- `Local-gov`: Precision: 0.7383 | Recall: 0.7182 | F1: 0.7281
- `Private`: Precision: 0.7363 | Recall: 0.6304 | F1: 0.6792
- `Self-emp-inc`: Precision: 0.7739 | Recall: 0.7542 | F1: 0.7639
- `Self-emp-not-inc`: Precision: 0.7182 | Recall: 0.5032 | F1: 0.5918
- `State-gov`: Precision: 0.7273 | Recall: 0.6575 | F1: 0.6906
- `Without-pay`: Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000

#### Education
- `10th`: Precision: 0.4286 | Recall: 0.2500 | F1: 0.3158
- `11th`: Precision: 1.0000 | Recall: 0.3636 | F1: 0.5333
- `12th`: Precision: 1.0000 | Recall: 0.4000 | F1: 0.5714
- `1st-4th`: Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
- `5th-6th`: Precision: 1.0000 | Recall: 0.5000 | F1: 0.6667
- `7th-8th`: Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
- `9th`: Precision: 1.0000 | Recall: 0.3333 | F1: 0.5000
- `Assoc-acdm`: Precision: 0.6744 | Recall: 0.6170 | F1: 0.6444
- `Assoc-voc`: Precision: 0.6364 | Recall: 0.5556 | F1: 0.5932
- `Bachelors`: Precision: 0.7535 | Recall: 0.7133 | F1: 0.7329
- `Doctorate`: Precision: 0.8548 | Recall: 0.9298 | F1: 0.8908
- `HS-grad`: Precision: 0.6533 | Recall: 0.4261 | F1: 0.5158
- `Masters`: Precision: 0.8093 | Recall: 0.8406 | F1: 0.8246
- `Preschool`: Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
- `Prof-school`: Precision: 0.8316 | Recall: 0.9405 | F1: 0.8827
- `Some-college`: Precision: 0.6901 | Recall: 0.5307 | F1: 0.6000

#### Marital Status
- `Divorced`: Precision: 0.7292 | Recall: 0.3398 | F1: 0.4636
- `Married-AF-spouse`: Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
- `Married-civ-spouse`: Precision: 0.7324 | Recall: 0.6862 | F1: 0.7085
- `Married-spouse-absent`: Precision: 1.0000 | Recall: 0.2500 | F1: 0.4000
- `Never-married`: Precision: 0.8214 | Recall: 0.4466 | F1: 0.5786
- `Separated`: Precision: 1.0000 | Recall: 0.4211 | F1: 0.5926
- `Widowed`: Precision: 1.0000 | Recall: 0.1579 | F1: 0.2727

#### Occupation
- `?`: Precision: 0.6923 | Recall: 0.4286 | F1: 0.5294
- `Adm-clerical`: Precision: 0.6623 | Recall: 0.5312 | F1: 0.5896
- `Armed-Forces`: Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
- `Craft-repair`: Precision: 0.6744 | Recall: 0.4807 | F1: 0.5613
- `Exec-managerial`: Precision: 0.7840 | Recall: 0.7406 | F1: 0.7617
- `Farming-fishing`: Precision: 0.5455 | Recall: 0.2143 | F1: 0.3077
- `Handlers-cleaners`: Precision: 0.6667 | Recall: 0.3333 | F1: 0.4444
- `Machine-op-inspct`: Precision: 0.5758 | Recall: 0.4043 | F1: 0.4750
- `Other-service`: Precision: 0.8333 | Recall: 0.1923 | F1: 0.3125
- `Priv-house-serv`: Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
- `Prof-specialty`: Precision: 0.7804 | Recall: 0.7704 | F1: 0.7754
- `Protective-serv`: Precision: 0.7273 | Recall: 0.5714 | F1: 0.6400
- `Sales`: Precision: 0.7310 | Recall: 0.6510 | F1: 0.6887
- `Tech-support`: Precision: 0.7000 | Recall: 0.6863 | F1: 0.6931
- `Transport-moving`: Precision: 0.5778 | Recall: 0.4062 | F1: 0.4771

#### Relationship
- `Husband`: Precision: 0.7349 | Recall: 0.6846 | F1: 0.7088
- `Not-in-family`: Precision: 0.7938 | Recall: 0.4096 | F1: 0.5404
- `Other-relative`: Precision: 1.0000 | Recall: 0.3750 | F1: 0.5455
- `Own-child`: Precision: 0.7500 | Recall: 0.1765 | F1: 0.2857
- `Unmarried`: Precision: 0.8571 | Recall: 0.2667 | F1: 0.4068
- `Wife`: Precision: 0.7113 | Recall: 0.7063 | F1: 0.7088

#### Race
- `Amer-Indian-Eskimo`: Precision: 0.6250 | Recall: 0.5000 | F1: 0.5556
- `Asian-Pac-Islander`: Precision: 0.7857 | Recall: 0.7097 | F1: 0.7458
- `Black`: Precision: 0.7600 | Recall: 0.5846 | F1: 0.6609
- `Other`: Precision: 1.0000 | Recall: 0.6667 | F1: 0.8000
- `White`: Precision: 0.7354 | Recall: 0.6345 | F1: 0.6812

#### Sex
- `Female`: Precision: 0.7209 | Recall: 0.5322 | F1: 0.6123
- `Male`: Precision: 0.7411 | Recall: 0.6525 | F1: 0.6940

#### Native Country
- `?`: Precision: 0.7586 | Recall: 0.7097 | F1: 0.7333
- `Cambodia`: Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
- `Canada`: Precision: 0.7778 | Recall: 0.8750 | F1: 0.8235
- `China`: Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
- `Columbia`: Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
- `Cuba`: Precision: 0.6667 | Recall: 0.8000 | F1: 0.7273
- `Dominican-Republic`: Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
- `Ecuador`: Precision: 1.0000 | Recall: 0.5000 | F1: 0.6667
- `El-Salvador`: Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
- `England`: Precision: 0.6667 | Recall: 0.5000 | F1: 0.5714
- `France`: Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
- `Germany`: Precision: 0.7500 | Recall: 0.6923 | F1: 0.7200
- `Greece`: Precision: 0.0000 | Recall: 0.0000 | F1: 0.0000
- `Guatemala`: Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
- `Haiti`: Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
- `Honduras`: Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
- `Hong`: Precision: 0.5000 | Recall: 1.0000 | F1: 0.6667
- `Hungary`: Precision: 1.0000 | Recall: 0.5000 | F1: 0.6667
- `India`: Precision: 0.8571 | Recall: 0.7500 | F1: 0.8000
- `Iran`: Precision: 0.3333 | Recall: 0.2000 | F1: 0.2500
- `Ireland`: Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
- `Italy`: Precision: 0.7500 | Recall: 0.7500 | F1: 0.7500
- `Jamaica`: Precision: 0.0000 | Recall: 1.0000 | F1: 0.0000
- `Japan`: Precision: 0.7500 | Recall: 0.7500 | F1: 0.7500
- `Laos`: Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
- `Mexico`: Precision: 1.0000 | Recall: 0.3333 | F1: 0.5000
- `Nicaragua`: Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000

## Ethical Considerations
While the model performs well on the provided datasets, it may not generalize to all possible data slices. Users should be cautious when deploying the model in real-world applications and consider potential biases in the training data.

## Caveats and Recommendations
The model may not perform well on data that is significantly different from the training and evaluation datasets. It is recommended to retrain or fine-tune the model with additional data if the application domain differs from the original training data.