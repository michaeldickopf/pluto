from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

'''requirements
    pip install email-to
    pip install flask
    pip install dotenv
'''

# TODO: sanethization
# TODO: CSRF token, XSS deflection, ...

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit_form', methods=['GET', 'POST'])
def form_input():

    if request.method == "POST":
        req = request.form
        email = request.form['email'] # TODO: sanethize the input field !

        with open('mailing_list.csv','a') as file:
            file.write(email)
            file.write("\n")
        
        send_one_email(email)

    return render_template('index.html')



def send_one_email(recipient):
    sender = os.getenv('SMTP_EMAIL')
    password = os.getenv('SMTP_PASSWORD')

    msg = MIMEText('heloWorld')    
    msg['Subject'] = 'hi'
    msg['From'] = sender
    msg['To'] = recipient
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       print('login successfull')
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")




if __name__ == '__main__':
    app.run(debug=True)