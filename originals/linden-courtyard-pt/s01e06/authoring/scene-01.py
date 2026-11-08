# Authoring module for linden-courtyard-pt-s01e06-scene-01.
ID = 'linden-courtyard-pt-s01e06-scene-01'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 6
SCENE = 1
TITLE = 'At the Iron Gate  (No portão de ferro)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'caleb': 'Caleb', 'owen': 'Owen', 'hannah': 'Hannah'}
INTRO = 'Lá fora, à sombra da árvore na pousada Linden Courtyard Inn, em Portland, o irmão mais velho, Owen, permanece de pé em seu casaco cinza diante de Caleb enquanto Hannah apoia um bule quente na mesa e se afasta discretamente. Ouça primeiro toda a cena.'
OPENER = 'Agora vamos repassar a conversa com calma, frase por frase.'
TRANSITION = 'Vamos ouvir toda a cena novamente em velocidade natural.'
OUTRO = 'Owen reconheceu a letra de Caleb em dois segundos e veio mesmo assim! Na próxima cena eles abrem o pacote de papel branco debaixo da árvore do pátio. Até a próxima.'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('owen', "So 'someone with something from Grandfather' was you all along, Caleb.", "Então 'alguém com uma lembrança do vovô' era você o tempo todo, Caleb."),
    ('caleb', 'Hello, Owen. Thank you for coming today.', 'Olá, Owen. Obrigado por vir hoje.'),
    ('owen', 'I recognized your neat block handwriting on that postcard in two seconds.', 'Eu reconheci a sua letra de forma caprichada naquele cartão-postal em dois segundos.'),
    ('caleb', 'Wait, you knew it was from me and came anyway?', 'Espere, você sabia que era meu e veio mesmo assim?'),
    ('owen', 'Of course I came. Why did you hide behind a mystery note?', 'Claro que eu vim. Por que você se escondeu atrás de um bilhete misterioso?'),
    ('caleb', 'Because I was afraid you were still angry. I missed you these three years.', 'Porque fiquei com medo de você ainda estar bravo. Senti sua falta nestes três anos.'),
    ('owen', 'Three stubborn years... honestly, little brother, I missed you too.', 'Três anos de teimosia... sinceramente, irmãozinho, eu também senti sua falta.'),
    ('hannah', 'Excuse me, gentlemen. Here is hot tea, and warm lemon cake is on the way.', 'Com licença, cavalheiros. Aqui está o chá quente, e o bolo morno de limão já está a caminho.'),
    ('owen', 'Lemon cake? Wait, how did she know about Friday lemon cake?', 'Bolo de limão? Espere, como ela sabia do bolo de limão de sexta-feira?'),
    ('caleb', 'Sit down, Owen, take off your heavy coat, and look at this blue suitcase.', 'Sente-se, Owen, tire seu casaco pesado e olhe esta mala azul.'),
    ('owen', "Is that the old dark blue bag from Grandfather's workshop?", 'Essa é a velha mala azul-escura da oficina do vovô?'),
    ('hannah', 'Take all the time you need. The courtyard is yours.', 'Fiquem o tempo que precisarem. O pátio é de vocês.'),
]
WALK = [
    (0, None, ["'Então alguém com uma lembrança do vovô era você o tempo todo, Caleb.' Veja como", (None, 'was you all along'), "concorda com 'someone' no singular: era você desde o começo."]),
    (1, None, ["'Olá, Owen. Obrigado por vir hoje.' A primeira frase simples da Hannah quebra o gelo na hora:", (None, 'Thank you for coming today'), 'direta e sincera.']),
    (2, None, ["'Eu reconheci a sua letra de forma caprichada naquele cartão-postal em dois segundos.' Para letra de forma, sem emendar as letras, o inglês diz", (None, 'block handwriting'), 'letra em bloco.']),
    (3, None, ["'Espere, você sabia que era meu e veio mesmo assim?' No final da pergunta,", (None, 'came anyway'), "significa exatamente 'veio mesmo assim'."]),
    (4, None, ["'Claro que eu vim. Por que você se escondeu atrás de um bilhete misterioso?' Em inglês não entra 'que' depois de 'claro': diga direto", (None, 'Of course I came'), 'claro que vim.']),
    (5, None, ["'Porque fiquei com medo de você ainda estar bravo. Senti sua falta nestes três anos.' Para dizer 'ter medo', o inglês usa o verbo ser ou estar com adjetivo:", (None, 'I was afraid'), 'eu estava com medo.']),
    (6, None, ["'Três anos de teimosia... sinceramente, irmãozinho, eu também senti sua falta.' Simples e emocionante,", (None, 'I missed you too'), 'fecha três anos de silêncio.']),
    (7, None, ["'Com licença, cavalheiros. Aqui está o chá quente, e o bolo morno de limão já está a caminho.' Muito usada no dia a dia,", (None, 'is on the way'), 'avisa que algo ou alguém já está chegando.']),
    (8, None, ["'Bolo de limão? Espere, como ela sabia do bolo de limão de sexta-feira?' Para saber a respeito de um assunto ou segredo, junte", (None, 'know about'), 'saber sobre.']),
    (9, None, ["'Sente-se, Owen, tire seu casaco pesado e olhe esta mala azul.' Para tirar casaco, sapatos ou chapéu, use sempre", (None, 'take off'), 'tirar do corpo.']),
    (10, None, ["'Essa é a velha mala azul-escura da oficina do vovô?' Repare novamente na posse com apóstrofo em", (None, "Grandfather's workshop"), 'a oficina do vovô.']),
    (11, None, ["'Fiquem o tempo que precisarem. O pátio é de vocês.' Duas frases cheias de acolhimento:", (None, 'Take all the time you need'), 'sem pressa, e', (None, 'is yours'), 'é de vocês.']),
]
