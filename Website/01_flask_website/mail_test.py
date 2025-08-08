import os
import email
from flask import current_app, render_template
from flask_mail import Message
import smtplib
from dotenv import load_dotenv

load_dotenv()

def send_email(to_address, subject, html_filepath, **kwargs):
    """Generic function to send email with SMTP authentication"""
    try:
        # SMTP connection
        conn = smtplib.SMTP(os.getenv('SMTP_SERVER'), os.getenv('SMTP_PORT'))
        print(f"Connected to SMTP server")
        conn.starttls()
        print("STARTTLS successful")
        
        # Authentication
        username =  "michael.dickopf@unibw.de" # os.getenv('SMTP_DEFAULT_SENDER')
        password = "Unraveled3_Plow2_Purging2_Pedicure6_Autopilot2" # os.getenv('SMTP_PASSWORD',)
        conn.login(username, password)
        print('Login successfull')

        # Create a proper email message
        from email.message import EmailMessage
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = username
        msg['To'] = to_address
        with open(html_filepath) as fp:
            msg.set_content(fp.read(), 'html')        
    
        print('Message built')
        
        # Send email
        conn.send_message(msg)
        print('Message sent')
        
        # Make sure conn is properly closed
        conn.quit()
        return True
    except Exception as e:
        print(f"Error sending SMTP email: {str(e)}")
        return False