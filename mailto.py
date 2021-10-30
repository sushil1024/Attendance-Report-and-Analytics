# to send email (report)
import yagmail


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
