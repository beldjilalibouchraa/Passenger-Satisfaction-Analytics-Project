import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Passenger Satisfaction Analysis")

df = pd.read_csv(r"C:\Users\HP\Downloads\passenger_survey_balanced.csv")

st.header("Business Problem")

st.write("""
The airport aims to improve passenger satisfaction and customer retention.
Using passenger survey data, this analysis identifies the factors that drive
satisfaction, highlights differences between customer segments, and explores
whether passenger satisfaction can be predicted using machine learning.
""")


st.header("Passenger Profile")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Age Distribution

age_counts = df["age_group"].value_counts()

axes[0, 0].bar(age_counts.index, age_counts.values, color="#4C78A8")
axes[0, 0].set_title("Age Distribution")
axes[0, 0].set_xlabel("Age Group")
axes[0, 0].set_ylabel("Passengers")
axes[0, 0].tick_params(axis='x', rotation=45)

# 2. Trip Purpose

trip_counts = df["trip_purpose"].value_counts().head(5)

axes[0, 1].bar(trip_counts.index, trip_counts.values, color="#F4A261")
axes[0, 1].set_title("Trip Purpose (Top 5)")
axes[0, 1].tick_params(axis='x', rotation=45)

# 3. Gender Distribution
gender_counts = df["gender"].value_counts()

axes[1, 0].pie(gender_counts.values, labels=gender_counts.index, autopct='%1.1f%%')
axes[1, 0].set_title("Gender Distribution")

# 4. Flight Type
flight_counts = df["flight_type"].value_counts()

axes[1, 1].bar(flight_counts.index, flight_counts.values, color="#E76F51")
axes[1, 1].set_title("Flight Type")

plt.tight_layout()
st.pyplot(fig)

st.write("""
         From the Age Distribution bar chart: The passenger base is concentrated in working-age adults, especially:

26–35 years /        
36–45 years

Together they account for the majority of passengers with known age information.
         
         From the Trip Purpose chart: The passenger base appears to be dominated by:

Leisure travelers
Business travelers

Together they represent the overwhelming majority of known travel purposes.

That means management should pay particular attention to:

convenience and efficiency for business travelers.
comfort and overall experience for leisure travelers.
         
         From the Gender Pie Chart: The distribution is fairly balanced.

Boarding passengers are slightly more male.

Disembarkation passengers are slightly more female.

No extreme imbalance exists.

That means:

Gender does not appear to be a major distinguishing characteristic of the passenger base.

Therefore, broad service improvements are likely to impact both genders similarly, rather than requiring heavily gender-specific initiatives.
         
         And from the Flight Type we conclude:

The airport's passenger base is overwhelmingly domestic.

This means:

- Most customer satisfaction improvements will affect domestic travelers.
- Domestic passenger experience should be the primary operational focus.
- International passengers are a smaller segment, but may still require specialized services such as immigration, customs, and language support.
         
         Which customer segments contribute the most passengers?

Based on what we found:

- Domestic passengers are the dominant segment (~90%).

- Most passengers with known age data are 26–45 years old.

- Leisure and business travelers are the largest travel-purpose groups.

- Gender distribution is relatively balanced.""")


st.header("Satisfaction Drivers")
st.write("""Insight:
  As internet quality increases, satisfaction increases sharply
From: 
13% → 72% .
That’s almost a 6x increase!

“Airport internet quality is a strong driver of passenger satisfaction, showing a clear upward trend across rating levels.”
""")

st.write("""  Boarding lounge comfort shows a non-linear relationship with passenger satisfaction, with a sharp increase in satisfaction after rating level 3, indicating a critical service threshold effect.

This suggests:

1. Low ratings are catastrophic

If lounge comfort is bad (1–3), satisfaction collapses.

2. Medium improvement has outsized impact

Going from “average” to “good” (3 → 4) is the biggest lever.

3. High-quality lounges strongly drive loyalty

At rating 5, satisfaction reaches 85% → very strong retention driver.""")

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

