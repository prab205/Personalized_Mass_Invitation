import os
import json
import time
import pandas as pd
from createImage import createInvitationCard
from sendMail import EmailWithAttachment

def sendMail(mailInvitationName, receiverMail, attachments=None):
    subject = 'Invitation to Leo Khel Rangotsav'
    body = f'''<html>
<head></head>
<body>
Respected <b>{mailInvitationName}</b>,<br><br>

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

    mail.sendMail(receiverMail, subject, body, attachments)


if __name__ == '__main__':  
    with open('variables.json') as varFiles:
        variables = json.load(varFiles)

    senderAddress, passphraseFile, mailCsvFile, csvMailHeader, csvNameHeader, prefixForName, attachments = variables['mail'].values()

    if variables['image']['imageCreation']:
        if variables['image']['createOnlyImage']:
            _, _, textForCreateOnlyImage, invitationSource, generatedImageName, viewGeneratedImage, overwriteIfExists, xCoordinate, yCoordinate, rgb_color, font, fontSize, _, _ = variables['image'].values()
            createInvitationCard(srcImg=invitationSource, text=textForCreateOnlyImage, destImg=generatedImageName, overwrite=overwriteIfExists, cordinates=(xCoordinate, yCoordinate), color=tuple(rgb_color), fontPath=font, fontSize=fontSize, display=True)
            exit(-1)
        else:
            _, _, textForCreateOnlyImage, invitationSource, generatedImageName, viewGeneratedImage, overwriteIfExists, xCoordinate, yCoordinate, rgb_color, font, fontSize, csvUserNameHeader, prefixToAdd = variables['image'].values()
            attachments['personal_invitation'] = generatedImageName

    with open(passphraseFile, 'r') as file:
        password = file.readline()

    mail = EmailWithAttachment()
    mail.establishConnection(senderAddress, password)

    print(f"Reading from {mailCsvFile}")
    time.sleep(2) #Intentional Delay for Verification

    df = pd.read_csv(mailCsvFile)
    for index, row in df.iterrows():
        try:
            createInvitationCard(srcImg=invitationSource, text=prefixToAdd + row[csvUserNameHeader], destImg=generatedImageName, overwrite=overwriteIfExists, cordinates=(xCoordinate, yCoordinate), color=tuple(rgb_color), fontPath=font, fontSize=fontSize, display=viewGeneratedImage)  
            sendMail(prefixForName + row[csvNameHeader], row[csvMailHeader], attachments)
            os.remove(generatedImageName)
        except KeyError as e:
            print(f"Keyerror, {e} column mentioned at line {e.__traceback__.tb_lineno} doesnot exist in csv file")
            exit(-1)
        except Exception as e:
            print(f"Exception occured on line {index+2}, ", e)

    del mail
