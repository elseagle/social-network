from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from . import mail
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)
        print("Sent!")


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()

    message = Mail(
        from_email=app.config["MAIL_USERNAME"],
        to_emails=to,
        subject=subject,
        html_content=template)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

    thr = Thread(target=send_async_email, args=[app, message])
    thr.start()
    return thr
