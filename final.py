import pandas as pd

# #From now on, for every place we are going to examine the data, we are marking the code as a "note" for efficiency.
# function for showing the head
def show_head(df):
    return df.head()


def show_data_type(df):
    return df.dtypes


def show_info(df):
    return df.info()

# 0. To start with, I have read the file to a dataframe.
"""
print(show_head(pd.read_excel('data/Amazon.xlsx')))
"""
# I wanted to skip the title and the empty row in order to have a better view.
df = pd.read_excel('data/Amazon.xlsx', skiprows=2)
# let's check the changed data
"""
print(show_head(df))
"""
df = pd.read_excel('data/Amazon.xlsx', header=None, skiprows=3)
# after the checking, it seems good. To check the datatype we first name columns
df.columns = ["Category", "Product ID", "Year", "Quarter", "Quarterly Sales", "Customer Rating", "Seller Rating",
              "Price", "Discount Rate", "Units Sold", "Revenue", "Shipping Method", "Location", "Advertising Cost"]
# 1. examine the variables and their datatypes
"""
print(show_data_type(df))
"""
# there seems to be problem with Discount Rate and Seller Rating, they should ve integer instead of floats.
# We are going to do this change later since it will be much easier
# 2. remove any separation error in variables.

# since we defined the header there is no need to check the existence of it
# check the exising of NA's
"""
print(df.isnull().any())
"""
# it is showed that there are NA's values in Seller Rating, Advertising Cost, Quarterly Sales

# Check if the column contains different types of values
for column in df.columns:
    unique_types = df[column].apply(type).unique()

    # Display the result
    if len(unique_types) > 1:
        print(f"The column: {column} contains different types: {unique_types}")
    else:
        print(f"The column: {column} contains only one type.")
# so, there is a problem only in The column: Quarterly Sales, we will consider it later

# Remove specified characters from string columns
df.replace(to_replace=[r'\{', r'\}', r';', r':', r',', r'\t', r'\n'], value='', regex=True, inplace=True)

# remove the all whitespaces
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# 4 we already fixed the column names

# 5 - The product ID column is unnecessary for data visualization, so I'm deleting it. Ask why to Liza? I have no idea what she is thinling about a
# I don't understand women
# df = df.drop("Product ID", axis=1)

# 6 - Now I'm going to eliminate the duplicates since they are not in the nature of the data.
duplicates = df.duplicated()
df.drop_duplicates(inplace=True)
# And by this, dropped the duplicates.
# 7 - Now I will check if we have any unnecessary strings in the values.
# we already checked it

# 8 - Now to remove the white spaces before the strings
# we already did it

# 9 - To format the string values we will check the names for nominal values
# I will do it later

# make all titles in same format
df["Category"] = df["Category"].str.title()

# 10 - We don't have to check if levels of categories are unique since we don't need it to be unique for this data set.

# 11 - We don't need to create a date column since we only have the quarter and year

# 12 - since we only have the year and quarter as the date's values,
# we should change "Year" (Quarter is already "object") to object
df['Year'] = df['Year'].astype(str)

# I will fix the datatypes later since if I do it now it will collapse the code

# 13.	Examine the descriptive statistics of numerical variables. Search for any unusual behavior.
# Are the variables in the correct range? If not, find the locations and correct them.
# first of all let's find NA values in all columns

for col in df.columns:
    na_amount = df[col].isna().sum()
    if na_amount != 0:
        print(f'{col} has {na_amount} NA values')

