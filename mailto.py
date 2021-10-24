import yagmail

yag = yagmail.SMTP("sushilwaghmaresmtp@gmail.com", "somepassword*&#@$$$$")

yag.send(
    to="rajmahajan657@gmail.com",
    subject="Attendance Report",
    contents="Attendance Report is as follows",
    attachments="records.csv",
)
