# Authoring module for linden-courtyard-pt-s01e01-scene-06.
ID = 'linden-courtyard-pt-s01e01-scene-06'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 1
SCENE = 6
TITLE = 'The Luggage Tag  (A etiqueta da bagagem)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'arthur': 'Arthur'}
INTRO = 'De volta à recepção, Hannah, Evelyn e o proprietário Arthur se debruçam sobre a mala azul sob a luminária do balcão. Finalmente Arthur dá bom uso aos óculos. Ouça primeiro a cena.'
OPENER = 'Vamos repassar cada linha com tranquilidade.'
TRANSITION = 'Agora vamos escutar a cena inteira de novo sem pausas.'
OUTRO = 'Ainda nada na estação de trem, e o dono misterioso mora a apenas cinco minutos dali. Na próxima cena, Tessa entra em ação para salvar a noite de Evelyn.'
CLOSING = ('arthur', 'See you soon!')
STORY = [
    ('arthur', 'Dear me, what a mix-up! Let me look at the tag with my glasses.', 'Minha nossa, que confusão! Deixe-me olhar a etiqueta com meus óculos.'),
    ('evelyn', 'Is there a name or a phone number on it?', 'Tem algum nome ou número de telefone nela?'),
    ('arthur', 'No phone number, unfortunately. Only two initials and an old street name.', 'Nenhum número de telefone, infelizmente. Só duas iniciais e o nome de uma rua antiga.'),
    ('hannah', 'Wait, that street is right here in our neighborhood, five minutes away!', 'Espere, essa rua fica bem aqui no nosso bairro, a cinco minutos daqui!'),
    ('evelyn', 'How strange! We rode the same morning train to the same district.', 'Que estranho! Viemos no mesmo trem da manhã para o mesmo bairro.'),
    ('arthur', 'Hannah, call the station lost and found office right away.', 'Hannah, ligue já para o setor de achados e perdidos da estação.'),
    ('hannah', 'I am dialing now... Hello? Did anyone report a swapped blue suitcase?', 'Estou discando agora... Alô? Alguém comunicou uma mala azul trocada?'),
    ('evelyn', 'Tell them mine has a red ribbon inside the top pocket!', 'Diga a eles que a minha tem uma fita vermelha dentro do bolso de cima!'),
    ('hannah', 'Not yet? Please take our guesthouse number and address. Thank you!', 'Ainda não? Por favor, anote o telefone e o endereço da nossa pousada. Obrigada!'),
    ('arthur', "They have nothing yet, ma'am, I am terribly sorry.", 'Eles ainda não têm nada, senhora, sinto muitíssimo.'),
    ('evelyn', 'It is not your fault. Still, I only have the coat on my back!', 'Não é culpa sua. Mesmo assim, só tenho o casaco do corpo!'),
    ('hannah', 'Wait one moment, Tessa in the cafe just waved to me with an idea!', 'Espere um instante, a Tessa lá no café acabou de acenar para mim com uma ideia!'),
]
WALK = [
    (0, None, ["'Minha nossa, que confusão! Deixe-me olhar a etiqueta com meus óculos.' Para exclamar diante de uma bagunça ou troca, o inglês diz", (None, 'what a mix-up'), 'colocando o artigo indefinido no meio.']),
    (1, None, ["'Tem algum nome ou número de telefone nela?' Na pergunta sobre existência, basta inverter a ordem para", (None, 'Is there'), "igualzinho ao nosso 'tem algum...?'."]),
    (2, None, ["'Nenhum número de telefone, infelizmente. Só duas iniciais e o nome de uma rua antiga.' Colocado direto antes do substantivo,", (None, 'No phone number'), "significa 'nenhum número de telefone'."]),
    (3, None, ["'Espere, essa rua fica bem aqui no nosso bairro, a cinco minutos daqui!' Para indicar distância no tempo ou no espaço, o inglês fecha a expressão com", (None, 'five minutes away'), 'a cinco minutos de distância.']),
    (4, None, ["'Que estranho! Viemos no mesmo trem da manhã para o mesmo bairro.' Quando a exclamação traz só um adjetivo sem substantivo, usamos", (None, 'How strange'), 'que estranho!']),
    (5, None, ["'Hannah, ligue já para o setor de achados e perdidos da estação.' Curiosamente o inglês inverte a nossa ordem consagrada e diz", (None, 'lost and found'), 'perdidos e achados.']),
    (6, None, ["'Estou discando agora... Alô? Alguém comunicou uma mala azul trocada?' Nas perguntas no passado, o auxiliar assume a marca do tempo em", (None, 'Did anyone report'), 'e o verbo principal volta à forma básica.']),
    (7, None, ["'Diga a eles que a minha tem uma fita vermelha dentro do bolso de cima!' O pronome", (None, 'mine'), "vale sozinho por 'a minha', sem artigo antes."]),
    (8, None, ["'Ainda não? Por favor, anote o telefone e o endereço da nossa pousada. Obrigada!' Duas palavrinhas essenciais ao telefone:", (None, 'Not yet'), 'ainda não.']),
    (9, None, ["'Eles ainda não têm nada, senhora, sinto muitíssimo.' Para pedir desculpas com bastante ênfase,", (None, 'terribly sorry'), 'é super idiomático e educado.']),
    (10, None, ["'Não é culpa sua. Mesmo assim, só tenho o casaco do corpo!' Veja duas ótimas expressões juntas:", (None, 'It is not your fault'), "para 'não é culpa sua' e", (None, 'the coat on my back'), 'a roupa do corpo.']),
    (11, None, ["'Espere um instante, a Tessa lá no café acabou de acenar para mim com uma ideia!' O advérbio curto em", (None, 'just waved'), 'mostra que o gesto acabou de acontecer há poucos segundos.']),
]
