alunos = []
orientadores = {}

def cadastrar_orientador():
    
    nome = input("Digite o nome do orientador: ")
    if nome not in orientadores:
        orientadores[nome] = []
        print("Orientador cadastrado com sucesso!")
    else:
        print("Orientador já cadastrado.")

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matrícula do aluno: ")
    orientador = input("Digite o nome do orientador: ")

    if orientador not in orientadores:
        print("Orientador não cadastrado. Cadastre o orientador antes.")
        return
    
    aluno = {
        "nome": nome,
        "matricula": matricula,
        "orientador": orientador,
        "entregas": []
    }
    alunos.append(aluno)
    orientadores[orientador].append(nome)
    print("Aluno cadastrado com sucesso!")

def buscar_aluno_por_matricula(matricula):
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            return aluno
    return None

def registrar_entrega():
    matricula = input("Digite a matrícula do aluno: ")
    aluno = buscar_aluno_por_matricula(matricula)
    
    if aluno:
        entregas = aluno["entregas"]
        pendentes = [e for e in entregas if e[2] is None]
        if pendentes:
            print("Entrega pendente de avaliação. Não é possível registrar nova entrega.")
            return
        
        versao = int(input("Digite o número da versão: "))
        data = input("Digite a data de entrega (Y-m-d): ")
        aluno["entregas"].append((versao, data, None))
        print("Entrega registrada com sucesso!")
    else:
        print("Aluno não encontrado.")

def registrar_nota():
    matricula = input("Digite a matrícula do aluno: ")
    aluno = buscar_aluno_por_matricula(matricula)
    
    if aluno:
        versao = int(input("Digite o número da versão a ser avaliada: "))
        for idx, entrega in enumerate(aluno["entregas"]):
            if entrega[0] == versao:
                if entrega[2] is not None:
                    print("Esta versão já foi avaliada.")
                    return
                nota = float(input("Digite a nota: "))
                aluno["entregas"][idx] = (entrega[0], entrega[1], nota)
                print("Nota atribuída com sucesso!")
                return
        print("Versão não encontrada.")
    else:
        print("Aluno não encontrado.")

def listar_alunos_por_orientador():
    orientador = input("Digite o nome do orientador: ")
    if orientador in orientadores:
        alunos_orientador = orientadores[orientador]
        print(f"Alunos orientados por {orientador}:")
        for aluno in alunos_orientador:
            print(f"- {aluno}")
    else:
        print("Orientador não encontrado.")

def listar_entregas_por_aluno():
    matricula = input("Digite a matrícula do aluno: ")
    aluno = buscar_aluno_por_matricula(matricula)
    
    if aluno:
        print(f"Entregas do aluno {aluno['nome']}:")
        for entrega in aluno["entregas"]:
            print(f"Versão {entrega[0]} - Data: {entrega[1]}")
    else:
        print("Aluno não encontrado.")

def listar_pendencias():
    print("Alunos com versões não avaliadas:")
    for aluno in alunos:
        pendencias = [e for e in aluno["entregas"] if e[2] is None]
        if pendencias:
            print(f"- {aluno['nome']} ({aluno['matricula']})")

def gerar_relatorio_orientador():
    orientador = input("Digite o nome do orientador: ")
    if orientador not in orientadores:
        print("Orientador não encontrado.")
        return

    alunos_orientados = orientadores[orientador]
    soma_notas = 0
    total_alunos_com_notas = 0

    for aluno_nome in alunos_orientados:
        aluno = next((a for a in alunos if a["nome"] == aluno_nome), None)
        if aluno:
            notas = [e[2] for e in aluno["entregas"] if e[2] is not None]
            if notas:
                media_aluno = sum(notas) / len(notas)
                print(f"Aluno: {aluno['nome']} - Média: {media_aluno:.2f}")
                ultima_nota = [e for e in aluno["entregas"] if e[2] is not None][-1][2]
                soma_notas += ultima_nota
                total_alunos_com_notas += 1
            else:
                print(f"Aluno: {aluno['nome']} - Sem avaliações.")

    if total_alunos_com_notas > 0:
        media_geral = soma_notas / total_alunos_com_notas
        print(f"\nMédia geral dos alunos orientados por {orientador}: {media_geral:.2f}")
    else:
        print("\nNenhum aluno avaliado ainda.")

def menu_operacoes():
    while True:
        print("\n--- Menu de Operações ---")
        print("1. Registrar nova entrega")
        print("2. Registrar nota")
        print("3. Listar alunos por orientador")
        print("4. Listar versões entregues por aluno")
        print("5. Listar pendências de avaliação")
        print("6. Gerar relatório do orientador")
        print("7. Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ")
        
        match opcao:
            case "1":
                registrar_entrega()
            case "2":
                registrar_nota()
            case "3":
                listar_alunos_por_orientador()
            case "4":
                listar_entregas_por_aluno()
            case "5":
                listar_pendencias()
            case "6":
                gerar_relatorio_orientador()
            case "7":
                break
            case "q" | "Q":
                exit()
            case _:
                print("Opção inválida.")

def main():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Cadastrar orientador")
        print("2. Cadastrar aluno")
        print("3. Operações")
        print("q. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        match opcao:
            case "1":
                cadastrar_orientador()
            case "2":
                cadastrar_aluno()
            case "3":
                menu_operacoes()
            case "q" | "Q":
                break
            case _:
                print("''Opção inválida.''")

if __name__ == "__main__":
    main()
