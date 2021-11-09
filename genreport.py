from fpdf import FPDF


def genpdf(stuname, rollno, dob, age, gender, residence, lecs):

    from genchart import makechart
    makechart(lecs, stuname)

    lecs = int(lecs)
    msg2 = ""
    if lecs < 60/3:
        leclost = 60/3 - lecs
        leclost = int(leclost)
        leclost = str(leclost)
        msg = "Student is in defaulter's list."
        msg2 = "Student needed to attend " + leclost + " more lectures to be out of defaulter's list."

    else:
        msg = "Student is not in defaulter's list."

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

    pdf.image(f"piecharts/chart - {stuname}.png", 0, 130)

    pdf.output(f"reportfolder/Attendance Report - {stuname}.pdf")
