import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
def emailSelf(you, user_id, confirm_code):
    gmail_user = 'classiccitycollection@gmail.com'
    gmail_password = 'CCC123!@'
    # Create message container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Verify your account"
    msg['From'] = gmail_user
    msg['To'] = you
    # Create the body of the message (a plain-text and an HTML version).
    user_id = str(user_id)
    confirm_code = str(confirm_code)
    text = "Your account has been created with the user ID: " + user_id +". However, you still need to verify your account."
    text += "Your security code is: " + confirm_code+".\n Click this link to verify your account: http://127.0.0.1:8000/confirmation"
    body = """\
    <html>
      <head></head>
      <body>
        <h1>Verify your account</h1>
        <p>Your account has been created with the user ID: """ + user_id + """, but you still need to verify your account.
           Your security code is: """ + confirm_code+""".\n Click <a href="http://127.0.0.1:8000/confirmation">this link</a> to verify your account.
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
        
def recoverEmail(email, confirm_code, id):
    gmail_user = 'classiccitycollection@gmail.com'
    gmail_password = 'CCC123!@'
    # Create message container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Recover Your Account"
    msg['From'] = gmail_user
    msg['To'] = email
    confirm_code = str(confirm_code)
    id = str(id)
    # Create the body of the message (a plain-text and an HTML version).
    text = "Hello, from Classic City Collections! Your confirmation code is: " + confirm_code + ".\
     Your id is " + id + ". Click this link to login: http://127.0.0.1:8000/resetpass/"
    body = """\
    <html>
      <head></head>
      <body>
        <h1>Recovery Password</h1>
        <p>Hello, from Classic City Collections! Your confirmation code is: <b>""" + confirm_code + """</b>.
           Your id is <b>""" + id + """</b>. Click <a href="http://127.0.0.1:8000/resetpass/">this link</a> to login.
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
    mail.sendmail(gmail_user, email, msg.as_string())
    mail.quit()
    return "Your email has been sent."
    
def accountChange(email):
    gmail_user = 'classiccitycollection@gmail.com'
    gmail_password = 'CCC123!@'
    # Create message container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Account Changes"
    msg['From'] = gmail_user
    msg['To'] = email
    # Create the body of the message (a plain-text and an HTML version).
    text = "Hello, from Classic City Collections! We just wanted to let you know that your account details have been changed.\n\
    If this was not you, please reset your password!"
    body = """\
    <html>
      <head></head>
      <body>
        <h1>Account Changes</h1>
        <p>Hello, from Classic City Collections! We just wanted to let you know that your account details have been changed.\n\
           If this was not you, please reset your password!.
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
    mail.sendmail(gmail_user, email, msg.as_string())
    mail.quit()
    return "Your email has been sent."
    
def promoEmail(email, promocode, percentage, start, end):
    gmail_user = 'classiccitycollection@gmail.com'
    gmail_password = 'CCC123!@'
    # Create message container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Promotional Email"
    msg['From'] = gmail_user
    msg['To'] = email
    # Create the body of the message (a plain-text and an HTML version).
    text = "Hello, from Classic City Collections! We have a new promotional code that you can use on all of our products!" \
    " The promocode is " + promocode + ". You can use it to get " + percentage + "% of your order! You can use the code" \
    "starting on " + start + ". You have until " + end + " to use it."
        
    body = """\
    <html>
      <head></head>
      <body>
        <h1>Promotional Code</h1>
        <p>Hello, from Classic City Collections! We have a new promotional code that you can use on all of our products!
           The promocode is """ + promocode + """. You can use it to get """ + percentage + """% of your order! You can use the 
           code starting on """ + start + """. You have until """ + end + """ to use it.
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
    mail.sendmail(gmail_user, email, msg.as_string())
    mail.quit()
    return "Your email has been sent."
    
    
def emailCheckout(you, user_id, first_name, cart, time):
    gmail_user = 'classiccitycollection@gmail.com'
    gmail_password = 'CCC123!@'
    # Create message container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Order Summary"
    msg['From'] = gmail_user
    msg['To'] = you
    # Create the body of the message (a plain-text and an HTML version).
    user_id = str(user_id)
    text = "We are processing your new order! Please review the information below:"
    body = """\
    <html>
      <head></head>
      <body>
        <h1><b>Order Summary</b></h1>
        <p>Hi, """ + first_name + """, we are processing your new order! Please review the information below:
    """
    body = body + "<h2>Order ID:" + time[:10] + "-" + user_id + "</h2>"
    body = body + "<h3>User ID:" + user_id + "</h3>"
    for item in cart:
        if item != "totalPrice":
            body = body + "<br><h3>" + cart[item]["book_title"] + "</h3>"
            body = body + "<p>Quantity:" + cart[item]["quantity"] + "</p>"
            body = body + "<p>Price per item: $%.2f</p>" % cart[item]["price"]
        else:
            body = body + "<h2>Total Price: $%.2f</h2>" % cart[item]
    body = body + "<br><p>Thank you so much for supporting The Classic City Collection! We hope to see you again soon.</p><br>"
    body = body + "<br><p>If you ever have any questions please reach out to us at classiccitycollection@gmail.com.</p><br>"
    body = body + """
        </p>
      </body>
    </html>
    """
    print("TEST")

    print("ENDTEST")
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