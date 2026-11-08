ID = 'pousada-do-cajueiro-s01e04-scene-04'
SHOW, SEASON, EPISODE, SCENE = 'pousada-do-cajueiro', 1, 4, 4
TITLE = 'Lá no porão  (Down in the Cellar)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'camila': 'Camila', 'jorge': 'Jorge'}

INTRO = ('Down in the brick cellar beneath the courtyard, Camila hands Jorge the new brass valve while shining a '
 'bright flashlight on the silent water heater. Listen first.')
OPENER = "Let's replay the repair in the cellar line by line."
TRANSITION = "Now let's listen to the whole cellar scene again from start to finish."
OUTRO = ("A steady blue flame, hot copper pipes, and Jorge calling Camila 'partner' instead of 'rookie'! Let's go "
 'upstairs next time as Rafael comes down for breakfast. See you next time.')
CLOSING = ('camila', 'Até logo!')

STORY = [
    ('camila', 'Aqui estão as duas válvulas, Jorge! Recuperar o fôlego? Nunca!', 'Here are both brass valves, Jorge! Catch my breath? Never!'),
    ('jorge', 'Segure esta lanterna bem firme em cima da junta do cano.', 'Hold this flashlight steady right over the pipe joint.'),
    ('camila', 'Segurei! Você já fechou o registro geral da água?', 'Got it! Did you already shut off the main water valve?'),
    ('jorge', 'Fechado e vazio. Me passe a chave inglesa pesada à sua esquerda.', 'Shut and drained. Pass me the heavy wrench on your left.'),
    ('camila', 'Esta grande de ferro? Aqui está.', 'This big iron one? Here it is.'),
    ('jorge', 'Uma volta, duas voltas... veja como a rosca nova encaixa limpa.', 'One turn, two turns... look how cleanly the new thread fits.'),
    ('camila', 'Nem um pingo vazando! Já podemos ligar o aquecedor?', 'Not a single drop leaking! Can we light the heater already?'),
    ('jorge', 'Abra o registro azul devagar para a esquerda, sem força.', 'Open the blue wheel slowly to the left, gently.'),
    ('camila', 'Girando devagar... escute! A água está entrando forte!', 'Turning slowly... listen! The water is rushing in!'),
    ('jorge', 'E lá vem a chama azul, firme, do jeito que deve ser.', 'And there comes the blue flame, steady, just how it ought to be.'),
    ('camila', 'Encoste no cano de cobre! Já está esquentando!', 'Touch the copper pipe! It is already heating up!'),
    ('jorge', 'Três minutos para subir ao terceiro andar. Bela corrida hoje, parceira.', 'Three minutes to reach the third floor. Fine run today, partner.'),
]

WALK = [(1,
  None,
  ["'Hold this flashlight steady right over the pipe joint.' Careful: ",
   (None, 'lanterna'),
   ' means both a handheld flashlight and a hanging paper lantern!']),
 (2,
  None,
  ["'Got it! Did you already shut off the main water valve?' Household plumbing calls the main shut-off tap ",
   (None, 'o registro geral'),
   ' of the building.']),
 (3,
  None,
  ["'Shut and drained. Pass me the heavy wrench on your left.' Curious name ",
   (None, 'chave inglesa'),
   " literally calls an adjustable wrench an 'English key'."]),
 (5,
  None,
  ["'One turn, two turns... look how cleanly the new thread fits.' Useful ",
   (None, 'encaixa'),
   " means 'fits neatly into place', from puzzle pieces to pipe threads."]),
 (7,
  None,
  ["'Open the blue wheel slowly to the left, gently.' Short ",
   (None, 'sem força.'),
   " literally 'without force', warns Camila not to twist too hard."]),
 (9,
  None,
  ["'And there comes the blue flame, steady, just how it ought to be.' Everyday chunk ",
   (None, 'do jeito que'),
   " means 'in the exact way that'."]),
 (10,
  None,
  ["'Touch the copper pipe! It is already heating up!' From 'warm', ",
   (None, 'esquentando!'),
   " means 'warming up' or 'getting hot'."]),
 (11,
  None,
  ["'Three minutes to reach the third floor. Fine run today, partner.' Yesterday Camila was 'rookie'; today "
   'Jorge promotes her to ',
   (None, 'parceira.'),
   " meaning 'partner' with the feminine 'a'."])]
