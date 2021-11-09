import pandas as pd
import time

# opening file
file = pd.read_csv('records.csv')


def inputnmail(roll, mailch):
    if roll is not None:
        try:
            roll = int(roll)
            with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
                temp = file.loc[[roll - 1]]  # temp variable stores value of the dataframe
                result = temp.to_html()

                with open("templates/result.html", "w") as f:
                    f.write(result)

            df = pd.read_csv('records.csv')

            studentname = df.iloc[roll - 1, 0]
            lecs = df.iloc[roll - 1, 8]
            emailid = df.iloc[roll - 1, 7]
            dob = df.iloc[roll - 1, 6]
            age = df.iloc[roll - 1, 5]
            gender = df.iloc[roll - 1, 1]
            country = df.iloc[roll - 1, 3]
            city = df.iloc[roll - 1, 2]

            residence = city + ", " + country

            roll = str(roll)
            age = str(age)
            lecs = str(lecs)
            if mailch == 'y' or mailch == 'Y':

                from genreport import genpdf
                genpdf(studentname, roll, dob, age, gender, residence, lecs)
                time.sleep(2)

                from mailto import sendmail
                sendmail(emailid, studentname)

        except Exception as val:
            print(val)
            return '<p>This type of value is not found in the data</p>'
