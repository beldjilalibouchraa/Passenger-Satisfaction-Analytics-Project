# Passenger-Satisfaction-Analytics-Project
This project analyzes airline passenger satisfaction data to identify the key drivers of customer experience, detect differences across passenger segments, and build a predictive model to estimate satisfaction levels.  The goal is to help airline management improve service quality, reduce dissatisfaction, and increase customer retention.

## Live Dashboard

https://passenger-satisfaction-analytics-project.streamlit.app/

## Dataset
The dataset includes passenger survey responses covering: (csv file above)

- Demographics (age, gender, income, nationality)
- Travel information (trip purpose, flight type, frequency)
- Airport experience (check-in, security, boarding, baggage)
- Service quality ratings (internet, food, cleanliness, comfort, etc.)
- Overall satisfaction (`liked` target variable)

## Data Processing
- Handled missing values using appropriate imputation methods
- Encoded categorical variables for analysis and modeling
- Created grouped features (e.g., waiting time categories)
- Performed segmentation analysis across key passenger groups

## Exploratory Data Analysis (EDA)
Key insights:
- Satisfaction is strongly influenced by **service quality and comfort factors**
- Business travelers are generally less satisfied than leisure travelers
- Frequent travelers show lower satisfaction levels than infrequent ones
- Returning passengers tend to be more critical in evaluations

## Predictive Model
A Logistic Regression model was trained to predict passenger satisfaction.

### Performance:
- Accuracy: **~73%**

### Key Drivers of Satisfaction:
- Boarding lounge comfort
- Baggage claim experience
- Food and beverage quality
- Check-in process
- Security screening experience
- Airport cleanliness

## Streamlit Dashboard
An interactive Streamlit dashboard was built to:

- Explore passenger demographics
- Visualize satisfaction across segments
- Analyze service quality impact
- Display model results and feature importance

## Business Recommendations
- Improve boarding lounge comfort and seating experience
- Optimize baggage handling efficiency
- Enhance food and beverage quality and variety
- Improve check-in and security processes
- Focus on frequent and business travelers for retention strategies

## Tools Used
- Python (Pandas, Matplotlib, Scikit-learn)
- Streamlit
- Jupyter Notebook
- Logistic Regression model

## How to Run This Project

### 1. Clone repository
git clone https://github.com/beldjilalibouchraa/Passenger-Satisfaction-Analytics-Project.git

### 2. Install requirements
pip install -r requirements.txt

### 3. Run Streamlit app
streamlit run app.py

## Author

Beldjilali Bouchra
Data Analyst Portfolio Project
