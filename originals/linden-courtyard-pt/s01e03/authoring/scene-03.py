# Authoring module for linden-courtyard-pt-s01e03-scene-03.
ID = 'linden-courtyard-pt-s01e03-scene-03'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 3
SCENE = 3
TITLE = 'Left at the Landing  (À esquerda no patamar)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'hannah': 'Hannah', 'tessa': 'Tessa', 'arthur': 'Arthur'}
INTRO = 'Dez minutos antes das oito, Hannah, Tessa e Arthur dão os retoques finais no quarto do terceiro andar. Cada detalhe importa antes que o viajante chegue da chuva. Ouça primeiro.'
OPENER = 'Vamos conferir cada frase com calma.'
TRANSITION = 'Agora vamos ouvir a cena inteira novamente.'
OUTRO = 'A luminária de latão já ilumina o quarto com luz acolhedora bem na hora em que toca o sino lá embaixo. Na próxima cena, Caleb entra fugindo da chuva. Até logo.'
CLOSING = ('hannah', 'Bye for now!')
STORY = [
    ('tessa', 'Tuck that sheet corner tight, Hannah! Here go the two soft pillows.', 'Prenda bem firme esse canto do lençol, Hannah! Aqui vão os dois travesseiros macios.'),
    ('hannah', 'Done! And the blue rug fits right beside the bed.', 'Pronto! E o tapete azul cabe certinho ao lado da cama.'),
    ('arthur', 'Where should I hang this round mirror? Left of the window or right?', 'Onde eu devo pendurar este espelho redondo? À esquerda da janela ou à direita?'),
    ('hannah', 'Right beside the desk, where the light is good.', 'Bem ao lado da escrivaninha, onde a luz é boa.'),
    ('tessa', "Plug in Graham's brass lamp... oh, look how warm that yellow light is!", 'Ligue na tomada a luminária de latão do Graham... ah, veja como essa luz amarela é aconchegante!'),
    ('arthur', 'Honestly, I almost want to sleep up here myself tonight!', 'Sinceramente, quase dá vontade de eu mesmo dormir aqui em cima hoje à noite!'),
    ('hannah', 'Wait, what discount should we offer him for changing rooms?', 'Espere, que desconto devemos oferecer a ele por trocar de quarto?'),
    ('arthur', 'Half price for tonight, and free breakfast all week!', 'Metade do preço por hoje à noite e café da manhã grátis a semana toda!'),
    ('tessa', 'Generous! Did you just hear the courtyard gate bell downstairs?', 'Que generoso! Vocês acabaram de ouvir o sino do portão lá embaixo?'),
    ('hannah', "Eight o'clock on the dot! Our guest is here!", 'Oito horas em ponto! Nosso hóspede chegou!'),
    ('arthur', 'My heart is pounding! Hannah, you explain it, you sound calm and honest!', 'Meu coração está disparado! Hannah, explique você, sua voz soa calma e sincera!'),
    ('hannah', 'Leave it to me. Let us go down and welcome him.', 'Deixe comigo. Vamos descer e dar as boas-vindas a ele.'),
]
WALK = [
    (0, None, ["'Prenda bem firme esse canto do lençol, Hannah! Aqui vão os dois travesseiros macios.' Em", (None, 'Tuck that sheet corner tight'), 'a última palavra mostra o resultado desejado: lençol bem esticado.']),
    (1, None, ["'Pronto! E o tapete azul cabe certinho ao lado da cama.' Colocar", (None, 'right beside'), "dá exatamente o tom do nosso 'bem ao lado de'."]),
    (2, None, ["'Onde eu devo pendurar este espelho redondo? À esquerda da janela ou à direita?' Para pedir opinião sobre o que fazer agora,", (None, 'Where should I hang'), 'é natural e educado.']),
    (3, None, ["'Bem ao lado da escrivaninha, onde a luz é boa.' O trecho", (None, 'where the light is good'), 'explica o motivo da escolha com palavras simples.']),
    (4, None, ["'Ligue na tomada a luminária de latão do Graham... ah, veja como essa luz amarela é aconchegante!' Para conectar qualquer aparelho na tomada usa-se o verbo com partícula", (None, 'Plug in'), 'plugar na tomada.']),
    (5, None, ["'Sinceramente, quase dá vontade de eu mesmo dormir aqui em cima hoje à noite!' O pronome", (None, 'myself'), "entra só para dar ênfase, exatamente como o nosso 'eu mesmo'."]),
    (6, None, ["'Espere, que desconto devemos oferecer a ele por trocar de quarto?' Depois de preposições em inglês, o verbo ganha sempre '-ing', como em", (None, 'for changing rooms'), 'por trocar de quarto.']),
    (7, None, ["'Metade do preço por hoje à noite e café da manhã grátis a semana toda!' Duas expressões essenciais de viagem:", (None, 'Half price'), 'pela metade do preço e', (None, 'free breakfast'), 'café da manhã incluso sem custo.']),
    (8, None, ["'Que generoso! Vocês acabaram de ouvir o sino do portão lá embaixo?' No inglês americano,", (None, 'Did you just hear'), "traduz direitinho o nosso 'acabou de ouvir?'."]),
    (9, None, ["'Oito horas em ponto! Nosso hóspede chegou!' Para dizer que alguém chegou cravado no horário,", (None, 'on the dot'), "equivale a 'em ponto'."]),
    (10, None, ["'Meu coração está disparado! Hannah, explique você, sua voz soa calma e sincera!' Manter o pronome antes do comando em", (None, 'you explain it'), "destaca quem deve falar: 'explique você'."]),
    (11, None, ["'Deixe comigo. Vamos descer e dar as boas-vindas a ele.' A frase curta", (None, 'Leave it to me'), 'é perfeita para assumir uma tarefa e tranquilizar o grupo.']),
]
