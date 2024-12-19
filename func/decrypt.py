import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Fonction pour chercher un dossier
def find_folder(folder_name, repo=os.path.expanduser("~")):    
    resultats = []
    
    for racine, dirs, _ in os.walk(repo):
        if folder_name in dirs:
            resultats.append(os.path.join(racine, folder_name))
    return resultats

# Fonction pour chercher un fichier
def find_file(file_name, repertoire=os.path.expanduser("~")):
    resultats = []
    for racine, _, file in os.walk(repertoire):
        if file_name in file:
            resultats.append(os.path.join(racine, file_name))
    return resultats

# On charge la clé
def get_key (key):
  with open(key, "rb") as f:
      key = f.read()
      return key

# Liste tous les fichiers dans un dossier
def list_file(folder):
    try:
        if not os.path.isdir(folder):
            print(f"folder not found")
            return []

        # Créer une liste contant les chemins de tous les fichiers du dossier
        files = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        return files

    except Exception as e:
        print(f"error")
        return []
    
# Fonction pour déchiffrer les fichiers
def decrypt_files(files, key):
    for file in files: # Parcourt les fichiers de la liste
        try:
            with open(file, 'rb') as f:
                content = f.read() # Lit le fichier
                iv = content[:16] # Récupère l'IV
                cipher = AES.new(key, AES.MODE_CBC, iv) # Initialise le déchiffrement
                content_decrypt = unpad(cipher.decrypt(content[16:]), AES.block_size) # Déchiffre le contenu

            # Ecrit le contenu déchiffré dans le fichier
            with open(file, 'wb') as f:
                f.write(content_decrypt)

            print("Vos fichiers ont bien été rendu")
        
        except Exception as e:
            print(f"{e}")


def decrypt_main():
    # Récupération de la clé
    key_file = "key.bin" 
    resultats_key_file = find_file(key_file)
    key = get_key(resultats_key_file[0])

    # Récupération du dossier
    folder = "dossier_confidentiel"
    resultats_folder = find_folder(folder)
    files = list_file(resultats_folder[0])

    # Déchiffrement des fichiers
    decrypt_files(files, key)

decrypt_main()