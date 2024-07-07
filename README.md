### Personalized Mass Invitation
Python program for sending mass mail with personal attachements. 
The program can embed text within an image as well as send mail with attachments.  

---

**image.py**  
Embeds text in an image.  
- <b>createInvitationCard</b>(srcImg, text, destImg=None, cordinates=(None, None), color=(0,0,0), fontPath=None, fontSize=50, display=False)  
  
---

**mail.py**  
Establishes connection with google smtp server using app specific password and sends mail to the receiver.  
- <b>establishConnection</b>(self, sender, password)  
 &emsp;&emsp;Establishes connection to gmail SMTP server if possible  

- <b>sendMail</b>(self, toAddr, subject, body, attachments)  
&emsp;&emsp;Send mail with necessary attachments  

---

**main.py**  
Things to configure beforehand  
1. senderMail  
2. passphraseFile  
    &emsp;File containing your [app-specific password](https://myaccount.google.com/apppasswords)
3. imageSrc  
    &emsp;The image source where text is to be embedded. 
4. imageDest  
    &emsp;Name of the file the edited image will be saved, requires file extension 
5. textCordinates [Optional]  
    &emsp;Value in (X-coordinate, Y-coordinate)  
    &emsp;Put None for center alignment along that coordinate. eg (None, Y-coordinate) 
6. textColor [Optional]  
    &emsp;in (r,g,b) value
7. font [Optional]  
    &emsp;Path to .ttf file of the font 
8. fontsize [Optional]  
9. mailList  
    &emsp;Path to csv file that contains data for sending mail
10. subject, body [sendMail()]  
11. attachments  
    &emsp;dictionary item -> {'display name':'path of item to attach'}  
    &emsp;can contain multiple key-value pair 

---

**To get the program running**
1. Clone the repo  
`git clone https://github.com/prab205/Personalized_Mass_Invitation.git`
2. Enter the project directory  
`cd Personalized_Mass_Invitation`
3. Create python virtual environment and activate it  
`python3 -m venv .venv`  
&emsp; Linux/MacOS  
`source .venv/bin/activate`  
&emsp; Windows  
`.venv\Scripts\activate [Windows]`  
4. Install dependencies  
`pip install -r requirements.txt`  
5. Correctly edit 'senderMail' variable at 'main.py' and insert your google app-specific password at ./resources/passphrase.txt file.  
6. Run the program  
`python3 main.py`  

Verify the mail by checking sent section of your mail.  
