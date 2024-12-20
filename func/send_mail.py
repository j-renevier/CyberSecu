import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender_email = "jooemcg77@gmail.com"
receiver_email = "jeanpierre.polnareff418@gmail.com"
password = "ebxw fwuh krkb iile" #mot de passe généré unique

def send_mail(receiver):

    subject = "Urgent - Sauvons les canards avant qu’il ne soit trop tard!"

    with open("mail_body.txt", 'r') as file:
        body = file.read()

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver, msg.as_string())
            print("Email envoyé avec succès.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        
send_mail(receiver_email)