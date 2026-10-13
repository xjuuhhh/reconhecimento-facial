import cv2
import os
from deepface import DeepFace

caminho = "img/img1.jpeg"

print(f"1. O arquivo existe? {os.path.exists(caminho)}")

# Tenta carregar com OpenCV
imagem = cv2.imread(caminho)

if imagem is None:
    print("2. ERRO: O OpenCV NÃO conseguiu ler a imagem! O arquivo pode estar corrompido ou o caminho está incorreto.")
else:
    print(f"2. Sucesso! Imagem lida. Resolução: {imagem.shape}")

    # Tenta rodar o DeepFace direto só na img1
    try:
        print("3. Testando detecção de rosto no DeepFace...")
        objs = DeepFace.extract_faces(img_path=caminho, enforce_detection=False)
        print("4. Sucesso! Rosto detectado/extraído no DeepFace.")
    except Exception as e:
        print(f"4. ERRO no DeepFace: {e}")