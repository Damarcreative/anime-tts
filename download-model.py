import os
import requests

# Base URL Hugging Face
base_url = "https://huggingface.co/tensor-diffusion/anime-tts/resolve/main/anime-tts-model/"

# Daftar file .pth
files = [
    "abyssinvoker.pth", "alice.pth", "ameth.pth", "asuna.pth", "ayaka-jp.pth", "azusa.pth", "bronya.pth",
    "chisato.pth", "doom.pth", "echo.pth", "eriko.pth", "eula.pth", "hatsune.pth", "herta.pth", "hina.pth",
    "hiyori.pth", "hoshino.pth", "iori.pth", "iroha.pth", "izuna.pth", "kafka.pth", "karin.pth", "keqing.pth",
    "kokoro.pth", "kyaru.pth", "kyoka.pth", "mika.pth", "misora.pth", "miyu.pth", "momoi.pth", "nahida-jp.pth",
    "pecorine.pth", "shiroko.pth", "takina.pth", "theresa.pth", "yuni.pth", "yuuka.pth", "zenyatta.pth"
]

# Folder tujuan
folder_tujuan = "./model/"

# Membuat folder tujuan jika belum ada
if not os.path.exists(folder_tujuan):
    os.makedirs(folder_tujuan)

# Mengunduh semua file .pth
for file in files:
    url = base_url + file
    path_tujuan = os.path.join(folder_tujuan, file)

    # Mengunduh file
    response = requests.get(url, stream=True)
    with open(path_tujuan, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    print(f"File {file} berhasil diunduh ke {path_tujuan}")
