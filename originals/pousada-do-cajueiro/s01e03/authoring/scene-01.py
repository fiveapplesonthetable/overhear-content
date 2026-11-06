ID = 'pousada-do-cajueiro-s01e03-scene-01'
SHOW, SEASON, EPISODE, SCENE = 'pousada-do-cajueiro', 1, 3, 1
TITLE = 'Trinta e cinco minutos  (Thirty-Five Minutes)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'otavio': 'Otávio', 'camila': 'Camila', 'jorge': 'Jorge'}

INTRO = ('Warm evening rain taps against the windows of the Cashew Tree Guesthouse in Recife. With a second Room 7 '
 'guest arriving in thirty-five minutes, Otavio, Camila, and Jorge hurry toward the stairs. Listen first.')
OPENER = "Let's go back through the countdown one line at a time."
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = ("Thirty-five minutes on the clock and four boxes in the way—let's climb up to the third-floor attic next "
 'time. See you next time.')
CLOSING = ('camila', 'Até logo!')

STORY = [('otavio',
  'Trinta e cinco minutos! Ele vai escrever uma avaliação horrível de uma estrela!',
  'Thirty-five minutes! He will write a terrible one-star review!'),
 ('camila',
  'Respire fundo, Seu Otávio. Ninguém escreveu nada ainda.',
  'Take a deep breath, Mr Otavio. Nobody has written anything yet.'),
 ('jorge',
  'Aqui está a chave prateada da porta do sótão no terceiro andar.',
  'Here is the silver key to the attic door on the third floor.'),
 ('otavio', 'Mas o sótão tem uma cama de verdade?', 'Does the attic even have a real bed?'),
 ('jorge',
  'Sim, uma boa cama de madeira, uma mesa limpa e a melhor vista da casa.',
  'Yes, a good wooden bed, a clean desk, and the best view in the house.'),
 ('camila',
  'Então por que a gente nunca aluga esse quarto para os hóspedes?',
  'Then why do we never rent that room to guests?'),
 ('jorge',
  'Porque a escada é estreita e o Seu Otávio guarda caixas velhas lá.',
  'Because the stairs are narrow and Mr Otavio keeps old boxes there.'),
 ('otavio', 'São só três caixas pequenas! Talvez quatro!', 'Only three small boxes! Maybe four!'),
 ('camila',
  'A gente tira quatro caixas em cinco minutos. Vamos subir agora mesmo!',
  'We can move four boxes in five minutes. Let us go up right now!'),
 ('jorge',
  'Subam a escada, virem à esquerda no patamar, última porta no alto.',
  'Go up the stairs, turn left at the landing, last door at the top.'),
 ('otavio',
  'Eu vou buscar lençóis brancos limpos no armário de roupa de cama!',
  'I will fetch clean white sheets from the linen cupboard!'),
 ('camila',
  'Vamos lá, quero ver quem chega primeiro ao terceiro andar!',
  "Come on, let's see who reaches the third floor first!")]

WALK = [(0,
  None,
  ["'Thirty-five minutes! He will write a terrible one-star review!' Online hotel ratings use ",
   (None, 'uma avaliação'),
   ' for a review or rating.']),
 (1,
  None,
  ["'Take a deep breath, Mr Otavio. Nobody has written anything yet.' Calming ",
   (None, 'Respire fundo,'),
   " literally says 'breathe deep' whenever someone starts panicking."]),
 (3,
  None,
  ["'Does the attic even have a real bed?' Adding ",
   (None, 'de verdade?'),
   " literally says 'of truth', turning 'bed' into 'a proper, real bed'."]),
 (4,
  None,
  ["'Yes, a good wooden bed, a clean desk, and the best view in the house.' Superlative ",
   (None, 'a melhor vista'),
   " means 'the best view', placing 'best' ahead of 'view' just like English."]),
 (5,
  None,
  ["'Then why do we never rent that room to guests?' Everyday ",
   (None, 'aluga'),
   ' works both ways in Portuguese: a landlord rents a room out, and a tenant rents it.']),
 (8,
  None,
  ["'We can move four boxes in five minutes. Let us go up right now!' Adding ",
   (None, 'agora mesmo!'),
   " intensifies 'now' into 'right this second!'."]),
 (9,
  None,
  ["'Go up the stairs, turn left at the landing, last door at the top.' Direction chunk ",
   (None, 'virem à esquerda'),
   " means 'turn to the left', essential for street and hallway directions."]),
 (11,
  None,
  ["'Come on, let's see who reaches the third floor first!' Energetic ",
   (None, 'Vamos lá,'),
   " literally 'let's go there', is an upbeat 'come on!' before starting any task."])]
