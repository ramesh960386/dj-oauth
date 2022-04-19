from email import message
from operator import sub
from django.core.mail import send_mail
import random
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from .models import User


def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None

def send_otp_via_email(email, otp):
    subject = 'Your account verification email'
    # otp = random.randint(100000, 999999)
    message = f'Your otp is {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject,message, email_from, [email])
    # try:
    #     user_obj = User.objects.get(email=email)
    #     user_obj.otp = otp
    #     user_obj.save()
    # except User.DoesNotExist as e:
    #     return None