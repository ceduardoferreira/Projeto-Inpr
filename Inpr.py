#Carlos Eduardo Ferreira da Silva 
#911

#biblioteca
import os


#função
def linha(): 
    print("===============================")

def assunto():
    print("""Olá, {} seja bem-vindo(a) a essa seção de estudo sobre impressionismo! Depois desse assunto, faça o quiz com atividades para fixar o conteúdo.
    
    O Impressionismo foi um movimento artístico que surgiu na França, na segunda metade do século XIX, durante o período da Belle Époque (Bela época).
    A principal proposta do impressionismo era mostrar, através das artes plásticas, principalmente a pintura, os efeitos da luz no ambiente, além de apresentar as impressões pessoais dos artistas quanto ao que observavam, através de cores primárias (também chamadas de cores puras).
    É conhecido como o movimento que deu origem a Arte Moderna e suas obras são conhecidas pela presença de contraste, efeitos de sombras feitos através das próprias pinceladas dos artistas, além da luz e da claridade das cores. 
    
    """.format(nome))

def quiz():
    print("""

        Vamos começar o nosso quiz sobre impressionismo
        
        Nesse quiz, vamos responder a 4 perguntinhas básicas, 
        valendo 10 pontos cada para testar seu nível de conhecimento.
        """)

    os.system('cls') or None

#============================================================================================================
#Pergunta 1
#============================================================================================================

    print ("\nOnde surgiu o Impressionismo?")

    print ("\na) Bélgica")
    print ("\nb) França")
    print ("\nc) Alemanha")
    print ("\nd) Suíça")

    resposta = input("\nDigite a opção correta: ")
    pontos = []
    pontuacao = 0

    if resposta == 'b':
        os.system('cls') or None
        linha()
        print ("""Parabéns, você acertou! +10 pontos""")
        linha()
        pontos.append(True)

    
    elif resposta != 'b':
        os.system('cls') or None
        linha()
        print ("""Você errou, tente acertar na próxima! -10 pontos """)
        linha()
        pontos.append(False)
        

#============================================================================================================
#Pergunta 2
#============================================================================================================

    print ("Em que século surgiu o Impressionismo?")

    print ("a) XIX")
    print ("b) XX")
    print ("c) XVI")
    print ("d) XV")

    resposta = input("\nDigite a opção correta: ")

    if resposta == 'a':
        os.system('cls') or None
        linha()
        print ("""Parabéns, você acertou!""")
        linha()
        pontos.append(True)
        

    elif resposta != 'a':
        os.system('cls') or None
        linha()
        print ("""Você errou, tente acertar na próxima! -10 pontos """)
        linha()
        pontos.append(False)
       

#============================================================================================================
#Pergunta 3
#============================================================================================================

    print ("Durante que época surgiu o impressionismo?")

    print ("a) Belle Epoque")
    print ("b) Idade Média")
    print ("c) Era Medieval")
    print ("d) Revolta Francesa")

    resposta = input("\nDigite a opção correta: ")

    if resposta == 'a':
        os.system('cls') or None
        linha()
        print ("""Parabéns, você acertou!""")
        linha()
        pontos.append(True)
        
    
    elif resposta != 'a':
        os.system('cls') or None
        linha()
        print ("""Você errou, tente acertar na próxima! -10 pontos """)
        linha()
        pontos.append(False)
        

#============================================================================================================
#Pergunta 4
#============================================================================================================

    print ("O impressionismo, é conhecido como o movimento que deu origem ao o que?")

    print ("a) Arte clássica")
    print ("b) Arte antiga")
    print ("c) Arte comtemporânea")
    print ("d) Arte moderna")

    resposta = input("\nDigite a opção correta: ")

    if resposta == 'd':
        os.system('cls') or None
        linha()
        print ("""Parabéns, você acertou!""")
        linha()
        pontos.append(True)
        os.system('cls') or None
        linha()
        

    elif resposta != 'd':
        os.system('cls') or None
        linha()
        print ("""Você errou, tente acertar na próxima! -10 pontos """)
        linha()
        pontos.append(False)
        linha()

    for i in pontos:
        if i == True:
            pontuacao += 10
        else:
            pontuacao -=10

    linha()
    print ("Parabéns, {}. Sua pontuação final foi de: ".format(nome), pontuacao)       
    linha()
    linha()
    
        


#variáveis
opcao = int

nome = str (input("""
Digite seu nome: 
\n"""))

os.system('cls') or None

linha()
print ("""Olá, {} seja bem-vindo! Aqui vamos aprender mais sobre o movimento artístico impressionismo.
A seguir, você irá ver um menu com as opções, espero que goste e bons estudos!""".format(nome))
linha()

#laço de repetição
while opcao != 3:
    print ("""\nDigite a opção desejada: \n""")
    opcao = int (input ("\n 1= Assunto \n 2= Quiz \n 3= Sair\n ="))
    linha()

    os.system('cls') or None

    if opcao == 1: 
        assunto()
        os.system('pause') or None

    elif opcao == 2: 
        quiz()
        os.system('pause') or None
