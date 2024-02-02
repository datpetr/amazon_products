## **Introduction to Data Processing and Visualization, Final Project**

### **Abstract**
 ![](RackMultipart20240202-1-4kap9l_html_832ac086151b03a6.png)

This project is based on a research of Amazon' sales

information. The dataset contained multiple continuous and categorical

variables that needed to be cleaned and organized in order to be used in the visualizations. We prepared 10 questions about 6 graphs of the sales in order to explore possible correlations and trends of various variables. Below, we will provide details of data, data cleaning, data exploration, and descriptive statistics. Afterward, we will use all of those to present visualizations and Exploratory Data Analysis to answer the questions about the data.

### **Introduction**

In our research, we've analyzed a dataset containing 120 different rows of data. Below, you can see the types of data for each of the variables. Furthermore, we will explain the data cleaning, analyzation, and visualization process. Following it, we have all the questions and answers, and finally, we have the general conclusion.

| **Variable Name** | **Description** | **Scale** |
| --- | --- | --- |
| Category | Represents the product category | Qualitative, Nominal |
| Product\_id | A unique identifier for each product | Qualitative, Nominal |
| Year | Year of the sale | Quantitative, Interval |
| Quarter | Quarter of the year | Qualitative, Ordinal |
| Quarterly sales | Quarterly sales' revenue in USD | Quantitative, Ratio, Continuous |
| Customer Rating | Customer satisfaction rating | Quantitative, Ordinal |
| Seller Rating | Seller satisfaction rating | Quantitative, Ordinal |
| Price | Product price in USD | Quantitative, Ratio, Continuous |
| Discount | Discount applied to the product (percentage) | Quantitative, Ratio, Continuous |
| Units Sold | Number of units sold | Quantitative, Ratio, Discrete |
| Revenue | Total revenue generated from the product | Quantitative, Ratio, Continuous |
| Shipping Method | Shipping method used | Qualitative, Nominal |
| Location | Location of the sale | Qualitative, Nominal |
| Advertising Cost | The cost of advertisement for each product | Quantitative, Ratio, Continuous |

### **Data Tidying and Cleaning Steps**

We used Python, with the Pandas library, for data cleaning. Data cleaning involves many steps, such as сhecking for missing values, dropping duplicates and unnecessary columns, etc. In fact, data cleaning is one of the most important parts when it comes to making conclusions from a dataset, since the answers may vary a lot based on whether the data is clean or not. In order to get reliable answers from the graphs and descriptive statistics, we need to make sure that our data is tidy and ready for future processes.

First, let's explore the head of the variables table to get the general info about the dataset. To start working on the dataset, we loaded the file into the data frame. Also, we skipped the title and the empty row for a better view. We established the columns' names and set them as headers. After all revisions, the data seems to be better structured.

The NA values may be a problem for data analysis, so by exploring the dataset, they were found in **"Seller Rating"** , **"Advertising Cost"** , and **"Quarterly Sales"**. First, let's remove white spaces and extra symbols at the end of the strings. Also, NA occurrences of a **"string"** type were replaced with pandas data type NA. After a second check, the NA values were found in the " **Quarterly Sales**", " **Seller Rating**", and " **Advertising Cost**" columns. Since the number of NA values in three columns was low (\<2%), we can simply replace them with the median or mean value of the column. For **"Seller Rating",** we used the median, and for **"Advertising Cost"** and **"Quarterly Sales",** we used the means of specified categories. Afterwards we rounded them up to the closest integer for easier view of the data.

The next step was checking for multiple data types in a column. They were found in the " **Quarterly Sales**" column, so " **Quarterly Sales**" was set to **"float64"**. Also, the values were sorted. Specific characters were deleted by observing for typos or unnecessary symbols in columns, and the **"Quarter"** column was unified to the **"Q#"** look. Categorical columns only consisted of letters, so no changes were made to them. The data became tidier when we dropped duplicates using pandas; we created a new column for the date of the **"** _ **year-number\_of\_quarter** _ **"** type. Also, the check for variables that were stored in both rows and columns revealed that there were no mistakes like that. Additionally, some cosmetic changes were made: standardizing the writing formatting for the data in the category columns and formatting the titles

