import customtkinter as ctk
import tkinter as tk
import random as rnd

def Settings():
    global Players_amount_string,Players_int,language
    def Back():
        Start_Button.place(x=75,y=200)
        Settings_Button.place(x=75, y=400)
        Quit_Button.place(x=75, y=600)
        Back_button.place_forget()
        Players_amount_button.place_forget()
        Players_amount_Label.place_forget()
        Players_amount_button_Down.place_forget()
        Players_amount_button_Up.place_forget()
        Save_Button.place_forget()
        Languagee_Label.place_forget()
        Language_Label.place_forget()
        Language_Button_next.place_forget()
        Language_Button_Before.place_forget()
        Customize_Label.place_forget()
        Customize_Button.place_forget()

    def Players_AMOUNT_Up():
        global Players_int
        if Players_int == 4:
            Players_int = 4
            Players_amount_string.set(Players_int)
            Players_amount_button.configure(textvariable=Players_amount_string)
        elif Players_int <4:
            Players_int += 1
            Players_amount_string.set(Players_int)
            Players_amount_button.configure(textvariable=Players_amount_string)

    def Players_AMOUNT_Down():
        global Players_int
        if Players_int == 2:
            Players_int = 2
            Players_amount_string.set(Players_int)
            Players_amount_button.configure(textvariable=Players_amount_string)
        elif Players_int >2:
            Players_int -= 1
            Players_amount_string.set(Players_int)
            Players_amount_button.configure(textvariable=Players_amount_string)

    def Save():
        with open("Data/Settings/Settings","w") as Plik:
            Plik.truncate(0)
            Plik.write(f'{str(Players_int)}\n')
            Plik.write(f'{str(language)} \n')
            Plik.write(f'{str(Custom_bg)} \n')

    def language_change_up():
        global language
        def Set_Pl():
            Languagee_Label.configure(text="Język:")
            Languagee_Label.place(x=280, y=10)

        def Set_Eng():
            Languagee_Label.configure(text="Language:")
            Languagee_Label.place(x=250, y=10)

        if language == 1 :
            language = 2
            Language_Label.configure(text="Pl",width=70)
            Set_Pl()

        elif language == 2 :
            language = 1
            Language_Label.configure(text="Eng",width=20)
            Set_Eng()
    def language_change_down():
        global language
        def Set_Pl():
            Languagee_Label.configure(text="Język:")
            Languagee_Label.place(x=280, y=10)

        def Set_Eng():
            Languagee_Label.configure(text="Language:")
            Languagee_Label.place(x=250, y=10)

        if language == 1:
            language = 2
            Language_Label.configure(text="Pl", width=70)
            Set_Pl()
        elif language == 2:
            language = 1
            Language_Label.configure(text="Eng", width=20)
            Set_Eng()

    def Customize():
        global Custom_bg
        if Custom_bg == 1:
            Background_label.configure(image=Orginal_background)
            Custom_bg = 0
            Customize_Button.configure(text=" ")
        elif Custom_bg == 0:
            Background_label.configure(image=Custom_Background)
            Custom_bg = 1
            Customize_Button.configure(text="✔")

    Start_Button.place_forget()
    Settings_Button.place_forget()
    Quit_Button.place_forget()
    Back_button.configure(command=Back)
    Back_button.place(x=0,y=0)
    Players_amount_Label.place(x=100,y=10)
    Players_amount_button.place(x=150,y=60)
    Players_amount_button_Up.place(x=175,y=60)
    Players_amount_button_Up.configure(command=Players_AMOUNT_Up)
    Players_amount_button_Down.place(x=135,y=60)
    Players_amount_button_Down.configure(command=Players_AMOUNT_Down)
    Save_Button.place(x=860,y=860)
    Save_Button.configure(command=Save)
    if language == 1:
        Languagee_Label.place(x=250,y=10)
    elif language == 2:
        Languagee_Label.place(x=280, y=10)
    Language_Label.place(x=300,y=60)
    Language_Button_next.place(x=365,y=60)
    Language_Button_next.configure(command=language_change_up)
    Language_Button_Before.place(x=280,y=60)
    Language_Button_Before.configure(command=language_change_down)
    Customize_Label.place(x=500,y=10)
    Customize_Button.place(x=550,y=60)
    Customize_Button.configure(command=Customize)
