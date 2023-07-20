import datetime

def Cadastrar_Disciplina(disciplina):
    diasSemana = ["Segunda", "Terça"]
    dias = []
    horários = []
    while True:
        código = input("Digite o código da disciplina: ")
        nome = input("Digite o nome da disciplina: ")
        turma = input("Digite o código da turma: ")
        while True:
            dia = input("1) Segunda \n2) Terça \n3) Quarta \n4) Quinta \n5) Sexta \n6) Sábado \n7) Domingo \nDigite a opção do dia da semana em que você tem essa aula: ")
            while True:
                posição = 0
                while posição < 24:
                    print(f"{posição + 1}) {posição}:00")
                    posição += 1
                horário = input("Digite o número do horário do seu compromisso: ")
                duração = input("Digite quantas horas essa aula tem de duração: ")
                outra_hora = input("Você tem outra aula da mesma disciplina esse dia? (s/n): ")
                horários = horários + [horário, duração]
                if outra_hora == "n":
                    break
            outro_dia = input("Você tem essa disciplina outro dia? (s/n): ")
            dias = dias + [dia, horários]
            if outro_dia == "n":
                break
        outra_disciplina = input("Deseja adicionar outra disciplina? (s/n): ")
        disciplina = disciplina + [[código, nome, turma, dias]]
        if outra_disciplina == "n":
            break
    return disciplina

def Editar_Disciplina(disciplinas):
    if len(disciplinas) == 0:
        print("Ainda não existem disciplinas cadastradas")
    else:
        posição = 0
        while posição < len(disciplinas):
            print(f"{posição + 1}) {disciplinas[posição][1]}")
            posição += 1
        editarDisciplina = input("Selecione o número do compromisso que deseja editar: ")
        editar = input("1) Código \n2) Nome da disciplina \n3) Turma \n4) Dias, horários e duração \nSelecione o número da informação que deseja editar: ")
        if editar == "4":
            novaInformação = []
            horários = []
            while True:
                dia = input("1) Segunda \n2) Terça \n3) Quarta \n4) Quinta \n5) Sexta \n6) Sábado \n7) Domingo \nDigite a opção do novo dia da semana em que você tem essa aula: ")
                while True:
                    horário = input("Digite o novo horário que começa a sua aula nesse dia no formato XX:00: ")
                    duração = input("Digite quantas horas essa aula tem de duração: ")
                    outra_hora = input("Você tem outra aula da mesma disciplina esse dia? (s/n): ")
                    horários = horários + [horário, duração]
                    if outra_hora == "n":
                        break
                outro_dia = input("Você tem essa disciplina outro dia? (s/n): ")
                novaInformação = novaInformação + [dia, horários]
                if outro_dia == "n":
                    break
        else:
            novaInformação = input("Digite a informação que substituirá a anterior: ")
        disciplinas[int(editarDisciplina) - 1][int(editar) - 1] = novaInformação
        return disciplinas
    
def Excluir_Disciplina(disciplinas):
    if len(disciplinas) == 0:
        print("Ainda não existem disciplinas cadastradas")
    else:
        posição = 0
        while posição < len(disciplinas):
            print(f"{posição + 1}) {disciplinas[posição][1]}")
            posição += 1
        excluir = input("Selecione o número da disciplina que deseja excluir: ")
        disciplinas.pop(int(excluir) -1)
    return disciplinas

def Cadastrar_Compromisso_Semanal(compromissosSemanais, disciplinas):
    tipoCompromisso = input("O compromisso é uma disciplina já existente em nosso sistema? (s/n): ")
    if tipoCompromisso == "s":
        posição = 0
        while posição < len(disciplinas):
            print(f"{posição + 1}) {disciplinas[posição][1]}")
            posição += 1
        escolherDisciplina = input("Selecione o número da disciplina que deseja cadastrar no calendário: ")
        compromissosSemanais[1] = compromissosSemanais[1] + [disciplinas[int(escolherDisciplina) - 1]]
    else:
        nome = input("Digite o nome do compromisso: ")
        diaSemana = input("1) Segunda \n2)Terça \n3)Quarta \n4)Quinta \n5)Sexta \n6)Sábado \n7)Domingo \nDigite o dia da semana do seu compromisso: ")
        posição = 0
        while posição < 24:
            print(f"{posição + 1}) {posição}:00")
            posição += 1
        horário = input("Digite o número do horário do seu compromisso: ")
        duração = input("Digite a duração do seu compromisso: ")
        compromissosSemanais[0] = compromissosSemanais[0] + [[nome, diaSemana, horário, duração]]
    return compromissosSemanais

