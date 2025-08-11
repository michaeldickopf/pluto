## Steps



## Linux Installation

0. Go to project root:
    cd 01_flask_website/    

1. create python venv
    python -m venv venv
    source ./venv/bin/activate

2. install pip requirements

Install quickly, if its still August 2025:

    pip install email-to
    pip install flask
    pip install dotenv
    pip install flask_mail

If you download this in 2100:

    pip install -r requirements.txt

3. run app on localhost 

flask --app 01_flask_test run --debug