def Start():
    global Players_int
    if Players_int == 2:
        def Dice():
            def update():
                nonlocal Diced1,Diced2
                if Diced1 == 1:
                    dice_Button1.configure(image=dice_roll_1)
                elif Diced1 == 2:
                    dice_Button1.configure(image=dice_roll_2)
                elif Diced1 == 3:
                    dice_Button1.configure(image=dice_roll_3)
                elif Diced1 == 4:
                    dice_Button1.configure(image=dice_roll_4)
                elif Diced1 == 5:
                    dice_Button1.configure(image=dice_roll_5)
                elif Diced1 == 6:
                    dice_Button1.configure(image=dice_roll_6)
                if Diced2 == 1:
                    dice_Button2.configure(image=dice_roll_1)
                elif Diced2 == 2:
                    dice_Button2.configure(image=dice_roll_2)
                elif Diced2 == 3:
                    dice_Button2.configure(image=dice_roll_3)
                elif Diced2 == 4:
                    dice_Button2.configure(image=dice_roll_4)
                elif Diced2 == 5:
                    dice_Button2.configure(image=dice_roll_5)
                elif Diced2 == 6:
                    dice_Button2.configure(image=dice_roll_6)
            global Actual_Pole_1,Actual_Pole_2,Actual_Pole_3,Actual_Pole_4,Player,Actual_Player
            Diced1 = rnd.randint(1,6)
            print(Diced1)
            Diced2 = rnd.randint(1,6)
            print(Diced2)
            Poles = Diced1 + Diced2
            update()
            if Player == 1:
                Actual_Player = 1
                Actual_Pole_1 += Poles
                if Actual_Pole_1 >= 38:
                    Actual_Pole_1 = Actual_Pole_1 - 38
                    if Actual_Pole_1 == 0:
                        Player_1.place(x=1499, y=812)
                    elif Actual_Pole_1 == 1:
                        Player_1.place(x=1409, y=812)
                    elif Actual_Pole_1 == 2:
                        Player_1.place(x=1320, y=812)
                    elif Actual_Pole_1 == 3:
                        Player_1.place(x=1230, y=812)
                    elif Actual_Pole_1 == 4:
                        Player_1.place(x=1140, y=812)
                    elif Actual_Pole_1 == 5:
                        Player_1.place(x=1054, y=812)
                    elif Actual_Pole_1 == 6:
                        Player_1.place(x=964, y=812)
                    elif Actual_Pole_1 == 7:
                        Player_1.place(x=874, y=812)
                    elif Actual_Pole_1 == 8:
                        Player_1.place(x=785, y=812)
                    elif Actual_Pole_1 == 9:
                        Player_1.place(x=696, y=812)
                    elif Actual_Pole_1 == 10:
                        Player_1.place(x=606, y=812)
                    elif Actual_Pole_1 == 11:
                        Player_1.place(x=517, y=812)
                    elif Actual_Pole_1 == 12:
                        Player_1.place(x=429, y=812)
                    elif Actual_Pole_1 == 13:
                        Player_1.place(x=318, y=812)
                    elif Actual_Pole_1 == 14:
                        Player_1.place(x=318, y=705)
                    elif Actual_Pole_1 == 15:
                        Player_1.place(x=318, y=596)
                    elif Actual_Pole_1 == 16:
                        Player_1.place(x=318, y=491)
                    elif Actual_Pole_1 == 17:
                        Player_1.place(x=318, y=386)
                    elif Actual_Pole_1 == 18:
                        Player_1.place(x=318, y=287)
                    elif Actual_Pole_1 == 19:
                        Player_1.place(x=318, y=158)
                    elif Actual_Pole_1 == 20:
                        Player_1.place(x=429, y=158)
                    elif Actual_Pole_1 == 21:
                        Player_1.place(x=517, y=158)
                    elif Actual_Pole_1 == 22:
                        Player_1.place(x=606, y=158)
                    elif Actual_Pole_1 == 23:
                        Player_1.place(x=696, y=158)
                    elif Actual_Pole_1 == 24:
                        Player_1.place(x=785, y=158)
                    elif Actual_Pole_1 == 25:
                        Player_1.place(x=874, y=158)
                    elif Actual_Pole_1 == 26:
                        Player_1.place(x=964, y=158)
                    elif Actual_Pole_1 == 27:
                        Player_1.place(x=1054, y=158)
                    elif Actual_Pole_1 == 28:
                        Player_1.place(x=1140, y=158)
                    elif Actual_Pole_1 == 29:
                        Player_1.place(x=1230, y=158)
                    elif Actual_Pole_1 == 30:
                        Player_1.place(x=1320, y=158)
                    elif Actual_Pole_1 == 31:
                        Player_1.place(x=1409, y=158)
                    elif Actual_Pole_1 == 32:
                        Player_1.place(x=1499, y=158)
                    elif Actual_Pole_1 == 33:
                        Player_1.place(x=1499, y=287)
                    elif Actual_Pole_1 == 34:
                        Player_1.place(x=1499, y=386)
                    elif Actual_Pole_1 == 35:
                        Player_1.place(x=1499, y=491)
                    elif Actual_Pole_1 == 36:
                        Player_1.place(x=1499, y=596)
                    elif Actual_Pole_1 == 37:
                        Player_1.place(x=1499, y=705)
                    elif Actual_Pole_1 == 38:
                        Player_1.place(x=1499, y=812)

                elif Actual_Pole_1 == 0:
                    Player_1.place(x=1499,y=812)
                elif Actual_Pole_1 == 1:
                    Player_1.place(x=1409, y=812)
                elif Actual_Pole_1 == 2:
                    Player_1.place(x=1320,y=812)
                elif Actual_Pole_1 == 3:
                    Player_1.place(x=1230, y=812)
                elif Actual_Pole_1 == 4:
                    Player_1.place(x=1140, y=812)
                elif Actual_Pole_1 == 5:
                    Player_1.place(x=1054, y=812)
                elif Actual_Pole_1 == 6:
                    Player_1.place(x=964, y=812)
                elif Actual_Pole_1 == 7:
                    Player_1.place(x=874, y=812)
                elif Actual_Pole_1 == 8:
                    Player_1.place(x=785, y=812)
                elif Actual_Pole_1 == 9:
                    Player_1.place(x=696,y=812)
                elif Actual_Pole_1 == 10:
                    Player_1.place(x=606, y=812)
                elif Actual_Pole_1 == 11:
                    Player_1.place(x=517, y=812)
                elif Actual_Pole_1 == 12:
                    Player_1.place(x=429, y=812)
                elif Actual_Pole_1 == 13:
                    Player_1.place(x=318, y=812)
                elif Actual_Pole_1 == 14:
                    Player_1.place(x=318, y=705)
                elif Actual_Pole_1 == 15:
                    Player_1.place(x=318, y=596)
                elif Actual_Pole_1 == 16:
                    Player_1.place(x=318, y=491)
                elif Actual_Pole_1 == 17:
                    Player_1.place(x=318, y=386)
                elif Actual_Pole_1 == 18:
                    Player_1.place(x=318, y=287)
                elif Actual_Pole_1 == 19:
                    Player_1.place(x=318, y=162)
                elif Actual_Pole_1 == 20:
                    Player_1.place(x=429, y=162)
                elif Actual_Pole_1 == 21:
                    Player_1.place(x=517, y=162)
                elif Actual_Pole_1 == 22:
                    Player_1.place(x=606, y=162)
                elif Actual_Pole_1 == 23:
                    Player_1.place(x=696, y=162)
                elif Actual_Pole_1 == 24:
                    Player_1.place(x=785, y=162)
                elif Actual_Pole_1 == 25:
                    Player_1.place(x=874, y=162)
                elif Actual_Pole_1 == 26:
                    Player_1.place(x=964, y=162)
                elif Actual_Pole_1 == 27:
                    Player_1.place(x=1054, y=162)
                elif Actual_Pole_1 == 28:
                    Player_1.place(x=1140, y=162)
                elif Actual_Pole_1 == 29:
                    Player_1.place(x=1230, y=162)
                elif Actual_Pole_1 == 30:
                    Player_1.place(x=1320, y=162)
                elif Actual_Pole_1 == 31:
                    Player_1.place(x=1409, y=162)
                elif Actual_Pole_1 == 32:
                    Player_1.place(x=1499, y=162)
                elif Actual_Pole_1 == 33:
                    Player_1.place(x=1499, y=287)
                elif Actual_Pole_1 == 34:
                    Player_1.place(x=1499, y=386)
                elif Actual_Pole_1 == 35:
                    Player_1.place(x=1499, y=491)
                elif Actual_Pole_1 == 36:
                    Player_1.place(x=1499, y=596)
                elif Actual_Pole_1 == 37:
                    Player_1.place(x=1499, y=705)
                elif Actual_Pole_1 == 38:
                    Player_1.place(x=1499, y=812)
                Player = 2

            elif Player == 2:
                Actual_Player = 2
                Actual_Pole_2 += Poles
                if Actual_Pole_2 >= 38:
                    Actual_Pole_2 = Actual_Pole_2 - 38
                    if Actual_Pole_2 == 0:
                        Player_2.place(x=1499, y=812)
                    elif Actual_Pole_2 == 1:
                        Player_2.place(x=1409, y=812)
                    elif Actual_Pole_2 == 2:
                        Player_2.place(x=1320, y=812)
                    elif Actual_Pole_2 == 3:
                        Player_2.place(x=1230, y=812)
                    elif Actual_Pole_2 == 4:
                        Player_2.place(x=1140, y=812)
                    elif Actual_Pole_2 == 5:
                        Player_2.place(x=1054, y=812)
                    elif Actual_Pole_2 == 6:
                        Player_2.place(x=964, y=812)
                    elif Actual_Pole_2 == 7:
                        Player_2.place(x=874, y=812)
                    elif Actual_Pole_2 == 8:
                        Player_2.place(x=785, y=812)
                    elif Actual_Pole_2 == 9:
                        Player_2.place(x=696, y=812)
                    elif Actual_Pole_2 == 10:
                        Player_2.place(x=606, y=812)
                    elif Actual_Pole_2 == 11:
                        Player_2.place(x=517, y=812)
                    elif Actual_Pole_2 == 12:
                        Player_2.place(x=429, y=812)
                    elif Actual_Pole_2 == 13:
                        Player_2.place(x=318, y=812)
                    elif Actual_Pole_2 == 14:
                        Player_2.place(x=318, y=705)
                    elif Actual_Pole_2 == 15:
                        Player_2.place(x=318, y=596)
                    elif Actual_Pole_2 == 16:
                        Player_2.place(x=318, y=491)
                    elif Actual_Pole_2 == 17:
                        Player_2.place(x=318, y=386)
                    elif Actual_Pole_2 == 18:
                        Player_2.place(x=318, y=287)
                    elif Actual_Pole_2 == 19:
                        Player_2.place(x=318, y=162)
                    elif Actual_Pole_2 == 20:
                        Player_2.place(x=429, y=162)
                    elif Actual_Pole_2 == 21:
                        Player_2.place(x=517, y=162)
                    elif Actual_Pole_2 == 22:
                        Player_2.place(x=606, y=162)
                    elif Actual_Pole_2 == 23:
                        Player_2.place(x=696, y=162)
                    elif Actual_Pole_2 == 24:
                        Player_2.place(x=785, y=162)
                    elif Actual_Pole_2 == 25:
                        Player_2.place(x=874, y=162)
                    elif Actual_Pole_2 == 26:
                        Player_2.place(x=964, y=162)
                    elif Actual_Pole_2 == 27:
                        Player_2.place(x=1054, y=162)
                    elif Actual_Pole_2 == 28:
                        Player_2.place(x=1140, y=162)
                    elif Actual_Pole_2 == 29:
                        Player_2.place(x=1230, y=162)
                    elif Actual_Pole_2 == 30:
                        Player_2.place(x=1320, y=162)
                    elif Actual_Pole_2 == 31:
                        Player_2.place(x=1409, y=162)
                    elif Actual_Pole_2 == 32:
                        Player_2.place(x=1499, y=162)
                    elif Actual_Pole_2 == 33:
                        Player_2.place(x=1499, y=287)
                    elif Actual_Pole_2 == 34:
                        Player_2.place(x=1499, y=386)
                    elif Actual_Pole_2 == 35:
                        Player_2.place(x=1499, y=491)
                    elif Actual_Pole_2 == 36:
                        Player_2.place(x=1499, y=596)
                    elif Actual_Pole_2 == 37:
                        Player_2.place(x=1499, y=705)
                    elif Actual_Pole_2 == 38:
                        Player_2.place(x=1499, y=812)

                elif Actual_Pole_2 == 0:
                    Player_2.place(x=1499, y=812)
                elif Actual_Pole_2 == 1:
                    Player_2.place(x=1409, y=812)
                elif Actual_Pole_2 == 2:
                    Player_2.place(x=1320, y=812)
                elif Actual_Pole_2 == 3:
                    Player_2.place(x=1230, y=812)
                elif Actual_Pole_2 == 4:
                    Player_2.place(x=1140, y=812)
                elif Actual_Pole_2 == 5:
                    Player_2.place(x=1054, y=812)
                elif Actual_Pole_2 == 6:
                    Player_2.place(x=964, y=812)
                elif Actual_Pole_2 == 7:
                    Player_2.place(x=874, y=812)
                elif Actual_Pole_2 == 8:
                    Player_2.place(x=785, y=812)
                elif Actual_Pole_2 == 9:
                    Player_2.place(x=696, y=812)
                elif Actual_Pole_2 == 10:
                    Player_2.place(x=606, y=812)
                elif Actual_Pole_2 == 11:
                    Player_2.place(x=517, y=812)
                elif Actual_Pole_2 == 12:
                    Player_2.place(x=429, y=812)
                elif Actual_Pole_2 == 13:
                    Player_2.place(x=318, y=812)
                elif Actual_Pole_2 == 14:
                    Player_2.place(x=318, y=705)
                elif Actual_Pole_2 == 15:
                    Player_2.place(x=318, y=596)
                elif Actual_Pole_2 == 16:
                    Player_2.place(x=318, y=491)
                elif Actual_Pole_2 == 17:
                    Player_2.place(x=318, y=386)
                elif Actual_Pole_2 == 18:
                    Player_2.place(x=318, y=287)
                elif Actual_Pole_2 == 19:
                    Player_2.place(x=318, y=162)
                elif Actual_Pole_2 == 20:
                    Player_2.place(x=429, y=162)
                elif Actual_Pole_2 == 21:
                    Player_2.place(x=517, y=162)
                elif Actual_Pole_2 == 22:
                    Player_2.place(x=606, y=162)
                elif Actual_Pole_2 == 23:
                    Player_2.place(x=696, y=162)
                elif Actual_Pole_2 == 24:
                    Player_2.place(x=785, y=162)
                elif Actual_Pole_2 == 25:
                    Player_2.place(x=874, y=162)
                elif Actual_Pole_2 == 26:
                    Player_2.place(x=964, y=162)
                elif Actual_Pole_2 == 27:
                    Player_2.place(x=1054, y=162)
                elif Actual_Pole_2 == 28:
                    Player_2.place(x=1140, y=162)
                elif Actual_Pole_2 == 29:
                    Player_2.place(x=1230, y=162)
                elif Actual_Pole_2 == 30:
                    Player_2.place(x=1320, y=162)
                elif Actual_Pole_2 == 31:
                    Player_2.place(x=1409, y=162)
                elif Actual_Pole_2 == 32:
                    Player_2.place(x=1499, y=162)
                elif Actual_Pole_2 == 33:
                    Player_2.place(x=1499, y=287)
                elif Actual_Pole_2 == 34:
                    Player_2.place(x=1499, y=386)
                elif Actual_Pole_2 == 35:
                    Player_2.place(x=1499, y=491)
                elif Actual_Pole_2 == 36:
                    Player_2.place(x=1499, y=596)
                elif Actual_Pole_2 == 37:
                    Player_2.place(x=1499, y=705)
                elif Actual_Pole_2 == 38:
                    Player_2.place(x=1499, y=812)
                Player = 1

        Background_label.place(x=0,y=0)
        Player_1.place(x=1499,y=812)
        Player_2.place(x=1499,y=812)
        dice_Button1.place(x=860,y=470)
        dice_Button1.configure(command=Dice)
        dice_Button2.place(x=970, y=470)
        dice_Button2.configure(command=Dice)
        Menu_Buy_See.place(x=0,y=142)
        Menu_2.place(x=1620,y=142)
        Actual_Pole_Name.place(x=1700,y=200)
    elif Players_int == 3:
        Background_label.place(x=0, y=0)
        Player_1.place(x=1499,y=812)
        Player_2.place(x=1499,y=812)
        Player_3.place(x=1499,y=812)
    elif Players_int == 4:
        Background_label.place(x=0, y=0)
        Player_1.place(x=1499,y=812)
        Player_2.place(x=1499,y=812)
        Player_3.place(x=1499,y=812)
        Player_4.place(x=1499,y=812)

