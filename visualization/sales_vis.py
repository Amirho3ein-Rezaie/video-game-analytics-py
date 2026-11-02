from matplotlib import pyplot as plot
from analysis import sales
from numpy import array


def top_selling_vis() -> None:
    "Visualizatio the top selling Global"

    dataframe = sales.top_salling(False)

    top = dataframe.head(10)

    plot.figure(figsize=(10, 6))
    bars = plot.barh(top["Name"], top["Global_Sales"])
    plot.bar_label(bars, fmt="{:.2f}", padding=3)

    plot.title("Top 10 best-selling games")
    plot.xlabel("Global sales (millions)")
    plot.ylabel("Game")

    plot.gca().invert_yaxis()
    plot.tight_layout()
    plot.show()

    print("The plot was displayed successfully ... !")


def regional_sales_comparison_vis() -> None:
    "Visualize total sales across different regions."

    dataframe = sales.regional_sales_comparison(False)

    # basic plot
    x = array(dataframe["Field name"])
    y = array(dataframe["Total selling (copy)"])
    plot.bar(x, y, 0.5)

    # make better the appearance
    plot.title("Regional Sales Comparison", fontsize=16)
    plot.xlabel("Regions")
    plot.ylabel("Total Sales (Units)")

    plot.grid(axis="y")

    plot.show()  # show the plot

    print("The plot was displayed successfully ... !")
