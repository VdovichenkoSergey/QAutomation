# Жду от вас письмо! (слайды 16-20). Воспользуйтесь менеджером контекста (with … as) (слайд 20)
import smtplib
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login('iulia.gaiduchienko@gmail.com','******')
    tolist = ["iulia.gaiduchienko@gmail.com", "el.piankova@gmail.com"]
    SUBJECT = "Test email from Python"
    text = "I did iT"
    BODY = "\r\n".join((
     "Subject: %s" % SUBJECT,
     "",
     text
    ))
    smtp.sendmail('iulia.gaiduchienko@gmail.com', tolist, BODY)