# we've found that values in Quarterly Sales is Revenue divide on Units Sold. So, instead of replacing
# all data by the mean/median/mode we can just replace it by Revenue divide on Units Sold
df['Quarterly Sales'] = df['Quarterly Sales'].replace('NA', pd.NA)
df['Quarterly Sales'] = df['Quarterly Sales'].fillna(df["Revenue"] // df["Units Sold"])
df['Quarterly Sales'] = df['Quarterly Sales'].astype(int)
# In the seller rating there are NA values. So, let's replace them by
# median of rating since all data in integer we should use meidna
df['Seller Rating'].fillna(df['Seller Rating'].median(), inplace=True)

# In the Advertisment cost it is impossible to estimate a advertismant cost to the product and we have only two NA
# we wouldn't lose so much if we remove two string and also all our data is integer we should change the datatype
# to integer

# df = df.dropna(subset=['Advertising Cost'])
# df["Advertising Cost"] = df["Advertising Cost"].astype(int)
# df['Advertising Cost'].fillna(df['Advertising Cost'].mean(), inplace=True)
df['Advertising Cost'].fillna(df['Advertising Cost'].mean(), inplace=True)

# range of rating is unlikely to be negative since almost all data is ranging
# from 0 to 5. we should change the negative values to positive one
# also convert all data to integer since all data is integer numbers
df["Customer Rating"] = df["Customer Rating"].abs().astype(int)

# some data in year is typed in a wring for example instead of 2019 there is written 20199

df['Year'] = df['Year'].str[:4]



# the discount rate has a different values one values with "%" other not let's convert all values to one datatype
df['Discount Rate'] = pd.to_numeric(df['Discount Rate'], errors='coerce')
df['Discount Rate'] = df["Discount Rate"].astype(int)

# 14 outliers
# first, we need to write a code which will check whether in column exist outliers or not
# Function to identify outliers using IQR
def identify_outliers_by_category(df, category_column, numerical_column):
    categories = df[category_column].unique()
    outliers_dict = {}

    for category in categories:
        subset = df[df[category_column] == category]
        column = subset[numerical_column]

        Q1 = column.quantile(0.25)
        Q3 = column.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 3 * IQR
        upper_bound = Q3 + 3 * IQR
        outliers = column[(column < lower_bound) | (column > upper_bound)]

        # Check if the number of outliers doesn't exceed 10% of the category's data
        if not outliers.empty:
            category_count = len(subset)
            outlier_count = len(outliers)
            if outlier_count / category_count <= 0.1:
                outliers_dict[category] = outliers

    return outliers_dict

outliers_by_category = {}
for numerical_column in df.select_dtypes(include='number').columns:
    if numerical_column not in ["Customer Rating", "Seller Rating", "Discount Rate"]:
        outliers_by_category[numerical_column] = {}
        for category_column in ['Category']:
            outliers_by_category[numerical_column][category_column] = identify_outliers_by_category(df, category_column,
                                                                                                    numerical_column)
# Displaying outliers for each category
for numerical_column, category_dict in outliers_by_category.items():
    print(f"\nOutliers in {numerical_column} by Category:")
    for category_column, outliers in category_dict.items():
        if outliers:
            for cat, out_vals in outliers.items():
                print(f"Outliers in {cat}: {out_vals.values}")
        else:
            print(f"No outliers in {category_column}")

# Replacing outliers by mean of the specific columns within each category
for numerical_column, category_dict in outliers_by_category.items():
    for category_column, outliers in category_dict.items():
        for cat, out_vals in outliers.items():
            category_mean = df.loc[df[category_column] == cat, numerical_column].mean().astype(int)
            df.loc[(df[category_column] == cat) & df[numerical_column].isin(out_vals), numerical_column] = category_mean



# def replace_outliers_with_mean(column):
#     Q1 = column.quantile(0.25)
#     Q3 = column.quantile(0.75)
#     IQR = Q3 - Q1
#     lower_bound = Q1 - 1.5 * IQR
#     upper_bound = Q3 + 1.5 * IQR
#
#     # Identify and replace outliers
#     outliers = column[(column < lower_bound) | (column > upper_bound)]
#     df.loc[outliers.index, column.name] = column.mean()
#
#     return column
#
#
# # Replace outliers in each numeric column
# for column in df.select_dtypes(include=['number']).columns:
#
#     df[column] = replace_outliers_with_mean(df[column])


# make all data in columns in one type
df['Category'] = df['Category'].replace({'BEAUTY': 'Beauty',
                                         'ELECTRONICS': 'Electronics',
                                         'Home - Kitchen': 'Home & Kitchen',
                                         'Book': 'Books'})
df['Location'] = df['Location'].replace({'United States': 'US', 'ASIA': 'Asia', 'European Union': 'EU'})

# change all strings to lower case

# change the datatypes of variables where it needed
df['Quarterly Sales'] = df['Quarterly Sales'].astype(float)
df['Seller Rating'] = df['Seller Rating'].astype(float)
df['Advertising Cost'] = df['Advertising Cost'].astype(float)
# change all variables to lower case
# df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)


#And with this step, the data cleaning part is done.
# Save data to Excel file and csv file
csv_filename = 'data/filtered_amazon.csv'
df.to_csv(csv_filename, index=False)

csv_filename = 'data/filtered_amazon.xlsx'
df.to_excel(csv_filename, index=False)
