import qrcode
import os.path
import re

def generateQrCode(text):
    """
    Genera un codice QR a partire da un testo fornito.
    
    Parametri:
    text (str): Il testo da codificare nel codice QR.
    
    """
    # Crea un oggetto QRCode con le impostazioni specificate
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Aggiunge i dati al codice QR
    qr.add_data(text)
    qr.make(fit=True)
    
    # Crea l'immagine del codice QR
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Estrae il nome del dominio dall'URL
    domain = text.replace("http://", "").replace("https://", "").split("/")[0]
    
    # Converte il nome del dominio in camelCase
    camelCaseDomain = "".join(word.capitalize() for word in domain.split("."))
    
    # Genera il nome del file QR in camelCase
    filename = f"{camelCaseDomain}.png"
    
    # Verifica se la cartella "qrCode_Generate" esiste, altrimenti la crea
    if not os.path.exists("qrCode_Generate"):
        os.makedirs("qrCode_Generate")
    
    # Salva l'immagine del codice QR nella cartella "qrCode_Genrate"
    img.save(os.path.join("qrCode_Generate", filename))
    
    print(f"Il codice QR è stato salvato come '{filename}' nella cartella 'qrCode_Generate'.")

# Chiede all'utente di inserire l'URL per il quale generare il codice QR
url = input("Inserisci l'URL per ottenere il tuo codice QR: ")

# Genera il codice QR per l'URL fornito
generateQrCode(url)
