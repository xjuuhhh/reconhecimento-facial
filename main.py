from deepface import DeepFace
from webcam import reconhecimento

#colocando as fotos em variaveis
foto_cadastro = "img/img1.jpeg"
foto_validar = reconhecimento()

if foto_validar is None:
    print("\nProcesso interrompido: Nenhuma foto foi capturada!")
else:
    print ("\nBuscando usuário no banco de fotos cadastradas..")

    try:
        #comparando as fotos
        resultado = DeepFace.verify( img1_path=foto_cadastro, img2_path=foto_validar)

        #resultado
        if resultado["verified"]:
            print ("\nCadastro encontrado")
            print ("Status: LIBERADO\n")
        else:
            print("\nCadastro não encontrado")
            print("Status: NEGADO\n")

    except Exception as erro:
        #se ocorrer algum erro nas imagens
        print(f"\nErro nas imagens: {erro}\n")