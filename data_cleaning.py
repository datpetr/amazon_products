import pandas as pd

# You might want to change the first pf.read to read a csv file instead of excel.
# Also the code I wrote does not
# change the original file.


"""
1.	Examine the variables and their data types.
2.	Examine the head and tail of the data frame. Make sure that you import your data correctly. 
Check for any separation argument problem (“;” or “,”) of the data, the existence of header in the dataset as well as the existence of NAs.
3.	Check whether
a.	Column headers are values, not variable names.
b.	Multiple variables are stored in one column.
c.	Variables are stored in both rows and columns.
d.	Multiple types of observational units are stored in the same table.
e.	A single observational unit is stored in multiple tables.
 If so, apply data tidying techniques such as stack/unstack, melt, and pivot. 
 Examine the head and tail of the tidy data frame.
4.	Fix the column names if you detect any typos.
5.	Drop unnecessary columns.
6.	Remove the duplicates if it is not the nature of the data. 
7.	Get rid of any unnecessary strings in the values.
8.	Remove the white spaces in the string values.
9.	Be sure that all strings are in the same format (e.g. all in lower-case). If not, correct them.
10.	Look at the value counts of strings and be sure that all levels of the categories are unique. If not, correct them.
11.	If you have year, month, and/or day columns, combine them and create a date column.
12.	Examine the data types again and be sure that numeric variables are float, categorical ones are object,
 and date is in date format. If not, correct it.
13.	Examine the descriptive statistics of numerical variables. Search for any unusual behavior. 
Are the variables in the correct range? If not, find the locations and correct them.
14.	Search for possible outliers. If there are outliers, replace them with the mean.
15.	Search for uniformity. The units in the numeric columns are in the same format or not. 
That is, examine whether some data are in meters but some in centimeters. If they are not consistent, 
convert them into the same units.
16.	Search for the missing values. Examine their percentage in each column. 
If the percentage is low, fill them with mean/median/mode. 
If the percentage is high (e.g >60%-65%), you can drop the column. 

"""

# 0 -- To start with, I have read the file to a dataframe. I wanted to skip the title and the empty row in order to have a better view.
# print(df.head)
# I checked how it is looking
# and it seemed fine to me.

# 1 - EXAMINE THE VARIABLES AND THEIR DATA TYPES

# 2 - Examine the head and tail of the data frame. Make sure that you import your data correctly.
# Check for any separation argument problem (“;” or “,”) of the data,
# the existence of header in the dataset as well as the existence of NAs.
# print(df.head)
# It seems that there are 3 rows in the beginning and some NAs
df = pd.read_excel('data/Amazon.xlsx', header=None, skiprows=3)

# YOU MIGHT WANT TO CHANGE THE CODE HERE BECAUSE I DON'T THINK THAT IT DELETES THE ROWS IN THE ACTUAL FILE

# I leave the question 3 on the above to you

# 4 -- Then I wanted to begin the process with fixing the column names.
df.columns = ["Category", "Product ID", "Year", "Quarter", "Quarterly Sales", "Customer Rating", "Seller Rating",
              "Price",
              "Discount Rate", "Units Sold", "Revenue", "Shipping Method", "Location", "Advertising Cost"]

# 5 - The product ID column is unnecessary for data visualization, so I'm deleting it.
df = df.drop("Product ID", axis=1)

# 6 - Now I'm going to eliminate the duplicates since they are not in the nature of the data.
duplicates = df.duplicated()
df.drop_duplicates(inplace=True)
# And by this, dropped the duplicates.

# 7 - Now I will check if we have any unnecessary strings in the values.
print(df.dtypes)
# It seems that there are no unnecessary strings in numerical values

# 8 - Now to remove the white spaces before the strings
df["Shipping Method"] = df["Shipping Method"].str.lstrip()
# And it's done.

# 9 - To format the string values we will check the names for nominal values
# You could write a code that creates a list of names in every categorical column
# (and years and quarters)(and customer/seller rating),
# like the list could be equal to something like [[Beauty, BEAUTY, Book, Books,...],[EU,US,European Union..] etc.]
# then you can use the codes below to change che names accordingly.
# You can use "value.counts()" function from pandas btw
"""
#I write the needed code to format the names in the category column and fix the inconsistency.
df["Category"] = df["Category"].str.title()
df["Shipping Method"].replace({"Book": "Books", "Home - Kitchen": "Home & Kitchen"}, inplace=True)
--------------------------------------------------------------------
The below is for fixing years column 

df["YEAR"] = df["YEAR"].astype(str)
df["YEAR"] = df["YEAR"].str[:4]
df["YEAR"] = pd.to_numeric(df["YEAR"], errors='coerce')

The below is for fixing customer ratings

df["CustomerRating"] = abs(df["Customer Rating"])
---------------------------------------------------------------
The below is for fixing the format in location column

wrong_notation_list = []
for row in df["Location"]:
    if row not in ["EU", "US", "ASIA"]:
        if row not in wrong_notation_list:
            wrong_notation_list.append(row)
# print(wrong_notation_list) I checked the list of wrong notations.
df["Shipping Method"].replace({"European Union": "EU", "United States": "US", "Asia": "ASIA"}, inplace=True)
------------------------------------------------------------------
"""

