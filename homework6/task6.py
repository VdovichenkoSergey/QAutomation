# Разобраться с получением email письма. Попробуйте поискать информацию самостоятельно (IMAP или POP3 протоколы получения писем).
import imaplib
import email
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('iulia.gaiduchienko@gmail.com', '****')
mail.list()
mail.select("inbox")
res, data = mail.search(None, "ALL")
id_list = data[0].split() # Разделяем ID писем
last_email = id_list[-1] #берем айди последнего письма
result, data = mail.fetch(last_email, "(RFC822)")
raw_email = data[0][1]
#письмо получили пытаемся что-то из текста достать
email_message = email.message_from_bytes(raw_email)
maintype = email_message.get_content_maintype()
if maintype == 'multipart':
      for part in email_message.get_payload():
            if part.get_content_maintype() == 'text':
                  body = part.get_payload()
elif maintype == 'text':
      body = email_message.get_payload()
print(f"To: {email_message['To']}\n"
      f"From: {email.utils.parseaddr(email_message['From'])[1]}\n"
      f"Date: {email_message['Date']}\n"
      f"Subject: {email_message['Subject']}\n"
      f"Body: {body}")# Вобщем текст конечно видно, но полностью распарсить у меня не вышло
mail.close()
mail.logout()
