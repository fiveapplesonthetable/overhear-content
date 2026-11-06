ID = 'pousada-do-cajueiro-s01e02-scene-01'
SHOW, SEASON, EPISODE, SCENE = 'pousada-do-cajueiro', 1, 2, 1
TITLE = 'A fita vermelha  (The Red Ribbon)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'camila': 'Camila', 'helena': 'Helena', 'jorge': 'Jorge'}

INTRO = ('Tuesday morning arrives bright and sunny at the Cashew Tree Guesthouse in Recife. Helena hurries '
 'downstairs to the front desk, where Camila and Jorge have her returned suitcase waiting. Listen to the '
 'whole scene first.')
OPENER = "Let's go back through their Tuesday morning reunion one line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = ('Helena has her teacup and dresses back, and a twenty-five-year-old memory is starting to stir. Next time, '
 'an urgent problem hits the breakfast kitchen. See you next time.')
CLOSING = ('helena', 'Até logo!')

STORY = [('camila',
  'Bom dia, Dona Helena! Olhe o que chegou ao nosso portão ontem à noite.',
  'Good morning, Madam Helena! Look what arrived at our gate last night.'),
 ('helena',
  'A minha mala! Deixe eu abrir o bolso de cima... sim, a minha fita vermelha!',
  'My suitcase! Let me open the top pocket... yes, my red ribbon!'),
 ('jorge',
  'E a sua xícara lá dentro? Continua inteira?',
  'And your teacup inside? Is it still in one piece?'),
 ('helena',
  'Nem um rachado! Quem trouxe a mala de volta?',
  'Not a single crack! Who brought the suitcase back?'),
 ('camila',
  'A gente não sabe. Alguém deixou a mala no degrau e tocou o sino.',
  'We do not know. Someone left the suitcase on the step and rang the bell.'),
 ('helena',
  'E ele não pediu a própria mala com o trenzinho de madeira?',
  'And he did not ask for his own suitcase with the wooden train?'),
 ('jorge',
  'Ele deixou um bilhete curto pedindo para guardar tudo até sexta-feira.',
  'He left a short note asking us to keep everything until Friday.'),
 ('helena',
  'Que curioso! A letra daquela etiqueta pareceu tão familiar para mim.',
  'How curious! The handwriting on that tag looked so familiar to me.'),
 ('camila', 'Mesmo? A senhora conhece alguém aqui no Recife?', 'Really? Do you know someone here in Recife?'),
 ('helena',
  'Vinte e cinco anos atrás eu dei aulas de piano perto daqui.',
  'Twenty-five years ago I gave piano lessons near here.'),
 ('jorge',
  'Por enquanto, a mala dele fica bem trancada a sete chaves.',
  'For now, his suitcase stays safely locked away.'),
 ('helena',
  'Ótimo! Agora estou pronta para um grande café da manhã.',
  'Great! Now I am ready for a big breakfast.')]

WALK = [(0,
  None,
  ["'Good morning, Madam Helena! Look what arrived at our gate last night.' Notice ",
   (None, 'ontem à noite.'),
   " literally 'yesterday at night', where English says 'last night'."]),
 (1,
  None,
  ["'My suitcase! Let me open the top pocket... yes, my red ribbon!' Top and bottom pockets are named with "
   'plain position words, so ',
   (None, 'o bolso de cima...'),
   " literally says 'the pocket of up top'."]),
 (2,
  None,
  ["'And your teacup inside? Is it still in one piece?' Using ",
   (None, 'Continua inteira?'),
   " literally asks 'does it continue whole?', a natural way to ask if something fragile survived "
   'unbroken.']),
 (7,
  None,
  ["'How curious! The handwriting on that tag looked so familiar to me.' Everyday ",
   (None, 'A letra'),
   " means both an individual alphabet letter and a person's handwriting."]),
 (8,
  None,
  ["'Really? Do you know someone here in Recife?' Portuguese splits 'to know' in two: ",
   (None, 'conhece'),
   ' is for knowing a person or a city, whereas facts take the word Camila used in line five.']),
 (9,
  None,
  ["'Twenty-five years ago I gave piano lessons near here.' Putting ",
   (None, 'atrás'),
   " after a span of time literally says 'twenty-five years behind', just like English 'ago'."]),
 (10,
  None,
  ["'For now, his suitcase stays safely locked away.' Colourful expression ",
   (None, 'a sete chaves.'),
   " literally says 'under seven keys', the classic Portuguese image for locking something up tight."]),
 (11,
  None,
  ["'Great! Now I am ready for a big breakfast.' Unlike most descriptors, ",
   (None, 'grande'),
   ' comes before the meal here to mean a hearty, generous spread.'])]