def Editar_Compromisso_Semanal(compromissoSemanal):
    compromissoOuDisciplina = input("Seu compromisso é uma diciplina? (s/n): ")
    if compromissoOuDisciplina == "s":
        compromissoSemanal[1] = Editar_Disciplina(compromissoSemanal[1])
    else:
        if len(compromissoSemanal) == 0:
            print("Ainda não existem compromissos pontuais cadastradas")
        else:
            posição = 0
            while posição < len(compromissoSemanal[0]):
                print(f"{posição + 1}) {compromissoSemanal[0][posição][0]}")
                posição += 1
            editarCompromisso = input("Selecione o número do compromisso que deseja editar: ")
            compromissoEditado = compromissoSemanal[0][int(editarCompromisso) - 1]
            editar = input(f"1) Nome: {compromissoEditado[0]} \n2) Dia da semana: {compromissoEditado[1]} \n3) Horário: {compromissoEditado[2]} \n4) Duração: {compromissoEditado[3]} \nSelecione o número da informação que deseja editar: ")
            if editar == "2":
                novaInformação = input("1) Segunda \n2) Terça \n3) Quarta \n4) Quinta \n5) Sexta \n6) Sábado \n7) Domingo \nDigite o novo dia da semana do seu compromisso: ")
            elif editar == "3":
                posição = 0
                while posição < 24:
                    print(f"{posição + 1}) {posição}:00")
                    posição += 1
                novaInformação = input("Digite o número do novo horário do seu compromisso: ")
            else:
                novaInformação = input("Digite a informação que substituirá a anterior: ")
            compromissoSemanal[0][int(editarCompromisso) - 1][int(editar) - 1] = novaInformação
    return compromissoSemanal

def Excluir_Compromisso_Semanal(compromissos):
    if len(compromissos[0]) == 0 and len(compromissos[1]) == 0:
        print("Ainda não existem compromissos cadastrados")
    else:
        posição = 0
        while posição < len(compromissos[0]):
            print(f"{posição + 1}) {compromissos[0][posição][0]}")
            posição += 1
        while (posição - len(compromissos[0])) < len(compromissos[1]):
            print(f"{posição + 1}) {compromissos[1][posição - 1][1]}")
            posição += 1
        excluir = input("Selecione o número do compromisso que deseja excluir: ")
        if (int(excluir) - 1) < len(compromissos[0]):
            compromissos[0].pop(int(excluir) - 1)
        else:
            compromissos[1].pop(int(excluir) - len(compromissos[0]) - 1)
    return compromissos

def Cadastrar_Compromisso_Pontual(compromissos):
    while True:
        nome = input("Digite o nome do compromisso: ")
        diaMes = input("Digite o dia, mês e ano do seu compromisso no formato dd/mm/aaaa: ")
        horário = input("Digite o horário do seu compromisso: ")
        duração = input("Digite a duração do seu compromisso: ")
        lembrete = input("Deseja adicionar um lembrete? (s/n): ")
        if lembrete == "s":
            lembrete = True
        else:
            lembrete = False
        compromissos = compromissos + [[nome, diaMes, horário, duração, lembrete]]
        outroCompromisso = input("Deseja adicionar outro compromisso pontual? (s/n): ")
        if outroCompromisso == "n":
            break
    return compromissos

def Editar_Compromisso_Pontual(compromissosPontuais):
    if len(compromissosPontuais) == 0:
        print("Ainda não existem compromissos pontuais cadastradas")
    else:
        posição = 0
        while posição < len(compromissosPontuais):
            print(f"{posição + 1}) {compromissosPontuais[posição][0]}")
            posição += 1
        editarCompromisso = input("Selecione o número do compromisso que deseja editar: ")
        compromissoEditado = compromissosPontuais[int(editarCompromisso) - 1]
        editar = input(f"1) Nome: {compromissoEditado[0]} \n2) Dia da semana: {compromissoEditado[1]} \n3) Horário: {compromissoEditado[2]} \n4)Duração: {compromissoEditado[3]} \n4)Lembrete: {compromissoEditado[4]} \nSelecione o número da informação que deseja editar: ")
        novaInformação = input("Digite a informação que substituirá a anterior: ")
        compromissosPontuais[int(editarCompromisso) - 1][int(editar) - 1] = novaInformação
    return compromissosPontuais

def Excluir_Compromisso_Pontual(compromissosPontuais):
    if len(compromissosPontuais) == 0:
        print("Ainda não existem compromissos cadastrados")
    else:
        posição = 0
        while posição < len(compromissosPontuais):
            print(f"{posição + 1}) {compromissosPontuais[posição][0]}")
            posição += 1
        excluir = input("Selecione o número do compromisso que deseja excluir: ")
        compromissosPontuais.pop(int(excluir) -1)
    return compromissosPontuais