def Quit():
    root.quit()

def Set():
    global language,Custom_bg

    def Set_Pl():
        Languagee_Label.configure(text="Język:")

    def Set_Eng():
        Languagee_Label.configure(text="Language:")

    if language == 2:
        language = 2
        Language_Label.configure(text="Pl", width=70)
        Set_Pl()
    elif language == 1:
        language = 1
        Language_Label.configure(text="Eng", width=20)
        Set_Eng()

    if Custom_bg == 0:
        Background_label.configure(image=Orginal_background)
        Customize_Button.configure(text=" ")
    elif Custom_bg == 1:
        Background_label.configure(image=Custom_Background)
        Customize_Button.configure(text="✔")

root = ctk.CTk()
root.geometry("1920x1080")
root.title("Misiowy Biznes")

with open("Data/Settings/Settings") as Setts:
    Players = Setts.readline().strip()
    Players_int = int(Players)

    language = Setts.readline().strip()
    language = int(language)

    Custom_bg = Setts.readline().strip()
    Custom_bg = int(Custom_bg)

Start_Button = ctk.CTkButton(root,text="Start",font=("Font1",40),fg_color="#434343",width=300,height=150,hover_color="#565656",command=Start)
Start_Button.place(x=75,y=200)

Settings_Button = ctk.CTkButton(root,text="Settings",font=("Font1",40),fg_color="#434343",width=300,height=150,command=Settings,hover_color="#565656")
Settings_Button.place(x=75,y=400)

