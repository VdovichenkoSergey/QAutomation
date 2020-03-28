import smtplib

'''Жду от вас письмо! (слайды 14-18). Воспользуйтесь менеджером контекста
(with … as) (слайд 20)
(Не забудьте для себя понять код из официальной документации – слайд 17).'''

with smtplib.SMTP('smtp.gmail.com', 587) as send_server:
    send_server.starttls()
    send_server.login('vdovi4enko.qa@gmail.com', '*********')

    send_list = ['el.piankova@gmail.com', 'vdovi4enko.qa@gmail.com']
    subject = 'Email from PyCharm from Vdovichenko Sergey'
    body = 'I did it!'
    msg = "\r\n".join((
     "Subject: %s" % subject,
     "",
     body
    ))
    send_server.sendmail('vdovi4enko.qa@gmail.com', send_list, msg)
    send_server.quit()


