import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, receiver_email, subject, audio_file_path):
    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the audio file
    with open(audio_file_path, "rb") as file:
        part = MIMEAudio(file.read())
        part.add_header("Content-Disposition", "attachment", filename=audio_file_path)
        encoders.encode_base64(part)
        message.attach(part)

    # Connect to the SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        # Login to the sender's email account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())

# Provide the required information
sender_email = "your_email@gmail.com"
sender_password = "your_password"
receiver_email = "recipient_email@example.com"
subject = "Audio File"

audio_file_path = "/path/to/audio.mp3"

# Send the email
send_email(sender_email, sender_password, receiver_email, subject, audio_file_path)
