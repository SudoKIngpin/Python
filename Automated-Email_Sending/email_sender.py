import smtplib

def send_emails(emails):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()

    sender_email='astinaam@gmail.com'
    password=input('Input Passwod : ')
    try:
        server.login(sender_email,password)
        print('login successful')
    except:
        print('Failed Autentication.')
        
    for name in emails:
        print('sending..')
        print(name)
        body = "Subject : Automated Email testing\n\n"
        body += "From : Abdullah Al Mahmud\n"
        body += "To : "+name+"\n"
        body += "Hi "+ emails[name] + ",\n"
        body += "\nSend Confirmation If you got this.\nThanks.\n"
        server.sendmail(sender_email,name,body)
    server.close()

def main():
    emails={}
    emails['abdulahalmahmud@gmail.com']='Mahmud'
    
    send_emails(emails)
    print('Email sent :)')

main()
