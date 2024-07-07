import os
import time
import pandas as pd
from createImage import createInvitationCard
from sendMail import EmailWithAttachment

def sendMail(mailInvitationName, receiverMail, attachments):
#********************** all variables ************************#
    '''mail related'''
    subject = 'Invitation to Leo Khel Rangotsav'
    body = f'''<html>
<head></head>
<body>
Respected <b>Leo {mailInvitationName}</b>,<br><br>

Thank you for registering for <b>Leo Khel Rangotsav</b>. We're thrilled to have you as well as leo members of your club at the event and expect you to bring along energy, enthusiasm, and sportsmanship.<br><br>

<b>Event Details</b><br>
<b>Date:</b> Chaitra 10, 2080 (Saturday)<br>
<b>Time:</b> 6:30 am onwards<br>
<b>Venue:</b> Southwestern State College, Basundhara<br><br>

Leo Khel Rangotsav is not just about the games and competitions; it's a wonderful opportunity for us to come together and strengthen the bonds between all the Leos within the Leo District Council 325J Nepal.<br><br>

Let's join hands and create lasting memories with all our fellow Leos. Your participation will make a significant difference in making this event truly memorable.<br><br>

We look forward to your presence and eagerly anticipate a day filled with fun, laughter, and the spirit of togetherness.<br><br>

<b>For Queries</b><br>
Event Coordinator: Leo <br>
Event Co-coordinator: Leo <br><br>

Regards,<br>
Leo Club of Kathmandu Budigandaki<br>
</body>
</html>'''

#********************** variables ended ************************#

    if attachments:
        mail.sendMail(receiverMail, subject, body, attachments)
    else:
        mail.sendMail(receiverMail, subject, body)


if __name__ == '__main__':  
    senderMail = 'your_mail@gmail.com'
    passphraseFile = 'resources/passphrase.txt'

    '''image related'''
    imageSrc = 'images/Invitation_Source.png'
    imageDest = 'Invitation1.png'

    textCordinates = (None, 1360) #center at X-axis
    textColor = (0,0,0)

    # put font=None for default font
    font = 'resources/GrandHotel-Regular.ttf'
    fontsize = 100

    # testing of text placement in image
    # final_image_location = createInvitationCard(srcImg=imageSrc, destImg=imageDest, text="Leo Prabin Paudel", cordinates=textCordinates, color=textColor, fontPath=font, fontSize=fontsize, display=True)

    mailList = "resources/demo.csv" #inside 'resources' directory

    with open(passphraseFile, 'r') as file:
        password = file.readline()
        # you can simply enter your app specific password here
        # https://myaccount.google.com/apppasswords

    mail = EmailWithAttachment()
    mail.establishConnection(senderMail, password)

    print(f"Reading from {mailList}")
    time.sleep(2) #Intentional Delay for Verification

    df = pd.read_csv(mailList)
    for index, row in df.iterrows():
        try:
            final_image_location = createInvitationCard(srcImg=imageSrc, destImg=imageDest, text="Leo" + row['Full Name'], cordinates=textCordinates, color=textColor, fontPath=font, fontSize=fontsize, display=False)
            attachments = {"personal_invitation":final_image_location, "banner":'./images/Banner.jpg'}   
            sendMail(row["Full Name"], row["Email"], attachments)
            os.remove(final_image_location)
        except KeyError as e:
            print(f"Keyerror, {e} column mentioned at line {e.__traceback__.tb_lineno} doesnot exist in csv file")
        except Exception as e:
            print(f"Exception occured on line {index+2}, ", e)

    del mail
