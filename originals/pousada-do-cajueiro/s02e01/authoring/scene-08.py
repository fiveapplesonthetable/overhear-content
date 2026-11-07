ID = 'pousada-do-cajueiro-s02e01-scene-08'
SHOW, SEASON, EPISODE, SCENE = 'pousada-do-cajueiro', 2, 1, 8
TITLE = "Não toque nesse interruptor  (Don't Touch That Switch)"
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'jorge': 'Jorge', 'otavio': 'Otávio', 'camila': 'Camila'}

INTRO = ('Back at the doorway of Room Nine, Jorge opens his leather tool bag to inspect the old brass wall switch, '
 'but an excited Otavio reaches past him, right beside Camila. Listen first.')
OPENER = "Let's replay that one fateful click, line by line."
TRANSITION = "Now let's listen to the whole scene again from the start."
OUTRO = ('One impatient click from Otavio blows the ground-floor fuse and shows that Room Nine needs new wiring '
 "before Friday. That's the end of the first episode of season two. See you in the next one.")
CLOSING = ('jorge', 'Até a próxima, pessoal!')

STORY = [('jorge',
  'Espere um minuto antes de tocar nesse interruptor de latão, chefe.',
  'Wait a minute before you touch that brass switch, boss.'),
 ('otavio',
  'Esperar por quê? Eu lembro desta luminária de vidro, olhe como ela brilha!',
  'Why wait? I remember this glass lamp, look how it shines!'),
 ('camila',
  'Seu Otávio, espere, o Jorge está com a chave de fenda na mão!',
  'Mr. Otavio, wait, Jorge has the screwdriver in his hand!'),
 ('otavio', 'Só um clique rápido... Ai, meu Deus!', 'Just one quick click... Oh, my goodness!'),
 ('camila', 'Que estouro foi esse no corredor?!', 'What was that bang in the hallway?!'),
 ('jorge',
  'Foi o fio velho queimando o fusível principal do térreo.',
  'That was the old wire blowing the main ground-floor fuse.'),
 ('otavio',
  'A luz da recepção apagou! Será que eu quebrei o forno da cozinha também?!',
  'The reception light went out! Did I break the kitchen oven too?!'),
 ('camila',
  'Ih, já estou ouvindo a Bianca chamando lá da cozinha escura!',
  'Uh-oh, I can already hear Bianca calling from the dark kitchen!'),
 ('jorge',
  'Fio de pano de trinta anos, chefe. Nunca ligue um interruptor antes de eu olhar.',
  'Thirty-year-old cloth wire, boss. Never flip a switch before I look.'),
 ('otavio',
  'Você consegue consertar antes do almoço, Jorge? Diga que tem fusível sobrando!',
  'Can you fix it before lunch, Jorge? Tell me you have spare fuses!'),
 ('jorge',
  'A cozinha eu resolvo em dois minutos, mas o Quarto Nove precisa de fio novo.',
  'The kitchen I can sort out in two minutes, but Room Nine needs new wire.'),
 ('camila',
  'Segure a lanterna, Seu Otávio. A nossa contagem de seis dias começou!',
  'Hold the flashlight, Mr. Otavio. Our six-day countdown has begun!')]

WALK = [(0,
  None,
  ["'Wait a minute before you touch that brass switch, boss.' Touching a thing needs a little 'on' in "
   'Portuguese, so ',
   (None, 'tocar nesse'),
   " is literally 'touch on that'."]),
 (2,
  None,
  ["'Mr. Otavio, wait, Jorge has the screwdriver in his hand!' A screwdriver is a ",
   (None, 'chave de fenda,'),
   ' literally a key for a slot, and Brazilian speakers say someone is with a tool, ',
   (None, 'está com,'),
   ' when they are holding it.']),
 (4,
  None,
  ["'What was that bang in the hallway?!' A sudden pop or bang is an ",
   (None, 'estouro,'),
   ' the same word for a balloon bursting or popcorn popping.']),
 (5,
  None,
  ["'That was the old wire blowing the main ground-floor fuse.' A fuse doesn't blow in Portuguese, it "
   'burns: ',
   (None, 'queimando'),
   ' is the word for burning, used for blown bulbs and fuses alike.']),
 (6,
  None,
  ["'The reception light went out! Did I break the kitchen oven too?!' Opening with ",
   (None, 'Será que'),
   " turns a sentence into a worried 'I wonder if', perfect for a nervous owner."]),
 (8,
  None,
  ["'Thirty-year-old cloth wire, boss. Never flip a switch before I look.' The verb ",
   (None, 'ligue'),
   ' means to switch on, and the same verb also means to phone someone.']),
 (9,
  None,
  ["'Can you fix it before lunch, Jorge? Tell me you have spare fuses!' Something left over is ",
   (None, 'sobrando,'),
   ' a useful word for spare keys, spare chairs or leftover cake.']),
 (10,
  None,
  ["'The kitchen I can sort out in two minutes, but Room Nine needs new wire.' Jorge puts the kitchen first "
   'for emphasis, and ',
   (None, 'resolvo'),
   ' is the everyday verb for sorting out any problem.'])]
