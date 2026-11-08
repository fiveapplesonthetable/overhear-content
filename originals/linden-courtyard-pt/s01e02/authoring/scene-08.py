# Authoring module for linden-courtyard-pt-s01e02-scene-08.
ID = 'linden-courtyard-pt-s01e02-scene-08'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 2
SCENE = 8
TITLE = 'Two Names, One Room  (Dois nomes, um quarto)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'Na quarta-feira à noitinha, enquanto escurece sobre Portland, Arthur sai do escritório pálido segurando tanto o tablet quanto o livro de papel do Graham. Hannah e Graham levantam os olhos na mesma hora. Ouça primeiro.'
OPENER = 'Vamos ver linha por linha o que Arthur acabou de descobrir.'
TRANSITION = 'Agora vamos ouvir toda a cena novamente em velocidade natural.'
OUTRO = 'Dois hóspedes reservados no quarto sete, chuva caindo lá fora e apenas quarenta minutos antes do trem das oito! Assim termina o episódio dois — venha com a gente no episódio três para descobrir se o sótão salva a noite.'
CLOSING = ('arthur', 'See you tomorrow!')
STORY = [
    ('arthur', 'Graham... Hannah... please tell me room six is free tonight.', 'Graham... Hannah... por favor me digam que o quarto seis está livre hoje à noite.'),
    ('hannah', 'No, Arthur, the couple from the south checked into room six an hour ago.', 'Não, Arthur, o casal do sul entrou no quarto seis há uma hora.'),
    ('graham', 'Every key from one to seven is taken, and room eight has wet paint.', 'Todas as chaves da um à sete estão ocupadas, e o quarto oito está com tinta fresca.'),
    ('arthur', 'Oh, disaster! Yesterday I took a phone booking on the tablet without my glasses!', 'Ah, que desastre! Ontem anotei uma reserva por telefone no tablet sem os meus óculos!'),
    ('hannah', 'Wait, let me look at the tablet screen and the paper book together.', 'Espere, deixe-me olhar a tela do tablet e o livro de papel juntos.'),
    ('graham', 'Let me guess. You promised somebody a room we do not have?', 'Deixe-me adivinhar. Você prometeu a alguém um quarto que não temos?'),
    ('hannah', 'Arthur! Room seven is already occupied, and you booked a second guest into room seven!', 'Arthur! O quarto sete já está ocupado, e você reservou um segundo hóspede no quarto sete!'),
    ('arthur', "And he arrives on the eight o'clock evening train, in forty minutes!", 'E ele chega no trem das oito da noite, daqui a quarenta minutos!'),
    ('graham', 'Told you that tablet is a trap.', 'Eu avisei que esse tablet é uma armadilha.'),
    ('arthur', 'It is raining outside and every hotel on our street is full! What do we do?', 'Está chovendo lá fora e todos os hotéis da nossa rua estão lotados! O que fazemos?'),
    ('hannah', 'Wait, what is on the third floor above the stairs?', 'Espere, o que tem no terceiro andar em cima da escada?'),
    ('graham', 'The old sunny attic study... follow me, quickly!', 'O antigo escritório ensolarado do sótão... venha comigo, rápido!'),
]
WALK = [
    (0, None, ["'Graham... Hannah... por favor me digam que o quarto seis está livre hoje à noite.' Um quarto vago e disponível para hospedagem é descrito direto como", (None, 'is free tonight'), 'está livre hoje à noite.']),
    (1, None, ["'Não, Arthur, o casal do sul entrou no quarto seis há uma hora.' Fazer o registro e entrar num quarto específico vira", (None, 'checked into room six'), 'seguido de', (None, 'an hour ago'), 'uma hora atrás.']),
    (2, None, ["'Todas as chaves da um à sete estão ocupadas, e o quarto oito está com tinta fresca.' Aviso clássico de parede recém-pintada em inglês:", (None, 'wet paint'), 'literalmente tinta molhada.']),
    (3, None, ["'Ah, que desastre! Ontem anotei uma reserva por telefone no tablet sem os meus óculos!' Com telas, celulares e computadores usamos sempre", (None, 'on the tablet'), 'no tablet.']),
    (4, None, ["'Espere, deixe-me olhar a tela do tablet e o livro de papel juntos.' No final da frase,", (None, 'together'), 'mostra que ela vai comparar os dois lado a lado.']),
    (5, None, ["'Deixe-me adivinhar. Você prometeu a alguém um quarto que não temos?' Antes de acertar em cheio uma suspeita,", (None, 'Let me guess'), "funciona igualzinho ao nosso 'deixe-me adivinhar'."]),
    (6, None, ["'Arthur! O quarto sete já está ocupado, e você reservou um segundo hóspede no quarto sete!' A mesma palavra que significa livro funciona como verbo para fazer reservas:", (None, 'you booked'), 'você reservou.']),
    (7, None, ["'E ele chega no trem das oito da noite, daqui a quarenta minutos!' Para dizer 'daqui a quarenta minutos' no futuro, o inglês usa simplesmente", (None, 'in forty minutes'), 'em quarenta minutos.']),
    (8, None, ["'Eu avisei que esse tablet é uma armadilha.' Na fala informal do dia a dia, cai fora o pronome inicial em", (None, 'Told you'), "o famoso 'eu te disse!'."]),
    (9, None, ["'Está chovendo lá fora e todos os hotéis da nossa rua estão lotados! O que fazemos?' Para perguntar o que fazer diante de um aperto, entra o auxiliar em", (None, 'What do we do'), 'o que a gente faz?']),
    (10, None, ["'Espere, o que tem no terceiro andar em cima da escada?' Nos Estados Unidos o térreo já conta como primeiro andar, então", (None, 'on the third floor'), 'fica dois lances acima.']),
    (11, None, ["'O antigo escritório ensolarado do sótão... venha comigo, rápido!' Para chamar alguém a ir atrás de você na hora, basta dizer", (None, 'follow me'), 'siga-me!']),
]
