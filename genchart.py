from matplotlib import pyplot as plt


def makechart(lecs, stuname):
    # Creating dataset
    attendance = ['Attended', 'Not attended']

    lecs = int(lecs)
    data = [lecs, 60-lecs]

    # Creating plot
    plt.pie(data, labels=attendance)

    plt.savefig(f"piecharts/chart - {stuname}.png")

