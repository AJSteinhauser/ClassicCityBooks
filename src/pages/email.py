import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def emailSelf(you, user_id):
    gmail_user = 'classiccitycollection@gmail.com'
    gmail_password = 'CCC123!@'
    #you = 'danielamacd@gmail.com'
    # Create message container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Verify your account"
    msg['From'] = gmail_user
    msg['To'] = you
    # Create the body of the message (a plain-text and an HTML version).
    user_id = str(user_id)
    text = "Your account has been created with the user ID: " + user_id +". However, you still need to verify your account.\
    \nClick this link to verify your account: http://127.0.0.1:8000/"
    body = """\
    <html>
      <head></head>
      <body>
        <h1>Verify your account</h1>
        <p>Your account has been created with the user ID: """ + user_id + """, but you still need to verify it.
           Click <a href="http://127.0.0.1:8000/">this link</a> to verify your account.
        </p>
      </body>
    </html>
    """
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(body, 'html')
    # Attach parts into message container.
    msg.attach(part1)
    msg.attach(part2)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(gmail_user, gmail_password)
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    mail.sendmail(gmail_user, you, msg.as_string())
    mail.quit()
    return "Your email has been sent."
        