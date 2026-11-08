# Authoring module for linden-courtyard-pt-s01e01-scene-05.
ID = 'linden-courtyard-pt-s01e01-scene-05'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 1
SCENE = 5
TITLE = 'Not My Clothes!  (Não são as minhas roupas!)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'evelyn': 'Evelyn', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'Dois minutos depois de subirem, a campainha do quarto quatro toca na recepção — não duas vezes, mas quatro seguidas. Hannah sobe correndo e encontra Evelyn e Graham olhando para a mala aberta. Ouça primeiro.'
OPENER = 'Vamos entender cada frase dessa surpresa com calma.'
TRANSITION = 'Vamos ouvir toda a cena novamente em ritmo natural.'
OUTRO = 'Em vez de vestidos e partituras, a mala azul guarda sapatos masculinos grandes e um trenzinho de madeira. Na próxima cena vamos ver o que está escrito na etiqueta.'
CLOSING = ('hannah', 'Goodbye!')
STORY = [
    ('hannah', 'Miss Evelyn, is everything all right? You rang the bell!', 'Dona Evelyn, está tudo bem? A senhora tocou a campainha!'),
    ('evelyn', 'Look inside this suitcase, Hannah! This is not my bag!', 'Olhe dentro desta mala, Hannah! Esta não é a minha mala!'),
    ('hannah', 'Wait, it is dark blue, just like yours!', 'Espere, ela é azul-escura, igualzinha à sua!'),
    ('evelyn', 'The outside is identical, yes! But look inside!', 'Por fora é idêntica, sim! Mas olhe lá dentro!'),
    ('graham', "Two pairs of big brown men's shoes and gray sweaters.", 'Dois pares de sapatos masculinos marrons grandes e suéteres cinzas.'),
    ('hannah', 'And what is this wrapped in white paper? A little wooden train!', 'E o que é isto embrulhado em papel branco? Um trenzinho de madeira!'),
    ('evelyn', 'I certainly do not wear size eleven shoes!', 'Eu certamente não calço sapatos tamanho onze!'),
    ('graham', 'No wonder it was so heavy. Wood and leather!', 'Não admira que estivesse tão pesada. Madeira e couro!'),
    ('evelyn', 'Someone at the train station took my blue suitcase by mistake!', 'Alguém na estação de trem pegou minha mala azul por engano!'),
    ('hannah', "Please sit down, ma'am. Do not worry, we will check the tag right now.", 'Sente-se, por favor, senhora. Não se preocupe, vamos conferir a etiqueta agora mesmo.'),
    ('graham', 'There is a small paper card tied to the side handle.', 'Tem um cartãozinho de papel amarrado na alça lateral.'),
    ('evelyn', 'Oh, let us bring it downstairs to the light!', 'Ah, vamos levá-la lá para baixo, perto da luz!'),
]
WALK = [
    (0, None, ["'Dona Evelyn, está tudo bem? A senhora tocou a campainha!' Usar", (None, 'Miss Evelyn'), 'com o primeiro nome traz um respeito caloroso e acolhedor, muito comum em pousadas americanas.']),
    (1, None, ["'Olhe dentro desta mala, Hannah! Esta não é a minha mala!' Para negar com o verbo ser, basta colocar a negação logo depois dele em", (None, 'This is not my bag'), 'de forma bem clara.']),
    (2, None, ["'Espere, ela é azul-escura, igualzinha à sua!' No fim da frase,", (None, 'just like yours'), 'usa o possessivo autônomo para não precisar repetir a palavra mala.']),
    (3, None, ["'Por fora é idêntica, sim! Mas olhe lá dentro!' Veja que contraste fácil de gravar:", (None, 'The outside'), 'para o lado de fora e', (None, 'inside'), 'para o lado de dentro.']),
    (4, None, ["'Dois pares de sapatos masculinos marrons grandes e suéteres cinzas.' Mesmo num plural irregular que não termina em esse, a posse ganha apóstrofo e esse em", (None, "men's shoes"), 'sapatos de homem.']),
    (5, None, ["'E o que é isto embrulhado em papel branco? Um trenzinho de madeira!' Da palavra madeira nasce o adjetivo tradicional em", (None, 'wooden train'), 'trem feito de madeira.']),
    (6, None, ["'Eu certamente não calço sapatos tamanho onze!' Para roupas, sapatos, chapéus ou óculos no corpo, o inglês usa sempre", (None, 'wear'), 'tanto para vestir quanto para calçar.']),
    (7, None, ["'Não admira que estivesse tão pesada. Madeira e couro!' A dupla", (None, 'No wonder'), "abre a frase com o sentido exato de 'não é à toa' ou 'não admira'."]),
    (8, None, ["'Alguém na estação de trem pegou minha mala azul por engano!' Guarde o bloco fixo", (None, 'by mistake'), "que aparece o tempo todo para dizer 'por engano'."]),
    (9, None, ["'Sente-se, por favor, senhora. Não se preocupe, vamos conferir a etiqueta agora mesmo.' Acalmar alguém em inglês começa quase sempre com", (None, 'Do not worry'), 'não se preocupe.']),
    (10, None, ["'Tem um cartãozinho de papel amarrado na alça lateral.' Onde falamos 'tem um cartão' no Brasil, o inglês apresenta a existência com", (None, 'There is'), 'nunca com o verbo ter.']),
    (11, None, ["'Ah, vamos levá-la lá para baixo, perto da luz!' Convites em grupo começam com", (None, 'let us bring it downstairs'), "e uma palavra só já indica 'para o andar de baixo'."]),
]
