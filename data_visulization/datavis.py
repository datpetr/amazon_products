import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

# All of the visualisations are done with defining functions for each of them.
# We initially had 13 plots when we started coding the visualisations. As we progressed and eliminated them, only 2nd, 5th, 8th, 11th, 13th was left.
# We decided to keep the names as they were to make it clearer which plot we are referring to.

amazon = pd.read_excel("/content/data/filtered/filtered_amazon.xlsx")  # Loads our Amazon Data Set Excel File into a pandas DataFrame.

mpl.rc('font', family="Lucida Sans Unicode", size=12)  # Sets a standard font.

the_colors = ["#FF9900", "#2C3B4E", "#01A7E1", "#008900", "#707868"]  # Sets a standard color palette.
sns.set_palette(the_colors)

sns.set_context("notebook")  # Sets a standard sizing.


###
###
###

# final_plot02. The Regression Plot.
def plot02():
    sns.set(style="darkgrid")  # Sets the background to darkgrid.

    # Seaborn regression plot itself and the necessary small customizations.
    ax = sns.regplot(
        data=amazon,
        scatter=True,
        fit_reg=True,
        ci=None,
        x="Advertising Cost",
        y="Revenue",
        order=2,
        scatter_kws={"color": "#3B4F68", "alpha": 0.5, "s": 75},
        line_kws={"color": "#FF9900", "alpha": 0.9, "linewidth": 3.5},
        x_jitter=16,
        y_jitter=16  # We saw jitter necessary for the graph and the correlations to seem more fluid.
    )

    ax.set_xlabel("Advertising Cost ($)")
    ax.set_ylabel("Revenue ($)")
    ax.set_title("Correlation of Revenue and Advertising Cost for Each Product", y=1.01, fontsize=15,
                 fontweight="bold")  # Setting the labels and titles.

    sns.despine(left=False, bottom=False, right=True, top=True)  # Getting rid of unnecessary spines

    fig = plt.gcf()
    fig.set_size_inches(7, 4.5)  # Sets a size for the visualisation.
    plt.savefig("final_plot02.png", dpi=300)  # Sets a resolution for the visualisation and saves it as png.

    plt.show()  # Displays the plot.


# final_plot05. Scatter Plot.
def plot05():
    sns.set(style="darkgrid")  # Sets the background to darkgrid.

    # Seaborn relational plot itself and the necessary small customizations.
    ax = sns.relplot(
        data=amazon,
        kind="scatter",
        x="Price",
        y="Units Sold",
        alpha=0.8,
        hue="Location",
        col="Location",
        size=100,
        sizes=(100, 101),
        palette=the_colors[:3],
        legend=False  # The legend was seen unnecessary.
    )

    axs = ax.axes[0, 0]  # Necessary for the axes to be defined for the next steps.

    ylim = axs.get_ylim()
    axs.set_ylim(0, ylim[1])  # This is done in order to have the y-axis start from 0 instead of other values.

    # This code is in order to put the mean lines and the dot where they coincide in the plot.
    for axs, location in zip(ax.axes.flatten(), amazon["Location"].unique()):
        mean_price = amazon[amazon["Location"] == location]["Price"].mean()
        mean_units = amazon[amazon["Location"] == location]["Units Sold"].mean()  # Calculation of the means.

        axs.axvline(mean_price, color="black", linestyle="dashed", linewidth=2, alpha=0.2, label="Mean Price")
        axs.axhline(mean_units, color="black", linestyle="dashed", linewidth=2, alpha=0.2,
                    label="Mean Units Sold")  # To axtually plot the mean lines.

        axs.scatter(mean_price, mean_units, color="black", marker="o", s=30, label="Mean Marker",
                    alpha=0.8)  # To put a point where the lines coincide.

        axs.text(mean_price + 3.5, mean_units + 3.5, "Mean", ha="left", va="bottom", fontsize=13, color="black",
                 alpha=0.5, fontweight="bold")  # The text.

    plt.suptitle("Correlation of Price and Number of Units Sold by Location", y=1.0, fontsize=15, fontweight="bold")
    ax.set_xlabels("Price ($)")
    ax.set_titles("{col_name}")  # Setting the labels and titles.
    plt.subplots_adjust(top=0.87)  # (just for location)

    sns.despine(left=False, bottom=False, right=True, top=True)  # Getting rid of unnecessary spines

    fig = plt.gcf()
    fig.set_size_inches(11.76, 3.92)  # Sets a size for the visualisation.
    plt.savefig("final_plot05.png", dpi=300)  # Sets a resolution for the visualisation and saves it as png.

    plt.show()  # Displays the plot.


