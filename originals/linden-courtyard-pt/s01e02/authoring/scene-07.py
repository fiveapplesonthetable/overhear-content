# Authoring module for linden-courtyard-pt-s01e02-scene-07.
ID = 'linden-courtyard-pt-s01e02-scene-07'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 2
SCENE = 7
TITLE = 'How Regulars Order  (Como os clientes habituais pedem)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'tessa': 'Tessa', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'Sob o sol calmo da tarde, Hannah faz uma pausa de dez minutos no cantinho do café enquanto Tessa limpa o balcão e Graham aperta o pé bambo de uma cadeira de madeira. Ouça primeiro.'
OPENER = 'Vamos conferir cada frase dessa pausa da tarde.'
TRANSITION = 'Vamos escutar a cena inteira de novo em ritmo natural.'
OUTRO = 'Uma xícara tranquila de café, uma cadeira firme e três colegas que já começam a formar um verdadeiro time. Falta uma cena no episódio dois — e Arthur está prestes a fazer uma descoberta preocupante. Até já.'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('tessa', 'Sit down, Hannah! You ran half the city this morning, drink some coffee.', 'Sente-se, Hannah! Você correu metade da cidade hoje de manhã, tome um café.'),
    ('hannah', 'Gladly! With milk and a little sugar, please.', 'Com prazer! Com leite e um pouquinho de açúcar, por favor.'),
    ('graham', 'Watch that corner chair, wait ten seconds while I tighten this screw.', 'Cuidado com essa cadeira do canto, espere dez segundos enquanto aperto este parafuso.'),
    ('hannah', 'Done already? You carry a screwdriver everywhere, Graham!', 'Já terminou? Você carrega uma chave de fenda para todo lado, Graham!'),
    ('graham', 'Old houses loosen one screw every Tuesday. Now sit.', 'Casas antigas afrouxam um parafuso toda terça-feira. Agora sente.'),
    ('tessa', 'Look, you survived the breakfast rush and the mystery phone call!', 'Olha só, você sobreviveu à correria do café da manhã e ao telefonema misterioso!'),
    ('hannah', 'Honestly, I like it here much better than my old gray office.', 'Sinceramente, gosto muito mais daqui do que do meu antigo escritório cinza.'),
    ('tessa', 'Wait until Friday at noon, I want a front row seat when the suitcase man walks in!', 'Espere até sexta-feira ao meio-dia, quero um lugar na primeira fila quando o homem da mala entrar!'),
    ('graham', 'Nobody stares at guests. We hand over the bag and mind our business.', 'Ninguém fica encarando os hóspedes. Entregamos a mala e cuidamos da nossa vida.'),
    ('tessa', 'Listen to him! Graham is twice as curious as we are!', 'Olha só para ele! O Graham está duas vezes mais curioso do que nós!'),
    ('graham', 'I am simply checking security. That is my job.', 'Estou simplesmente conferindo a segurança. Esse é o meu trabalho.'),
    ('hannah', 'Sure, Graham, your secret is safe with us!', 'Claro, Graham, seu segredo está seguro com a gente!'),
]
WALK = [
    (0, None, ["'Sente-se, Hannah! Você correu metade da cidade hoje de manhã, tome um café.' Repare na posição direta sem preposição em", (None, 'half the city'), 'metade da cidade.']),
    (1, None, ["'Com prazer! Com leite e um pouquinho de açúcar, por favor.' Com substantivos incontáveis como açúcar, 'um pouquinho de' vira", (None, 'a little sugar'), 'direto antes do nome.']),
    (2, None, ["'Cuidado com essa cadeira do canto, espere dez segundos enquanto aperto este parafuso.' Do adjetivo 'apertado' forma-se o verbo", (None, 'tighten'), 'apertar ou firmar um parafuso.']),
    (3, None, ["'Já terminou? Você carrega uma chave de fenda para todo lado, Graham!' O nome da ferramenta", (None, 'screwdriver'), 'junta parafuso com a ideia de girar e conduzir.']),
    (4, None, ["'Casas antigas afrouxam um parafuso toda terça-feira. Agora sente.' Aqui aparece o verbo exatamente oposto ao anterior:", (None, 'loosen'), 'afrouxar ou soltar.']),
    (5, None, ["'Olha só, você sobreviveu à correria do café da manhã e ao telefonema misterioso!' Diferente do português, sobreviver não pede preposição em inglês:", (None, 'survived the breakfast rush'), 'sobreviveu ao horário de pico.']),
    (6, None, ["'Sinceramente, gosto muito mais daqui do que do meu antigo escritório cinza.' Para intensificar a comparação irregular, juntamos", (None, 'much better than'), 'muito melhor do que.']),
    (7, None, ["'Espere até sexta-feira ao meio-dia, quero um lugar na primeira fila quando o homem da mala entrar!' Onde usamos futuro do subjuntivo 'quando ele entrar', o inglês usa presente simples:", (None, 'when the suitcase man walks in'), 'quando ele entrar.']),
    (8, None, ["'Ninguém fica encarando os hóspedes. Entregamos a mala e cuidamos da nossa vida.' Olhar fixamente é", (None, 'stares at'), "e 'cuidar da própria vida' se diz", (None, 'mind our business'), 'cuidar dos nossos assuntos.']),
    (9, None, ["'Olha só para ele! O Graham está duas vezes mais curioso do que nós!' Comparações com 'o dobro de' usam a moldura", (None, 'twice as curious as'), 'duas vezes tão curioso quanto.']),
    (10, None, ["'Estou simplesmente conferindo a segurança. Esse é o meu trabalho.' Para falar da sua função ou cargo, a palavra contável certa é", (None, 'my job'), 'minha função.']),
    (11, None, ["'Claro, Graham, seu segredo está seguro com a gente!' A frase pronta", (None, 'your secret is safe with us'), 'promete guardar segredo em tom de brincadeira amiga.']),
]
