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
print("25 df.head: ", df.head())

# Step 1: Standardize Product Names
# Ensure product names follow a consistent naming convention.

# Define a list of unnecessary words
unneccesarry_words = ['large', 'compact', 'advanced']
# Create a regex pattern to match the unnecessary words
pattern = '|'.join(unneccesarry_words)

# Ensure product names follow a consistent naming convention
df['product_name'] = df['product_name'].str.lower().replace(pattern, ' ', regex=True)


# Step 2: Convert Units to a Consistent Format
def convert_to_kg(weight):
    if pd.isnull(weight):
        return np.nan
    elif 'lbs' in weight:
        return float(weight.replace('lbs', '').strip()) * 0.453592
    elif 'kg' in weight:
        return float(weight.replace('kg', '').strip())
    else:
        return np.nan

df['weight_kg'] = df['weight'].apply(convert_to_kg)
print("39: ", df.head())
# Step 3: Trim Lengthy Descriptions
df['description'] = df['description'].apply(lambda x: x[:50] if isinstance(x, str) else x)

# Step 4: Handle Missing Product Details
# Identify missing values and decide how to handle them (e.g., fill, drop, or use a placeholder).

# df['description'].fillna('No description', inplace=True)
# df['weight_kg'].fillna(df['weight_kg'].mean(), inplace=True)

df.fillna({'description': 'No description'}, inplace=True)
df['weight_kg'] = df['weight_kg'].fillna(df['weight_kg'].mean())
print("49: ", df.head())

# Step 5: Remove Duplicate Entries
# Keep the first
df = df.drop_duplicates(subset='product_id', keep='first')
print("56: ", df.head())

# Step 6: Save the Cleaned Data
# Save the cleaned DataFrame for inventory management use.

df.to_csv('____', index=False)
print("61: ", df)