# final_plot08. Line Plot.
def plot08():
    sns.set(style="darkgrid")  # Sets the background to darkgrid.

    amazon_year = amazon.groupby(['Year', "Category"])['Advertising Cost'].sum().reset_index()
    amazon_p08 = amazon_year[amazon_year['Year'].isin(
        [2019, 2020, 2021])]  # This is to exclude the years that didn't have enough data to draw inferences form.

    # Seaborn line plot itself and the necessary small customizations.
    ax = sns.lineplot(
        data=amazon_p08,
        y="Advertising Cost",
        x="Year",
        hue="Category",
        palette=the_colors,
        hue_order=["Home & Kitchen", "Electronics", "Beauty", "Clothing", "Books"],
        errorbar=None,
        linewidth=3.5
    )

    ylim = ax.get_ylim()
    ax.set_ylim(0, ylim[1])  # This is done in order to have the y-axis start from 0 instead of other values.

    sns.set_theme()
    legend = plt.legend(title="Categories")
    title = legend.get_title()
    title.set_position((12, 0))
    title.set_fontweight("bold")
    legend.get_frame().set_facecolor("white")  # Plotting the legend to have a different background especially.

    # Normally since years are defined as numerical values, so it was showing in the graph decimal points. This snippet of code is to prevent that.
    plt.xticks(ticks=amazon_p08['Year'].unique(), labels=[str(year) for year in amazon_p08['Year'].unique()])

    ax.set_ylabel("Advertising Cost ($)")
    ax.set_title("Advertising Costs of Categories (2019-2021)", fontsize=15,
                 fontweight="bold")  # Setting the labels and titles.

    sns.despine(left=False, bottom=False, right=True, top=True)  # Getting rid of unnecessary spines

    fig = plt.gcf()
    fig.set_size_inches(7, 4.5)  # Sets a size for the visualisation.
    plt.savefig("final_plot08.png", dpi=300)  # Sets a resolution for the visualisation and saves it as png.

    plt.show()  # Displays the plot.


# final_plot09. Bar Chart.
def plot09():
    sns.set(style="darkgrid")  # Sets the background to darkgrid.

    # Seaborn bar plot itself and the necessary small custiomizations.
    ax = sns.countplot(
        data=amazon,
        x="Shipping Method",
        hue="Customer Rating",
        palette=the_colors[:3],
    )

    ax.set_xlabel("")
    ax.set_ylabel("Count of Products")
    ax.set_title("           Mean Customer Review of Products by the Shipping Method", fontsize=15,
                 fontweight="bold")  # Setting the labels and titles.

    sns.set_theme()
    legend = plt.legend(title="Customer Rating", loc='upper left', bbox_to_anchor=(1, 1))
    title = legend.get_title()
    title.set_position((0, 0))
    title.set_fontweight("bold")
    legend.get_frame().set_facecolor("white")  # Plotting the legend.

    sns.despine(left=False, bottom=False, right=True, top=True)  # Getting rid of unnecessary spines.

    plt.tight_layout()
    fig = plt.gcf()
    fig.set_size_inches(7, 3.75)  # Sets a size for the visualisation.
    plt.savefig("final_plot09.png", dpi=300)  # Sets a resolution for the visualisation and saves it as png.

    plt.show()  # Displays the plot.


# final_plot11. Violin Plot.
def plot11():
    sns.set(style="darkgrid")  # Sets the background to darkgrid.

    # Seaborn bar plot itself and the necessary small customizations.
    ax = sns.violinplot(
        data=amazon,
        y="Discount Rate",
        x="Shipping Method",
        hue="Shipping Method",
        palette=the_colors[:2],
        width=0.5,
        alpha=0.8,
    )

    ylim = ax.get_ylim()
    ax.set_ylim(0, ylim[1])  # This is done in order to have the y-axis start from 0 instead of other values.

    ax.set_xlabel("")
    ax.set_ylabel("Discount Rate (%)")
    ax.set_title("Discount Rates of Items by Shipping Method Used", fontsize=15,
                 fontweight="bold")  # Setting labels and titles.

    sns.despine(left=False, bottom=False, right=True, top=True)  # Getting rid of unnecessary spines.

    plt.tight_layout()
    fig = plt.gcf()
    fig.set_size_inches(6.5, 3.75)  # Sets a size for the visualisation.
    plt.savefig("final_plot11.png", dpi=300)  # Sets a resolution for the visualisation and saves it as png.

    plt.show()  # Displays the plot.