Now, let's verify negative values in the numerical columns (they can't exist due to the range of 1 to 5). They were found in the **"Customer rating"** column. So, we changed all negatives to positives. It's time for an outliers check. We are going to check the outliers based on the categories since the values vary a lot between different ones. They were found in **"Electronics"** and **"Books"** in the **"Category"** column and replaced with corresponding mean values. For the last step, we examine the variables and their data types before saving the changes into a new file. It was found that many numerical columns have an **"integer"** type instead of **"float"** ; We fixed all of them except for the " **Year**" column. Finally, the updated data were saved into both CSV and Excel files (filtered\_amazon).

### **Exploratory Data Analysis**

We've created the plots below using Seaborn, Matplotlib, and Pandas. The colors used in the graphs were specially chosen to be associated with Amazon as a company. We used the classical Amazon orange, dark gray, blue, green, and light gray tones often used in advertisements and designs by Amazon's designers. The questions aim to find trends and correlations among the variables, such as the Advertising Cost and Revenue, to improve future investments and gain insights into the purchase habits of their customers.

**Descriptive Statistics for Numerical Variables**

Before we begin answering the questions with the help of visualizations, it would be helpful to get familiar with the numerical data and its descriptive measures. Below, we see the summarized data. Values were rounded to the second decimal.

With COV (coefficient of variation), we can see how spread the data is. The variable with the highest COV is **"Units sold"** , with 74.42, and the variable with the lowest COV is **"Customer Rating"** , with 12.31. We have 2 columns that we can say are somewhat symmetrically distributed: **"Seller Rating"** and **"discount rate".****"Quarterly Sales" **,**"Customer Rating, price" **,**"Units Sold" **,**"Revenue" **, and**"Advertising Cost"** are skewed to the right. None of the variables are skewed to the left. When we look at the min/max values, we can clearly see that the highest discount rate that Amazon applies is 20%. There are no ratings lower than 3 for either the customer or seller ratings. And the max. revenue is 63000$, more than 1.5 standard deviations away from the mean. However, we didn't count this as an outlier, since the revenue of a product depends on many things and can vary a lot, which might cause very spread values. Thus, the value of 63000 was important for us to include in our analysis. So, in the data analysis part, we checked for the extreme outliers instead of the usual ones. ![](RackMultipart20240202-1-4kap9l_html_ea75a7e6d5005ee5.jpg)

**Questions and Graphs**

**1. Are there any drastic sales increases or decreases in any categories throughout 2019-2021? Which category had the lowest number of sales in 2020?**![](RackMultipart20240202-1-4kap9l_html_3eded9bc03398bd7.png)

The graph is a stacked bar chart for the number of units sold for each of the five categories for years from 2019 to 2021. Each category has a separate bar and sections colored based on the year of the sale. For each colorful section, we can see the number of units sold that year, written on top for easier comparison. Overall, it seems like the leader in sales throughout 2019-2021 was the **"Clothing"** category.

From each bar, we can see the dynamic of sold goods of different categories. **"Electronics"** , for example, remains almost the same throughout 2019-2021. **"Home & Kitchen"** had an overall growth of 50% in 2 years, going from 140 units sold in 2019 to 210 units sold in 2021. **"Beauty"** has decreased in popularity during the pandemic period but then slightly increased in 2021 compared to pre-pandemic 2019. The opposite situation is with the **"Books"** category: It increased by almost %50 in 2020, but a year later, in 2021, it returned to the sale number of 2019. The different situation is with the **"Clothing"** category: it had a significant decrease in the pandemic year, then slightly recovered from it. So, as a result, we can say that all categories except **"Electronics"** had significant changes throughout 2019-2021.

As we can see in the graph, in 2020, the highest number of sales belonged to the **"Clothing"** category, with 710 units sold. The lowest number of sales came from **"Home & Kitchen"** ; it only had 145 sales in 2020.

