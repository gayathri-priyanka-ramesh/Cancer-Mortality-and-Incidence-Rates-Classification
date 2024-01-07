# Cancer-Mortality-and-Incidence-Rates-Classification

## Project Description
Cancer is a complex and multifaceted disease that can have a profound impact on individuals, families, and communities. In order to understand the scope and impact of cancer, it is important to track key measures such as cancer mortality and incidence rates. These measures provide important insights into the prevalence and impact of cancer within a given population, as well as how this burden is changing over time. The causes of cancer mortality and incidence rates are complex and multifactorial, involving a combination of genetic, environmental, and lifestyle factors. Machine learning algorithms can be trained on large datasets of cancer-related data, including patient demographics, medical histories, genetic data, and other relevant factors, to identify patterns and predict cancer mortality and incidence rates. The goal of this task is to predict status of cancer incidence or mortality rate based on a set of features.

## Attribute Information
The attributes provided in the dataset can serve as input features for the prediction task. Here's a breakdown of the attributes and their potential roles in the prediction:
1.	Index: Index or unique identifier for each data entry. It doesn't provide any predictive value and can be ignored during the modeling process.
2.	County: The county attribute represents the geographical location of the data entry. It can be useful for analyzing regional variations in cancer rates and potentially capturing the impact of localized factors.
3.	FIPS: Federal Information Processing Standards, which is a standardized numerical code for identifying counties and other geographic entities. Similar to the county attribute, it can be used to capture geographic variations. However, it may not directly contribute to the prediction task and could be excluded or transformed as needed.
4.	Age-Adjusted Incidence Rate (ÃŠ) - cases per 100,000: Incidence rate of cancer per 100,000 people, adjusted for age. It is a critical feature for the prediction task as it directly relates to the target variable.
5.	Lower 95% Confidence Interval: Lower bound of the confidence interval for the incidence rate used to estimate the uncertainty around the incidence rate.
6.	Upper 95% Confidence Interval: Upper bound of the confidence interval for the incidence rate provides information about the range within which the true incidence rate is likely to fall.
7.	Average Annual Count: Average annual count of cancer cases. It can be a relevant feature as it provides information about the frequency of cancer cases.
8.	Recent Trend (falling, stable, rising, *, _, __): Recent trend in cancer rates, with categories such as falling, stable, rising. It can provide valuable information for predicting future rates, as it captures the direction of change. This will be the target variable that you'll aim to predict.
9.	Recent 5-Year Trend (Ë†) in Incidence Rates: 5-year trend in incidence rates provides a more extended period for analyzing the direction of change compared to the previous attribute.
10.	Lower 95% Confidence Interval.1: Lower bound of the confidence interval for the recent 5-year trend in incidence rates provides additional information about the uncertainty associated with the trend.
11.	Upper 95% Confidence Interval.1: Upper bound of the confidence interval for the recent 5-year trend in incidence rates provides information about the range within which the true trend is likely to fall.

## Result
Cancer Status -> Falling, Stable, Rising

## Tech at Play
### Python libraries
Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn
### Algorithm
Implemented machine learning algorithms in Python.

## Standout Characteristics
Achieved a high predictive accuracy of 85% in determining cancer incidence or mortality rates, showcasing the effectiveness of the machine learning model.  
Comprehensive documentation was done ensuring the transfer of knowledge and insights derived from the project.
