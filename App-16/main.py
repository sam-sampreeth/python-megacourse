from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
import datetime
import os
from dotenv import load_dotenv
from flask_mail import Mail, Message

load_dotenv()
gmail_pass = os.getenv('APP_PASS')
gmail_id = os.getenv('APP_USER')
app = Flask(__name__)

app.config['SECRET_KEY'] = 'myapp123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config["MAIL_USERNAME"] = gmail_id
app.config["MAIL_PASSWORD"] = gmail_pass

db=SQLAlchemy(app)

mail=Mail(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email_name = db.Column(db.String(80))
    date= db.Column(db.Date)
    occupation = db.Column(db.String(80))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['fname']
        last_name = request.form['lname']
        email = request.form['email']
        date = request.form['date']
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
        current_occupation = request.form['selections']

        form = Form(first_name=first_name, last_name=last_name, email_name=email, date=date_obj, occupation=current_occupation)
        db.session.add(form)
        db.session.commit()

        message = Message("New Submission", sender= gmail_id, recipients=[gmail_id], body = f"New Submission by {form.first_name} {form.last_name}")
        mail.send(message)
        flash(f"{first_name}'s form submitted!", "success")

    return render_template("index.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)