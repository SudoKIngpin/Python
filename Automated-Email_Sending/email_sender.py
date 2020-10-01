import smtplib

def send_emails(emails):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls() #Transport Layer Secuirity

    sender_email='astinaam@gmail.com'
    password=input('Enter Password : ')
    try:
        server.login(sender_email,password)
        print('Login Successful')
    except:
        print('Failed Autentication.')
        
        print("Please enable access to less secure apps from link given below ")
        
        print("https://myaccount.google.com/u/0/lesssecureapps")
        
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
