import pandas as pd

roll = None
studentName = None

# opening file
file = pd.read_csv('records2.csv')
try:
    # accepting roll number
    roll = int(input("Enter roll no to search: "))
    if roll is not None:
        try:
            with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
                print(file.loc[[roll - 1]])  # add function to process

        except Exception as val:
            print(val)
            print("This type of value is not found in the data")

except:
    pass

try:

    # accepting student name
    studentName = str(input("Enter name to search: "))
    studentName = studentName.title()

except:
    pass


if studentName is not None:
    try:
        contain_values = file[file['Name'].str.contains(studentName)]
        with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
            print(contain_values)  # add function to process

    except Exception as val:
        print(val)
        print("This type of value is not found in the data")

