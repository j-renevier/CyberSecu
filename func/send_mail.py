import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_mail():
        
    sender_email = "jooemcg77@gmail.com"
    receiver_email = "joe-94240@hotmail.fr"
    password = "ebxw fwuh krkb iile" #mot de passe généré unique

    subject = "Test d'envoi"
    body = "Ceci est un simple test d'email."

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    filename = "./projet/dist/récompense.data" #Piece jointe a importer

    try:
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={filename}",
        )
        msg.attach(part)
    except FileNotFoundError:
        print(f"Le fichier {filename} est introuvable.")

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email envoyé avec succès.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        
send_mail()