df.groupby("airport_internet")["liked"].mean()
internet_table = df.groupby("airport_internet")["liked"].mean().reset_index()
internet_table.columns = ["airport_internet", "pct_liked"]
internet_table["pct_liked"] = internet_table["pct_liked"] * 100
axes[0].plot(internet_table["airport_internet"], internet_table["pct_liked"])
axes[0].set_title("Internet vs Satisfaction")
axes[0].set_xlabel("Rating")
axes[0].set_ylabel("% Liked")

comfort_table = df.groupby("boarding_lounge_comfort")["liked"].mean().reset_index()

comfort_table.columns = ["boarding_lounge_comfort", "pct_liked"]
comfort_table["pct_liked"] = comfort_table["pct_liked"] * 100
axes[1].plot(comfort_table["boarding_lounge_comfort"], comfort_table["pct_liked"])
axes[1].set_title("Lounge Comfort vs Satisfaction")
axes[1].set_xlabel("Rating")
axes[1].set_ylabel("% Liked")

plt.tight_layout()
st.pyplot(fig)

food_table = df.groupby("food_beverage_outlets")["liked"].mean().reset_index()

food_table.columns = ["food_beverage_outlets", "pct_liked"]
food_table["pct_liked"] = food_table["pct_liked"] * 100

cleanliness_table = df.groupby("overall_airport_cleanliness")["liked"].mean().reset_index()

cleanliness_table.columns = ["overall_airport_cleanliness", "pct_liked"]
cleanliness_table["pct_liked"] = cleanliness_table["pct_liked"] * 100

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(food_table["food_beverage_outlets"], food_table["pct_liked"])
axes[0].set_title("Food Beverage Outlets vs Satisfaction")
axes[0].set_xlabel("Rating")
axes[0].set_ylabel("% Liked")

axes[1].plot(cleanliness_table["overall_airport_cleanliness"], cleanliness_table["pct_liked"])
axes[1].set_title("Airport Cleanliness vs Satisfaction")
axes[1].set_xlabel("Rating")
axes[1].set_ylabel("% Liked")

plt.tight_layout()
st.pyplot(fig)

st.write(""" 1. Weak impact at low-mid range
1 → 3 barely changes (10% → 22%)

 passengers are still mostly dissatisfied even with small improvements

2. Strong jump after level 3
3 → 4: 22% → 51%

 this is the key threshold
 
3. High quality matters a lot
5 reaches 72%

 good food experience strongly supports satisfaction

 Interpretation

--> Food & beverage is a “mid-to-high sensitivity driver”

Not critical when bad (like lounge comfort or cleanliness)
But becomes important once basic service is decent

Business meaning:
Improving from “average” to “good” has the biggest ROI

Food quality is a supporting satisfaction enhancer, not the primary driver.""")
st.write(""" 1. Extremely low tolerance for poor cleanliness
Ratings 1–3 → satisfaction is basically near zero

 This is a hard failure zone

2. Massive threshold effect at rating 4
3 → 4 jumps:

8% → 43% (!!)

3. Strong satisfaction only at top level

5 → 75%

Interpretation:

--> Cleanliness is a “critical hygiene factor”

This is NOT optional.

It behaves like:

If bad → passengers are strongly dissatisfied

If good → satisfaction rises sharply

Business meaning:
  Cleanliness is a non-negotiable baseline requirement.
It directly impacts perception of the entire airport.""")

st.write(""" Which service factors have the strongest impact on satisfaction?

🔴 Critical drivers (HIGHEST impact)

boarding_lounge_comfort
overall_airport_cleanliness

 These show:

- extreme low satisfaction when poor
- strong threshold effects
- big jumps at rating 4–5

🟠 Strong supporting drivers
airport_internet

 smooth increase, strong linear effect

🟡 Secondary drivers
food_beverage_outlets

 matters, but not as catastrophic when poor

Passenger satisfaction is primarily driven by core airport experience factors (cleanliness and lounge comfort), which act as critical thresholds, while digital services and food & beverage act as secondary enhancers that improve satisfaction once baseline experience is acceptable.""")


st.header("Waiting Time Impact on Satisfaction")

bins = [0, 3600, 7200, 10800]
labels = ["<1h", "1-2h", "2-3h"]

df["connection_group"] = pd.cut(
    df["connection_wait_time"],
    bins=bins,
    labels=labels
)

connection_results = df.groupby("connection_group", observed=True)["liked"].mean()
connection_pct = connection_results * 100

