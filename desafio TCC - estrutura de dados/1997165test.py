alunos = {}
orientadores = {}

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matrícula do aluno: ")
    orientador = input("Digite o nome do orientador: ")
    
    if orientador not in orientadores:
        orientadores[orientador] = []
    
    orientadores[orientador].append(nome)
    alunos[matricula] = {"nome": nome, "matricula": matricula, "orientador": orientador, "entregas": []}
    
    print("Aluno cadastrado com sucesso!")

def cadastrar_orientador():
    nome = input("Digite o nome do orientador: ")
    
    if nome not in orientadores:
        orientadores[nome] = []
        print("Orientador cadastrado com sucesso!")
    else:
        print("Orientador já cadastrado.")

def registrar_entrega():
    matricula = input("Digite a matrícula do aluno: ")
    
    if matricula in alunos:
        versao = int(input("Digite o número da versão: "))
        data = input("Digite a data de entrega (Y-m-d): ")
        alunos[matricula]["entregas"].append((versao, data, None))
        print("Entrega registrada com sucesso!")
    else:
        print("Aluno não encontrado.")

def atribuir_nota():
    matricula = input("Digite a matrícula do aluno: ")
    
    if matricula in alunos:
        versao = int(input("Digite o número da versão: "))
        nota = float(input("Digite a nota: "))
        
        for i, entrega in enumerate(alunos[matricula]["entregas"]):
            if entrega[0] == versao:
                alunos[matricula]["entregas"][i] = (entrega[0], entrega[1], nota)
                print("Nota atribuída com sucesso!")
                return
        
        print("Versão não encontrada.")
    else:
        print("Aluno não encontrado.")

def verificar_pendencias():
    matricula = input("Digite a matrícula do aluno: ")
    
    if matricula in alunos:
        entregas = alunos[matricula]["entregas"]
        pendencias = [versao for versao, data, nota in entregas if nota is None]
        
        if pendencias:
            print("Pendências:")
            for pendencia in pendencias:
                print(f"Versão {pendencia}")
        else:
            print("Não há pendências.")
    else:
        print("Aluno não encontrado.")

def relatorio_orientador():
    orientador = input("Digite o nome do orientador: ")
    
    if orientador in orientadores:
        alunos_orientador = orientadores[orientador]
        
        for aluno in alunos_orientador:
            for matricula, info in alunos.items():
                if info["nome"] == aluno:
                    print(f"Aluno: {aluno}")
                    print("Entregas:")
                    for entrega in info["entregas"]:
                        print(f"Versão {entrega[0]} - Data: {entrega[1]} - Nota: {entrega[2] if entrega[2] else 'Não atribuída'}")
                    print("------------------------")
    else:
        print("Orientador não encontrado.")

def main():
    while True:
        print("1. Cadastrar aluno")
        print("2. Cadastrar orientador")
        print("3. Registrar entrega")
        print("4. Atribuir nota")
        print("5. Verificar pendências")
        print("6. Relatório do orientador")
        print("7. Sair")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            cadastrar_orientador()
        elif opcao == "3":
            registrar_entrega()
        elif opcao == "4":
            atribuir_nota()
        elif opcao == "5":
            verificar_pendencias()
        elif opcao == "6":
            relatorio_orientador()
        elif opcao == "7":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()