import smtplib
import datetime

#debuglevel = 0

user_name = 'joerozen@gmail.com'
password = 'ovfrivyzqlvuineb'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    #smtp.set_debuglevel(debuglevel)
    connection.login(user_name, password)
    connection.sendmail(
        from_addr=user_name,
        to_addrs='tsmtp79@gmail.com',
        msg='Subject:Hello test 4\n\nHello world!'
    )
