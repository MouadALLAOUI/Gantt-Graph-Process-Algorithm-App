import matplotlib.pyplot as plt


class GanttGraph:

    def __init__(
        self,
        size=(10, 2),
        ypos=1,
        colors=None,
        xlabel="Time",
        title="FIFO",
    ):
        self.size = size
        self.ypos = ypos
        self.colors = colors or [
            "skyblue",
            "lightgreen",
            "salmon",
            "gold",
            "plum",
        ]
        self.xlabel = xlabel
        self.title = title

    def setTitle(self, title):
        self.title = title

    def drawGraph(self, data):
        if not data:
            print("No data provided for the Gantt chart.")
            return
        fig, ax = plt.subplots(figsize=self.size)
        color = self.colors
        for i, process in enumerate(data):
            ax.barh(
                self.ypos,
                process["CPUs"],
                left=process["startTime"],
                color=color[i % 5],
            )
            ax.text(
                process["startTime"] + process["CPUs"] / 2,
                self.ypos,
                f"{process["name"]}\n{process["CPUs"]}",
                ha="center",
                va="center",
                color="black",
                fontsize=10,
            )
            ax.text(
                process["startTime"],  # Start of the bar
                self.ypos - 0.2,  # Slightly below the bar
                f"{process['startTime']}",  # Start time as text
                ha="center",  # Horizontal alignment
                va="center",  # Vertical alignment
                color="black",  # Text color
                fontsize=8,  # Font size
            )

        ax.set_xlabel(self.xlabel)
        ax.set_yticks([])
        ax.set_title(f"{self.title} Gantt Chart")
        ax.grid(True, axis="x", linestyle="--", alpha=0.5)
        plt.show()
