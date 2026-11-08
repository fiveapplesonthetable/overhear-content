# Authoring module for linden-courtyard-pt-s01e01-scene-04.
ID = 'linden-courtyard-pt-s01e01-scene-04'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = 'Room Four on the Second Floor  (O quarto quatro no segundo andar)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = 'Na recepção, Evelyn, professora de piano aposentada, entra vinda do táxi puxando uma mala grande azul-escura. Hannah recebe sua primeira hóspede de verdade enquanto Graham fica a postos para ajudar com a bagagem. Vamos ouvir.'
OPENER = 'Vamos ouvir cada fala com atenção e calma.'
TRANSITION = 'Agora escute toda a cena seguida mais uma vez.'
OUTRO = 'Hannah conduziu seu primeiro check-in com tranquilidade, mas Graham reparou que aquela mala azul estava estranhamente pesada. Até a próxima para descobrir o motivo.'
CLOSING = ('evelyn', 'Take care!')
STORY = [
    ('hannah', "Welcome! Good morning, ma'am.", 'Bem-vinda! Bom dia, senhora.'),
    ('evelyn', 'Good morning, my dear. I have a room for Evelyn.', 'Bom dia, minha querida. Tenho um quarto reservado para Evelyn.'),
    ('hannah', 'Yes, room four on the second floor! How was your train trip?', 'Sim, quarto quatro no segundo andar! Como foi sua viagem de trem?'),
    ('evelyn', 'Quiet and pleasant, thank you, though this suitcase feels very heavy today.', 'Tranquila e agradável, obrigada, embora esta mala pareça muito pesada hoje.'),
    ('graham', 'Allow me. Goodness, did you pack stones in here?', 'Permita-me. Minha nossa, a senhora colocou pedras aqui dentro?'),
    ('evelyn', 'Only dresses, sheet music, and my favorite teacup!', 'Só vestidos, partituras e minha xícara de chá favorita!'),
    ('hannah', 'Here is your key, number four. Breakfast is from seven thirty to ten.', 'Aqui está sua chave, número quatro. O café da manhã é das sete e meia às dez.'),
    ('evelyn', 'Wonderful. Is the window facing the street or the courtyard?', 'Maravilha. A janela dá para a rua ou para o pátio?'),
    ('hannah', 'The courtyard, right above the old tree. It is very quiet.', 'Para o pátio, bem acima da árvore velha. É muito silencioso.'),
    ('evelyn', 'Just what I need. Where are the stairs?', 'Exatamente o que eu preciso. Onde fica a escada?'),
    ('graham', 'Right through this archway. I will carry the blue bag up for you.', 'Bem ali passando por este arco. Vou levar a mala azul lá para cima para a senhora.'),
    ('evelyn', 'Thank you both very much.', 'Muito obrigada a vocês dois.'),
]
WALK = [
    (0, None, ["'Bem-vinda! Bom dia, senhora.' No inglês americano, a forma mais natural e cortês de tratar uma cliente é", (None, "ma'am"), 'abreviação simpática e respeitosa.']),
    (1, None, ["'Bom dia, minha querida. Tenho um quarto reservado para Evelyn.' Ao chegar à recepção de um hotel, basta dizer", (None, 'I have a room for'), 'seguido do seu nome.']),
    (2, None, ["'Sim, quarto quatro no segundo andar! Como foi sua viagem de trem?' Para perguntar sobre um trajeto que acabou de acontecer, use", (None, 'How was your train trip'), 'direto e gentil.']),
    (3, None, ["'Tranquila e agradável, obrigada, embora esta mala pareça muito pesada hoje.' Aqui", (None, 'feels very heavy'), 'descreve a sensação física de peso nas mãos.']),
    (4, None, ["'Permita-me. Minha nossa, a senhora colocou pedras aqui dentro?' Ao oferecer ajuda com peso,", (None, 'Allow me'), 'soa muito educado, e', (None, 'Goodness'), "é uma exclamação leve como 'minha nossa!'."]),
    (5, None, ["'Só vestidos, partituras e minha xícara de chá favorita!' Partitura musical impressa se chama", (None, 'sheet music'), 'tratada como incontável, sem plural.']),
    (6, None, ["'Aqui está sua chave, número quatro. O café da manhã é das sete e meia às dez.' Na fala cotidiana, dizer horas quebradas é super simples:", (None, 'seven thirty'), 'sete e trinta.']),
    (7, None, ["'Maravilha. A janela dá para a rua ou para o pátio?' Onde dizemos 'dar para a rua', o inglês diz que a janela está de frente para ela:", (None, 'facing the street'), 'encarando a rua.']),
    (8, None, ["'Para o pátio, bem acima da árvore velha. É muito silencioso.' A combinação", (None, 'right above'), 'reforça a posição exata: bem em cima da árvore antiga.']),
    (9, None, ["'Exatamente o que eu preciso. Onde fica a escada?' Repare que escada fixa entre andares aparece no plural em inglês:", (None, 'Where are the stairs'), 'com o verbo no plural.']),
    (10, None, ["'Bem ali passando por este arco. Vou levar a mala azul lá para cima para a senhora.' Quando você decide ajudar naquele instante, o inglês usa", (None, 'I will carry'), 'completando o sentido de subida com', (None, 'up'), 'logo depois.']),
    (11, None, ["'Muito obrigada a vocês dois.' Agradecer a duas pessoas ao mesmo tempo fica muito natural encaixando", (None, 'both'), 'em', (None, 'Thank you both'), 'logo após o pronome.']),
]