def Visualizar_Compromissos(compromissosSemanais, compromissosPontuais):
    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    espacamento = 2
    for dia in dias_semana:
        print(f'{dia: >{espacamento+10}}', end='')
    print()
    for hora in range(24):
        print(f'{hora:02d}:00', end='')
        for dia in range(7):
            tarefa_encontrada = False
            for tarefa in compromissosSemanais[0]:
                horas = []
                duração = 0
                while duração < int(tarefa[3]):
                    horas = horas + [int(tarefa[2]) + duração]
                    duração += 1
                if int(tarefa[1]) == dia and hora in horas:
                    print(f'{tarefa[0]: ^12}', end='')
                    tarefa_encontrada = True
                    break
            for tarefa2 in compromissosSemanais[1]:
                posição = 0
                diasDisciplina = []
                while posição < len(tarefa2[3]):
                    diasDisciplina = diasDisciplina + [int(tarefa2[3][posição])]
                    posição += 2
                posição = 1
                horasDisciplina = []
                while posição < len(tarefa2[3]):
                    duração = 0
                    while duração < int(tarefa2[3][posição][1]):
                        horasDisciplina = horasDisciplina + [int(tarefa2[3][0]) + duração]
                        duração += 1
                    posição += 2
                if dia in diasDisciplina and hora in horasDisciplina:
                    print(f'{tarefa2[1]: ^12}', end='')
                    tarefa_encontrada = True
                    break

            if not tarefa_encontrada:
                print('{:^12}'.format('-----'), end='')

        print()

def Visualizar_Lembretes(compromissosPontuais):
    hoje = datetime.datetime.now()
    uma_semana = datetime.timedelta(days=7)
    prazo = hoje + uma_semana
    for i in compromissosPontuais:
        i[1] = datetime.datetime.strptime(i[1], "%d/%m/%Y")
        if hoje < i[1] < prazo and i[4] == True:
            print((f"Nome: {i[0]} / Dia da semana: {i[1]} / Horário: {i[2]} / Duração: {i[3]} / Lembrete: {i[4]}"))

def main():
    disciplinas = []
    compromissosSemanais = [[],[]]
    compromissosPontuais = []
    while True:
        opção = input("1) Alterar lista de disciplinas \n2) Alterar lista de compromissos \n3) Vizualizar compromissos \n4) Vizualizar lembretes \n5) Fechar programa \nSelecione uma opção: ")
        if opção == "1":
            escolher = input("1) Cadastrar nova disciplina \n2) Editar disciplina existente \n3) Excluir disciplina \nSelecione uma opção: ")
            if escolher == "1":
                disciplinas = Cadastrar_Disciplina(disciplinas)
            elif escolher == "2":
                disciplinas = Editar_Disciplina(disciplinas)
            elif escolher == "3":
                disciplinas = Excluir_Disciplina(disciplinas)
            else:
                input("Opção invalida \nPressione enter para voltar ao menu principal")
        if opção == "2":
            escolhaCompromissos = input("1) Alterar lista de compromissos semanais \n2) Alterar lista de comprosmissos pontuais \nSelecione uma opção: ")
            if escolhaCompromissos == "1":
                escolhaCompromissosSemanais = input("1) Cadastrar novo compromisso \n2) Editar comprosmisso existente \n3) Excluir compromisso \nSelecione uma opção: ")
                if escolhaCompromissosSemanais == "1":
                    compromissosSemanais = Cadastrar_Compromisso_Semanal(compromissosSemanais, disciplinas)
                elif escolhaCompromissosSemanais == "2":
                    compromissosSemanais = Editar_Compromisso_Semanal(compromissosSemanais)
                elif escolhaCompromissosSemanais == "3":
                    compromissosSemanais = Excluir_Compromisso_Semanal(compromissosSemanais)
                else:
                    input("Opção invalida \nPressione enter para voltar ao menu principal")
            elif escolhaCompromissos == "2":
                escolhaCompromissosPontuais = input("1) Cadastrar novo compromisso \n2) Editar comprosmisso existente \n3) Excluir compromisso \nSelecione uma opção: ")
                if escolhaCompromissosPontuais == "1":
                    compromissosPontuais = Cadastrar_Compromisso_Pontual(compromissosPontuais)
                elif escolhaCompromissosPontuais == "2":
                    compromissosPontuais = Editar_Compromisso_Pontual(compromissosPontuais)
                elif escolhaCompromissosPontuais == "3":
                   compromissosPontuais = Excluir_Compromisso_Pontual(compromissosPontuais)
                else:
                    input("Opção invalida \nPressione enter para voltar ao menu principal")
        if opção == "3":
            Visualizar_Compromissos(compromissosSemanais, compromissosPontuais)
        if opção == "4":
            Visualizar_Lembretes(compromissosPontuais)
        if opção == "5":
            break
        
if __name__ == "__main__":
    main()