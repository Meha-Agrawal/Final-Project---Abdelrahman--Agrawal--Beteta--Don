import time
import serial
import smtplib

def send_baby():
    TO = 'salma.zakaria@gmail.com'
    GMAIL_USER = 'tempalertgwc@gmail.com'
    GMAIL_PASS = 'GWCROCKS'
    SUBJECT = 'THERMALERT: Baby on Board!'
    TEXT = 'You seem to have forgotten your baby in the car seat.' \
            'Remember, it is illegal to leave a child in an unattended vehicle. '
    ser = serial.Serial('COM3', 9600)
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

while True:
    message = ser.readline()
    print(message)
    if message[0] == 'B' :
        send_email()
    time.sleep(0.5)

def send_warning():
    TO = 'salma.zakaria@gmail.com'
    GMAIL_USER = 'tempalertgwc@gmail.com'
    GMAIL_PASS = 'GWCROCKS'
    SUBJECT = 'THERMALERT: Reaching Unsafe Temperatures!'
    TEXT = 'Your car is reaching unsafe temperatures for your child or pet. The temperature is now:'
    ser = serial.Serial('COM3', 9600)
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


while True:
    message = ser.readline()
    print(message)
    if message[0] == 'W' :
        send_email()
    time.sleep(0.5)

def send_danger():
    TO = 'salma.zakaria@gmail.com'
    GMAIL_USER = 'tempalertgwc@gmail.com'
    GMAIL_PASS = 'GWCROCKS'
    SUBJECT = 'THERMALERT: Reaching DEADLY Temperatures!'
    TEXT = 'YOUR CAR IS NOW REACHING DEADLY TEMPERATURES. PLEASE RETRIEVE YOUR CHILD OR PET IMMEDIATELY!'
    ser = serial.Serial('COM3', 9600)
    print("Sending Danger Email")
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


while True:
    message = ser.readline()
    print(message)
    if message[0] == 'D' :
        send_email()
    time.sleep(0.5)

