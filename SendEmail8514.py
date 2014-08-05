import time
import serial
import smtplib
ser = serial.Serial('COM3', 9600)

def send_baby():
    TO = '3056065141@txt.att.net'
    GMAIL_USER = 'tempalertgwc@gmail.com'
    GMAIL_PASS = 'GWCROCKS'
    SUBJECT = 'THERMALERT: Baby on Board!'
    TEXT = 'You seem to have forgotten your baby in the car seat.Remember, it is illegal to leave a child in an unattended vehicle.'

    print("Sending Baby Email")
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'
    print header
    msg = header + '\n' + TEXT + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, TO, msg)
    smtpserver.close()

def send_warning(temp_hot):
    TO = '3056065141@txt.att.net'
    GMAIL_USER = 'tempalertgwc@gmail.com'
    GMAIL_PASS = 'GWCROCKS'
    SUBJECT = 'THERMALERT: Reaching Unsafe Temperatures!'
    TEXT = 'Your car is reaching unsafe temperatures for your child or pet. The temperature is now:'+ temp_hot

    print("Sending Warning Email")
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'
    print header
    msg = header + '\n' + TEXT + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, TO, msg)
    smtpserver.close()


def send_danger(temp_danger):
    TO = '3056065141@txt.att.net'
    GMAIL_USER = 'tempalertgwc@gmail.com'
    GMAIL_PASS = 'GWCROCKS'
    SUBJECT = 'THERMALERT: Reaching DEADLY Temperatures!'
    TEXT = 'YOUR CAR IS NOW REACHING DEADLY TEMPERATURES. PLEASE RETRIEVE YOUR CHILD OR PET IMMEDIATELY! The Temperature is now:'+temp_danger
    print("Sending Danger Email")
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'
    print header

while True:

    message = ser.readline()
    print(message)
    if message[0] == 'B' :
        send_baby()
    elif message[0] =='W':
        temp_hot= message[14:]
        send_warning(temp_hot)
    elif message[0]=='D':
        temp_danger= message[13:]
        send_danger(temp_danger)
    time.sleep(0.5)

