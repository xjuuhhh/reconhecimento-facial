import cv2

def reconhecimento():

    #iniciando a camera para captura
    captura = cv2.VideoCapture(0)

    #verifica se a camera abriu
    if not captura.isOpened():
        print("ERRO: Camera não identificada")
        return None

    print("\nCamera iniciada")
    print("\nPressione 'c' para tirar a foto do paciente")
    print("Pressione 'q' para cancelar\n")

    captura_foto = None

    #visão da camera
    while True:
        ret, frame = captura.read()

        if not ret:
            print("ERRO ao capturar imagem da camera")
            break

        cv2.imshow ("Recepção - Enquadre do paciente", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('c'):
            captura_foto = frame
            print("Foto capturada com sucesso!")
            break

        elif key == ord('q'):
            print("Operação cancelada!! Tente novamente")
            break

    #limpeza camera
    captura.release()
    cv2.destroyAllWindows()

    return captura_foto

