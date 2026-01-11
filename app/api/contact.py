from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from typing import Optional

router = APIRouter()

class ContactForm(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str

@router.post("/send-email")
async def send_contact_email(contact: ContactForm):
    try:
        # Email configuration
        smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
        smtp_port = int(os.getenv("SMTP_PORT", "587"))
        smtp_username = os.getenv("SMTP_USERNAME")
        smtp_password = os.getenv("SMTP_PASSWORD")
        recipient_email = os.getenv("EMAIL_TO", "it@goconstructioltd.com")

        # For development/testing, if SMTP not configured, just log and return success
        if not smtp_username or not smtp_password:
            print(f"EMAIL NOT SENT (SMTP not configured): To: {recipient_email}, Subject: Contact Form: {contact.subject}")
            print(f"From: {contact.email}, Name: {contact.name}")
            print(f"Message: {contact.message}")
            return {"message": "Email logged successfully (SMTP not configured)"}

        # Create message
        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = recipient_email
        msg['Subject'] = f"Contact Form: {contact.subject}"

        # Email body
        body = f"""
        New contact form submission from GO Construction website:

        Name: {contact.name}
        Email: {contact.email}
        Subject: {contact.subject}

        Message:
        {contact.message}

        ---
        This email was sent from the GO Construction contact form.
        """

        msg.attach(MIMEText(body, 'plain'))

        # Send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail(smtp_username, recipient_email, text)
        server.quit()

        return {"message": "Email sent successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")