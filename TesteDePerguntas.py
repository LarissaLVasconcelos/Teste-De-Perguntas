
print("*" * 50)
print("* TESTE DE QI *")
print("*" * 50)

    
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))


pontuacao = 0


perguntas = [
    "1.) Qual foi o último ano que o time de futebol Botafogo foi campeão do brasileirão série A??\na)1995 b) Nunca foi campeão c) 1974 d) 1975\nResposta: ",
    "2.) Quem foi o primeiro presidente do Brasil?\na)Floriano Peixoto b) Deodoro da Fonseca c) Afonso Pena d) Juscelino Kubitschek e) Não sei responder\nResposta: ",
    "3.) Qual é a capital da França? \na) Madri b) Roma c) Paris d) Berlim\nResposta: ",
    "4.) Qual é o planeta mais próximo do Sol no nosso sistema solar? \na) Vênus b) Terra c) Marte d) Mercúrio\nRespostas: ",
    "5.) Quem escreveu a peça de teatro 'Romeu e Julieta'? \na) William Shakespeare b) Charles Dickens c) Jane Austen d) F. Scott Fitzgerald\nResposta: ",
    "6.) Qual é o maior oceano do mundo? \na) Oceano Atlântico b) Oceano Índico c) Oceano Pacífico d) Oceano Ártico\nResposta: ",
    "7.) Qual é o símbolo químico para o elemento oxigênio? \na) Boi b) O2 c) Oxg d) O\nResposta: ",
    "8.) Qual é a maior cordilheira das montanhas do mundo? \na) Montanhas Rochosas b) Andes c) Montanhas Urais d) Himalaias\nResposta: ",
    "9.) Quem é o autor da famosa pintura 'Mona Lisa'? \na) Leonardo da Vinci b) Pablo Picasso c) Vincent van Gogh d) Michelangelo\nResposta: ",
    "10.) Qual é o maior rio do mundo em termos de volume de água? \na) Rio Nilo b) Rio Amazonas c) Rio Yangtze d) Rio Mississipi\nResposta: ",
]

respostas = ["a", "b", "c", "d", "a", "c", "d", "d", "a", "b"]  


for i, pergunta in enumerate(perguntas):
    print(f"\nQuestão {i + 1}:\n{pergunta}")
    resposta = input().strip().lower()
    if resposta == respostas[i]:
        pontuacao += 2


print("\nPONTUAÇÃO: (Cada questão certa vale 2 pontos)")
print(f"Total de pontos: {pontuacao}")


if pontuacao == 2:
    print("Você foi muito mal. Que tal começar a se informar um pouquinho mais? Os jornais e os livros estão aí para isso.")
elif pontuacao >= 4 and pontuacao <= 6:
    print("Você foi mal, precisa prestar mais atenção no que faz e desenvolver o pensamento lógico. Preste mais atenção ao mundo que te rodeia.")
elif pontuacao >= 8 and pontuacao <= 12:
    print("Você foi razoavelmente bem, só precisa pensar um pouco mais nas propostas de cada tarefa que a vida pode lhe oferecer. Só assim conseguirá se sair bem de situações difíceis.")
elif pontuacao >= 14 and pontuacao <= 16:
    print("Você foi muito bem, seu jeito de pensar e agir é bem definido e dificilmente se deixará levar por dificuldades. Terá sempre as respostas certas para tudo.")
elif pontuacao >= 18 and pontuacao <= 20:
    print("Você é excepcional. Tem capacidade para agir e reagir de forma coerente e precisa. Você tem talento. Seu futuro está garantido!")