Quit_Button = ctk.CTkButton(root,text="Quit",font=("Font1",40),fg_color="#434343",width=300,height=150,hover_color="#565656",command=Quit)
Quit_Button.place(x=75,y=600)

Back_button = ctk.CTkButton(root,text="<-",font=("Font1",40),fg_color="#242424",hover_color="#434343",width=20)

Players_amount_string = tk.IntVar()
Players_amount_string.set(Players_int)

Players_amount_Label = ctk.CTkLabel(root,text="Players:",font=("Font1",40))

Players_amount_button = ctk.CTkEntry(root,textvariable=Players_amount_string,width=20,height=40,font=("Font1",40),border_width=0,fg_color="#434343",bg_color="#434343")

Players_amount_button_Up = ctk.CTkButton(root,text="⮕",border_width=0,width=25,height=48,fg_color="#434343",hover_color="#565656")

Players_amount_button_Down = ctk.CTkButton(root,text="⬅",border_width=0,width=25,height=48,fg_color="#434343",hover_color="#565656")

Save_Button = ctk.CTkButton(root,text="Save",width=200,height=100,fg_color="#434343",hover_color="#565656",font=("Font1",40))

Players_amount_button.lift()

Languagee_Label = ctk.CTkLabel(root,text="",font=("Font1",40))

