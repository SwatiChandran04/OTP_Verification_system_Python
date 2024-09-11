import gradio as gr                                            
from validate_email_address import validate_email              
import smtplib
import random


def send_mail(enter_email_id):             #For verification of email id, generating and sending OTP
    
    global result 

    is_valid = validate_email(enter_email_id, check_format=True, check_blacklist=True, check_dns=True, dns_timeout=10)
    
    if is_valid:
        server = smtplib.SMTP('smtp.gmail.com',587)

        server.starttls()

        server.login("cp4swati@gmail.com", 'nhbq cxif rxzn sjry')

        otp = random.randint(100000,999999)

        result = str(otp)
    
        otp1 = "Your OTP is - " + result

        server.sendmail('cp4swati@gmail.com',enter_email_id,otp1)

        return "Email sent successfully"
        
    else:
        return "The email ID entered is incorrect"




def otp_verification(enter_otp):                                   # For OTP verification
    for i in range(3):
        if enter_otp == result:
            return"The entered OTP is correct"
        else:
            return "The entered OTP is incorrect, Please try again"
    return "Your attempts are over"

        
        
  
sendemail_interface = gr.Interface(fn=send_mail,inputs=["text"], outputs=["text"])   # interface for generating and sending OTP

verification_interface = gr.Interface(fn=otp_verification,inputs=["text"], outputs=["text"])      # interface for OTP verification 

demo = gr.TabbedInterface([sendemail_interface, verification_interface], ["Sending_otp", "Otp_verification"])

demo.launch()