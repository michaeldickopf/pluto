from flask import Flask, request, render_template, redirect, url_for
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from mail_test import send_email

load_dotenv()

app = Flask(__name__)

'''requirements
    pip install email-to
    pip install flask
    pip install dotenv
    pip install flask_mail
'''

# TODO: sanethization
# TODO: CSRF token, XSS deflection, ...

@app.route('/')
def home():
    line_count = int(count_csv_lines('mailing_list.csv'))
    print(line_count)
    return render_template('index.html', line_count=line_count) # TODO only 4 digit number supported, may break at 10.000 !


@app.route('/submit_form', methods=['GET', 'POST'])
def form_input():
    
    if request.method == "POST":
        req = request.form
        email = request.form['email'] # TODO: sanethize the input field !

        with open('mailing_list.csv','a') as file:
            file.write(email)
            file.write("\n")
        
        # send_email(email, subject='Welcome to Pluto!', html_filepath='email_response.html') # TODO reactivate email sending
    

    return redirect(url_for('home'))


def count_csv_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        line_count = sum(1 for line in file)
    return line_count
    

if __name__ == '__main__':
    app.run(debug=True)