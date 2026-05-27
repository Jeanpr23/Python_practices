import os
import  webbrowser
import datetime
from datetime import datetime



birth_year = 2006
birth_month = 4
birth_day = 4


while True:

    def get_age(byear, bmonth, bday):
        today = datetime.today()

        age = today.year - byear

        if (today.month, today.day) < (bmonth, bday):
            age -= 1    
    
        return age

    user = input("You: ")

    if user.lower() == "hello":
        print("AI: Hello Jean Paul how I can help you today?")

    elif user.lower() == "hi":
        print("AI: Hi Jean paul how I can help you today?")


        
#----------Date and time code---------------------------------
        
        
    elif "what time is it?" in user.lower():
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        print("AI:", current_time)

    elif "what day is it?" in user.lower():
        now = datetime.datetime.now()
        current_day = now.strftime("%A")
        print("AI:", current_day)



#-----------------Opening programs or websites-----------------
    
    elif user.lower() == "open youtube":
        print ("AI: Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif user.lower() == "open google":
        print("AI: Opening Google...")
        webbrowser.open("https://www.google.com")

    elif "open roblox" in user.lower():
        print("AI: Opening Roblox...")
        os.startfile("roblox:")

    elif "open discord" in user.lower():
        print("AI: opening Discord...")
        os.startfile("discord:")
    
    elif user.lower() == "open whatsapp":
        print("AI: opening Whatsapp...")
        os.startfile("whatsapp:")

    elif user.lower() == "open chatgpt":
        print("AI: opening ChatGPT...")
        os.startfile("ChatGpt:")
    
    elif user.lower() == "open store":
        print("AI: opening Microsoft Store...")
        os.startfile("ms-windows-store:")

    elif user.lower() == "open outlook":
        print("AI: opening Outlook...")
        os.system("start outlook")

    elif user.lower() == "open edge":
        print("AI: opening Microsoft Edge...")
        os.system("start msedge")

    elif user.lower() == "open github":
        print("AI: opening GitHub...")     
        webbrowser.open("https://github.com/")


#---------Camera-command----------

    elif "open camera" in user.lower():
        print("AI: Opening Camera Sky Detection...")
        print('AI: Press Esc to close the camera')
        os.system("python cameraskydetection.py")

#--------Calculator-----------------------
   
    elif "open calculator" in user.lower():
        os.system("python calculator.py")
    

#-----------My-birthday------------------



    
    elif user.lower() == "what is my age?":
        age = get_age(birth_year, birth_month, birth_day)
        print("AI: You are:", age)


    elif user.lower() =="birthday check":
        age = get_age(birth_year, birth_month, birth_day)

        print("AI: Your current age is:", age)
        
        
#---------Extra commands-------------------------

    elif user.lower() =="who is your creator?":
        print("AI: Jean Paul is my creator")

    elif user.lower() =="what is my name?":
        print("AI: your name is Jean Paul")

    elif user.lower() == "bye":
        print("AI: Goodbye")
        break

    else:
        print("AI: I'm sorry Jean Paul, I don't understand that command.")