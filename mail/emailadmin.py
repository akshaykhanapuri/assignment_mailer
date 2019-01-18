from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.contrib import messages
from django.conf import settings
from .models import Mail
import os
import time
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def em_admin():
    while True:

        summary_obj = Mail.objects.all()
        count = Mail.objects.all().count()
        summary_list = []
        for iter in range(count):
            summary_list.append('Email sent to:')
            summary_list.append(summary_obj[iter].rec_id)
            summary_list.append('at')
            summary_list.append(str(summary_obj[iter].mail_time))
            summary_list.append('____')

        lst = str(summary_list)
        emailadmin = EmailMessage(
        'Summary',
        lst,
        'akshaykhanapuri12@gmail.com',
        ['akshaykhanapuri12@gmail.com'],
        None,
        None,
        None,
        None,
        None
        )
        emailadmin.send(fail_silently=False)
        time.sleep(1800)

def em_user(request):
    mailobj = Mail()
    mailobj.rec_id = str(request.POST['em'])
    mailobj.cc = str(request.POST['cc'])
    mailobj.bcc = str(request.POST['bcc'])
    mailobj.sub = str(request.POST['sub'])
    mailobj.message = str(request.POST['mess'])
    #mailobj.mail_time = str(datetime.now)
    non_rep_reclist = []
    non_rep_reclist.append(mailobj.rec_id)
    if request.FILES.get('csv_file',False):
        mailobj.csv = request.FILES.get('csv_file',False)
        mailobj.save()
        csv_file_name = mailobj.csv.name
        csv_handler = open(os.path.join(BASE_DIR, 'media/') + csv_file_name)
        csv_lines = csv_handler.readlines()
        rec_list = []
        for eachline in csv_lines:
            rec_list.append(eachline.rstrip('\n').split(','))

        for eachlist in rec_list:
            for eachelement in eachlist:
                if eachelement not in non_rep_reclist:
                    non_rep_reclist.append(eachelement)
        print(non_rep_reclist)
    mailobj.save()
    email = EmailMessage(
    mailobj.sub,
    mailobj.message,
    'akshaykhanapuri12@gmail.com ',
    non_rep_reclist,
    [mailobj.bcc],
    None,
    None,
    None,
    [mailobj.cc]

    )
    email.send(fail_silently=False)
