# Authoring module for linden-courtyard-pt-s01e04-scene-04.
ID = 'linden-courtyard-pt-s01e04-scene-04'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 4
SCENE = 4
TITLE = 'Down in the Cellar  (Lá embaixo no porão)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah'}
INTRO = 'Lá embaixo no porão de tijolos sob o pátio, Hannah entrega a nova válvula de latão a Graham enquanto segura firme uma lanterna iluminando a caldeira silenciosa. Vamos ouvir.'
OPENER = 'Vamos repassar o diálogo frase por frase.'
TRANSITION = 'Ouça novamente a cena inteira em velocidade natural.'
OUTRO = "Uma chama azul firme, canos de cobre esquentando e Graham chamando Hannah de 'parceira' em vez de 'novata'! Na próxima cena subimos para o café da manhã. Até a próxima."
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('hannah', 'Here are both brass valves, Graham! Catch my breath? Never!', 'Aqui estão as duas válvulas de latão, Graham! Recuperar o fôlego? Jamais!'),
    ('graham', 'Hold this flashlight steady on the pipe joint right here.', 'Segure esta lanterna bem firme na junta do cano bem aqui.'),
    ('hannah', 'Got it! Did you turn off the main water tap already?', 'Pode deixar! Você já fechou o registro geral de água?'),
    ('graham', 'Off and drained. Pass me the heavy wrench on your left.', 'Fechado e esvaziado. Me passe a chave inglesa pesada à sua esquerda.'),
    ('hannah', 'This big iron one? Here you go.', 'Esta grande de ferro? Aqui está.'),
    ('graham', 'One turn, two turns... look how clean that new brass thread fits.', 'Uma volta, duas voltas... veja como essa rosca nova de latão encaixa limpinho.'),
    ('hannah', 'No drips at all! Can we light the boiler now?', 'Nem um pingo sequer! Já podemos acender a caldeira agora?'),
    ('graham', 'Open the blue wheel slowly to the left, not too fast.', 'Abra a válvula azul devagar para a esquerda, não rápido demais.'),
    ('hannah', 'Turning slowly... listen! Water is rushing in!', 'Girando devagar... escute! A água está entrando com tudo!'),
    ('graham', 'And there goes the burner flame, steady blue, just how it should be.', 'E lá vai a chama do queimador, azul e firme, exatamente como deve ser.'),
    ('hannah', 'Touch the copper pipe! It is warming up already!', 'Toque no cano de cobre! Já está esquentando!'),
    ('graham', 'Three minutes to reach the third floor. Good run today, partner.', 'Três minutos para chegar ao terceiro andar. Boa corrida hoje, parceira.'),
]
WALK = [
    (0, None, ["'Aqui estão as duas válvulas de latão, Graham! Recuperar o fôlego? Jamais!' Depois de correr, a expressão natural para retomar o ar é", (None, 'Catch my breath'), 'recuperar meu fôlego.']),
    (1, None, ["'Segure esta lanterna bem firme na junta do cano bem aqui.' Em", (None, 'Hold this flashlight steady'), 'a palavra final pede para manter a mão firme sem balançar.']),
    (2, None, ["'Pode deixar! Você já fechou o registro geral de água?' Tanto para desligar aparelhos quanto para fechar registros de água usamos", (None, 'turn off'), 'fechar ou desligar.']),
    (3, None, ["'Fechado e esvaziado. Me passe a chave inglesa pesada à sua esquerda.' No inglês dos Estados Unidos, chave inglesa ou de boca chama-se", (None, 'wrench'), "com 'w' mudo na pronúncia."]),
    (4, None, ["'Esta grande de ferro? Aqui está.' Ao passar algo para a mão de alguém, diga", (None, 'Here you go'), 'informal e muito simpático.']),
    (5, None, ["'Uma volta, duas voltas... veja como essa rosca nova de latão encaixa limpinho.' Nas exclamações com 'how', o verbo vai para o fim:", (None, 'how clean that new brass thread fits'), 'como encaixa bem.']),
    (6, None, ["'Nem um pingo sequer! Já podemos acender a caldeira agora?' Aqui", (None, 'light the boiler'), "usa 'light' como verbo: acender o fogo da caldeira."]),
    (7, None, ["'Abra a válvula azul devagar para a esquerda, não rápido demais.' Antes de adjetivos ou advérbios,", (None, 'too fast'), "indica excesso: 'rápido demais'."]),
    (8, None, ["'Girando devagar... escute! A água está entrando com tudo!' O contínuo", (None, 'is rushing in'), 'mostra a água correndo depressa para dentro do encanamento.']),
    (9, None, ["'E lá vai a chama do queimador, azul e firme, exatamente como deve ser.' Guarde o fechamento", (None, 'just how it should be'), 'bem do jeito que tem de ser.']),
    (10, None, ["'Toque no cano de cobre! Já está esquentando!' Com a partícula 'up',", (None, 'is warming up'), 'expressa aquecer gradualmente.']),
    (11, None, ["'Três minutos para chegar ao terceiro andar. Boa corrida hoje, parceira.' Atenção: o verbo em", (None, 'reach the third floor'), "vai direto ao lugar sem preposição 'to' ou 'at'."]),
]
