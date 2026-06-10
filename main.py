### Sistema Integrado de Carregadores GoodWee

# status = (falha, carregando (consumo e tamamnho da bateria do carro), esperando concluido)

## 1. Configurar parâmetros:
# - quantidade de carregadores
# - energia total disponível
# - consumo de energia
# - status de cada carregador

## 2. Visualizar status:
# - Listar todos os carregadores e seus status
# - Exibir em formato de matriz: eixo y: carregadores, eixo x: status
# - Exibir energia total disponível e consumo total

## 3 Simular situações:
# - aumento ou diminuição na energia diponível
# - atualização de qualquer status dos carregadores

## 4. Sair
 
lista_carregadores = []

def add_carregadores(num_carregadores):
    for i in range(num_carregadores):
        status = input(f"Digite o status do carregador {i + 1} (falha, carregando, esperando, concluido): ")
        consumo = float(input(f"Digite o consumo de energia do carregador {i + 1}: "))
        lista_carregadores.append({"id": i + 1, "status": status, "consumo": consumo})
        print(f"Carregador {i + 1} adicionado com sucesso!")

lista_carregadores.append({"id": 1, "status": "falha", "consumo": 0.0})
lista_carregadores.append({"id": 2, "status": "carregando", "consumo": 20.0}) # esses três são somentes para testes
lista_carregadores.append({"id": 3, "status": "esperando", "consumo": 0.0})

def exibir_status():
    for carregador in lista_carregadores:
        print(f"Carregador {carregador['id']} | Status: {carregador['status']} | Consumo: {carregador['consumo']} kW")


exibir_status()

# while True:
#     print("========================================================")
#     print("Sistema Integrado de Carregadores GoodWee - Versão Alpha")
#     print("========================================================")
#     print("(1) Configurar parâmetros")
#     print("(2) Visualizar status")
#     print("(3) Simular situações")
#     print("(4) Sair")
#     print("========================================================")

#     opcao = int(input("Escolha uma opção: "))
#     print()

#     match opcao:
#         case 1:
#             print("=== Configurar parâmetros ===")

#         case 2:
#             print("=== Visualizar status ===")


#         case 3:
#             print("=== Simular situações ===")


#         case 0:
#             print("Saindo do sistema...")
#             break

#         case _:
#             print("Opção inválida")
        