fig, ax = plt.subplots(figsize=(7, 4))

ax.barh(connection_pct.index, connection_pct.values, color="#4C78A8")

ax.set_xlabel("% Satisfied")
ax.set_title("Satisfaction by Connection Wait Time")

st.pyplot(fig)

bins = [0, 5400, 9000, 10801]
labels = ["<90 min", "90-150 min", ">150 min"]

df["arrival_group"] = pd.cut(
    df["arrival_lead_time"],
    bins=bins,
    labels=labels
)

arrival_results = df.groupby("arrival_group", observed=True)["liked"].mean()
arrival_pct = arrival_results * 100

fig, ax = plt.subplots(figsize=(7, 4))

ax.barh(arrival_pct.index, arrival_pct.values, color="#E76F51")

ax.set_xlabel("% Satisfied")
ax.set_title("Satisfaction by Arrival Lead Time")

st.pyplot(fig)

st.write(""" Connection waiting time does not appear to have a meaningful impact on overall passenger satisfaction within the observed range (45 minutes to 3 hours).

Passenger satisfaction remains relatively stable regardless of how early passengers arrive at the airport.

Passenger satisfaction is driven much more by service quality and comfort factors than by arrival lead times or connection waiting times.""")


st.header("Most Satisfied Customer Groups")

trip_purpose_comp = (
    df[df['trip_purpose'].isin(['Business', 'Leisure'])]
      .groupby('trip_purpose')
      .agg(
          satisfaction_rate=('liked', lambda x: round(x.mean() * 100, 2)),
          passengers=('liked', 'count')
      )
      .reset_index()
)
st.write(""" Leisure travelers show a higher satisfaction rate (51.75%) than business travelers (43.75%). Despite representing a slightly larger passenger segment, leisure travelers are considerably more satisfied with the airport experience. Business travelers appear to be more demanding and may be more sensitive to service quality, convenience, and efficiency issues.""")

returning_vs_new = (
    df[df['used_airport_before_last_12_months'].isin(['Yes', 'No'])]
      .groupby('used_airport_before_last_12_months')
      .agg(
          satisfaction_rate=('liked', lambda x: round(x.mean() * 100, 2)),
          passengers=('liked', 'count')
      )
      .reset_index()
)
st.write(""" Combined with the trip purpose analysis:

Leisure travelers are more satisfied than business travelers.

New passengers are more satisfied than returning passengers.

A possible interpretation is that repeat users develop higher expectations and become more critical of airport services, while first-time or occasional users tend to evaluate the experience more positively.""")

dom_int_comp = (
    df.groupby('flight_type')
      .agg(
          satisfaction_rate=('liked', lambda x: round(x.mean() * 100, 2)),
          passengers=('liked', 'count')
      )
      .reset_index()
)

mapping = {
    '0': 0,
    '1': 1,
    '2 to 3': 2.5,
    '4 to 5': 4.5,
    '6 to 10': 8,
    '11+': 12
}

df['trips_num'] = df['trips_last_12_months'].map(mapping)
df['travel_frequency'] = df['trips_num'].apply(
    lambda x: 'Frequent' if x >= 4 else 'Infrequent'
)

freq_comp = (
    df.groupby('travel_frequency')
      .agg(
          satisfaction_rate=('liked', lambda x: round(x.mean() * 100, 2)),
          passengers=('liked', 'count')
      )
      .reset_index()
)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

data = trip_purpose_comp.sort_values('satisfaction_rate')

axes[0, 0].barh(
    data['trip_purpose'],
    data['satisfaction_rate'],
    color='#4C78A8'
)
axes[0, 0].set_title('Trip Purpose')
axes[0, 0].set_xlabel('Satisfaction Rate (%)')
axes[0, 0].set_xlim(0, 100)

for i, v in enumerate(data['satisfaction_rate']):
    axes[0, 0].text(v + 1, i, f"{v:.1f}%", va='center')


axes[0, 1].bar(
    returning_vs_new['used_airport_before_last_12_months'],
    returning_vs_new['satisfaction_rate'],
    color='#F4A261'
)
axes[0, 1].set_title('Returning vs New')
axes[0, 1].set_ylabel('Satisfaction Rate (%)')
axes[0, 1].set_ylim(0, 100)

