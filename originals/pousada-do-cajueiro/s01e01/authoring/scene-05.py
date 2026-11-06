ID = 'pousada-do-cajueiro-s01e01-scene-05'
SHOW, SEASON, EPISODE, SCENE = 'pousada-do-cajueiro', 1, 1, 5
TITLE = 'Não são as minhas roupas!  (Not My Clothes!)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'camila': 'Camila', 'helena': 'Helena', 'jorge': 'Jorge'}

INTRO = ("Two minutes after going upstairs, Room 4's buzzer rings at the desk—not twice, but four times in a row. "
 'Camila hurries upstairs to find Helena and Jorge staring into the open blue suitcase. Listen first.')
OPENER = "Now let's go back through the surprise in Room 4 line by line."
TRANSITION = "Now let's hear the whole scene once more from start to finish."
OUTRO = ('Instead of dresses and sheet music, the dark-blue suitcase holds size forty-two shoes and a carved wooden '
 "train. Let's check that paper tag downstairs next time. See you next time.")
CLOSING = ('camila', 'Até logo!')

STORY = [('camila',
  'Dona Helena, está tudo bem? A senhora tocou a campainha!',
  'Madam Helena, is everything alright? You rang the bell!'),
 ('helena',
  'Olhe dentro desta mala, Camila! Esta mala não é minha!',
  'Look inside this suitcase, Camila! This suitcase is not mine!'),
 ('camila', 'Espere, ela é azul-escura, igual à sua!', 'Wait, it is dark blue, just like yours!'),
 ('helena',
  'Por fora é igual, sim! Mas olhe aqui dentro!',
  'On the outside it is identical, yes! But look in here!'),
 ('jorge',
  'Dois pares de sapatos marrons grandes e blusas cinzas.',
  'Two pairs of big brown shoes and grey sweaters.'),
 ('camila',
  'E o que é isto embrulhado em papel branco? Um trenzinho de madeira!',
  'And what is this wrapped in white paper? A little wooden train!'),
 ('helena',
  'Eu com certeza não calço tamanho quarenta e dois!',
  'I certainly do not wear shoe size forty-two!'),
 ('jorge', 'Por isso estava tão pesada. Madeira e couro!', 'That is why it was so heavy. Wood and leather!'),
 ('helena',
  'Alguém na rodoviária pegou a minha mala azul por engano!',
  'Someone at the bus station took my blue suitcase by mistake!'),
 ('camila',
  'Pode sentar, senhora. Fique tranquila, a gente vai olhar a etiqueta agora.',
  'Please sit down, madam. Do not worry, we will check the tag now.'),
 ('jorge',
  'Tem um cartão pequeno amarrado na alça do lado.',
  'There is a small card tied to the side handle.'),
 ('helena', 'Ah, vamos descer com ela para a luz!', 'Oh, let us go downstairs with it to the light!')]

WALK = [(0,
  None,
  ["'Madam Helena, is everything alright? You rang the bell!' Pairing ",
   (None, 'Dona'),
   " with a woman's first name is the counterpart to the polite male title—warm, polite Brazilian respect."]),
 (1,
  None,
  ["'Look inside this suitcase, Camila! This suitcase is not mine!' Putting ",
   (None, 'minha!'),
   " at the end means 'mine', matching the feminine gender of 'suitcase'."]),
 (3,
  None,
  ["'On the outside it is identical, yes! But look in here!' Short contrast ",
   (None, 'Por fora'),
   " literally says 'by outside', a neat two-word chunk opposite 'inside'."]),
 (5,
  None,
  ["'And what is this wrapped in white paper? A little wooden train!' From the word for 'train', Portuguese "
   'builds affectionate ',
   (None, 'trenzinho'),
   ' for a small toy train, followed by ',
   (None, 'de madeira!'),
   " meaning 'made of wood'."]),
 (6,
  None,
  ["'I certainly do not wear shoe size forty-two!' Portuguese has a dedicated action word just for shoes: ",
   (None, 'calço'),
   " means 'I wear on my feet', and size ",
   (None, 'quarenta e dois!'),
   " is a large men's shoe in Recife."]),
 (7,
  None,
  ["'That is why it was so heavy. Wood and leather!' Two-word connector ",
   (None, 'Por isso'),
   " literally means 'for that', working just like 'no wonder' or 'that's why'."]),
 (8,
  None,
  ["'Someone at the bus station took my blue suitcase by mistake!' In Brazilian Portuguese, an intercity "
   'coach terminal is a ',
   (None, 'rodoviária'),
   ' built from the word for highway, and ',
   (None, 'por engano!'),
   " means 'by mistake'."]),
 (9,
  None,
  ["'Please sit down, madam. Do not worry, we will check the tag now.' Reassuring ",
   (None, 'Fique tranquila,'),
   " literally tells Helena 'stay calm', a gentle phrase people in Recife use constantly to put someone at "
   'ease.'])]
