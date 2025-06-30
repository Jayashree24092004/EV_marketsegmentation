import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')

# ----------------------------------------
# Load CSV #1: State-wise Annual Sales
# ----------------------------------------
state_df = pd.read_csv("Demographics_Data.csv", header=None,
                       names=["SNo", "State", "2019", "2020", "2021", "2022"])

state_df.drop(columns=["SNo"], inplace=True)

# Convert sales columns to numeric
for col in ["2019", "2020", "2021", "2022"]:
    state_df[col] = pd.to_numeric(state_df[col], errors='coerce')

# Add Total Sales Column
state_df["Total"] = state_df[["2019", "2020", "2021", "2022"]].sum(axis=1)

# ----------------------------------------
# Load CSV #2: Monthly E-2 Wheeler Sales
# ----------------------------------------
monthly_df = pd.read_csv("Ev_2_Wheeler_Sales_by_years.csv", header=None,
                         names=["Vehicle_Type", "Year", "Month", "Units_Sold"])

# Month ordering for consistency
month_order = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
               'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar']
monthly_df['Month'] = pd.Categorical(monthly_df['Month'], categories=month_order, ordered=True)

# ----------------------------------------
# Plot 1: Top 10 States by Total Sales
# ----------------------------------------
top_states = state_df.sort_values(by='Total', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(data=top_states, x='State', y='Total', palette='crest')
plt.title('Top 10 States by Total EV Sales (2019–2022)')
plt.ylabel('Units Sold')
plt.xlabel('State')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----------------------------------------
# Plot 2: Yearly National EV Sales (Sum of All States)
# ----------------------------------------
yearly_total = state_df[["2019", "2020", "2021", "2022"]].sum().reset_index()
yearly_total.columns = ['Year', 'Units_Sold']

plt.figure(figsize=(8, 5))
sns.lineplot(data=yearly_total, x='Year', y='Units_Sold', marker='o')
plt.title('EV Sales in India by Year (All States Combined)')
plt.xlabel('Year')
plt.ylabel('Units Sold')
plt.tight_layout()
plt.show()

# ----------------------------------------
# Plot 3: Monthly Trend of E-2 Wheelers
# ----------------------------------------
plt.figure(figsize=(14, 6))
sns.lineplot(data=monthly_df, x='Month', y='Units_Sold', hue='Year', marker='o')
plt.title('Monthly E-2 Wheeler Sales by Year')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.tight_layout()
plt.show()

# ----------------------------------------
# Plot 4: Top 5 Highest Selling Months
# ----------------------------------------
top_months = monthly_df.sort_values(by='Units_Sold', ascending=False).head(5)
print("\nTop 5 Highest-Selling Months:")
print(top_months[['Year', 'Month', 'Units_Sold']])
