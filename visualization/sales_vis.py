from matplotlib import pyplot as plt
from analysis import sales


def top_selling_vis(file: bool = False) -> None:
    "Visualizatio the top selling Global"

    dataframe = sales.top_salling(False)

    top = dataframe.head(10)

    plt.figure(figsize=(10, 6))
    bars = plt.barh(top["Name"], top["Global_Sales"])
    plt.bar_label(bars, fmt="{:.2f}", padding=3)

    plt.title("Top 10 best-selling games")
    plt.xlabel("Global sales (millions)")
    plt.ylabel("Game")

    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