for i, v in enumerate(returning_vs_new['satisfaction_rate']):
    axes[0, 1].text(i, v + 1, f"{v:.1f}%", ha='center')


freq_sorted = freq_comp.sort_values('satisfaction_rate')

axes[1, 0].barh(
    freq_sorted['travel_frequency'],
    freq_sorted['satisfaction_rate'],
    color='#2A9D8F'
)
axes[1, 0].set_title('Travel Frequency')
axes[1, 0].set_xlabel('Satisfaction Rate (%)')
axes[1, 0].set_xlim(0, 100)

for i, v in enumerate(freq_sorted['satisfaction_rate']):
    axes[1, 0].text(v + 1, i, f"{v:.1f}%", va='center')


axes[1, 1].bar(
    dom_int_comp['flight_type'],
    dom_int_comp['satisfaction_rate'],
    color='#E76F51'
)
axes[1, 1].set_title('Domestic vs International')
axes[1, 1].set_ylabel('Satisfaction Rate (%)')
axes[1, 1].set_ylim(0, 100)

for i, v in enumerate(dom_int_comp['satisfaction_rate']):
    axes[1, 1].text(i, v + 1, f"{v:.1f}%", ha='center')



plt.tight_layout()
st.pyplot(fig)


st.write(""" Insight:

Domestic passengers are slightly more satisfied than international passengers, but the gap is small (~1.2 percentage points).

Interpretation

This suggests:

The core airport experience is fairly consistent across flight types

International passengers experience slightly more friction, likely due to:
immigration procedures - 
security complexity - 
longer processing times - 
multi-step journeys

But the difference is not large enough to indicate a major structural problem.""")

st.write(""" Frequent travelers are less satisfied than infrequent travelers.

Frequent users are likely:

more familiar with airport processes -
more sensitive to inefficiencies - 
have higher expectations for service quality

So they tend to rate the experience more critically.

Infrequent users:

have lower expectations - 
are more tolerant of delays or service gaps - 
evaluate experience more positively - 

The airport is performing better for occasional users, but underperforming for high-value, high-frequency passengers.""")


st.header("Predictive Model (Logistic Regression)")

importance = pd.read_csv(r"C:\Users\HP\Downloads\importance.csv")
st.dataframe(importance.head(10))
st.write(""" 1. What drives satisfaction (strong positive factors)

🔝 Top drivers:

- boarding_lounge_comfort (+1.34)
- baggage_claim_process (+1.10)
- food_beverage_quality_variety (+0.68)
- security_screening_process (+0.65)
- checkin_process (+0.62)
- airport_internet (+0.49)
- restroom_cleanliness (+0.45)

🧠 Insight: 

Passenger satisfaction is dominated by physical experience and service quality, especially:

- Comfort in waiting areas
- Baggage experience (final impression matters a lot)
- Food & beverage quality
- Core operational flows (check-in, security)

👉 This confirms earlier EDA finding:

Operational comfort factors matter more than timing variables.

📉 2. Weak or negative drivers

Negative or weak contributors:

- Older age groups (46+) → negative coefficients
- Shopping trips → negative satisfaction
- Unknown / unclear trip purpose → strongly negative (-0.25)
- High-income groups slightly negative

🧠 Insight

- Older passengers are more critical / less satisfied
- Non-clear travel intent = lower satisfaction (important data quality + experience signal)
- Higher expectations likely reduce satisfaction among wealthier travelers

✈️ 3. Interesting weak signals:

flight_type_International (~0) → almost no impact

👉 International vs domestic is NOT a satisfaction driver

gender, age 26–35, traveling alone → almost neutral

👉 These are not meaningful segmentation factors compared to service quality.

💼 4. Business interpretation :

The predictive model shows that passenger satisfaction is primarily driven by service quality and airport experience factors rather than demographic or travel-type variables. In particular, comfort-related features such as boarding lounge comfort, baggage handling, and food & beverage quality have the strongest positive impact.

🚨 5. Key business takeaway :

Improving physical airport experience (comfort, food, baggage handling, and check-in processes) will have a significantly higher impact on satisfaction than targeting specific passenger demographics.""")


