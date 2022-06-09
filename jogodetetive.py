from tokenize import String


print ('                                         ![Jogo Detetive]!')

print ('|           Bob Marley morreu em sua escola no centro academico , ele estava junto com 3 alunos ,        |')
print ('|no comeco foi considerado um ataque cardíaco , porem a pericia encontrou vetigios de veneno em seu copo |')
print ('|         entao o detetive ira pegar as pistas para voce desvendar o caso , voce tera 2 tentativas.      |')

menupista = 0
tentativas = 2
tentativaresp = String

while True :
    while menupista == 0 :
        print ('                  [Pistas]')
        print ('[1] Revista na casa dos Suspeitos.')
        print ('[2] Veneno utilizado ')
        print ('[3] Relatos de motivos para um assassinato')
        print ('----------------------------------------------')
        print ('[4] Eu sei quem e o ASSASSINO')
        print ('----------------------------------------------')
        menupista = int(input("Escolha : "))
        print ('----------------------------------------------')


        if (menupista == 1):
            print ('|  [Nome]  | [Objeto suspeito] |')
            print ('|Erika     |faca de mao        |')
            print ('|Diogo     |frasco do veneno   |')
            print ('|Fredy     |pistola glock19    |')
            print ('----------------------------------------------')
            investigarmenupista = int(input('  Deseja investigar algum ?\n'
                                            '     [1]Sim   [2]Nao \n     '))
            print ('----------------------------------------------')

            while investigarmenupista == 1:
                print(' Investigar')
                print ('[1] Erika ')
                print ('[2] Diogo ')
                print ('[3] Fredy ')
                print ('[4] Sair ')
                print ('----------------------------------------------')
                explicationobj = int(input('Escolha : '))
                print ('----------------------------------------------')

                if (explicationobj == 1):
                    print ('[Erika]')
                    print ('"Eu ganhei essa faca de presente do meu pai para me proteger"')
                    print ('-------------------------------------------------------------')
                    investigarmenupista = 1
                if (explicationobj == 2):
                    print ('[Diogo]')
                    print ('"Eu peguei esse frasco pra fazer um cartaz pra Erika voltar pra mim"')
                    print ('--------------------------------------------------------------------')
                    investigarmenupista = 1
                if (explicationobj == 3):
                    print ('[Fredy]')
                    print ('"Eu estou com medo de ser o proximo , vou me proteger"')
                    print ('------------------------------------------------------')
                    investigarmenupista = 1
                if (explicationobj == 4):
                    break
            menupista = 0

            if (investigarmenupista == 2):
                menupista = 0 

            
        if (menupista == 2):
            print ('               [Locais do veneno]')
            print ('|--------------------------------------------------|')
            print ('|O veneno se encontra no laboratorio               |')
            print ('|O veneno se encontra na sala do zelador do colegio|')
            print ('|--------------------------------------------------|')
            verestoque = int(input('           Deseja investigar algum ?\n'
                                   '               [1]Sim   [2]Nao \n     '))
            print ('----------------------------------------------')

            while verestoque == 1:
                print ('    [Estoques]')
                print ('|----------------|')
                print ('|[1] Laboratorio |') 
                print ('|[2] Zelador     |')
                print ('|[3] Sair        |')
                print ('|----------------|')
                investigarestoque = int(input('Escolha : '))
                print ('----------------------------------------------')
                if (investigarestoque == 1):
                    print ('| Dia | domingo | segunda |')
                    print ('| Qtd |   277   |   277   |')
                    print ('----------------------------------------------')
                    verestoque = 1
                if (investigarestoque == 2):
                    print ('[Zelador]')
                    print ('"eu nao conto estoque nao , outro aluno morreu envenenado ? rss"')
                    print ('----------------------------------------------') 
                    verestoque = 1 
                if (investigarestoque == 3):
                    break
                menupista = 0 

            if (verestoque == 2):
                menupista = 0
            

        while (menupista == 3):
            print ('| [Relatos] |')
            print ('|[1] Erika  |')   
            print ('|[2] Diogo  |')
            print ('|[3] Fredy  |')
            print ('|[4] Zelador|')
            print ('----------------------------------------------')
            verrelatos = int(input('Deseja investigar algum ?\n'
                                   '   [1]Sim   [2]Nao \n     '))
            print ('----------------------------------------------')

            if (verrelatos == 2):
                menupista = 0

            if (verrelatos == 1):
                menurelatos = int(input('Escolha : '))

                while menurelatos == 1:
                    print ('[Erika]') 
                    print ('"Eu gostava muito do Bob, mas nao o conhecia tao bem."')
                    print ('----------------------------------------------')
                    print ('[1] Sabado')
                    print ('[2] Domingo')
                    print ('[3] Segunda')
                    print ('[4] Investigar outros')
                    print ('----------------------------------------------')
                    erikarelato = int(input('Escolha : '))
                    print ('----------------------------------------------')
                    if (erikarelato == 1):
                        print ('[Sabado]')
                        print ('"Eu e o Diogo , fomos em uma festa , onde conheci o Bob ')
                        print (' eu achei o Bob muito gente boa , mas fiquei sebendo que')
                        print (' ele brigou com o Fredy no Dia."')
                        print ('----------------------------------------------')
                        menurelatos = 1
                    if (erikarelato == 2):
                        print ('[Domingo]') 
                        print ('"Eu e o Diogo fomos conversar no colegio,')
                        print (' mas acabamos brigando e terminando."')
                        print ('----------------------------------------------')
                        menurelatos = 1
                    if (erikarelato == 3):
                        print ('[Segunda]') 
                        print ('"Aquele dia horroso , Bob chamou nos 3 para conversar,')
                        print (' depois de muita conversa , e muito perdao entre nos ,')
                        print (' voltei a namorar o Diogo , e quando derrepente o Bob ')
                        print (' cai no chao morto , aquilo foi um choque."')
                        print ('----------------------------------------------')
                        menurelatos = 1
                    if (erikarelato == 4):
                        break
                    menupista = 3

                while menurelatos == 2:
                    print ('[Diogo]') 
                    print ('"Bob era meu bro , ando com ele desde o primario."')
                    print ('----------------------------------------------')
                    print ('[1] Sabado')
                    print ('[2] Domingo')
                    print ('[3] Segunda')
                    print ('[4] Investigar outros')
                    print ('----------------------------------------------')
                    diogorelato = int(input('Escolha : '))
                    print ('----------------------------------------------')
                    if (diogorelato == 1):
                        print ('[Sabado]')
                        print ('"Eu e Erika , fomos em uma festa , tudo estava tranquilo ')
                        print (' foi entao que vi Bob beijando Erika , e a festa virou um')
                        print (' lixo , eu queria so ma... sair da festa."')
                        print ('----------------------------------------------')
                        menurelatos = 2
                    if (diogorelato == 2):
                        print ('[Domingo]') 
                        print ('"Eu fui resolver minha situacao com Erika ')
                        print (' entao fomos conversar no colegio , porem ')
                        print (' eu neguei o perdao dela e terminamos."')
                        print ('----------------------------------------------')
                        menurelatos = 2
                    if (diogorelato == 3):
                        print ('[Segunda]') 
                        print ('"O dia que o Bob morreu , Comecou com Bob chamando nos 3 para conversar,')
                        print (' falando que a Erika nao tinha culpa , ou seja , no final eu acabei ')
                        print (' perdoando os dois , voltei a namorar Erika , e a ser amigo de Bob ')
                        print (' quando do nada o Bob da um pirepaque e morre."')
                        print ('----------------------------------------------')
                        menurelatos = 2
                    if (diogorelato == 4):
                        break
                    menupista = 3

                while menurelatos == 3:
                    print ('[Fredy]') 
                    print ('"Bob era meu irmao , nunca ia machuca-lo."')
                    print ('----------------------------------------------')
                    print ('[1] Sabado')
                    print ('[2] Domingo')
                    print ('[3] Segunda')
                    print ('[4] Investigar outros')
                    print ('----------------------------------------------')
                    fredyrelato = int(input('Escolha : '))
                    print ('----------------------------------------------')
                    if (fredyrelato == 1):
                        print ('[Sabado]')
                        print ('"Eu e Bob , fomos em uma festa , entao eu fui pegar uma ')
                        print (' gatinha , mas o Bob veio de graca e acabou tomando um ')
                        print (' soco pra para de ser otario , como o clima tava ruim ,')
                        print (' eu fui embora ."')
                        print ('----------------------------------------------')
                        menurelatos = 3
                    if (fredyrelato == 2):
                        print ('[Domingo]') 
                        print ('"Eu fiquei em casa jogando um joguinho."')
                        print ('----------------------------------------------')
                        menurelatos = 3
                    if (fredyrelato == 3):
                        print ('[Segunda]') 
                        print ('"O Bob devia ta com medo de apanhar denovo, entao chamou geral pra ')
                        print (' conversar , dai que descobri que ele era talarico tambem , devia ')
                        print (' ter ficado na festa mais um tempo , mas acho que o Diogo nao tem a')
                        print (' moral de bater em ninguem , depois de tudo certo , do nada , Bob morre."')
                        print ('----------------------------------------------')
                        menurelatos = 3
                    if (fredyrelato == 4):
                        break
                    menupista = 3
                
                if (menurelatos == 4):
                    print('[Zelador]')
                    print('"Entao eu nao gostava desse menino mesmo , mas nao lembro de ter visto ele no dia."')
                    print ('----------------------------------------------')
                    menupista = 3
        
        while menupista == 4:
            print ('Ja descobriu o assassino?')
            print ('----------------------------------------------')
            prontaresp = int(input('[1]Sim [2]Nao'))
            print ('----------------------------------------------')

            if prontaresp == 2:
                print ('Deseja voltar para as pistas ?')
                print ('----------------------------------------------')
                desistente = int(input('[1]Sim [2] Nao , Desisto '))
                print ('----------------------------------------------')
                if desistente == 1:
                    menupista = 0
                if desistente == 2:
                    print ('----------------------------------------------')
                    print ('[O pior detetive do Brasil]')
                    break
            if prontaresp == 1:
                tentativaresp = input('Digite o nome do culpado : ')
                print ('----------------------------------------------')
                if (tentativaresp == 'Erika'):
                    print ('[Voce errou]')
                    print ('----------------------------------------------')
                    tentativas -= 1
                    if tentativas == 0 :
                        print ('[Voce perdeu] | Newba')  
                        break                     
                    else :
                        menupista = 4

                if (tentativaresp == 'erika'):
                    print ('[Voce errou]')
                    print ('----------------------------------------------')
                    tentativas -= 1
                    menupista = 4
                    if tentativas == 0 :
                        print('[Voce perdeu] | Newba')  
                        break                     
                    else :
                        menupista = 4

                if (tentativaresp == 'Diogo'):
                    print ('                                      [Historia]')
                    print ('|---------------------------------------------------------------------------------------------|')                  
                    print ('|Diogo depois de tomar um chifre , fica vingativo                                             |')
                    print ('|E deduzido depois da revista, que Diogo armou um plano de roubar o veneno do zelador,        |')
                    print ('|ja que , o estoque do laboratorio estava normal , e o zelador nao conta o seu                |')
                    print ('|como Diogo estava na escola no domingo e concluido que foi nesse dia que ele roubou o frasco |')
                    print ('|---------------------------------------------------------------------------------------------|')
                    print ('                            [Voce Acertou] | como a policia ')
                    print ('                                [Parabens] | Detetive       ')
                    break
                if (tentativaresp == 'diogo'):
                    print ('                                      [Historia]')
                    print ('|---------------------------------------------------------------------------------------------|')
                    print ('|Diogo depois de tomar um chifre , fica vingativo                                             |')
                    print ('|E deduzido depois da revista, que Diogo armou um plano de roubar o veneno do zelador,        |')
                    print ('|ja que , o estoque do laboratorio estava normal , e o zelador nao conta o seu                |')
                    print ('|como Diogo estava na escola no domingo e concluido que foi nesse dia que ele roubou o frasco |')
                    print ('|---------------------------------------------------------------------------------------------|')
                    print ('                            [Voce Acertou] | como a policia ')
                    print ('                                [Parabens] | Detetive       ')
                    break

                if (tentativaresp == 'Fredy'):
                    print ('[Voce errou]')
                    print ('----------------------------------------------')
                    tentativas -= 1
                    menupista = 4
                    if tentativas == 0 :
                        print('[Voce perdeu] | Newba')  
                        break                     
                    else :
                        menupista = 4

                if (tentativaresp == 'fredy'):
                    print ('[Voce errou]')
                    print ('----------------------------------------------')
                    tentativas -= 1
                    menupista = 4
                    if tentativas == 0 :
                        print('[Voce perdeu] | Newba')  
                        break                     
                    else :
                        menupista = 4

                if (tentativaresp == 'Zelador'):
                    print ('                               [Historia]')
                    print ('|-----------------------------------------------------------------------|')
                    print ('|O zelador e um assassino em serie                                      |')
                    print ('|Apos sua descoberta , calculasse que o zelador matou mais de 50 alunos |')
                    print ('|-----------------------------------------------------------------------|')
                    print ('            [Parabens voce acertou] | Diferente da policia')
                    print ('                     [O melhor detetive do Brasil]       ')
                    break
                if (tentativaresp == 'zelador'):
                    print ('                               [Historia]')
                    print ('|-----------------------------------------------------------------------|')
                    print ('|O zelador e um assassino em serie                                      |')
                    print ('|Apos sua descoberta , calculasse que o zelador matou mais de 50 alunos |')
                    print ('|-----------------------------------------------------------------------|')
                    print ('            [Parabens voce acertou] | Diferente da policia')
                    print ('                     [O melhor detetive do Brasil]       ')
                    break
                else:
                    print ('Voce nao digitou nenhum suspeito da historia')
                    print ('             |Tente Novamente|')
                    print ('--------------------------------------------')
                    menupista = 4



