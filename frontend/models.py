from django.db import models


class Contact(models.Model):
    SCHADEN_MELDEN = 0
    PROBLEM_MELDEN = 1
    KOSTEN_ANFRAGE = 2
    KARIERRE = 3
    SONSTIGES = 4
   
    topics = (
        (SCHADEN_MELDEN, 'Schaden am Auto'),
        (PROBLEM_MELDEN, 'Problem am Auto'),
        (KOSTEN_ANFRAGE, 'Kostenanfrage'),
        (KARIERRE, 'Karriere'),
        (SONSTIGES, 'Sonstiges'),
    )

    topic = models.IntegerField(
        default=0, choices=topics, verbose_name='Anliegen')
    firstname = models.CharField(max_length=100, verbose_name='Vorname*')
    lastname = models.CharField(max_length=100, verbose_name='Nachname*')
    email = models.EmailField(verbose_name='Email*')
    tel = models.CharField(max_length=26, null=True,
                           blank=True, verbose_name='Telefonnummer*')
    message = models.TextField(verbose_name='Nachricht')
    inquiry_send_at_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Datum')
    checked = models.BooleanField(default=False, verbose_name='Bearbeitet?')

    def __str__():
        return f'{self.firstname}s contact'
