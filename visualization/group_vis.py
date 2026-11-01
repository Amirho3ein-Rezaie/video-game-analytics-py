from tools.func_analysis import group_analysis
from tools.classes import DatasetFields
from numpy import array
from matplotlib import pyplot as plot


def group_analysis_vis(group_field: DatasetFields.GroupByFields, sales_field) -> None:
    "Visual the dataframe that includes the data of group fields"

    # variables
    dataframe = group_analysis(group_field, sales_field, False)
    columns = ["total_sales", "avg_sales", "count"]
    colors = ["royalblue", "orange", "seagreen"]

    # make the plot
    plot.figure(figsize=(12, 10))
    for i, column in enumerate(columns, start=1):
        plot.subplot(3, 1, i)

        x = array(dataframe[group_field])
        y = array(dataframe[column])

        plot.plot(x, y, marker="o", color=colors[i - 1])

        # make the appearance
        plot.ylabel(column)
        plot.grid(axis="y", alpha=0.3)
        plot.xticks(rotation=45)

    # show the plot
    plot.suptitle(f"Sales statistics by {group_field} in {sales_field}")
    plot.tight_layout()
    plot.show()

    # the result
    print("The plot was displayed successfully ... !")


def genre_analysis_vis(sales_field) -> None:
    "Visual the dataframe that includes the data of genre"

    # use the function that show the plot
    group_analysis_vis(DatasetFields.GroupByFields.Genre.value, sales_field)
