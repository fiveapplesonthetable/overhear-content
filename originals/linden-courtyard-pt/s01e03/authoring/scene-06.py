# Authoring module for linden-courtyard-pt-s01e03-scene-06.
ID = 'linden-courtyard-pt-s01e03-scene-06'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 3
SCENE = 6
TITLE = 'A Five-Star Sigh of Relief  (Um suspiro de alívio cinco estrelas)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = 'De volta ao balcão do térreo, Arthur anda de um lado para o outro ansioso até Hannah descer sorrindo ao encontro dele e de Tessa. Então Hannah nota um objeto deixado ao lado da campainha. Vamos ouvir.'
OPENER = 'Vamos repassar cada frase da conversa com calma.'
TRANSITION = 'Ouça novamente toda a cena em ritmo natural.'
OUTRO = 'Desenhos caprichados a lápis e uma nota nove de dez convenceram os três de que Caleb é um inspetor secreto de guia de viagens, bem na hora em que um estalo metálico ecoa pela casa! Até a próxima.'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('arthur', 'Well? Did he shout? Did he ask for his money back?', 'E então? Ele gritou? Pediu o dinheiro de volta?'),
    ('hannah', 'Neither! He loved the quiet roof beams and thanked us.', 'Nem uma coisa nem outra! Ele adorou as vigas silenciosas do telhado e nos agradeceu.'),
    ('arthur', 'Hannah, you have a gift for hospitality! My blood pressure is saved!', 'Hannah, você leva muito jeito para a hospitalidade! Minha pressão arterial está salva!'),
    ('tessa', 'He even finished every drop of vegetable soup before going up.', 'Ele até tomou cada gota da sopa de legumes antes de subir.'),
    ('hannah', 'Wait, whose small brown leather notebook is this on the counter?', 'Esperem, de quem é este pequeno caderno de couro marrom no balcão?'),
    ('tessa', 'Caleb set it down when he took the dry towel from me!', 'O Caleb o apoiou aí quando pegou a toalha seca da minha mão!'),
    ('arthur', 'Do not snoop, of course... wait, it fell open to the middle page!', 'Não bisbilhotem, é claro... esperem, ele caiu aberto bem na página do meio!'),
    ('hannah', 'Why are there neat pencil drawings of three guesthouses on our street?', 'Por que tem desenhos caprichados a lápis de três pousadas da nossa rua?'),
    ('tessa', "Look at the words beside ours: 'Courtyard width, street noise, quiet score: nine out of ten!'", "Olhem as palavras ao lado da nossa: 'Largura do pátio, barulho da rua, nota de silêncio: nove de dez!'"),
    ('arthur', 'Nine out of ten?! Nobody measures lobbies unless...', 'Nove de dez?! Ninguém mede recepções a não ser que...'),
    ('tessa', 'Unless he writes for the annual Portland Travel Guide!', 'A não ser que ele escreva para o Guia Anual de Viagens de Portland!'),
    ('hannah', 'Quick, close it! Let us take it upstairs... wait, what is that loud clanking sound?', 'Rápido, feche isso! Vamos levar lá para cima... esperem, que barulho alto de metal batendo é esse?'),
]
WALK = [
    (0, None, ["'E então? Ele gritou? Pediu o dinheiro de volta?' Veja como", (None, 'ask for his money back'), "fecha com 'back' para dar toda a ideia de devolução."]),
    (1, None, ["'Nem uma coisa nem outra! Ele adorou as vigas silenciosas do telhado e nos agradeceu.' Para negar duas perguntas seguidas de uma vez só,", (None, 'Neither'), "responde 'nenhum dos dois'."]),
    (2, None, ["'Hannah, você leva muito jeito para a hospitalidade! Minha pressão arterial está salva!' A expressão", (None, 'have a gift for'), 'elogia um dom natural para lidar com pessoas.']),
    (3, None, ["'Ele até tomou cada gota da sopa de legumes antes de subir.' Depois de 'before' indicando ação, o verbo ganha '-ing':", (None, 'before going up'), 'antes de subir.']),
    (4, None, ["'Esperem, de quem é este pequeno caderno de couro marrom no balcão?' Para perguntar a quem pertence algo,", (None, 'whose'), 'vem grudado antes do substantivo e seus adjetivos.']),
    (5, None, ["'O Caleb o apoiou aí quando pegou a toalha seca da minha mão!' O verbo com partícula", (None, 'set it down'), 'mostra o gesto de pousar um objeto sobre o balcão.']),
    (6, None, ["'Não bisbilhotem, é claro... esperem, ele caiu aberto bem na página do meio!' A dupla", (None, 'fell open'), 'descreve um caderno que se abre sozinho ao cair na mesa.']),
    (7, None, ["'Por que tem desenhos caprichados a lápis de três pousadas da nossa rua?' Para perguntar 'por que há...?' no plural, o inglês inverte para", (None, 'Why are there'), "antes de 'drawings'."]),
    (8, None, ["'Olhem as palavras ao lado da nossa: Largura do pátio, barulho da rua, nota de silêncio: nove de dez!' Em notas e avaliações usa-se sempre", (None, 'nine out of ten'), 'nove em dez.']),
    (9, None, ["'Nove de dez?! Ninguém mede recepções a não ser que...' A conjunção", (None, 'unless'), "concentra numa palavra só o nosso 'a menos que' ou 'a não ser que'."]),
    (10, None, ["'A não ser que ele escreva para o Guia Anual de Viagens de Portland!' Enquanto o português pede subjuntivo, o inglês segue no presente simples:", (None, 'Unless he writes'), 'com esse no verbo.']),
    (11, None, ["'Rápido, feche isso! Vamos levar lá para cima... esperem, que barulho alto de metal batendo é esse?' A expressão", (None, 'clanking sound'), 'imita o próprio som pesado de ferro batendo em ferro.']),
]
