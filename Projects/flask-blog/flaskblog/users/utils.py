import os
import secrets
from flaskblog import app, mail
from PIL import Image
from flask import url_for
from flask_mail import Message


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path, "static/profile_pics", picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    link_expiration_time = 1800

    token = user.get_reset_token(link_expiration_time)
    msg = Message("Password Reset Request")
    msg.sender = "noreply@demo.com"
    msg.recipients = [user.email]
    msg.body = f"""To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

Please be aware that the link will expire in {int(link_expiration_time/60 + link_expiration_time%60)} minutes.

If you did not make this request, then simply ignore this email and no changes will be made.
"""
    mail.send(msg)