Language_Label = ctk.CTkLabel(root,text="Eng",width=20,height=48,font=("Font1",40),fg_color="#434343",bg_color="#434343")

Language_Button_next = ctk.CTkButton(root,text="⮕",width=25,height=48,fg_color="#434343",hover_color="#565656")

Language_Button_Before = ctk.CTkButton(root,text="⬅",width=25,height=48,fg_color="#434343",hover_color="#565656")

Language_Label.lift()

Customize_Label = ctk.CTkLabel(root,text="Custom:",font=("Font1",40))

Customize_Button = ctk.CTkButton(root,text=" ",fg_color="#434343",hover_color="#565656",font=("Font1",40),width=48,height=48)

Orginal_background = tk.PhotoImage(file="Data/Textures/Background.png")

Custom_Background = tk.PhotoImage(file="Data/Customize/Replace.png")

Background_label = tk.Label(root,image=Orginal_background,borderwidth=0)

Player = 1

Actual_Player = 1

Actual_Pole_1 = 0

Player_1_image = tk.PhotoImage(file="Data/Textures/Pawn/Pawn1.png")

Player_1 = tk.Label(root,image=Player_1_image,font=("Font1",40),bg="#7b7b7b")

Actual_Pole_2 = 0

Player_2_image = tk.PhotoImage(file="Data/Textures/Pawn/Pawn4.png")

