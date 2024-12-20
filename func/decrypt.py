import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def find_folder(folder_name, repo=os.path.expanduser("~")):    
    resultats = []
    for racine, dirs, _ in os.walk(repo):
        if folder_name in dirs:
            resultats.append(os.path.join(racine, folder_name))
    return resultats

def find_file(file_name, repertoire=os.path.expanduser("~")):
    resultats = []
    for racine, _, file in os.walk(repertoire):
        if file_name in file:
            resultats.append(os.path.join(racine, file_name))
    return resultats

def get_key (key):
  with open(key, "rb") as f:
      key = f.read()
      return key

def list_file(folder):
    try:
        if not os.path.isdir(folder):
            print(f"folder not found")
            return []

        files = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        return files

    except Exception as e:
        print(f"error")
        return []
    
def decrypt_files(files, key):
    for file in files:
        try:
            with open(file, 'rb') as f:
                content = f.read()
                iv = content[:16]
                cipher = AES.new(key, AES.MODE_CBC, iv)
                content_decrypt = unpad(cipher.decrypt(content[16:]), AES.block_size)

            if file.endswith(".enc"):
                decrypted_file = file[:-4]
            else:
                decrypted_file = file
            with open(decrypted_file, 'wb') as f:
                f.write(content_decrypt)
            file_path = file.replace("\\", "/")
            os.remove(file_path)

            print("Vos fichiers ont bien été rendu")
        
        except Exception as e:
            print(f"{e}")


def decrypt_main():
    key_file = "key.bin" 
    resultats_key_file = find_file(key_file)
    
    key = get_key(resultats_key_file[0])
    folder = "dossier_confidentiel"
    resultats_folder = find_folder(folder)
    files = list_file(resultats_folder[0])

    decrypt_files(files, key)

decrypt_main()