# matplotlib to make a pie chart
from matplotlib import pyplot as plt


# function to make a pie chart
def makechart(lecs, stuname):

    # defining labels
    attendance = ['Attended', 'Not attended']

    # converted into integer type because plt.pie accepts integer as first parameter
    lecs = int(lecs)
    data = [lecs, 60-lecs]

    # Creating plot
    plt.pie(data, labels=attendance)

    # export the pie chart in png format
    plt.savefig(f"piecharts/chart - {stuname}.png")
