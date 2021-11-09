import pandas as pd


# input function to process inputs given by the user
def inputnmail(roll, mailch):
    if roll is not None:
        try:
            roll = int(roll)

            # opening record.csv file
            df = pd.read_csv('records.csv')

            # reading the csv file and assigning values of that roll no in csv to the current python variables
            studentname = df.iloc[roll - 1, 0]
            lecs = df.iloc[roll - 1, 8]
            emailid = df.iloc[roll - 1, 7]
            dob = df.iloc[roll - 1, 6]
            age = df.iloc[roll - 1, 5]
            gender = df.iloc[roll - 1, 1]
            country = df.iloc[roll - 1, 3]
            city = df.iloc[roll - 1, 2]

            residence = city + ", " + country

            # converting integer type variables to string type in order to make a pie chart
            roll = str(roll)
            age = str(age)
            lecs = str(lecs)

            # if input is 'y' or 'Y', then the user wants the email to be sent
            if mailch == 'y' or mailch == 'Y':

                # making a report pdf by taking some data from above
                from genreport import genpdf
                genpdf(studentname, roll, dob, age, gender, residence, lecs)

                # sends the pdf file to the specified email id of the candidate
                from mailto import sendmail
                sendmail(emailid, studentname)

        # exception
        except Exception as val:
            print(val)
            print('This type of value is not found in the data')
