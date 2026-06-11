import time
import random

energia_total_local= 0.0
bateria_capacidade_kWh = 50.0
lista_carregadores = []

def mostrar_carregadores():
    if len(lista_carregadores) == 0:
        print("Nenhum carregador configurado! Por favor, adicione carregadores para visualizar.")
        return
    
    print("---------------------------------------------------------------------")
    for c in lista_carregadores:
        bateria_text = f"Bateria: {int(round(c['bateria']))}%"
        print(f"Carregador {c['id']:<2} | Status: {c['status']:<9} | {bateria_text:<13} | Consumo: {c['consumo']:<5.2f} kW")
    print("---------------------------------------------------------------------")

def add_carregadores():
    lista_carregadores.clear()  
    num_carregadores = int(input("Quantos carregadores deseja? "))

    while num_carregadores <= 0 or num_carregadores > 999:
        print("Número inválido! Por favor, insira um valor inteiro ntre 1 e 999.")
        num_carregadores = int(input("Quantos carregadores deseja? "))

    for i in range(num_carregadores):
        lista_carregadores.append({"id": i + 1, "status": "Disponível", "consumo": 0.0, "bateria": 0})

    print("\n---------------------------------------------------------------------")
    print("Carregadores configurados com sucesso!")    
    mostrar_carregadores()

def configurar_energia():
    global energia_total_local
    print(f"Energia total atual é {energia_total_local} kW.")
    nova_energia = float(input(f"Digite o novo limite: "))
    
    while nova_energia <= 0:
        nova_energia = float(input("Valor inválido! Por favor, insira um valor maior que zero: "))
                
    energia_total_local = nova_energia
    print(f"Nova energia total disponível: {energia_total_local} kW\n")

def exibir_status():
    print(f"Energia Total Disponível: {energia_total_local} kW")
    
    mostrar_carregadores()

def simular_carregamento():
    minuto = 0
    todos_terminaram = False

    if len(lista_carregadores) == 0:
        print("Nenhum carregador configurado! Por favor, adicione carregadores antes de iniciar a simulação.")
        return

    while todos_terminaram == False:
        minuto += 1
        print(f"\n--- Tempo de Simulação: {minuto} min ---")

        p = min(0.05 * len(lista_carregadores), 0.75)
        if random.random() < p:
            disponiveis = [c for c in lista_carregadores if c["status"] == "Disponível"]
            if disponiveis:
                escolhido = random.choice(disponiveis)
                escolhido["status"] = "Carregando"
                print(f"Carregador {escolhido['id']} iniciou o carregamento.")
        
        ativos = 0
            
        for c in lista_carregadores:
            if c["status"] == "Carregando":
                ativos += 1

        for c in lista_carregadores:
            if c["status"] == "Carregando" and ativos > 0:
                c["consumo"] = energia_total_local/ativos
                
                energia_entregue_kwh = c["consumo"] * (1/60)
                aumento_percentual = (energia_entregue_kwh / bateria_capacidade_kWh) * 100
                c["bateria"] += aumento_percentual

                if c["bateria"] >= 100:
                    c["bateria"] = 100
                    c["status"] = "Concluído "
                    c["consumo"] = 0.0
                    
            elif c["status"] != "Carregando" and c["status"] != "Concluído ":
                c["consumo"] = 0.0

        mostrar_carregadores()

        todos_terminaram = all(c["bateria"] >= 100 for c in lista_carregadores)

        if todos_terminaram:
            print("\nTodos os veículos foram carregados com sucesso!")
            for c in lista_carregadores:
                c["status"] = "Disponível"
                c["consumo"] = 0.0
                c["bateria"] = 0
            break

        time.sleep(0.5)

while True:
    print("\n========================================================")
    print("Sistema Integrado de Carregadores GoodWee - Versão Alpha")
    print("========================================================")
    print("(1) Configurar Parâmetros")
    print("(2) Visualizar Status")
    print("(3) Executar Recarga")
    print("(0) Sair")
    print("========================================================")

    opcao = int(input("Escolha uma opção: "))
    print()

    match opcao:
        case 1:
            print("=== Configurar Parâmetros ===")
            add_carregadores()
            configurar_energia()
            
        case 2:
            print("=== Visualizar Status ===")
            exibir_status()

        case 3:
            print("=== Iniciando Simulação de Recarga Dinâmica ===")
            simular_carregamento()

        case 0:
            print("Saindo do sistema...")
            break
        case _:
            print("Opção inválida! Tente novamente.")
