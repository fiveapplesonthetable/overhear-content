ID = 'pousada-do-cajueiro-s02e01-scene-02'
SHOW, SEASON, EPISODE, SCENE = 'pousada-do-cajueiro', 2, 1, 2
TITLE = 'Tirem os livros  (Move the Books)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'bianca': 'Bianca', 'camila': 'Camila', 'jorge': 'Jorge'}

INTRO = ('In the quiet back hallway behind the kitchen, Camila and Jorge stand before a tall wooden bookcase packed '
 "with old travel guides. Bianca hurries out of the café corner, wiping flour from her hands. Let's listen "
 'in first.')
OPENER = "Let's take the bookcase apart again, one line at a time."
TRANSITION = "Now let's hear the whole hallway scene from start to finish."
OUTRO = ('The heavy bookcase is pushed aside, and the hidden lock turns on the very first try. Lift, pull, turn: '
 'those action words will keep coming back. See you next time.')
CLOSING = ('bianca', 'Tchau, gente!')

STORY = [('bianca',
  'É verdade? Tem mesmo um quarto secreto atrás da minha cozinha?',
  'Is it true? Is there really a secret room behind my kitchen?'),
 ('camila',
  'Me ajuda a colocar esses livros verdes na cadeira, Bianca.',
  'Help me put these green books on the chair, Bianca.'),
 ('jorge',
  'Tirem a prateleira de cima primeiro, assim a madeira fica leve.',
  'Take off the top shelf first, that way the wood gets light.'),
 ('bianca',
  'Esses guias de viagem são mais velhos que nós duas, Camila!',
  'These travel guides are older than the two of us, Camila!'),
 ('camila',
  'É a última prateleira. Vamos puxar no três, Jorge?',
  "That's the last shelf. Shall we pull on three, Jorge?"),
 ('jorge',
  'Um, dois, três! Puxem o lado esquerdo para mim!',
  'One, two, three! Pull the left side toward me!'),
 ('bianca',
  'Olhem atrás da madeira! Tinta branca e uma fechadura de latão!',
  'Look behind the wood! White paint and a brass lock!'),
 ('camila',
  'Uma porta de verdade, escondida aqui no corredor!',
  'A real door, hidden right here in the hallway!'),
 ('jorge', 'Vamos testar a chave grande da caixa de cedro.', "Let's try the big key from the cedar box."),
 ('bianca', 'Ela gira, Jorge?', 'Does it turn, Jorge?'),
 ('jorge',
  'Uma volta firme para a direita... e o trinco abriu!',
  'One firm turn to the right... and the latch is open!'),
 ('camila',
  'Levante a maçaneta primeiro, igual à porta da frente!',
  'Lift the handle first, just like the front door!')]

WALK = [(0,
  None,
  ["'Is it true? Is there really a secret room behind my kitchen?' Tucked in after the verb, ",
   (None, 'mesmo'),
   " works like 'really', turning a plain question into an amazed one."]),
 (1,
  None,
  ["'Help me put these green books on the chair, Bianca.' Between friends Camila says ",
   (None, 'Me ajuda'),
   ", with the little 'me' up front, the relaxed Brazilian way to ask a colleague for help."]),
 (2,
  None,
  ["'Take off the top shelf first, that way the wood gets light.' The shelf at the top is simply the shelf ",
   (None, 'de cima'),
   ", literally 'of above'; the bottom one would be the shelf of below."]),
 (3,
  None,
  ["'These travel guides are older than the two of us, Camila!' Two women say ",
   (None, 'nós duas'),
   ', with the feminine word for two; two men would use the masculine one.']),
 (5,
  None,
  ["'One, two, three! Pull the left side toward me!' Jorge gives orders to both women at once, so the ending "
   'of ',
   (None, 'Puxem'),
   " is the plural 'you all' command."]),
 (7,
  None,
  ["'A real door, hidden right here in the hallway!' The word ",
   (None, 'escondida'),
   ' ends in an a because it describes the door, which is feminine in Portuguese.']),
 (10,
  None,
  ["'One firm turn to the right... and the latch is open!' A full turn of a key is a ",
   (None, 'volta'),
   ', the same word Brazilian speakers use for coming back home.']),
 (11,
  None,
  ["'Lift the handle first, just like the front door!' Swap in anything after ",
   (None, 'igual à'),
   " to say 'just like'; here it joins with the feminine word for the door."])]