# final_plot13. Stacked Bar Chart
def plot13():
    # Unfortunately we noticed that it was not possible to plot a stacked bar chart using seaborn only. Thus we decided to use our prior matplotlib knowledge
    # and do some extra search in order to achieve this visualisation.

    sns.set(style="darkgrid")  # Sets the background to darkgrid.

    amazonmod = amazon[amazon['Year'].isin([2019, 2020, 2021])]
    amazonmod = amazonmod.groupby(['Category', 'Year'])['Units Sold'].sum().unstack().reset_index()
    # This is to exclude the years that didn't have enough data to draw inferences form.

    fig, ax = plt.subplots()

    bottom_position = None
    for i, year in enumerate(amazonmod.columns[1:]):
        if bottom_position is None:
            bottom_position = 0
        ax.bar(amazonmod['Category'], amazonmod[year], label=str(year), alpha=0.8, color=the_colors[i],
               bottom=bottom_position, linewidth=0)
        bottom_position += amazonmod[year]  # This is in order to make the bars stacked

    vals = []
    for y in amazonmod.index:
        for c in amazonmod.columns:
            vals.append(amazonmod.loc[y, c])

    vals = [val for val in vals if type(val) != str]
    pozs = [[0, 120], [0, 340], [0, 570], [1, 220], [1, 780], [1, 1360], [2, 750], [2, 1720], [2, 2500], [3, 80],
            [3, 250], [3, 420], [4, 60], [4, 200], [4, 370]]

    for i, val in enumerate(vals):
        ax.text(pozs[i][0], pozs[i][1], s=str(val), ha="center", va="center", fontsize=10, color="white", alpha=0.95,
                fontweight="bold")
    # These are to add the text on the bars that are the values.

    ax.set_xlabel('')
    ax.set_ylabel('Units Sold')
    ax.set_title("Units Sold Each Year by Category", fontsize=15, fontweight="bold")  # Sets the lables and titles.

    sns.set_theme()
    legend = plt.legend(title="Years", loc='upper right', bbox_to_anchor=(1, 1))
    title = legend.get_title()
    title.set_position((0, 0))
    title.set_fontweight("bold")
    legend.get_frame().set_facecolor("white")  # Plotting the legend.

    sns.despine(left=False, bottom=False, right=True, top=True)  # Getting rid of unnecessary spines.

    fig = plt.gcf()
    fig.set_size_inches(10, 5)  # Sets a size for the visualisation.
    plt.savefig("final_plot13.png", dpi=300)  # Sets a resolution for the visualisation and saves it as png.

    plt.show()  # Displays the plot.


###
###
###


# This is for the descriptive statistics of numerical columns.
result_list = []
for column in amazon.columns:
    # Check if the column data is numerical.
    if pd.api.types.is_numeric_dtype(amazon[column]):
        # Calculation of the necessary statistics.
        mean_val = amazon[column].mean()
        median_val = amazon[column].median()
        std_val = amazon[column].std()
        min_val = amazon[column].min()
        max_val = amazon[column].max()
        cov_val = std_val / mean_val * 100 if mean_val != 0 else 0  # (Coefficient of Variation)

        # Appends the results to the result list.
        result_list.append([
            column,
            mean_val,
            median_val,
            std_val,
            min_val,
            max_val,
            cov_val
        ])
result_df = pd.DataFrame(result_list, columns=['Column', 'Mean', 'Median', 'Std', 'Min', 'Max', 'CoV'])
# Saves the result to an Excel file.
result_df.to_excel('descriptive_statistics_results.xlsx', index=False)

plot02()
plot05()
plot08()
plot09()
plot11()
plot13()

# Displaying everything back to back