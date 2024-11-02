Topic: Standardizing Product Listings for Inventory Management
DataFrames in Python are data a structure, a lot like a supercharged excel sheet on 3 Redbulls. Its design permits efficient handling of rows and columns, each labeled and capable of independent data types, thereby facilitating complex data operations with precision. Unlike traditional spreadsheet software, a DataFrame executes entirely in memory, enabling rapid manipulation of large datasets without reliance on manual inputs. It is optimized for computational tasks—statistical calculations, data cleansing, and even machine learning preparation—executed through precise, reproducible code. It is an analysis tool, not a database. 

Objective: Organize a dataset of product listings to ensure uniform data across multiple vendors for inventory management.
	•	Dataset Structure: You receive a CSV file with product listings, each with inconsistent naming conventions, units, and descriptions.
	•	Task Requirements: Standardize product names, convert units (e.g., lbs to kg), and trim lengthy descriptions to a consistent format.
	•	Challenges: Handle missing product details, recognize product variants, and eliminate duplicate listings based on product ID.
	•	Expected Outcome: A cleaned dataset with standardized product names, uniform units, and concise descriptions, ready for accurate inventory tracking.
0. Generating Mock Product Listings Data
This setup generates mock data with issues commonly seen in product listings, including inconsistent naming, units, and lengthy descriptions.

import pandas as pd
import numpy as np

np.random.seed(0)

data = {
    'product_id': np.arange(1, 101),
    'product_name': np.random.choice(['Widget A', 'widget-a', 'Widget A Large', 'Gadget B', 'gadget-b'], 100),
    'weight': np.random.choice(['2 lbs', '0.9 kg', '3 lbs', '1.4 kg', np.nan], 100),
    'description': np.random.choice([
        'A very useful widget that performs a variety of functions and tasks, suitable for home and office use.',
        'A compact gadget, easy to store and very efficient for small tasks.',
        'An advanced widget with extended features, ideal for professional use.',
        'A large-sized gadget offering high performance and durability.',
        np.nan
    ], 100)
}

df = pd.DataFrame(data)

duplicate_ids = np.random.choice(df['product_id'], 10)
df = pd.concat([df, df[df['product_id'].isin(duplicate_ids)]])

# Check the first few rows
df.head()


Steps with Incomplete Code Snippets
Step 1: Standardize Product Names
Ensure product names follow a consistent naming convention.

df['product_name'] = df['product_name'].str.lower().replace(____, regex=True)

Define a dictionary or regex pattern to remove unnecessary words like "large" or replace "-" with spaces.
Step 2: Convert Units to a Consistent Format
Convert weights to kilograms for consistency across listings.

def convert_to_kg(weight):
    if pd.isnull(weight):
        return np.nan
    elif 'lbs' in weight:
        return float(weight.replace('lbs', '').strip()) * 0.453592
    elif 'kg' in weight:
        return float(weight.replace('kg', '').strip())
    else:
        return np.nan

df['weight_kg'] = df['weight'].apply(____)

Fill in the function name (convert_to_kg) to standardize units.
Step 3: Trim Lengthy Descriptions
Limit descriptions to a certain length for uniformity.

df['description'] = df['description'].apply(lambda x: x[:____] if isinstance(x, str) else x)

Specify the number of characters to keep (e.g., 50).
Step 4: Handle Missing Product Details
Identify missing values and decide how to handle them (e.g., fill, drop, or use a placeholder).

df['description'].fillna(____, inplace=True)

df['weight_kg'].fillna(df['weight_kg'].____(), inplace=True)

Decide on a placeholder for missing descriptions and a method to handle missing weights.
Step 5: Eliminate Duplicate Listings
Remove duplicate product listings based on product_id.

df = df.drop_duplicates(subset='product_id', keep=____)

Specify whether to keep the first or last duplicate.
Step 6: Save the Cleaned Data
Save the cleaned DataFrame for inventory management use.

df.to_csv('____', index=False)



