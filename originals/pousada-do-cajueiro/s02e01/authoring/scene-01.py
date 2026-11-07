ID = 'pousada-do-cajueiro-s02e01-scene-01'
SHOW, SEASON, EPISODE, SCENE = 'pousada-do-cajueiro', 2, 1, 1
TITLE = 'A nona chave  (The Ninth Key)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'otavio': 'Otávio', 'jorge': 'Jorge', 'camila': 'Camila'}

INTRO = ('It is early Saturday morning at the Cashew Tree Guesthouse in Recife, just hours after Jorge carried a '
 'dusty cedar box stamped Room Nine up from the cellar. Camila and Otavio lean over the front desk as Jorge '
 'turns the tiny brass key. Listen to the scene first.')
OPENER = "Let's go back through the box opening one line at a time."
TRANSITION = "Now let's hear the whole front-desk scene again from the top."
OUTRO = ('Inside the cedar box sit a heavy door key and a floor plan pointing straight behind the hallway bookcase. '
 "Don't worry if a word or two went past quickly; they come back soon. See you next time.")
CLOSING = ('camila', 'Até mais!')

STORY = [('otavio',
  'Gire a chave pequena devagar, Jorge, meu coração está acelerado!',
  'Turn the small key slowly, Jorge, my heart is racing!'),
 ('jorge',
  'Calma, chefe. Fechadura de latão do porão nunca quebra.',
  'Relax, boss. A brass lock from the cellar never breaks.'),
 ('camila', 'Abriu! Levante a tampa de madeira, Jorge!', 'It opened! Lift the wooden lid, Jorge!'),
 ('jorge',
  'Aqui dentro tem uma chave grande, uma planta azul e uns postais.',
  "In here there's a big key, a blue floor plan and some postcards."),
 ('otavio',
  'Leia o papel azul dobrado! Cadê os meus óculos?',
  'Read the folded blue paper! Where are my glasses?'),
 ('camila',
  'Continuam na sua testa, Seu Otávio, desde ontem à noite.',
  "They're still on your forehead, Mr. Otavio, since last night."),
 ('otavio',
  'Ah! Olhe aqui: Térreo, Quarto Nove, Jardim de Inverno!',
  'Aha! Look here: Ground Floor, Room Nine, Sunroom!'),
 ('camila',
  'Espere, a gente tem um jardim de inverno no térreo?!',
  'Wait, we have a sunroom on the ground floor?!'),
 ('jorge',
  'Olhem a seta atrás da estante do corredor dos fundos.',
  'Look at the arrow behind the bookcase in the back hallway.'),
 ('otavio',
  'Aquela estante pesada está nessa parede há vinte anos!',
  'That heavy bookcase has been against that wall for twenty years!'),
 ('camila',
  'Então atrás dos livros velhos tem uma nona porta!',
  "So behind the old books there's a ninth door!"),
 ('jorge',
  'Primeiro um gole de café, depois a gente tira os livros.',
  'First a sip of coffee, then we take the books out.')]

WALK = [(0,
  None,
  ["'Turn the small key slowly, Jorge, my heart is racing!' The command ",
   (None, 'Gire'),
   ' comes from the verb for spinning, the same root you find in the word for sunflower, the flower that '
   'turns to follow the sun.']),
 (1,
  None,
  ["'Relax, boss. A brass lock from the cellar never breaks.' Jorge's teasing title for the owner, ",
   (None, 'chefe,'),
   ' came into Portuguese from French, just like the English word chef.']),
 (3,
  None,
  ["'In here there's a big key, a blue floor plan and some postcards.' In a garden a ",
   (None, 'planta'),
   ' is a plant, but on paper it is the floor plan of a building.']),
 (4,
  None,
  ["'Read the folded blue paper! Where are my glasses?' Brazilian speakers in a hurry skip the textbook "
   'question and say ',
   (None, 'Cadê'),
   ", a spoken squeeze of three old words meaning roughly 'what became of'."]),
 (5,
  None,
  ["'They're still on your forehead, Mr. Otavio, since last night.' Camila says ",
   (None, 'Continuam'),
   ", a plural verb, because the Portuguese word for glasses is always plural, like English 'glasses'."]),
 (6,
  None,
  ["'Aha! Look here: Ground Floor, Room Nine, Sunroom!' A glassed-in sunroom is literally a winter garden, ",
   (None, 'Jardim de Inverno'),
   ', even in warm Recife.']),
 (9,
  None,
  ["'That heavy bookcase has been against that wall for twenty years!' Where English says 'has been', "
   'Portuguese keeps the present ',
   (None, 'está'),
   ' and adds the little time marker ',
   (None, 'há vinte anos'),
   '.']),
 (11,
  None,
  ["'First a sip of coffee, then we take the books out.' One ",
   (None, 'gole'),
   ' is a single swallow, and Jorge plans exactly one before the heavy lifting.'])]
