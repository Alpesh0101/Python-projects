import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, my_mail, message):
    server = smtplib.SMTP('alpeshpatil0510gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('Sender_Email', 'Sender_Email_password')
    email = EmailMessage()
    email['From'] = 'alpeshpatil0510@gmail.com'
    email['To'] = 'appupatil562@gmail.com',
    email['Subject'] = my_mail
    email.set_content(message)
    server.send_message(email)


email_list = {
    'alpesh patil': 'alpeshpatil0510@gmail.com',
    'Alpesh.D Patil': 'appupatil562@gmail.com',
    'Alpesh': 'alpeshpatil0510@gmail.com',
    'Alpesh.D Patil': 'alpeshpatil0510@gmail.com',
    'Alpesh': 'appupatil562@gmail.com',
}


def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    my_mail = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, my_mail, message)
    talk('Hey lazy ass. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()