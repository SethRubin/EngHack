import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# example usage:
# bulk_email("hello world", ["sorrymarko@gmail.com"])
def bulk_email(word, recipients):
	me = "sorrymarko@gmail.com"

	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Test " + word
	msg['From'] = me

	text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
	html = """\
	<html>
	  <head></head>
	  <body>
	    <p>Hi!<br>
	       How are you?<br>
	       Here is the <a href="https://www.python.org">link</a> you wanted.
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
