import random
import smtplib
from email.message import EmailMessage


phone_number = input("Enter your phone number with out any spaces or dashes: ")
print("AT&T")
print("Sprint")
print("T-Mobile")
print("Verizon")
provider = input("Enter your data provider exactly how it is written above: ")
if provider == "AT&T":
    provider = "@mms.att.net"
elif provider == "Sprint":
    provider = "@pm.sprint.com"
elif provider == "T-Mobile":
    provider = "@tmomail.net"
elif provider == "Verizon":
    provider = "@vzwpix.com"
person = phone_number + provider

run = 1
while run == 1:
    def email_alert(subject, body, to):
        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = subject
        msg['to'] = to

        user = "dhruv0223@gmail.com"
        msg['from'] = user
        password = "yqqmcvzsxocprhbw"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)

        server.quit()

    user = ''
    def shuffle(string):
        tempList = list(string)
        random.shuffle(tempList)
        return ''.join(tempList)

    uppercaseLetter1=chr(random.randint(65,90)) 
    uppercaseLetter2=chr(random.randint(65,90))
    num1 = str(random.randint(0,9))
    num2 = str(random.randint(0,9))

    password = uppercaseLetter1 + uppercaseLetter2 + num1 + num2
    password = shuffle(password)

    

    email_alert("Your verification code:", password, person)

    user = input('Enter 4-digit code: ')
    print("It may take up to 30 second to send")
    if user == password:
        print("You may now access your passwords")
        run = 2
    else:
        print("The code that you have written is incorrect, enter new code")
        run = 1
        
a = input('Press a key to exit')
if a:
    exit(0)