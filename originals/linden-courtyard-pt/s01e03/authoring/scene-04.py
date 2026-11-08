# Authoring module for linden-courtyard-pt-s01e03-scene-04.
ID = 'linden-courtyard-pt-s01e03-scene-04'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 3
SCENE = 4
TITLE = 'In from the Rain  (Entrando da chuva)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'hannah': 'Hannah', 'caleb': 'Caleb', 'tessa': 'Tessa'}
INTRO = 'Lá embaixo na recepção, Caleb, um viajante tranquilo de trinta e poucos anos, entra sacudindo o guarda-chuva molhado. Hannah o recebe no balcão enquanto Tessa traz uma toalha seca. Vamos ouvir primeiro.'
OPENER = 'Vamos repassar o diálogo linha por linha.'
TRANSITION = 'Agora ouça a cena completa mais uma vez no ritmo natural.'
OUTRO = 'Sinceridade, uma toalha seca e uma xícara de sopa quente mantiveram a conversa tranquila. Na próxima cena, Caleb sobe a escada para conhecer o sótão. Até a próxima.'
CLOSING = ('caleb', 'See you soon!')
STORY = [
    ('hannah', 'Good evening! Come inside out of the rain, sir.', 'Boa noite! Entre para sair da chuva, senhor.'),
    ('caleb', 'Good evening. Sorry for dripping water on your clean floor.', 'Boa noite. Desculpe por pingar água no seu piso limpo.'),
    ('hannah', 'Do not worry at all! You must be Caleb.', 'Não se preocupe nem um pouco! O senhor deve ser o Caleb.'),
    ('caleb', 'Yes, Caleb. I booked room seven by phone yesterday.', 'Sim, Caleb. Eu reservei o quarto sete por telefone ontem.'),
    ('tessa', 'Here is a dry towel for your coat and a cup of hot soup, sir.', 'Aqui está uma toalha seca para o seu casaco e uma xícara de sopa quente, senhor.'),
    ('caleb', 'Hot soup? After that cold walk in the rain, that sounds wonderful.', 'Sopa quente? Depois daquela caminhada fria na chuva, isso parece maravilhoso.'),
    ('hannah', 'Sir, before we go upstairs, I owe you an honest apology.', 'Senhor, antes de subirmos, eu lhe devo um pedido sincero de desculpas.'),
    ('caleb', 'Oh? Is there a problem with my booking?', 'Ah, é? Há algum problema com a minha reserva?'),
    ('hannah', 'We accidentally booked two guests into room seven tonight.', 'Por engano, colocamos dois hóspedes no quarto sete hoje à noite.'),
    ('caleb', 'Ah... in this rain? Every hotel near the station looked full.', 'Ah... nessa chuva? Todos os hotéis perto da estação pareciam lotados.'),
    ('hannah', 'Please do not worry! We prepared our quiet third floor attic study just for you.', 'Por favor, não se preocupe! Preparamos nosso silencioso estúdio do sótão no terceiro andar especialmente para o senhor.'),
    ('caleb', 'An attic study? May I see it first?', 'Um estúdio no sótão? Posso vê-lo primeiro?'),
]
WALK = [
    (0, None, ["'Boa noite! Entre para sair da chuva, senhor.' Repare como o inglês junta o movimento para dentro e para fora do mau tempo em", (None, 'inside out of the rain'), 'para dentro, longe da chuva.']),
    (1, None, ["'Boa noite. Desculpe por pingar água no seu piso limpo.' Para pedir desculpa por algo que está acontecendo,", (None, 'Sorry for dripping'), "combina 'sorry for' com o verbo em '-ing'."]),
    (2, None, ["'Não se preocupe nem um pouco! O senhor deve ser o Caleb.' Acrescentar", (None, 'at all'), "no fim de uma frase negativa reforça a gentileza: 'nem um pouco'."]),
    (3, None, ["'Sim, Caleb. Eu reservei o quarto sete por telefone ontem.' Ao indicar o meio de comunicação usamos", (None, 'by phone'), "sem artigo no meio, igual a 'por telefone'."]),
    (4, None, ["'Aqui está uma toalha seca para o seu casaco e uma xícara de sopa quente, senhor.' Ao entregar algo às mãos de alguém,", (None, 'Here is a dry towel'), "funciona como um acolhedor 'aqui está'."]),
    (5, None, ["'Sopa quente? Depois daquela caminhada fria na chuva, isso parece maravilhoso.' Quando uma ideia parece ótima logo ao ouvir, responda", (None, 'that sounds wonderful'), 'isso soa maravilhoso.']),
    (6, None, ["'Senhor, antes de subirmos, eu lhe devo um pedido sincero de desculpas.' O verbo em", (None, 'I owe you'), 'serve tanto para valores quanto para favores e desculpas.']),
    (7, None, ["'Ah, é? Há algum problema com a minha reserva?' Invertendo a ordem para", (None, 'Is there a problem'), "transformamos 'há' na pergunta direta 'tem algum problema?'."]),
    (8, None, ["'Por engano, colocamos dois hóspedes no quarto sete hoje à noite.' O verbo", (None, 'booked'), 'é o jeito mais direto de dizer que alguém foi registrado ou hospedado numa reserva.']),
    (9, None, ["'Ah... nessa chuva? Todos os hotéis perto da estação pareciam lotados.' Onde dizemos 'todos os hotéis' no plural, o inglês prefere o singular com", (None, 'Every hotel'), 'cada hotel.']),
    (10, None, ["'Por favor, não se preocupe! Preparamos nosso silencioso estúdio do sótão no terceiro andar especialmente para o senhor.' O final", (None, 'just for you'), "transmite cuidado especial: 'só para você'."]),
    (11, None, ["'Um estúdio no sótão? Posso vê-lo primeiro?' Para pedir permissão com bastante educação,", (None, 'May I see it'), "soa mais cortês e elegante do que 'can'."]),
]
