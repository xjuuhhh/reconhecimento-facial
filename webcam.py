import cv2

def reconhecimento():

    # Iniciando a câmera para captura
    captura = cv2.VideoCapture(0)

    # Verifica se a câmera abriu
    if not captura.isOpened():
        print("ERRO: Câmera não identificada")
        return None

    print("\nCâmera iniciada")
    print("\nPressione 'c' para tirar a foto do paciente")
    print("Pressione 'q' para cancelar\n")

    captura_foto = None

    # Visão da câmera
    while True:
        ret, frame = captura.read()

        if not ret:
            print("ERRO ao capturar imagem da câmera")
            break

        # Exibe o vídeo ao vivo na tela
        cv2.imshow("Recepção - Enquadre do paciente", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('c'):
            # Converte BGR para RGB para garantir a precisão das cores no Facenet512
            captura_foto = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            print("Foto capturada com sucesso!")
            break

        elif key == ord('q'):
            print("Operação cancelada!! Tente novamente")
            break

    # Limpeza da câmera
    captura.release()
    cv2.destroyAllWindows()

    return captura_foto
