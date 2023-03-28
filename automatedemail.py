import smtplib
from email.message import EmailMessage
import logging

''' most likely required to generated seperate password from your gmail account. First you need to enable 2 step verification 
    and then you need to generate separate App password. '''


# Enter your email and generated password
email = ''
password = ''

# Add all the e-mails in this contacts list
contacts = []

# Configuring logging
logging.basicConfig(filename='automatedemail.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

for contact in contacts:
    try:
        logging.info(f'creating email for {contact}....')
        msg = EmailMessage()

        # Enter Subject
        msg['Subject'] = 'My Subject'
        msg['From'] = email
        msg['To'] = contact

        # Plain text email content (uncomment next line)
        # msg.set_content('')

        # HTML Body
        # Note --- Use images which are available online for inline images eg <img src="https://cdn-icons-png.flaticon.com/512/124/124021.png">--
        # msg.add_alternative(string, subtype='html')
        msg.add_alternative(
            """
                       <h1>This is HTML heading</h1>
                   
                    """, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email, password)
            smtp.send_message(msg)
            logging.info(f'Successfully sent email to {contact}')
    except Exception as e:
        logging.error(f'occurred while sending email to {contact} : {e}')

