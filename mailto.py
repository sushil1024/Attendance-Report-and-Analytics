# to send email (report)
import yagmail
import os


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

    if os.path.exists(f"piecharts/chart - {stuname}.png"):
        os.remove(f"piecharts/chart - {stuname}.png")
    if os.path.exists(f"reportfolder/Attendance Report - {stuname}.pdf"):
        os.remove(f"reportfolder/Attendance Report - {stuname}.pdf")
