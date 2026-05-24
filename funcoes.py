from classe import Chamado, ChamadoUrgente, ChamadoAgendado

def adicionar_chamado(chamados):
    usuario = input("Digite o seu nome: ")
    problema = input("Digite o problema: ")
    status = input("Digite o status: ").lower()
    tipo = input("Digite o tipo (urgente/agendado/comum): ").lower()

    if tipo == "urgente":
        chamados.append(ChamadoUrgente(usuario, problema, status))
    elif tipo == "agendado":
        data = input("Digite a data do agendamento (dd/mm/aaaa): ")
        chamados.append(ChamadoAgendado(usuario, problema, status, data))
    else:
        chamados.append(Chamado(usuario, problema, status))

def listar_chamado(chamados):
    for chamado in chamados:
        print(chamado.exibir())

def filtrar_status(chamados):
    for chamado in chamados:
        if chamado.esta_aberto():
            print(chamado.exibir())

def salvar_arquivo(chamados):
    with open("chamados.txt", "w") as arquivo:
        for chamado in chamados:
            arquivo.write(chamado.exibir() + "\n")
    print("Armazenado com Sucesso!")

def exibir_arquivo():
    try:
        with open("chamados.txt", "r") as arquivo:
            for linha in arquivo:
                print(linha.strip())
    except FileNotFoundError:
        print("O arquivo 'chamados.txt' não foi encontrado. Salve os chamados primeiro (opção 4).")

def resumo_chamados(chamados):
    contagem = {"aberto": 0, "fechado": 0}
    for chamado in chamados:
        if chamado.esta_aberto():
            contagem["aberto"] += 1
        else:
            contagem["fechado"] += 1
    return contagem

def buscar_chamado(chamados, nome):
    encontrou = False
    for chamado in chamados:
        if chamado.usuario == nome:
            print(chamado.exibir())
            encontrou = True
    if not encontrou:
        print("Nome não encontrado!")
