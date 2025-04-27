import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
file_path = "Data Analyst Intern Assignment - Excel.xlsx"
user_details  = pd.read_excel(file_path,"UserDetails.csv")
cooking_sessions  = pd.read_excel(file_path,"CookingSessions.csv")
order_details  = pd.read_excel(file_path,"OrderDetails.csv")

# Cleaning UserDetails
user_details.drop_duplicates(subset=['User ID'], inplace=True)
user_details['Phone'] = user_details['Phone'].str.replace(r'\D', '', regex=True)
user_details['Registration Date'] = pd.to_datetime(user_details['Registration Date'])
user_details.fillna({'Favorite Meal': 'Unknown'}, inplace=True)

# Cleaning CookingSessions
cooking_sessions.drop_duplicates(subset=['Session ID'], inplace=True)
cooking_sessions['Session Start'] = pd.to_datetime(cooking_sessions['Session Start'])
cooking_sessions['Session End'] = pd.to_datetime(cooking_sessions['Session End'])
cooking_sessions['Duration (mins)'] = (cooking_sessions['Session End'] - cooking_sessions['Session Start']).dt.total_seconds() / 60
cooking_sessions['Session Rating'] = cooking_sessions['Session Rating'].fillna(cooking_sessions['Session Rating'].mean())

# Cleaning OrderDetails
order_details.drop_duplicates(subset=['Order ID'], inplace=True)
order_details['Order Date'] = pd.to_datetime(order_details['Order Date'])
order_details['Amount (USD)'] = order_details['Amount (USD)'].fillna(0)
order_details.loc[order_details['Order Status'] == 'Cancelled', 'Amount (USD)'] = 0
order_details['Rating'] = order_details['Rating'].fillna(order_details['Rating'].mean())

