import tkinter as tk
import webbrowser
from random import randint
import pygame

def link():
    webbrowser.open("https://www.binance.com/fr/price/dogecoin")

def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load("audio.mp3")
    pygame.mixer.music.play()

def show_popup():
    screen_width = 1920
    screen_height = 1080

    popups = [] #Liste des pop-up à générer

    for _ in range(42):
        play_audio()

        # On ouvre une fenêtre
        popup = tk.Tk()
        popup.wm_title("ALERT MESSAGE")

        # On ajoute un p'tit message
        message = "Nous avons chiffré votre dossier_confidentiel contenant: \n -Rapport_Sensibilite_Securite_Nucleaire.docx\n -Données_Surveillance_Risques_Nucleaires.xlsx\n Afin de récupérer vos données, vous devez payer une rançon d'une valeur de 2048 Dogecoin. \n Vous avez 24 heures avant suppression définitive de vos données."
        label = tk.Label(popup, text=message, padx=20, pady=20)
        label.pack()

        # On créer un boutton pour payer
        link_button = tk.Button(popup, text="Payer", command=link, padx=10, pady=5)
        link_button.pack()

        x = randint(0, screen_width - 300)
        y = randint(0, screen_height - 200)
        popup.geometry(f"+{x}+{y}")

        popups.append(popup)

    tk.mainloop()


show_popup()