**2. Did the 2020 COVID-19 pandemic change the advertising cost of items? Which categories had the highest overall advertising cost throughout 2019-2021?**

![](RackMultipart20240202-1-4kap9l_html_e2cb3c3fb70cac00.png)

The graph is a time series line chart. It shows progress in advertisement cost for each of the 5 categories, and we can easily distinguish each category because they are multicolored.

We can see from the graph that before the pandemic, the leading category in advertisement cost was **"Home & Kitchen,"** which had positive stagnation. **"Electronics"** (-10%), **"Beauty"** (-12%), and **"Clothing"** (-20%) had a decrease from 2019 to 2020. **"Books"** is the category with the lowest advertising cost in 2019 and is the fastest-growing, as it more than doubled in 2020. After the pandemic, the situation had some changes: **"Home & Kitchen"** had a ~40% growth in only one year, which is much higher when compared to the years prior. We see a slow decline in the **"Books"** category, -9 % in advertisement cost in 2021, which is surprising if we look at the rapid growth before 2020. The **"Beauty"** category started to grow gradually after the decline before the pandemic but couldn't reach the exact advertising cost it had before 2020. **"Electronics"** had a 19% decrease in 2021, unlike **"Clothing,"** which had an increment of 13% in 2021. As a result, the pandemic affected the advertisement cost of all categories differently.

For the second question, let's examine which categories had the highest advertising costs from 2019 to 2021. In 2019, the leading category was **"Home & Kitchen"** (~3.500$), with **"Electronics"** (~3.000$) and **"Beauty"** (~2.500$) following it. In 2021, the leading category is still **"Home & Kitchen"** (~6.000$). For the following 2 categories, we can see that in comparison to 2019, **"Beauty"** (~2.400$) surpassed **"Electronics"** (~2.100$) in 2021.

**3. Does the price of an item affect its number of sales? Which region had the highest mean for the price and the units sold?**

![](RackMultipart20240202-1-4kap9l_html_a075379e2f35f943.png)

In the scatter plot above, we can see the correlation between the number of units sold and the price of each item. As we can see above, the plots are separated by the country of sale, and due to this, we can use the information to compare the tendencies between the countries. We also see dashed parallel and vertical lines on each plot representing the mean of "Units Sold" and **"Price."**

We see the same tendency in all three regions: items with low prices are the most frequently bought, and as the item's price increases, the number of units sold declines, so **"Units Sold"** and **"Price"** have a negative correlation. From the plots, we can also observe that the relationship between the two variables is non-linear and seems to have a curve. This means that items that cost from 0$ to 50$ have a vast spread for the units sold, ranging from 30-200 for all three plots. Regarding items that are $50-$250, we can see that the number of units sold ranges only from ~20-65 per item. The lowest number of sales seems to be for the items priced ~120$-130$ for all three regions. so we can conclude that the price negatively affects the number of sales.

When we observe each graph separately, with the help of the dashed lines that represent the means, we see the difference between the regions. Regarding the Price, the highest mean belongs to Asia; the average price of items was $100, but the difference between the regions is very insignificant. The highest average number of units sold is seen for the EU, then the US and Asia; 75, 68 and 63 units respectively.

**4. Does the method of shipping used affect the customer rating?**

![](RackMultipart20240202-1-4kap9l_html_27d5bf62710afaf7.png)

The graph shows the distribution of the customer ratings (3-5) based on the shipping method used. We used the **"Units Sold"** to measure the number of reviews for each rating. This information can help the company understand the influence of these two topics and possible correlations. As we see in the plot, the most common customer rating is very different based on the shipping method used. We can't be sure this correlation has any direct causation, but it is still vital for future research.

The most common rating for the **"Standard"** delivery option is **'4'** , and the **"Express"** one's **'5'**. Also, we see that the overwhelming majority of reviews were of the values mentioned above. As a result, we can conclude that people rate the **"Express"** shipping method higher than the **"Standard"** one. It may be a sign to bring changes to the **"Standard"** shipping option to improve customer service.

