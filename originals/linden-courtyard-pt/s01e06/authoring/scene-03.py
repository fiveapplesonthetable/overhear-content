# Authoring module for linden-courtyard-pt-s01e06-scene-03.
ID = 'linden-courtyard-pt-s01e06-scene-03'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 6
SCENE = 3
TITLE = 'Thirty Days on Paper  (Trinta dias no papel)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'De volta atrás do balcão da recepção, Arthur está abatido ao lado do quadro de chaves enquanto Graham e Hannah conversam baixinho debruçados sobre o balcão. Ouça primeiro.'
OPENER = 'Vamos repassar cada frase desta conversa.'
TRANSITION = 'Agora ouça a cena inteira novamente sem pausas.'
OUTRO = 'Hannah lembrou que eles têm um especialista em prédios históricos com pátio sentado bem debaixo da árvore! Na próxima cena, Tessa leva o bolo e Owen percebe que algo preocupa a equipe lá dentro.'
CLOSING = ('graham', 'Bye for now!')
STORY = [
    ('arthur', 'Fifteen years of polishing brass keys and straightening ties... gone in thirty days!', 'Quinze anos lustrando chaves de latão e alinhando gravatas... perdidos em trinta dias!'),
    ('graham', 'Stop burying us before we read the whole document, Arthur.', 'Pare de nos enterrar antes de lermos o documento inteiro, Arthur.'),
    ('hannah', 'Yes! Earlier I noticed a second page clipped behind the cover letter.', 'Sim! Mais cedo eu notei uma segunda página presa com clipe atrás da carta principal.'),
    ('arthur', 'Legal paragraphs give me a headache even with two pairs of glasses!', 'Parágrafos jurídicos me dão dor de cabeça até com dois pares de óculos!'),
    ('graham', 'This house survived eighty winters and one broken boiler valve yesterday.', 'Esta casa sobreviveu a oitenta invernos e a uma válvula de caldeira quebrada ontem.'),
    ('hannah', 'Wait, who is sitting ten meters away in our courtyard right now?', 'Esperem, quem está sentado a dez metros daqui no nosso pátio agora mesmo?'),
    ('arthur', 'Two brothers eating lemon cake?', 'Dois irmãos comendo bolo de limão?'),
    ('hannah', 'An architect who works with historic courtyard buildings all over Portland!', 'Um arquiteto que trabalha com prédios históricos com pátio por toda Portland!'),
    ('graham', 'Smart thinking, Hannah. Caleb reads city building rules every single week.', 'Bem pensado, Hannah. O Caleb lê regras municipais de construção toda santa semana.'),
    ('arthur', 'Oh, I could never bother a paying guest with our landlord troubles!', 'Ah, eu jamais poderia incomodar um hóspede pagante com nossos problemas de aluguel!'),
    ('hannah', 'After we guarded his blue suitcase all week? He will want to help!', 'Depois de guardarmos a mala azul dele a semana toda? Ele vai querer ajudar!'),
    ('graham', 'Wait, here comes Tessa back from their table right now.', 'Esperem, lá vem a Tessa voltando da mesa deles agora mesmo.'),
]
WALK = [
    (0, None, ["'Quinze anos lustrando chaves de latão e alinhando gravatas... perdidos em trinta dias!' Depois de 'of' os verbos vêm com '-ing', e", (None, 'gone in thirty days'), "resume 'acabados em trinta dias'."]),
    (1, None, ["'Pare de nos enterrar antes de lermos o documento inteiro, Arthur.' Depois de 'stop', o verbo em '-ing'", (None, 'Stop burying us'), 'indica parar de vez com aquela atitude.']),
    (2, None, ["'Sim! Mais cedo eu notei uma segunda página presa com clipe atrás da carta principal.' Em documentos formais,", (None, 'cover letter'), 'é a carta de apresentação na frente.']),
    (3, None, ["'Parágrafos jurídicos me dão dor de cabeça até com dois pares de óculos!' Em inglês, dor de cabeça é contável e pede artigo:", (None, 'give me a headache'), 'me dão dor de cabeça.']),
    (4, None, ["'Esta casa sobreviveu a oitenta invernos e a uma válvula de caldeira quebrada ontem.' Note que", (None, 'survived eighty winters'), "não usa preposição depois de 'survived'."]),
    (5, None, ["'Esperem, quem está sentado a dez metros daqui no nosso pátio agora mesmo?' Para indicar distância acrescentamos 'away':", (None, 'ten meters away'), 'a dez metros de distância.']),
    (6, None, ["'Dois irmãos comendo bolo de limão?' Igualzinho ao português,", (None, 'Two brothers eating'), "usa o '-ing' direto depois do substantivo."]),
    (7, None, ["'Um arquiteto que trabalha com prédios históricos com pátio por toda Portland!' Para dizer 'pela cidade inteira', use", (None, 'all over Portland'), 'por toda Portland.']),
    (8, None, ["'Bem pensado, Hannah. O Caleb lê regras municipais de construção toda santa semana.' O elogio curto", (None, 'Smart thinking'), 'valoriza um raciocínio rápido na hora.']),
    (9, None, ["'Ah, eu jamais poderia incomodar um hóspede pagante com nossos problemas de aluguel!' Juntar 'could' e 'never' em", (None, 'I could never bother'), 'demonstra grande delicadeza.']),
    (10, None, ["'Depois de guardarmos a mala azul dele a semana toda? Ele vai querer ajudar!' Cheia de confiança,", (None, 'He will want to help'), 'garante que ele terá prazer em ajudar.']),
    (11, None, ["'Esperem, lá vem a Tessa voltando da mesa deles agora mesmo.' Com nomes próprios em", (None, 'here comes Tessa'), 'o verbo vem antes do nome para anunciar quem está chegando.']),
]
