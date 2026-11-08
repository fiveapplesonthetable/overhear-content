# Authoring module for linden-courtyard-pt-s01e04-scene-01.
ID = 'linden-courtyard-pt-s01e04-scene-01'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 4
SCENE = 1
TITLE = 'Six Forty-Five  (Seis e quarenta e cinco)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah'}
INTRO = 'São seis e quarenta e cinco da manhã na pousada Linden Courtyard Inn, em Portland. Enquanto os hóspedes ainda dormem lá em cima, Graham desenha no papel um mapa rápido das ruas para Hannah. Ouça primeiro toda a cena em inglês.'
OPENER = 'Agora vamos repassar a conversa com calma, frase por frase.'
TRANSITION = 'Vamos ouvir toda a cena novamente em velocidade natural.'
OUTRO = 'À esquerda no portão, atravessar a ponte, passar pela farmácia verde e virar na pracinha: Hannah já partiu na missão do amanhecer. Até a próxima.'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('hannah', 'Good morning, Graham! Are the showers upstairs really cold already?', 'Bom dia, Graham! Os chuveiros lá em cima já estão mesmo frios?'),
    ('graham', 'Cold as river water. Take this broken brass valve in your coat pocket.', 'Frios como água de rio. Leve esta válvula de latão quebrada no bolso do seu casaco.'),
    ('hannah', 'Got it. Now tell me how to find the hardware shop.', 'Entendido. Agora me diga como encontrar a loja de ferragens.'),
    ('graham', 'Turn left outside our gate and walk straight to the stone bridge.', 'Vire à esquerda saindo do nosso portão e siga reto até a ponte de pedra.'),
    ('hannah', 'Left at the gate, straight to the bridge. Do I cross the river?', 'À esquerda no portão, reto até a ponte. Eu atravesso o rio?'),
    ('graham', 'Yes, cross the bridge, then pass the green pharmacy on your right.', 'Sim, atravesse a ponte e depois passe pela farmácia verde à sua direita.'),
    ('hannah', 'Bridge, then green pharmacy on the right. And after that?', 'Ponte, depois farmácia verde à direita. E depois disso?'),
    ('graham', 'Turn left into the small square. Look for a blue wooden door.', 'Vire à esquerda entrando na pracinha. Procure uma porta de madeira azul.'),
    ('hannah', 'Does the shop have a big sign outside?', 'A loja tem uma placa grande do lado de fora?'),
    ('graham', 'Only a painted golden key above the door. Show the clerk this valve.', 'Só uma chave dourada pintada acima da porta. Mostre esta válvula ao balconista.'),
    ('hannah', 'Twenty millimeters, brass, boiler valve. I will repeat it all the way!', 'Vinte milímetros, latão, válvula de caldeira. Vou repetir isso o caminho inteiro!'),
    ('graham', 'Run fast, Hannah. Room four wakes up at seven fifteen!', 'Corra rápido, Hannah. O quarto quatro acorda às sete e quinze!'),
]
WALK = [
    (0, None, ["'Bom dia, Graham! Os chuveiros lá em cima já estão mesmo frios?' Repare como", (None, 'Are the showers upstairs'), 'coloca a localização logo depois do substantivo sem preposição.']),
    (1, None, ["'Frios como água de rio. Leve esta válvula de latão quebrada no bolso do seu casaco.' A comparação curta", (None, 'Cold as river water'), 'soa direta e natural na fala cotidiana.']),
    (2, None, ["'Entendido. Agora me diga como encontrar a loja de ferragens.' Curtíssimo e super usado,", (None, 'Got it'), "confirma 'peguei' ou 'entendi' na hora."]),
    (3, None, ["'Vire à esquerda saindo do nosso portão e siga reto até a ponte de pedra.' Ao pedir ou dar direções na rua, guarde o bloco", (None, 'walk straight to'), 'caminhe reto até.']),
    (4, None, ["'À esquerda no portão, reto até a ponte. Eu atravesso o rio?' Quando você confere um caminho passo a passo, usa o presente simples em", (None, 'Do I cross'), 'eu atravesso?']),
    (5, None, ["'Sim, atravesse a ponte e depois passe pela farmácia verde à sua direita.' Para indicar o lado da rua usa-se a preposição 'on':", (None, 'on your right'), 'à sua direita.']),
    (6, None, ["'Ponte, depois farmácia verde à direita. E depois disso?' A perguntinha", (None, 'And after that'), 'é ótima para puxar a próxima etapa de qualquer explicação.']),
    (7, None, ["'Vire à esquerda entrando na pracinha. Procure uma porta de madeira azul.' Ao virar entrando num espaço novo, juntamos", (None, 'Turn left into'), 'indicando movimento para dentro da praça.']),
    (8, None, ["'A loja tem uma placa grande do lado de fora?' No final da frase,", (None, 'outside'), "resolve sozinho o nosso 'do lado de fora'."]),
    (9, None, ["'Só uma chave dourada pintada acima da porta. Mostre esta válvula ao balconista.' Veja a ordem sem preposição em", (None, 'Show the clerk this valve'), 'primeiro quem recebe, depois o objeto.']),
    (10, None, ["'Vinte milímetros, latão, válvula de caldeira. Vou repetir isso o caminho inteiro!' A expressão", (None, 'all the way'), 'cobre todo o percurso do começo ao fim.']),
    (11, None, ["'Corra rápido, Hannah. O quarto quatro acorda às sete e quinze!' O verbo com partícula", (None, 'wakes up'), 'significa acordar, e o horário é dito número por número:', (None, 'seven fifteen'), 'sete e quinze.']),
]
