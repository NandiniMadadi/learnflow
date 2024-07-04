
import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import os

# SMTP server configuration (example for Gmail)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

def send_email(email_subject, email_body, recipient_emails):
    msg = MIMEMultipart()
    msg['From'] = SMTP_USER
    msg['To'] = ', '.join(recipient_emails)
    msg['Subject'] = email_subject

    msg.attach(MIMEText(email_body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, recipient_emails, msg.as_string())
            print(f"Email sent to {', '.join(recipient_emails)}")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")

def schedule_email(email_subject, email_body, recipient_emails, send_datetime):
    current_time = datetime.now()
    delay = (send_datetime - current_time).total_seconds()

    if delay < 0:
        print("Scheduled time is in the past. Please provide a future time.")
        return

    def job():
        send_email(email_subject, email_body, recipient_emails)

    schedule.every(delay).seconds.do(job)
    print(f"Email scheduled to be sent to {', '.join(recipient_emails)} at {send_datetime}")

def main():
    print("Email Automation Script")

    email_subject = input("Enter the subject: ")
    email_body = input("Enter the body of the email: ")
    recipient_emails = input("Enter recipient email addresses (comma separated): ").split(',')

    send_now = input("Send now? (yes/no): ").strip().lower()

    if send_now == 'yes':
        send_email(email_subject, email_body, recipient_emails)
    else:
        send_date_str = input("Enter the date to send the email (YYYY-MM-DD): ")
        send_time_str = input("Enter the time to send the email (HH:MM): ")
        send_datetime_str = f"{send_date_str} {send_time_str}"
        
        try:
            send_datetime = datetime.strptime(send_datetime_str, "%Y-%m-%d %H:%M")
            schedule_email(email_subject, email_body, recipient_emails, send_datetime)
        except ValueError as e:
            print("Invalid date/time format. Please try again.")
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
