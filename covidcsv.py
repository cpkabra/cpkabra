import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter


def covidata():
    # If you want to fetch any date field then use parse_dates method in read_csv method for that column
    # dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
    # parse_dates=['Date Announced']
    df = pd.read_csv('http://api.covid19india.org/csv/latest/raw_data.csv')  # raw_data3.csv
    # IMPORTDATA("https://api.covid19india.org/csv/latest/raw_data3.csv")
    # df = pd.read_csv('C:\\Users\\chandraprakash_kabra\\Desktop\\PythonExe\\DataScience\\raw_data3 (3).csv')
    df["Date Announced"] = pd.to_datetime(df["Date Announced"], format="%d/%m/%Y")
    # df = pd.read_csv('raw_data3.csv')
    filter = df["Nationality"] == "India"

    # df["Date1"] = pd.to_datetime(df["DateC"], format="%d/%m/%Y")
    df = df.sort_values(by='Date Announced', ascending=True)

    # DataFrame.dropna(self, axis=0, how='any', thresh=None, subset=None, inplace=False)
    dfIndia = df[
        ['Patient Number', 'Date Announced', 'Detected District', 'Detected State', 'State code', 'Nationality',
         'Current Status', 'Notes', 'Source_1']].where(filter).dropna(thresh=2)

    fig, ax = plt.subplots(figsize=(20, 10))
    # use unstack()
    dfIndia.groupby([dfIndia['Date Announced'].dt.date, 'Current Status'])['Patient Number'].count().unstack().plot(
        ax=ax, rot=45, kind='line', marker='o', linestyle='-')  # this value is only for
    # dfIndia.groupby([dfIndia['Date Announced'].dt.date,'Current Status'])['Patient Number'].count().unstack().plot(ax=ax,rot=90,kind='bar',x_compat=True)#this value is only for kind =line,  marker='o', linestyle='-'

    date_form = DateFormatter("%d-%b")
    ax.xaxis.set_major_formatter(date_form)

    # Ensure a major tick for each week using (interval=1)
    # ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
    ax.xaxis.set_minor_locator(mdates.DayLocator())
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
    plt.show()
    fig.savefig('my_plot.png')
    html = """
    <img src='my_plot.png'>
    """

    # Write HTML String to file.html
    with open("index.html", "w") as file:
        file.write(html)

covidata()
