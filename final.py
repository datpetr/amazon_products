import pandas as pd

#You might want to change the first pf.read to read a csv file instead of excel. Also the code I wrote does not
#change the original file.


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


#0 -- To start with, I have read the file to a dataframe. I wanted to skip the title and the empty row in order to have a better view.
df = pd.read_excel('Amazon.xlsx')
#print(df.head)
#I checked how it is looking and it seemed fine to me.

#1 - EXAMINE THE VARIABLES AND THEIR DATA TYPES

#2 - Examine the head and tail of the data frame. Make sure that you import your data correctly.
# Check for any separation argument problem (“;” or “,”) of the data,
# the existence of header in the dataset as well as the existence of NAs.
#print(df.head)
#It seems that there are 3 rows in the beginning and some NAs
df = pd.read_excel('Amazon.xlsx', header = None, skiprows = 3)

#YOU MIGHT WANT TO CHANGE THE CODE HERE BECAUSE I DON'T THINK THAT IT DELETES THE ROWS IN THE ACTUAL FILE

#I leave the question 3 on the above to you

#4 -- Then I wanted to begin the process with fixing the column names.
df.columns = ["Category","Product ID","Year","Quarter","Quarterly Sale","Customer Rating","Seller Rating","Price",
                 "Discount Rate","Units Sold","Revenue","Shipping Method","Location","Advertising Cost"]

#5 - The product ID column is unnecessary for data visualization, so I'm deleting it.
df = df.drop("Product ID", axis=1)

#6 - Now I'm going to eliminate the duplicates since they are not in the nature of the data.
duplicates = df.duplicated()
df.drop_duplicates(inplace=True)
#And by this, dropped the duplicates.

#7 - Now I will check if we have any unnecessary strings in the values.
print(df.dtypes)
#It seems that there are no unnecessary strings in numerical values

#8 - Now to remove the white spaces before the strings
df["Shipping Method"] = df["Shipping Method"].str.lstrip()
#And it's done.

#9 - To format the string values we will check the names for nominal values
#You could write a code that creates a list of names in every categorical column (and years and quarters)(and customer/seller rating),
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

#10 - We don't have to check if levels of categories are unique since we don't need it to be unique for this data set.

#11 - We don't need to create a date column since we only have the quarter and year

#12 - It says that we should make the date values's types as "date" but I don't know how to do it.

#Im leaving 13, 14 and 15 to you. For 15 you only need to consider the discount rate since it has "%" sign on some of
#the values. You can handle it with the code below

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

#16 - At last I checked the rows with missing values.
'''for column in df:
    null_count = df[column].isnull().sum()
    percentage_null = (null_count / len(df)) * 100
    print(f"{column} has {percentage_null:.2f}% null values")
'''
#By this I checked the null percentages, and it checks all the values are 98%,
# so I wanted to continue with deleting empty rows. (I haven't used dropna since the rows were written as "NA", not NaN
problematic_values = df[df['Quarterly Sale'].str.strip() == 'NA']
df = df[df['Quarterly Sales'].str.strip() != 'NA']
df['Quarterly Sales'] = pd.to_numeric(df['Quarterly Sales'])

"""

#And with this step, the data cleaning part is done.



"""
WE WILL USE THE PART 3 ONLY IF WE CHOOSE TO NOT DROP THE PRODUCT ID COLUMN
#3 -- Then I wanted to continue with changing the product id code for books. I thought that changing it to BK would fix the confusion
modified_id = []
category = df["Category"]
id = df["Product ID"]

for i, cat_value in enumerate(category):
    if cat_value == "Books":
        id[i] = 'BK' + id[i][1:]
df["Product ID"] = id
#print(df["Product ID"][27:])
"""
