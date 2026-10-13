from deepface import DeepFace

#colocando as fotos em variaveis
foto_cadastro = "img/img1.jpeg"
foto_valida = "img/img2.jpeg"  #mudar para img 2 se quiser liberae e para img 3 se quiser negar

print ("\nBuscando usuário no banco de fotos cadastradas..")

try:
    #comparando as fotos
    resultado = DeepFace.verify( img1_path=foto_cadastro, img2_path=foto_valida)

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