import pandas as pd
import matplotlib.pyplot as plt

# Load the logistics dataset
df = pd.read_csv("../03_Data/Delivery_Logistics.csv")

# Display the first 5 rows
print(df.head())
# Check the columns in the dataset
print(df.columns)
# Check data types of all columns
print(df.dtypes)
# Check number of rows and columns
print("Dataset Shape:", df.shape)
# Check missing values in each column
print("Missing Values:")
print(df.isnull().sum())
# Check duplicate records
print("Duplicate Records:", df.duplicated().sum())
# Display basic statistics for numerical columns
print("Basic Statistics:")
print(df.describe())
# Check delivery status distribution
print("Delivery Status Count:")
print(df["delivery_status"].value_counts())
# Check delayed status distribution
print("Delayed Status Count:")
print(df["delayed"].value_counts())
# Calculate Delivery Delay Rate
delay_rate = (df["delayed"] == "yes").mean() * 100

print("Delivery Delay Rate:", round(delay_rate, 2), "%")
# Calculate On-Time Delivery Rate
on_time_rate = (df["delayed"] == "no").mean() * 100

print("On-Time Delivery Rate:", round(on_time_rate, 2), "%")
# Check delivery time values
print("Delivery Time Examples:")
print(df["delivery_time_hours"].head(10))
# Check expected delivery time values
print("Expected Time Examples:")
print(df["expected_time_hours"].head(10))
# Check unique delivery time values
print("Delivery Time Values:")
print(df["delivery_time_hours"].value_counts().head(20))
# Check unique expected time values
print("Expected Time Values:")
print(df["expected_time_hours"].value_counts().head(20))
# Convert delivery time from timestamp format to hours
df["delivery_time_hours"] = pd.to_datetime(
    df["delivery_time_hours"]
).dt.nanosecond

# Convert expected time from timestamp format to hours
df["expected_time_hours"] = pd.to_datetime(
    df["expected_time_hours"]
).dt.nanosecond

print(df[["delivery_time_hours", "expected_time_hours"]].head(10))
# Calculate average delivery and expected time
average_delivery_time = df["delivery_time_hours"].mean()
average_expected_time = df["expected_time_hours"].mean()

print("Average Delivery Time:", round(average_delivery_time, 2), "hours")
print("Average Expected Time:", round(average_expected_time, 2), "hours")
# Calculate average transportation cost per delivery
average_delivery_cost = df["delivery_cost"].mean()

print("Average Transportation Cost per Delivery:",
      round(average_delivery_cost, 2))
# Calculate Order Fulfillment Rate
fulfillment_rate = (df["delivery_status"] == "delivered").mean() * 100

print("Order Fulfillment Rate:", round(fulfillment_rate, 2), "%")
# Count deliveries by status
status_counts = df["delivery_status"].value_counts()

print("Delivery Status Count:")
print(status_counts)
# Calculate delivery status percentages
status_percentage = df["delivery_status"].value_counts(normalize=True) * 100

print("Delivery Status Percentage:")
print(status_percentage.round(2))
# Count deliveries by delivery partner
partner_counts = df["delivery_partner"].value_counts()

print("Delivery Partner Count:")
print(partner_counts)
# Calculate average delivery cost by partner
partner_cost = df.groupby("delivery_partner")["delivery_cost"].mean().sort_values(ascending=False)

print("Average Delivery Cost by Partner:")
print(partner_cost.round(2))
# Calculate delay rate by delivery partner
partner_delay_rate = (
    df.groupby("delivery_partner")["delayed"]
    .apply(lambda x: (x == "yes").mean() * 100)
    .sort_values(ascending=False)
)

print("Delay Rate by Partner:")
print(partner_delay_rate.round(2))
# Calculate delay rate by region
region_delay_rate = (
    df.groupby("region")["delayed"]
    .apply(lambda x: (x == "yes").mean() * 100)
    .sort_values(ascending=False)
)

print("Delay Rate by Region:")
print(region_delay_rate.round(2))
# Calculate delay rate by vehicle type
vehicle_delay_rate = (
    df.groupby("vehicle_type")["delayed"]
    .apply(lambda x: (x == "yes").mean() * 100)
    .sort_values(ascending=False)
)

print("Delay Rate by Vehicle Type:")
print(vehicle_delay_rate.round(2))
# Calculate delay rate by weather condition
weather_delay_rate = (
    df.groupby("weather_condition")["delayed"]
    .apply(lambda x: (x == "yes").mean() * 100)
    .sort_values(ascending=False)
)

print("Delay Rate by Weather Condition:")
print(weather_delay_rate.round(2))
# Calculate delay rate by delivery mode
mode_delay_rate = (
    df.groupby("delivery_mode")["delayed"]
    .apply(lambda x: (x == "yes").mean() * 100)
    .sort_values(ascending=False)
)

print("Delay Rate by Delivery Mode:")
print(mode_delay_rate.round(2))
# Create a bar chart for delivery status
status_counts = df["delivery_status"].value_counts()

status_counts.plot(kind="bar")

plt.title("Delivery Status Distribution")
plt.xlabel("Delivery Status")
plt.ylabel("Number of Deliveries")
plt.xticks(rotation=0)

plt.show()
# Create a bar chart for delay rate by weather condition
weather_delay_rate.plot(kind="bar")

plt.title("Delivery Delay Rate by Weather Condition")
plt.xlabel("Weather Condition")
plt.ylabel("Delay Rate (%)")
plt.xticks(rotation=0)

plt.show()
# Create a new figure for weather delay rate
plt.figure()

weather_delay_rate.plot(kind="bar")

plt.title("Delivery Delay Rate by Weather Condition")
plt.xlabel("Weather Condition")
plt.ylabel("Delay Rate (%)")
plt.xticks(rotation=0)

plt.show()
# Create a bar chart for delay rate by delivery mode
plt.figure()

mode_delay_rate.plot(kind="bar")

plt.title("Delivery Delay Rate by Delivery Mode")
plt.xlabel("Delivery Mode")
plt.ylabel("Delay Rate (%)")
plt.xticks(rotation=0)

plt.show()
# Create a scatter plot for distance and delivery cost
plt.figure()

plt.scatter(df["distance_km"], df["delivery_cost"])

plt.title("Distance vs Delivery Cost")
plt.xlabel("Distance (km)")
plt.ylabel("Delivery Cost")

plt.show()