# 10 - We don't have to check if levels of categories are unique since we don't need it to be unique for this data set.

# 11 - We don't need to create a date column since we only have the quarter and year

# 12 - It says that we should make the date values's types as "date" but I don't know how to do it.

# Im leaving 13, 14 and 15 to you. For 15 you only need to consider the discount rate since it has "%" sign on some of
# the values. You can handle it with the code below

# 13.	Examine the descriptive statistics of numerical variables. Search for any unusual behavior.
# Are the variables in the correct range? If not, find the locations and correct them.
# first of all let's find NA values in all columns

for col in df.columns:
    na_amount = df[col].isna().sum()
    if na_amount != 0:
        print(f'{col} has {na_amount} NA values')

# the quarterly sales is revenue / unit_sold
df['Quarterly Sales'] = df['Quarterly Sales'].fillna(df["Revenue"] / df["Units Sold"])

# In the Seller rating it is impossible to estimate a rating to the product and we have only one na we wouldn't
# lose so much if we remove one string
df = df.dropna(subset=['Seller Rating'])

# In the Advertisment cost it is impossible to estimate a advertismant cost to the product and we have only two NA
# we wouldn't lose so much if we remove two string and also all our data is integer we should change the datatype
# to integer

df = df.dropna(subset=['Advertising Cost'])
df["Advertising Cost"] = df["Advertising Cost"].astype(int)

# range of rating is unlikely to be negative since almost all data is ranging
# from 0 to 5. we should change the negative values to positive one
# also convert all data to integer since all data is integer numbers
df["Customer Rating"] = df["Customer Rating"].abs().astype(int)

# some data in year is typed in a wring for example instead of 2019 there is written 20199
df['Year'] = df['Year'].astype(str)
df['Year'] = df['Year'].str[:4]
df['Year'] = df['Year'].astype(int)

# the discount rate has a different values one values with "%" other not let's convert all values to one datatype
df['Discount Rate'] = pd.to_numeric(df['Discount Rate'], errors='coerce')
df['Discount Rate'] = df["Discount Rate"].astype(int)

# 14 outliers
# first, we need to write a code which will check whether in column exist outliers or not
# Function to identify outliers using IQR
def identify_outliers(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = column[(column <= lower_bound) | (column >= upper_bound)]
    return outliers

# Identify outliers in each column
outliers_dict = {}
for column in df.select_dtypes(include=['number']).columns:
    outliers_dict[column] = identify_outliers(df[column])


print()
# Displaying outliers
for column, outliers in outliers_dict.items():
    if not outliers.empty:
        print(f"Outliers in {column}: {outliers.values}")
    else:
        print(f"No outliers in {column}")

def replace_outliers_with_mean(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Identify and replace outliers
    outliers = column[(column <= lower_bound) | (column >= upper_bound)]
    df.loc[outliers.index, column.name] = column.mean()

    return column


# Replace outliers in each numeric column
for column in df.select_dtypes(include=['number']).columns:
    df[column] = replace_outliers_with_mean(df[column])

"""
for index, value in enumerate(df["Discount Rate"]):
    #if type(value) != int:
        #print(value)by this, I saw the problem is that since some of the values were written with "%" symbol, 
        some of the rates were interpreted as small floats
    continue

mask = df["Discount Rate"] < 1
df.loc[mask, "Discount Rate"] = df.loc[mask, "Discount Rate"] * 100
df["Discount Rate"] = df["Discount Rate"].astype(str).str.replace('%', '')
df["Discount Rate"] = pd.to_numeric(df["Discount Rate"], errors='coerce')
df["Discount Rate"] = df["Discount Rate"].astype(int)
-------------------------------------------------------------------------
"""

# 16 - At last I checked the rows with missing values.
'''for column in df:
    null_count = df[column].isnull().sum()
    percentage_null = (null_count / len(df)) * 100
    print(f"{column} has {percentage_null:.2f}% null values")
'''
# By this I checked the null percentages, and it checks all the values are 98%,
# so I wanted to continue with deleting empty rows. (I haven't used dropna since the rows were written as "NA", not NaN
# problematic_values = df[df['Quarterly Sales'].str.strip() == 'NA']
# df = df[df['Quarterly Sales'].str.strip() != 'NA']
# df['Quarterly Sales'] = pd.to_numeric(df['Quarterly Sales'])

"""

#And with this step, the data cleaning part is done.



"""
# 3 -- Then I wanted to continue with changing the product id code for books. I thought that changing it to BK would fix the confusion
# modified_id = []
# category = df["Category"]
# id = df["Product ID"]
#
# for i, cat_value in enumerate(category):
#     if cat_value == "Books":
#         id[i] = 'BK' + id[i][1:]
# df["Product ID"] = id
# print(df["Product ID"][27:])
