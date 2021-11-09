# To send email (pdf report), yagmail (Yet Another Gmail Client) is used
import yagmail

# to delete current file after processing and emailing it
import os


# function to send email
def sendmail(emailid, stuname):
    # credentials of sender
    yag = yagmail.SMTP("sushilwaghmaresmtp@gmail.com", "somepassword*&#@$$$$")

    # details of the email
    yag.send(
        to=emailid,
        subject="Attendance Report",
        contents="Attendance Report is as follows",
        attachments=f"reportfolder/Attendance Report - {stuname}.pdf",
    )

    # delete pie chart png file, if exists
    if os.path.exists(f"piecharts/chart - {stuname}.png"):
        os.remove(f"piecharts/chart - {stuname}.png")

    # delete attendance report pdf file, if exists
    if os.path.exists(f"reportfolder/Attendance Report - {stuname}.pdf"):
        os.remove(f"reportfolder/Attendance Report - {stuname}.pdf")
