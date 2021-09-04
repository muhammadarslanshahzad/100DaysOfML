
#  ----------------------- Day 16 ----------------------
#  ----- Modules  -------------------------
#  --- Date: 01.09.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------


import smtplib    


def main():
    sender_mail = 'sender@fromdomain.com'    
    receivers_mail = ['reciever@todomain.com']    
    message = """From: From Person %s  
    To: To Person %s  
    Subject: Sending SMTP e-mail   
    This is a test e-mail message.  
    """%(sender_mail,receivers_mail)    
    try:    
        smtpObj = smtplib.SMTP('localhost')    
        smtpObj.sendmail(sender_mail, receivers_mail, message)    
        print("Successfully sent email")    
    except Exception:    
        print("Error: unable to send email")

if __name__ == "__main__":
    main()


# Sample output
# hello world
# 12
# Arslan