Player_2 = tk.Label(root,image=Player_2_image,font=("Font1",40),bg="#7b7b7b")

Actual_Pole_3 = 0

Player_3_image = tk.PhotoImage(file="Data/Textures/Pawn/Pawn2.png")

Player_3 = tk.Label(root,image=Player_3_image,font=("Font1",40),bg="#7b7b7b")

Actual_Pole_4 = 0

Player_4_image = tk.PhotoImage(file="Data/Textures/Pawn/Pawn5.png")

Player_4 = tk.Label(root,image=Player_4_image,font=("Font1",40),bg="#7b7b7b")

dice_image = tk.PhotoImage(file="Data/Textures/Dice.png")

dice_Button1 = tk.Button(root,image=dice_image,borderwidth=0)

dice_Button2 = tk.Button(root,image=dice_image,borderwidth=0)

dice_roll_1 = tk.PhotoImage(file="Data/Textures/Dice/1.png")

dice_roll_2 = tk.PhotoImage(file="Data/Textures/Dice/2.png")

dice_roll_3 = tk.PhotoImage(file="Data/Textures/Dice/3.png")

dice_roll_4 = tk.PhotoImage(file="Data/Textures/Dice/4.png")

dice_roll_5 = tk.PhotoImage(file="Data/Textures/Dice/5.png")

dice_roll_6 = tk.PhotoImage(file="Data/Textures/Dice/6.png")

Set()

Menu_Buy_See_Image = tk.PhotoImage(file="Data/Textures/Menu.png")

Menu_Buy_See = tk.Label(root,image=Menu_Buy_See_Image,borderwidth=0)

Menu_2_image = tk.PhotoImage(file="Data/Textures/Menu.png",width=400)

Menu_2 = tk.Label(root,image=Menu_Buy_See_Image,borderwidth=0)
Menu_2.lower(Player_1)

Actual_Pole_Name = tk.Label(root,text="Start",borderwidth=0,font=("Font1",40))

root.mainloop()