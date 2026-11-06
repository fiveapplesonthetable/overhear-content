ID = 'pousada-do-cajueiro-s01e01-scene-04'
SHOW, SEASON, EPISODE, SCENE = 'pousada-do-cajueiro', 1, 1, 4
TITLE = 'Quarto quatro no segundo andar  (Room Four on the Second Floor)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'camila': 'Camila', 'helena': 'Helena', 'jorge': 'Jorge'}

INTRO = ('At the front desk, retired piano teacher Helena steps inside from her taxi pulling a large dark-blue '
 "suitcase. Camila greets her first guest while Jorge stands ready to help with the heavy bag. Let's hear "
 'how it goes.')
OPENER = "Let's step through the check-in one line at a time."
TRANSITION = "Now let's listen to the whole check-in again from start to finish."
OUTRO = ('Camila handled her first check-in smoothly, though Jorge noticed that dark-blue suitcase felt unusually '
 'heavy. See you next time to find out what is inside.')
CLOSING = ('helena', 'Até logo!')

STORY = [('camila', 'Bem-vinda! Bom dia, senhora.', 'Welcome! Good morning, madam.'),
 ('helena',
  'Bom dia, querida. Tenho uma reserva em nome de Helena.',
  'Good morning, my dear. I have a booking under the name Helena.'),
 ('camila',
  'Sim, quarto quatro no segundo andar! Como foi a viagem de ônibus?',
  'Yes, room four on the second floor! How was the bus trip?'),
 ('helena',
  'Tranquila e boa, obrigada, mas esta mala parece muito pesada hoje.',
  'Calm and good, thank you, though this suitcase feels very heavy today.'),
 ('jorge',
  'Com licença, senhora. Nossa, a senhora trouxe pedras aqui dentro?',
  'Allow me, madam. Goodness, did you bring stones in here?'),
 ('helena',
  'Só vestidos, partituras e a minha xícara favorita!',
  'Only dresses, sheet music, and my favourite teacup!'),
 ('camila',
  'Aqui está a sua chave, número quatro. O café da manhã é das sete e meia às dez.',
  'Here is your key, number four. Breakfast is from seven thirty to ten.'),
 ('helena',
  'Que maravilha. A janela dá para a rua ou para o pátio?',
  'Wonderful. Does the window face the street or the courtyard?'),
 ('camila',
  'Para o pátio, bem em cima do cajueiro velho. É muito silencioso.',
  'The courtyard, right above the old cashew tree. It is very quiet.'),
 ('helena', 'É tudo o que eu quero. Onde fica a escada?', 'It is everything I want. Where are the stairs?'),
 ('jorge',
  'Logo ali depois do arco. Eu vou levar a mala azul para a senhora.',
  'Right there past the arch. I will carry the blue suitcase for you.'),
 ('helena', 'Muito obrigada aos dois.', 'Thank you both very much.')]

WALK = [(1,
  None,
  ["'Good morning, my dear. I have a booking under the name Helena.' Kind older Brazilian speakers often "
   'call a helpful young woman ',
   (None, 'querida.'),
   " meaning 'dear', setting a gentle tone right away."]),
 (2,
  None,
  ["'Yes, room four on the second floor! How was the bus trip?' Linking a trip to its transport uses plain "
   "'of', so ",
   (None, 'viagem de ônibus?'),
   " literally says 'trip of bus'."]),
 (4,
  None,
  ["'Allow me, madam. Goodness, did you bring stones in here?' Mild exclamation ",
   (None, 'Nossa,'),
   " is short for 'Our Lady' and works like a polite 'goodness!' or 'wow!' when Jorge lifts the bag."]),
 (6,
  None,
  ["'Here is your key, number four. Breakfast is from seven thirty to ten.' Notice ",
   (None, 'O café da manhã'),
   " literally 'the coffee of the morning', the everyday Brazilian name for breakfast."]),
 (7,
  None,
  ["'Wonderful. Does the window face the street or the courtyard?' Saying a window ",
   (None, 'dá para'),
   " literally says it 'gives toward' the street or courtyard—a handy chunk for hotel views."]),
 (8,
  None,
  ["'The courtyard, right above the old cashew tree. It is very quiet.' Tree names in Portuguese often share "
   'a special tree ending: ',
   (None, 'cajueiro'),
   ' is the cashew tree built from the word for the cashew fruit.']),
 (10,
  None,
  ["'Right there past the arch. I will carry the blue suitcase for you.' To talk about the future, Brazilian "
   "speakers simply pair 'I go' with the action: ",
   (None, 'Eu vou levar'),
   " means 'I am going to carry'."]),
 (11,
  None,
  ["'Thank you both very much.' Adding ",
   (None, 'aos dois.'),
   " fuses 'to' and 'the' before 'two', thanking Camila and Jorge together."])]
