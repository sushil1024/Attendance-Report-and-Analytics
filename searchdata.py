import pandas as pd
import cgi
from IPython.display import HTML


form = cgi.FieldStorage()

# opening file
file = pd.read_csv('records.csv')
temp = None

def inputroll(roll):
    # accepting roll number
    # roll = int(input("Enter roll no to search: "))
    if roll is not None:
        try:
            with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
                temp = file.loc[[roll - 1]]  # temp variable stores value of the dataframe
                # print(file.loc[[roll - 1]])  # add function to process
                result = temp.to_html()

                with open("templates/result.html", "w") as f:
                    f.write(result)

            df = pd.read_csv('records.csv')

            studentName = df.iloc[roll - 1, 0]
            lecs = df.iloc[roll - 1, 8]
            emailid = df.iloc[roll - 1, 7]
            dob = df.iloc[roll - 1, 6]
            age = df.iloc[roll - 1, 5]
            gender = df.iloc[roll - 1, 1]

            country = df.iloc[roll - 1, 3]
            city = df.iloc[roll - 1, 2]

            residence = city + ", " + country

            if lecs < 60 / 3:
                print("Student is a defaulter")
                print("Student have missed", 60 / 3 - lecs, "lectures to be out of defaulter's list")

            else:
                print("Student is not a defaulter")
            roll = str(roll)
            age = str(age)
            lecs = str(lecs)

            mailch = input(str("Do you want the report sent on the given email id?(y/n): "))
            if mailch == 'y' or mailch == 'Y':
                from genreport import genpdf

                genpdf(studentName, roll, dob, age, gender, residence, lecs)

                from mailto import sendmail

                out1 = sendmail(emailid, studentName)
                print(f"Report sent to " + "'" + emailid + "'")

            else:
                print("Report not sent!")

        except Exception as val:
            print(val)
            print("This type of value is not found in the data")
