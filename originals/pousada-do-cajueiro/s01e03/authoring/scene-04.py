ID = 'pousada-do-cajueiro-s01e03-scene-04'
SHOW, SEASON, EPISODE, SCENE = 'pousada-do-cajueiro', 1, 3, 4
TITLE = 'Vindo da chuva  (In from the Rain)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'camila': 'Camila', 'rafael': 'Rafael', 'bianca': 'Bianca'}

INTRO = ('Down in the lobby, soft-spoken traveller Rafael steps inside shaking out a wet umbrella. Camila greets him '
 'at the front desk while Bianca brings a dry towel and hot soup. Listen first.')
OPENER = "Let's listen again to how Camila breaks the news gently."
TRANSITION = "Now let's hear the whole lobby arrival scene once more."
OUTRO = ('Honesty, a dry towel, and a mug of hot soup kept everything calm and friendly. Next time, Rafael climbs '
 'the stairs to judge the third-floor attic for himself. See you next time.')
CLOSING = ('rafael', 'Até logo!')

STORY = [
    ('camila', 'Boa noite! Entre para sair da chuva, senhor.', 'Good evening! Come in out of the rain, sir.'),
    ('rafael', 'Boa noite. Desculpe molhar o chão limpo de vocês.', 'Good evening. Sorry for wetting your clean floor.'),
    ('camila', 'Imagina, não tem problema! O senhor deve ser o Rafael.', 'Not at all, no problem! You must be Rafael.'),
    ('rafael', 'Isso mesmo, Rafael. Eu reservei o quarto sete por telefone ontem.', "That's right, Rafael. I booked room seven by phone yesterday."),
    ('bianca', 'Aqui estão uma toalha seca e uma xícara de sopa quente, senhor.', 'Here are a dry towel and a cup of hot soup, sir.'),
    ('rafael', 'Sopa quente? Depois daquela caminhada fria na chuva, parece um sonho.', 'Hot soup? After that cold walk in the rain, that sounds wonderful.'),
    ('camila', 'Senhor, antes de subir, eu preciso pedir desculpas com toda sinceridade.', 'Sir, before going up, I need to apologize in all honesty.'),
    ('rafael', 'Ah, é? Aconteceu algum problema com a minha reserva?', 'Oh, really? Did some problem happen with my booking?'),
    ('camila', 'Por engano, colocamos dois hóspedes no quarto sete para hoje.', 'We accidentally booked two guests into room seven tonight.'),
    ('rafael', 'Puxa... com esta chuva? Todos os hotéis perto da rodoviária estavam lotados.', 'Gosh... in this rain? Every hotel near the bus station was packed.'),
    ('camila', 'Fique tranquilo! Preparamos o nosso estúdio silencioso do terceiro andar só para o senhor.', 'Do not worry! We prepared our quiet third-floor study just for you.'),
    ('rafael', 'Um estúdio no sótão? Posso conhecer o quarto primeiro?', 'An attic study? May I see the room first?'),
]

WALK = [(1,
  None,
  ["'Good evening. Sorry for wetting your clean floor.' Notice ",
   (None, 'molhar'),
   " turning 'wet' into a single action word: 'to get something wet'."]),
 (2,
  None,
  ["'Not at all, no problem! You must be Rafael.' When someone apologizes for something small, ",
   (None, 'Imagina,'),
   " literally 'imagine!', brushes the apology warmly aside like 'don't even think of it!'."]),
 (3,
  None,
  ["'That's right, Rafael. I booked room seven by phone yesterday.' Means of communication take 'by', so ",
   (None, 'por telefone'),
   " means 'by phone'."]),
 (6,
  None,
  ["'Sir, before going up, I need to apologize in all honesty.' Instead of a single word for 'apologize', "
   'Portuguese says ',
   (None, 'pedir desculpas'),
   " literally 'to ask excuses'."]),
 (7,
  None,
  ["'Oh, really? Did some problem happen with my booking?' Tiny ",
   (None, 'Ah, é?'),
   " literally 'oh, is it?', works just like a surprised 'oh, really?'."]),
 (9,
  None,
  ["'Gosh... in this rain? Every hotel near the bus station was packed.' Mild reaction ",
   (None, 'Puxa...'),
   ' expresses gentle dismay, and ',
   (None, 'lotados.'),
   ' means completely full or sold out.']),
 (10,
  None,
  ["'Do not worry! We prepared our quiet third-floor study just for you.' Adding ",
   (None, 'só para o senhor.'),
   " warmly emphasizes 'just for you'."]),
 (11,
  None,
  ["'An attic study? May I see the room first?' When viewing a room or visiting a place for the first time, ",
   (None, 'conhecer'),
   " means 'get to see' or 'check out'."])]
