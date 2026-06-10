
while True:    
    pergunta = input("Seu carro está carregado?(s/n)").strip().lower()
    match pergunta:
        case "s":
            print("ViVA :D")
            break
        case "n":
            print("Que pena :c")
        case _:
            print("Resposta inválida. Digite 's' ou 'n'.")
    

  