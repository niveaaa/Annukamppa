import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication  # For file attachments
from report_generator import generate_report
from datetime import date
import time

file = date.today()

def send_email(report, attachment_path=None):
    sender_email = "starader47@gmail.com"  # Add your sender email
    receiver_email = "aryandashing608@gmail.com"  # Add the recipient email
    password = "pmup ayxm pcal xwwn"  # Add your email password or app password

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Daily Report"

    # Attach the report text
    msg.attach(MIMEText(report, 'plain'))

    # Attach the file if a path is provided
    if attachment_path:
        try:
            with open(attachment_path, 'rb') as file:
                # Read the file
                attachment = MIMEApplication(file.read(), Name=attachment_path)
                # Add a header to the attachment
                attachment['Content-Disposition'] = f'attachment; filename="{attachment_path}"'
                # Attach the file to the message
                msg.attach(attachment)
        except FileNotFoundError:
            print(f"Attachment file not found: {attachment_path}")
        except Exception as e:
            print(f"Failed to attach file. Error: {str(e)}")

    try:
        # Set up the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        # Convert the message to a string and send it
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")
    finally:
        server.quit()  # Close the SMTP server connection

# Example usage:
if __name__ == "__main__":
    report = generate_report()  # Assuming generate_report() function is defined elsewhere
    send_email(report, f'{file}.csv')  # Replace with your actual file path

