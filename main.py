from classe import Chamado, ChamadoUrgente, ChamadoAgendado
from funcoes import adicionar_chamado, listar_chamado, filtrar_status, salvar_arquivo, exibir_arquivo, resumo_chamados, buscar_chamado

if __name__ == "__main__":
    chamados = []
    while True:
        print("====== MENU =====".center(40))
        print("1. Adicionar chamado".center(20))
        print("2. Listar chamados".center(20))
        print("3. Exibir chamados abertos".center(20))
        print("4. Salvar os chamados em arquivo".center(20))
        print("5. Exibir chamados do arquivo".center(20))
        print("6. Sair".center(20))
        print("7. Resumo de chamados".center(20))
        print("8. Buscar chamado".center(20))
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                adicionar_chamado(chamados)
            elif opcao == 2:
                listar_chamado(chamados)
            elif opcao == 3:
                filtrar_status(chamados)
            elif opcao == 4:
                salvar_arquivo(chamados)
            elif opcao == 5:
                exibir_arquivo()
            elif opcao == 6:
                break
            elif opcao == 7:
                resultado = resumo_chamados(chamados)
                print(f"Abertos: {resultado['aberto']} | Fechados: {resultado['fechado']}")
            elif opcao == 8:
                nome = input("Digite o nome do usuário: ")
                buscar_chamado(chamados, nome)
            else:
                print("Opção inválida")
        except ValueError:
            print("Digite apenas número!")
