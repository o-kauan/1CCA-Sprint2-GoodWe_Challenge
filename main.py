import time

energia_total_local= 44.0  # Limite de energia do shopping (kW)
lista_carregadores = []

## 1. Configurar parâmetros:
# - energia total disponível, consumo de energia, status de cada carregador, bateria
lista_carregadores.append({"id": 1, "status": "Disponível", "consumo": 0.0, "bateria": 0})
lista_carregadores.append({"id": 2, "status": "Disponível", "consumo": 0.0, "bateria": 0})
lista_carregadores.append({"id": 3, "status": "Disponível", "consumo": 0.0, "bateria": 0})


## 2. Visualizar status:

def configurar_parametros():
    global energia_total_local
    print("--- Configuração do Sistema ---")
    nova_energia = float(input(f"Energia total atual é {energia_total_local}kw. Digite o novo limite: "))
    energia_total_local= nova_energia
    print(f"✅ Nova energia total disponível: {energia_total_local}kW\n")


def exibir_status():
    print("\n================ STATUS ================")
    consumo_atual_total = 0.0

    for c in lista_carregadores:
        print(
            f"Carregador {c['id']} | Status: {c['status']:<25} | Bateria: {c['bateria']}% | Consumo: {c['consumo']} kW")
        consumo_atual_total += c["consumo"]

    print("--------------------------------------------------")
    print(f"⚡ Energia Total do Shopping: {energia_total_local}kW")
    print(f"Consumo Atual dos Eletropostos: {consumo_atual_total} kW")

    if consumo_atual_total > energia_total_local:
        print("ALERTA: Consumo atingiu nível crítico! Reduzindo carga.")
    print("==================================================\n")


def simular_carregamento():
    print("=== Iniciando Simulação de Recarga Dinâmica ===")
    print("Três carros vão entrar na simulação com intervalos de tempo de 15 segundos.\n")

    for c in lista_carregadores:
        c["bateria"] = 0
        c["status"] = "Aguardando Carro"
        c["consumo"] = 0.0

    for segundo in range(1, 60):
        print(f"\n--- Tempo de Simulação: {segundo}s ---")

        if segundo >= 1 and lista_carregadores[0]["bateria"] < 100:
            lista_carregadores[0]["status"] = "Carregando"
        if segundo >= 15 and lista_carregadores[1]["bateria"] < 100:
            lista_carregadores[1]["status"] = "Carregando"
        if segundo >= 30 and lista_carregadores[2]["bateria"] < 100:
            lista_carregadores[2]["status"] = "Carregando"
        ativos = 0
        for c in lista_carregadores:
            if c["status"] == "Carregando":
                ativos += 1

        for c in lista_carregadores:
            if c["status"] == "Carregando" and ativos > 0:
                c["consumo"] = energia_total_local/ativos
                c["bateria"] += int(c["consumo"] * 0.1)

                if c["bateria"] >= 100:
                    c["bateria"] = 100
                    c["status"] = "Concluido (Taxa Ocupação)"
                    c["consumo"] = 0.0
                    print(f"⚠️ Carregador {c['id']} chegou a 100%! Energia cortada e redistribuída.")
            elif c["status"] != "Carregando" and c["status"] != "Concluido (Taxa Ocupação)":
                c["consumo"] = 0.0

        for c in lista_carregadores:
            print(f"[Posto {c['id']}] Status: {c['status']} | Bateria: {c['bateria']}% | Potência: {c['consumo']:.1f} kW")

        todos_terminaram = True
        for c in lista_carregadores:
            if c["bateria"] < 100:
                todos_terminaram = False

        if todos_terminaram:
            print("\nTodos os veículos foram carregados com sucesso!")
            break

        time.sleep(1)


while True:
    print("========================================================")
    print("Sistema Integrado de Carregadores GoodWee - Versão Alpha")
    print("========================================================")
    print("(1) Configurar parâmetros")
    print("(2) Visualizar status")
    print("(3) Simular situações (Executar Recarga)")
    print("(4) Sair")
    print("========================================================")

    opcao = int(input("Escolha uma opção: "))
    print()

    match opcao:
        case 1:
            configurar_parametros()
        case 2:
            exibir_status()
        case 3:
            simular_carregamento()
        case 4:
            print("Saindo do sistema... Trabalho Concluído!")
            break
        case _:
            print("Opção inválida! Tente novamente.")
