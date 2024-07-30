import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

class EmailWithAttachment():
    def __init__ (self):
        self.s = None #set SMTP connection to None

    def __del__(self):
        if self.s:
            try:
                self.s.quit()
                print("Connection dissolved")
            except:
                pass

    def establishConnection(self, sender, password):
        print("Establishing SMTP connection")
        s = smtplib.SMTP('smtp.gmail.com', 587)  
        s.starttls()
        try:
            s.login(sender, password)
            print("Connection established successfully")
            self.s = s
        except:
            print("ERR_CONNECTION_REFUSED\nPlease check the credentials or network connection")
            exit()


    def sendMail(self, toAddr, subject, body, attachments=None):
        if not self.s:
            print("SMTP CONNECTION ERROR.\nPlease establish connection by providing sendermail and app specific passphrase")
            exit()

        if not toAddr or not body:
            print("Receiving Address or Body is empty")
            exit()
        
        msg = MIMEMultipart()
        msg['To'] = toAddr
        msg['Subject'] = subject
        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'html'))

        try:
            for key, value in attachments.items():
                att = open(value, "rb")

                p = MIMEBase('application', 'octet-stream')
                # To change the payload into encoded form
                p.set_payload((att).read())
                
                # encode into base64
                encoders.encode_base64(p)

                ''' attachment adds the file to the mail.
                filename gives information about the field: image, pdf etc.
                So,include extension type in name.'''

                #for attachments' name, key + extension of original image from value
                attName = key + '.' + value.rsplit('.', 1)[-1]
                p.add_header('Content-Disposition', "attachment; filename= %s" %attName)
                msg.attach(p)
        except AttributeError:
            pass
        except Exception as e:
            print(f"Failed to open the attachment {value}")
            exit()

        text = msg.as_string()

        self.s.sendmail('This doesnot really matter', toAddr, text)
        print(f"Mail sent ---> {toAddr}")