**5. Does higher advertising cost mean higher revenue? What is the optimal advertising cost for the product to have the highest revenue?**![](RackMultipart20240202-1-4kap9l_html_5f99c612a06a9e10.png)

This plot is based on a scatter plot of **"Advertising Cost"** and **"Revenue"**. We also can see the line of best fit with a bright orange color. This graph could be associated with the upside-down Amazon logo, as it also has orange and gray tones.

From the graph, we can see that the correlation between advertising cost (x-axis) and revenue (y-axis) is curvilinear. Up to the advertising cost of 575$, we have a positive relationship, and every extra dollar spent results in increased revenue. However, since the relationship is non-linear and has the shape of an upside-down curve, spending extra money after reaching 575$ results in shrunk revenue, so, as a result, we can see that ~575$ is the optimal spending value for advertisement cost, which leads to the highest mean revenue.

Despite a seemingly strong positive relationship for the part up to ~575$, we shouldn't forget that correlation does not mean causation, and we may be dealing with confounding variables. For example, the same advertising cost may have different effects on goods of different price ranges and categories.

**6. If an item has a higher discount rate, which shipping method do people prefer?**

![](RackMultipart20240202-1-4kap9l_html_4c28ffbc4916e9a0.png)

In the graph, we can see the violin plot. Let's take a look at the orange graph on the left first. Inside, you can see a narrow black line that takes all the values from 5-20% . It represents all discount rates that goods take. The bold black line is divided by the short white line, and the thinner black lines on the sides represent the whiskers. The part that lies above the white line until the end of the black bold line represents 25% of the date, which had a ~13-20% discount rate. The lower part represents 25% of the data, lying below the median with an ~8-13% discount rate. The short white line is the median, meaning %50 of the data lies above it and the other %50 under it. On the outside, we see that the figure has a changing width. Width represents the number of observations having a specific value. So, a wider area means a higher number of sales for that value, and a narrow area means a lower number of sales. For example, there are equal numbers of goods having 9% and 16% discount rates for standard shipping. On the other hand, for express shipping, 13% and 18% discounts had the same purchase frequency. One of the interesting points of this graph is that the violin plot representing the standard shipping seems to be bimodal, with peak points at %9 and %16.

Let's now deconstruct the gray graph on the right. It has the same median value of a 12% discount rate, with the same range of 5-20% discount applied. However, the middle 50% of data lies between 8-13% discount rate for **"Express Shipping"** , and 50% of all data lies in 8-17% discount percentage for standard shipping. The most number of goods delivered by express shipping have a 10% discount applied.

We can conclude that people usually choose **"Standard"** shipping rather than **"Express"** shipping. We especially see the preference towards standard shipping when it comes to items with higher discount rates.

### **Conclusion:**

In conclusion, the dataset had many problems and discrepancies that were fixed with data cleaning. Additionally, we analyzed the numerical variables with descriptive statistics and then prepared questions based on the knowledge we gained.

We can see that during the pandemic year, there was a discretion in the sales of **"Clothing"** and **"Beauty"**. However, we can see the contrary that there was a nearly 50% increase in the sales of **"Books"**.

There's an insignificant difference between the mean **"Price"** and average number of **"Units Sold"** between the regions.

We can see that the high **"Advertising Cost"** doesn't always lead to a high number of sales, as we can see on the 1st and 2nd graphs, the categories with the highest **"Advertising Cost"** seemed to have the lowest number of sales and vice versa. Additionally, we discovered that high **"Advertising Cost"** doesn't always mean high **"Revenue"** and that the relationship between these 2 variables is _curvilinear_.

The most popular way of shipping seems to be the **"Standard Shipping,"** but it has the lowest **"Customer Rating"**. On the contrary, people seem to be satisfied by **"Express Shipping"** since it mostly has **'5'** as **"Customer Rating"**.

While offering actionable insights, further research is needed to understand the complex causal relationships in the dynamic e-commerce landscape.
