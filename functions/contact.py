import smtplib, ssl
from email.message import EmailMessage
import os

def main():
    send_email("John Smith", "johnsmith@gmail.com", "Project", "Loved your earthquake tracker!")

def send_email(user_name, user_email, subject, message):
    '''Receive email from user who filled out contact form''' 
    #portfolio email sends contact form to personal email 
    portfolio_email=os.getenv(PORTFOLIO_EMAIL)
    personal_email = os.getenv(PERSONAL_EMAIL)
    #password for sender email
    passkey = os.getenv(PASSKEY)

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = portfolio_email #portfolio email
    msg["To"]  = personal_email #own email
    msg["Reply-To"] = user_email #users email

    #content of contact form sent to own email
    msg.set_content(f"""
        Name: {user_name}
        Email: {user_email}

        Subject: {subject}

        Message: 
        {message}
    """)

    #send email
    port = 465
    sender_email = portfolio_email
    receiver_email = personal_email
    password = passkey
    with smtplib.SMTP_SSL("smtp.gmail.com", port) as server:
        server.login(sender_email, password) 
        print("Logged in!")
        server.send_message(msg)
        print(f"{user_name} ({user_email}) message was successfully sent to {receiver_email} by {sender_email}")

if __name__ == "__main__":
    main()