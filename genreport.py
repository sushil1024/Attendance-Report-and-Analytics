
# fpdf is a module which generates pdf
from fpdf import FPDF


# function which take some values as parameters from 'searchdata.py' to make a pdf file
def genpdf(stuname, rollno, dob, age, gender, residence, lecs):

    # make pie chart
    from genchart import makechart
    makechart(lecs, stuname)

    # after making pie chart the 'lecs' variable is converted back to integer type
    lecs = int(lecs)
    msg2 = ""

    # if lecs (lectures attended) is less than one third of the total lectures, then student is a defaulter
    if lecs < 60/3:
        # lectures missed by the defaulter student
        leclost = 60/3 - lecs

        # converted into integer type to eliminate the fractional part
        leclost = int(leclost)

        # converted into string type to make a pdf
        leclost = str(leclost)
        msg = "Student is in defaulter's list."
        msg2 = "Student needed to attend " + leclost + " more lectures to be out of defaulter's list."

    # Student is not a defaulter
    else:
        msg = "Student is not in defaulter's list."

    # conversion to string type to be printed into the pdf
    rollno = str(rollno)
    lecs = str(lecs)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", 'BU', size=25)
    pdf.set_text_color(255, 0, 0)
    # (width, height, string)
    pdf.cell(200, 10, "ATTENDANCE REPORT", align='C')
    pdf.ln()
    pdf.set_font("Helvetica", size=20)
    pdf.set_text_color(0, 0, 0)
    pdf.ln()
    pdf.cell(40, 10, "Name: " + stuname)
    pdf.ln()
    pdf.cell(40, 10, "Roll No: " + rollno)
    pdf.ln()
    pdf.cell(40, 10, "Date of Birth: " + dob)
    pdf.ln()
    pdf.cell(40, 10, "Age: " + age)
    pdf.ln()
    pdf.cell(40, 10, "Gender: " + gender)
    pdf.ln()
    pdf.cell(40, 10, "Residence: " + residence)
    pdf.ln()
    pdf.cell(40, 10, "Lectures Attended: " + lecs + " out of 60")
    pdf.ln()
    pdf.set_font("Courier", size=12)
    pdf.set_text_color(255, 0, 0)
    pdf.cell(40, 10, msg)
    pdf.ln()
    pdf.cell(40, 10, msg2)

    # pie chart is inserted into the pdf
    pdf.image(f"piecharts/chart - {stuname}.png", 0, 130)

    # pdf is exported to 'reportfolder' folder
    pdf.output(f"reportfolder/Attendance Report - {stuname}.pdf")
