# we will add tippgeber as "contact-reason" in the regular contactform.
# the Reasons in contactform: "Tippgeber",


from django.forms import ModelForm, forms
from captcha.fields import ReCaptchaField

from .models import *


# this is the GOOGLE RECAPTCHA Form !


class ContactForm(ModelForm):
    #captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = ['topic', 'firstname', 'lastname', 'email',
                  'tel', 'message']
