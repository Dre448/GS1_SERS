import random

def gerar_dados_simulados():
    return {
        "temperatura": random.randint(-10, 60),
        "energia": random.randint(0, 100),
        "comunicacao": random.choice(["Ativa", "Instável", "Sem sinal"]),
        "modulo": random.choice(["Operacional", "Atenção", "Falha"])
    }

def analisar_dados(dados):
    alertas = []

    if dados["temperatura"] < 10:
        alertas.append("Temperatura muito baixa. Ativar aquecimento interno.")
    elif dados["temperatura"] > 35:
        alertas.append("Temperatura muito alta. Ativar sistema de resfriamento.")
    if dados["energia"] < 40:
        alertas.append("Energia crítica. Ativar modo de economia.")
    elif dados["energia"] < 70:
        alertas.append("Energia moderada. Monitorar consumo dos módulos.")

    if dados["comunicacao"] == "Instável":
        alertas.append("Comunicação instável. Reposicionar antena.")
    elif dados["comunicacao"] == "Sem sinal":
        alertas.append("Perda de comunicação. Iniciar protocolo de reconexão.")

    if dados["modulo"] == "Atenção":
        alertas.append("Módulo em atenção. Realizar verificação preventiva.")
    elif dados["modulo"] == "Falha":
        alertas.append("Falha detectada no módulo. Isolar sistema afetado.")

    return alertas

def exibir_painel(dados, alertas):
    print("=============================================")
    print("            Monitor de Dados")
    print("=============================================")

    print(f"Temperatura: {dados['temperatura']} °C")
    print(f"Energia: {dados['energia']}%")
    print(f"Comunicação: {dados['comunicacao']}")
    print(f"Status do módulo: {dados['modulo']}")

    print("=============================================")

    if alertas:
        print("ALERTAS GERADOS:")
        for alerta in alertas:
            print(f"- {alerta}")
    else:
        print("Sistema operando normalmente.")

    print("=============================================")

def calcular_potencia(energia):
    potencia_base = 500
    potencia_atual = potencia_base * (energia / 100)
    return potencia_atual

def recomendar(energia):
    if energia < 40:
        return "Priorizar uso de energia solar e desligar sistemas não essenciais."
    elif energia < 70:
        return "Reduzir consumo e manter monitoramento dos painéis solares."
    else:
        return "Energia estável. Sistemas sustentáveis funcionando bem."

def executar_monitoramento():
    dados = gerar_dados_simulados()
    alertas = analisar_dados(dados)
    potencia = calcular_potencia(dados["energia"])
    recomendacao = recomendar(dados["energia"])

    exibir_painel(dados, alertas)

    print(f"Potência estimada disponível: {potencia:.2f} W")
    print(f"Recomendação sustentável: {recomendacao}")

while True:
    print("\n===== Estação Espacial =====")
    print("1 - Iniciar monitoramento")
    print("2 - Encerrar sistema")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        continuar = "s"

        while continuar == "s":
            executar_monitoramento()
            continuar = input("Deseja realizar outro monitoramento? (s/n): ").lower()

    elif opcao == "2":
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida.")