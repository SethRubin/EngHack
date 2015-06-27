import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# example usage:
# bulk_email("hello world", ["sorrymarko@gmail.com"])
def bulk_email(words, recipients):
    me = "sorrymarko@gmail.com"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "WordBuzz! Words are Trending"
    msg['From'] = me

    text = "The following words you have subscribed to are trending:\n\n" \
           + "\n".join(words) \
           + "\n\nMake sure to check them out while they're hot!"
    html = """\
    <html>
      <head></head>
      <body>
        <p>The following words you have subscribed to are trending:<br><br>""" \
           + "<br>".join(words) \
           + """<br><br>
           Make sure to check them out while they're hot!
        </p>
      </body>
    </html>
    """

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login('sorrymarko@gmail.com', 'sorrymarko1')

    for recipient in recipients:
        msg['To'] = recipient
        s.sendmail(me, recipient, msg.as_string())

    s.quit()
