# Authoring module for linden-courtyard-pt-s01e04-scene-07.
ID = 'linden-courtyard-pt-s01e04-scene-07'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 4
SCENE = 7
TITLE = 'Sunlight on the Tag  (Sol na etiqueta)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = 'Ao meio-dia, Graham abre o armário do corredor para arejar depois da tempestade e apoia a mala azul sem dono perto da recepção, bem quando a senhorita Evelyn chega para falar com Hannah. Ouça primeiro.'
OPENER = 'Vamos repassar cada frase desta cena.'
TRANSITION = 'Agora ouça a cena inteira de novo sem interrupções.'
OUTRO = 'A luz clara do sol sobre uma antiga etiqueta de bagagem acabou de revelar vinte e cinco anos de história: dois irmãos na rua Linden e o trenzinho de madeira do avô! Falta uma cena no episódio quatro.'
CLOSING = ('evelyn', 'Bye for now!')
STORY = [
    ('graham', 'Let me set this blue suitcase here for five minutes while I sweep the closet.', 'Deixe eu apoiar esta mala azul aqui por cinco minutos enquanto varro o armário.'),
    ('hannah', 'Careful with it, Graham. Tomorrow at noon is Friday!', 'Cuidado com ela, Graham. Amanhã ao meio-dia é sexta-feira!'),
    ('evelyn', "Oh, is that the twin suitcase from Monday's train?", 'Ah, essa é a mala gêmea do trem de segunda-feira?'),
    ('hannah', "Yes, ma'am, still waiting for its owner.", 'Sim, senhora, ainda esperando pelo dono.'),
    ('evelyn', 'May I look at the paper tag again here in the bright sunlight?', 'Posso olhar a etiqueta de papel de novo aqui na luz clara do sol?'),
    ('graham', "Go right ahead, ma'am. Monday afternoon the lobby was dark.", 'Fique à vontade, senhora. Na segunda-feira à tarde a recepção estava escura.'),
    ('evelyn', 'Wait a moment... Number twelve, Linden Street, and two childhood initials carved on the corner!', 'Espere um instante... Número doze da rua Linden, e duas iniciais de infância entalhadas no canto!'),
    ('hannah', 'Miss Evelyn, you look amazed! Do you know Number twelve, Linden Street?', 'Senhorita Evelyn, a senhora parece espantada! Conhece o número doze da rua Linden?'),
    ('evelyn', 'Know it? Every Friday for six years I climbed those wooden stairs to teach piano!', 'Se conheço? Toda sexta-feira durante seis anos eu subi aquela escada de madeira para ensinar piano!'),
    ('graham', 'Twenty-five years ago? In that same house?', 'Vinte e cinco anos atrás? Naquela mesma casa?'),
    ('evelyn', 'A carpenter lived there with his two grandsons. The older boy played piano, and the little one loved trains!', 'Um carpinteiro morava lá com seus dois netos. O menino mais velho tocava piano, e o pequeno adorava trens!'),
    ('hannah', 'A carpenter... and a little wooden toy train inside the bag!', 'Um carpinteiro... e um trenzinho de brinquedo de madeira dentro da mala!'),
]
WALK = [
    (0, None, ["'Deixe eu apoiar esta mala azul aqui por cinco minutos enquanto varro o armário.' Para indicar por quanto tempo algo dura, usamos", (None, 'for five minutes'), 'por cinco minutos.']),
    (1, None, ["'Cuidado com ela, Graham. Amanhã ao meio-dia é sexta-feira!' Meio-dia pede sempre a preposição pontual:", (None, 'at noon'), 'ao meio-dia.']),
    (2, None, ["'Ah, essa é a mala gêmea do trem de segunda-feira?' Usar", (None, 'twin suitcase'), 'é um jeito expressivo de dizer que as duas malas são idênticas.']),
    (3, None, ["'Sim, senhora, ainda esperando pelo dono.' Repare no possessivo neutro sem apóstrofo em", (None, 'waiting for its owner'), 'referindo-se ao dono da mala.']),
    (4, None, ["'Posso olhar a etiqueta de papel de novo aqui na luz clara do sol?' Para dizer 'ao sol' ou 'na luz do sol', o inglês usa 'in':", (None, 'in the bright sunlight'), 'na luz brilhante do sol.']),
    (5, None, ["'Fique à vontade, senhora. Na segunda-feira à tarde a recepção estava escura.' Para dar permissão de forma calorosa, use", (None, 'Go right ahead'), 'pode ir em frente, fique à vontade.']),
    (6, None, ["'Espere um instante... Número doze da rua Linden, e duas iniciais de infância entalhadas no canto!' A forma", (None, 'carved on the corner'), 'indica letras gravadas na madeira ou no couro.']),
    (7, None, ["'Senhorita Evelyn, a senhora parece espantada! Conhece o número doze da rua Linden?' Depois do verbo parecer visualmente, vem o adjetivo direto:", (None, 'you look amazed'), 'você parece maravilhada.']),
    (8, None, ["'Se conheço? Toda sexta-feira durante seis anos eu subi aquela escada de madeira para ensinar piano!' Depois de 'teach', instrumentos musicais podem vir sem artigo:", (None, 'teach piano'), 'dar aulas de piano.']),
    (9, None, ["'Vinte e cinco anos atrás? Naquela mesma casa?' A ordem em", (None, 'Twenty-five years ago'), "bate certinho com o nosso 'vinte e cinco anos atrás'."]),
    (10, None, ["'Um carpinteiro morava lá com seus dois netos. O menino mais velho tocava piano, e o pequeno adorava trens!' Para não repetir 'menino', entra o pronome", (None, 'the little one'), 'o pequenininho.']),
    (11, None, ["'Um carpinteiro... e um trenzinho de brinquedo de madeira dentro da mala!' Veja a sequência natural antes do substantivo em", (None, 'little wooden toy train'), 'tamanho, material e tipo.']),
]
