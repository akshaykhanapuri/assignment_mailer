# assignment_mailer

For the dependencies to be installed refer requirements.txt

Things to be configured while testing:
1) In settings.py,
++ EMAIL_HOST_USER = 'Enter your gmail user ID'
++ EMAIL_HOST_PASSWORD = 'Enter your gmail password' as I am using gmail SMTP

2) In emailadmin.py module go to em_admin() function definition, Inside it I have created an instance 'emailadmin' of class 'EmailMessage'.
++ I have HARDCODED akshaykhanapuri12@gmail.com as the 'to' and 'from' email id of admin. You will have to change it to your gmail id.

3) To install ELK refer: https://logz.io/blog/elk-mac/

4) To link logstash with the app, run
./logstash -f path/to/logstash.conf

./logstash ==> PATH WHERE LOGSTACH IS INSTALLED
path/to/logstash.conf ==> This file is present in assignment_mailer folder

5) To create the Elastic search index, run
python manage.py search_index --rebuild

6) Open the Kibana UI (127.0.0.1:5601)
management >> index patterns >> Create index pattern
++ create one for logstash: logstash-*
++ create one for elasticsearch : mails

You will be able to monitor live logs on the discover tab
And also a summary email will be sent to the admin emailid after every 30 mins
