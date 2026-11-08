# Authoring module for linden-courtyard-pt-s01e02-scene-06.
ID = 'linden-courtyard-pt-s01e02-scene-06'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 2
SCENE = 6
TITLE = 'The Friday Caller  (A ligação de sexta-feira)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'Depois do café da manhã, a recepção volta a ficar silenciosa enquanto Hannah atualiza o livro de papel e Graham lubrifica a dobradiça da porta. De repente o telefone do balcão toca. Vamos escutar.'
OPENER = 'Vamos analisar com calma cada frase deste telefonema.'
TRANSITION = 'Agora ouça novamente toda a cena seguida.'
OUTRO = 'Agora eles têm um horário marcado — sexta-feira ao meio-dia — e uma voz nervosa ao telefone que se recusa a dizer o nome. Até a próxima cena.'
CLOSING = ('hannah', 'Bye for now!')
STORY = [
    ('hannah', 'Linden Courtyard Inn, good morning! Hannah speaking.', 'Linden Courtyard Inn, bom dia! Aqui é a Hannah falando.'),
    ('graham', 'Who is it? Another booking for the weekend?', 'Quem é? Outra reserva para o fim de semana?'),
    ('hannah', 'Wait, hello, sir! You are calling about the dark blue suitcase?', 'Espere, alô, senhor! O senhor está ligando sobre a mala azul-escura?'),
    ('graham', 'Ask him his name! Write it down!', 'Pergunte o nome dele! Anote aí!'),
    ('hannah', 'Yes, sir, we locked your bag safely in our closet. What is your name, please?', 'Sim, senhor, trancamos sua mala em segurança no nosso armário. Qual é o seu nome, por favor?'),
    ('graham', 'What is he saying? Why are you frowning?', 'O que ele está dizendo? Por que você está franzindo a testa?'),
    ('hannah', "Sir? He says, 'Please do not open the white paper package. I will come Friday at noon.'", 'Senhor? Ele disse: "Por favor, não abram o pacote de papel branco. Eu vou na sexta-feira ao meio-dia."'),
    ('graham', 'Give me the phone, let me ask him properly!', 'Me dê o telefone, deixe que eu pergunte direito!'),
    ('hannah', "Too late! He said 'Thank you' and hung up!", 'Tarde demais! Ele disse "Obrigado" e desligou!'),
    ('graham', 'Polite voice? Young or old?', 'Voz educada? Jovem ou mais velho?'),
    ('hannah', 'Quiet, polite, maybe thirty-five. He sounded nervous, not angry.', 'Baixa, educada, talvez uns trinta e cinco anos. Ele parecia nervoso, não bravo.'),
    ('graham', 'Nervous about a wooden toy train? This story gets stranger every hour.', 'Nervoso por causa de um trenzinho de madeira? Essa história fica mais estranha a cada hora.'),
]
WALK = [
    (0, None, ["'Linden Courtyard Inn, bom dia! Aqui é a Hannah falando.' Ao atender o telefone comercialmente, basta dizer seu nome seguido de", (None, 'Hannah speaking'), 'Hannah falando.']),
    (1, None, ["'Quem é? Outra reserva para o fim de semana?' Ao perguntar quem está na linha ou na porta, o inglês usa o pronome neutro:", (None, 'Who is it'), 'quem é?']),
    (2, None, ["'Espere, alô, senhor! O senhor está ligando sobre a mala azul-escura?' Pela entonação surpresa, Hannah mantém a ordem direta em", (None, 'You are calling about'), 'confirmando o assunto da ligação.']),
    (3, None, ["'Pergunte o nome dele! Anote aí!' Passar uma informação para o papel se diz sempre", (None, 'Write it down'), 'anote por escrito.']),
    (4, None, ["'Sim, senhor, trancamos sua mala em segurança no nosso armário. Qual é o seu nome, por favor?' Onde dizemos 'qual é o seu nome?', o inglês pergunta", (None, 'What is your name'), "sempre com 'o quê' em vez de 'qual'."]),
    (5, None, ["'O que ele está dizendo? Por que você está franzindo a testa?' Uma única palavra,", (None, 'frowning'), 'descreve o gesto de franzir a testa preocupada.']),
    (6, None, ['\'Senhor? Ele disse: "Por favor, não abram o pacote de papel branco. Eu vou na sexta-feira ao meio-dia."\' Para marcar meio-dia em ponto usamos a preposição exata:', (None, 'at noon'), 'ao meio-dia.']),
    (7, None, ["'Me dê o telefone, deixe que eu pergunte direito!' O advérbio", (None, 'properly'), "equivale ao nosso 'direito' ou 'como manda o figurino'."]),
    (8, None, ['\'Tarde demais! Ele disse "Obrigado" e desligou!\' Encerrar uma chamada telefônica usa o passado irregular', (None, 'hung up'), 'desligou o telefone.']),
    (9, None, ["'Voz educada? Jovem ou mais velho?' Graham faz perguntas curtinhas de detetive:", (None, 'Young or old'), 'jovem ou velho?']),
    (10, None, ["'Baixa, educada, talvez uns trinta e cinco anos. Ele parecia nervoso, não bravo.' Para impressões que vêm pela voz, usamos", (None, 'He sounded nervous'), 'ele soava nervoso.']),
    (11, None, ["'Nervoso por causa de um trenzinho de madeira? Essa história fica mais estranha a cada hora.' Adjetivos curtos ganham terminação comparativa para indicar aumento gradual:", (None, 'gets stranger'), 'fica mais estranha.']),
]
