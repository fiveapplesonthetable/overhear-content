# Authoring module for linden-courtyard-pt-s01e04-scene-02.
ID = 'linden-courtyard-pt-s01e04-scene-02'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 4
SCENE = 2
TITLE = 'The Blue Door  (A porta azul)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'Dez minutos depois, Hannah já atravessou a ponte sobre o rio em Portland, mas duas ruas estreitas se abrem atrás da farmácia. Ela liga para Graham ao lado de um chafariz de pedra. Vamos ouvir primeiro.'
OPENER = 'Agora vamos conferir cada frase da ligação com calma.'
TRANSITION = 'Vamos ouvir novamente a cena inteira no ritmo normal.'
OUTRO = 'Duas válvulas novas no bolso e passos matinais já soando na escada! Na próxima cena, Tessa e Arthur tentam distrair todo mundo no café da manhã. Até logo.'
CLOSING = ('graham', 'Bye for now!')
STORY = [
    ('hannah', 'Graham, can you hear me? I just passed the green pharmacy!', 'Graham, você está me ouvindo? Acabei de passar pela farmácia verde!'),
    ('graham', 'Loud and clear. Are you standing by the little stone fountain?', 'Alto e bom som. Você está parada perto do pequeno chafariz de pedra?'),
    ('hannah', 'Yes! There are two small streets on the left. Which one do I take?', 'Sim! Tem duas ruas pequenas à esquerda. Qual delas eu pego?'),
    ('graham', 'Take the second street, beside the flower stand, not the narrow alley.', 'Pegue a segunda rua, ao lado da banca de flores, não o beco estreito.'),
    ('hannah', 'Walking now... oh, I see the golden key sign and the blue door!', 'Andando agora... ah, já estou vendo a placa da chave dourada e a porta azul!'),
    ('graham', 'Good! Is the shutter open?', 'Boa! A porta de enrolar está aberta?'),
    ('hannah', 'He is unlocking it right now! Stay on the phone one second.', 'Ele está destrancando agora mesmo! Fique na linha um segundo.'),
    ('graham', 'Make sure the brass ring inside is twenty millimeters wide.', 'Garanta que o anel de latão por dentro tenha vinte milímetros de largura.'),
    ('hannah', 'He matched it against the old one. He has two left on the shelf!', 'Ele comparou com a velha. Ele ainda tem duas sobrando na prateleira!'),
    ('graham', 'Buy both! A spare valve saves next winter too.', 'Compre as duas! Uma válvula reserva salva o próximo inverno também.'),
    ('hannah', 'Paid in cash! Keep your toolbox open, I am running back across the bridge!', 'Pago em dinheiro! Deixe sua caixa de ferramentas aberta, estou voltando correndo pela ponte!'),
    ('graham', 'Hurry, I just heard footsteps on the second floor stairs!', 'Depressa, acabei de ouvir passos na escada do segundo andar!'),
]
WALK = [
    (0, None, ["'Graham, você está me ouvindo? Acabei de passar pela farmácia verde!' Ao telefone, o inglês pergunta usando 'can':", (None, 'can you hear me'), 'você consegue me ouvir?']),
    (1, None, ["'Alto e bom som. Você está parada perto do pequeno chafariz de pedra?' A confirmação clássica de áudio limpo ao telefone é", (None, 'Loud and clear'), 'alto e claro.']),
    (2, None, ["'Sim! Tem duas ruas pequenas à esquerda. Qual delas eu pego?' Quando há poucas opções bem na sua frente, use", (None, 'Which one'), "evitando repetir 'street'."]),
    (3, None, ["'Pegue a segunda rua, ao lado da banca de flores, não o beco estreito.' Nos Estados Unidos,", (None, 'flower stand'), 'é o jeito natural de chamar uma barraca ou banca de flores.']),
    (4, None, ["'Andando agora... ah, já estou vendo a placa da chave dourada e a porta azul!' Com verbos dos sentidos basta o presente simples:", (None, 'I see'), 'estou vendo.']),
    (5, None, ["'Boa! A porta de enrolar está aberta?' A palavra", (None, 'shutter'), 'serve tanto para veneziana de janela quanto para a porta metálica de loja.']),
    (6, None, ["'Ele está destrancando agora mesmo! Fique na linha um segundo.' Para pedir que a pessoa não desligue, diga", (None, 'Stay on the phone'), "usando a preposição 'on'."]),
    (7, None, ["'Garanta que o anel de latão por dentro tenha vinte milímetros de largura.' Em medidas, o adjetivo fecha a expressão:", (None, 'twenty millimeters wide'), 'vinte milímetros de largura.']),
    (8, None, ["'Ele comparou com a velha. Ele ainda tem duas sobrando na prateleira!' Muito útil em compras,", (None, 'two left'), 'indica quantas unidades restam no estoque.']),
    (9, None, ["'Compre as duas! Uma válvula reserva salva o próximo inverno também.' Para se referir aos dois itens juntos basta", (None, 'Buy both'), 'compre ambas.']),
    (10, None, ["'Pago em dinheiro! Deixe sua caixa de ferramentas aberta, estou voltando correndo pela ponte!' Para pagamentos em espécie, lembre sempre de", (None, 'in cash'), 'em dinheiro vivo.']),
    (11, None, ["'Depressa, acabei de ouvir passos na escada do segundo andar!' Sozinha no começo da frase,", (None, 'Hurry'), "já vale por 'corra, depressa!'."]),
]
