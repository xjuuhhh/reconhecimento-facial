from deepface import DeepFace
from webcam import reconhecimento

# Colocando as fotos em variáveis
foto_cadastro = "img/img9.jpg"
foto_validar = reconhecimento()

if foto_validar is None:
    print("\nProcesso interrompido: Nenhuma foto foi capturada!")
else:
    print("\nBuscando usuário no banco de fotos cadastradas..")

    try:
        # Comparando as fotos com modelo de ALTA PRECISÃO (Facenet512)
        resultado = DeepFace.verify(
            img1_path=foto_cadastro, 
            img2_path=foto_validar,
            model_name="Facenet512",      # Troca o VGG-Face pelo Facenet512 (Muito mais preciso)
            distance_metric="cosine",     # Métrica ideal para calcular a diferença biométrica
            enforce_detection=True        # Exige que haja um rosto nítido
        )

        # Imprime a distância biométrica exata no terminal para você acompanhar a precisão
        distancia = resultado["distance"]
        limiar = resultado["threshold"]
        print(f"Distância calculada: {distancia:.4f} (Limiar máximo permitido: {limiar:.4f})")

        # Resultado da verificação
        if resultado["verified"]:
            print("\nCadastro encontrado")
            print("Status: LIBERADO\n")
        else:
            print("\nCadastro não encontrado")
            print("Status: NEGADO\n")

    except Exception as erro:
        # Se não encontrar um rosto evidente na câmera
        print(f"\nErro no processamento da imagem: {erro}\n")