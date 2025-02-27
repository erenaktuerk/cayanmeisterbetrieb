from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.mail import EmailMultiAlternatives, BadHeaderError, EmailMessage, send_mail
from django.views.decorators.http import require_POST
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def send_contact_mail(whichform, firstname, lastname, email, customerMessage, tel,topic):
    # we enter the data that the form includes
    context = {
        'whichform': whichform,
        'firstname': firstname,
        'lastname': lastname,
        'email': email,
        'message': customerMessage,
        'tel': tel,
        'topic': topic,
    }

    subject = "Ein Kunde hat geschrieben! Cayan Meisterbetrieb Website."
    message = render_to_string(
        "frontend/mail.html", context
    )
    # print(message)
    striped_message = strip_tags(message)
    #print("we are here 2")
    # HERE IS THE PROBLEM
    msg = EmailMultiAlternatives(subject, striped_message,
                                 from_email=settings.SERVER_EMAIL, to=[settings.CAYAN_MAIL])
    msg.attach_alternative(message, "text/html")
    # if m == 1, than the message has been successfully sended
    m = msg.send(fail_silently=True)
    print('message is ', m)

def anfrageerhalten(request):
    context={}
    return render(request, 'frontend/anfrageerhalten.html', context)

def home(request):
    context = {}
    return render(request, 'frontend/home.html', context)

def aboutus(request):
    context = {}
    return render(request, 'frontend/aboutus.html', context)

def kontakt(request):
    context = {}
    if request.method == 'POST':
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            #captcha = contactform.get('captcha')
            # request.POST.get('recaptcha_form')
            """

                    if not captcha:
                recaptcha_form = FormWithCaptcha()
                form = ContactForm()
                print("recaptcha error")
                print(captcha)
                context['form'] = form
                context['recaptcha_form'] = recaptcha_form
                context['error_captcha'] = "Du musst den Recaptcha Test bestehen"
                return render(request, 'pages/contact.html', context)
            
            
            """

            c = contactform.save()

            send_contact_mail(
                'Kontaktformular', request.POST['firstname'], request.POST['lastname'], request.POST['email'], request.POST['message'], request.POST['tel'],request.POST['topic'])
            form = ContactForm()
            context['form']=form
            context['success']='Erfolgreich abgesendet'
            return render(request, 'frontend/kontakt.html', context)
            # now send a mail to tumuratas, so that he can notice that there has arrived a mai
        else:
            context['form'] = ContactForm(
                initial={
                    'topic': request.POST['topic'],
                    'firstname': request.POST['firstname'],
                    'lastname': request.POST['lastname'],
                    'email': request.POST['email'],
                    'tel': request.POST['tel'],
                    'street': request.POST['street'],
                    'postialcode': request.POST['postialcode'],
                    'city': request.POST['city'],
                    'message': request.POST['message'],

                }
            )
            context['errors'] = "Moment. Es gab einen Fehler."
            return render(request, 'frontend/kontakt.html', context)
    else:
        #recaptcha_form = FormWithCaptcha()
        form = ContactForm()
        context['form'] = form
        #context['recaptcha_form'] = recaptcha_form
    return render(request, 'frontend/kontakt.html', context)

def leistung(request):
    context = {}
    return render(request, 'frontend/leistung.html', context)


def impressum(request):
    context = {}
    return render(request, 'frontend/impressum.html', context)

def datenschutz(request):
    context = {}
    return render(request, 'frontend/datasecurity.html', context)

def agb(request):
    context = {}
    return render(request, 'frontend/agb.html', context)

def error_404(request, exception):
    context = {}
    return render(request, 'frontend/404.html', context)