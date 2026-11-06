ID = 'pousada-do-cajueiro-s01e02-scene-06'
SHOW, SEASON, EPISODE, SCENE = 'pousada-do-cajueiro', 1, 2, 6
TITLE = 'A ligação de sexta-feira  (The Friday Caller)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'camila': 'Camila', 'jorge': 'Jorge'}

INTRO = ('After breakfast, the lobby settles down while Camila updates the paper ledger and Jorge oils the front '
 "door hinge. Suddenly the desk telephone rings. Let's listen in.")
OPENER = "Let's replay the mysterious phone call line by line."
TRANSITION = "Now let's hear the whole phone call scene once more."
OUTRO = ('Now they have an exact appointment—Friday at noon—and a polite caller who hung up before giving his name. '
 'See you next time.')
CLOSING = ('camila', 'Até logo!')

STORY = [('camila',
  'Pousada do Cajueiro, bom dia! É a Camila falando.',
  'Cashew Tree Guesthouse, good morning! Camila speaking.'),
 ('jorge', 'Quem é? Mais uma reserva para o fim de semana?', 'Who is it? Another booking for the weekend?'),
 ('camila',
  'Espere... alô, senhor! O senhor está ligando sobre a mala azul-escura?',
  'Wait... hello, sir! Are you calling about the dark-blue suitcase?'),
 ('jorge', 'Pergunte o nome dele! Anote aí no papel!', 'Ask his name! Write it down on the paper!'),
 ('camila',
  'Sim, senhor, guardamos a sua mala no armário. Qual é o seu nome, por favor?',
  'Yes, sir, we kept your suitcase in the closet. What is your name, please?'),
 ('jorge',
  'O que ele está dizendo? Por que você franziu a testa?',
  'What is he saying? Why are you frowning?'),
 ('camila',
  "Senhor? Ele disse: 'Por favor, não abram o pacote branco. Eu passo aí sexta ao meio-dia.'",
  "Sir? He said: 'Please do not open the white parcel. I will stop by Friday at noon.'"),
 ('jorge', 'Me passe o telefone, deixe que eu pergunto direito!', 'Hand me the phone, let me ask properly!'),
 ('camila', "Tarde demais! Ele disse 'Obrigado' e desligou!", "Too late! He said 'Thank you' and hung up!"),
 ('jorge', 'Voz educada? Jovem ou mais velha?', 'Polite voice? Young or older?'),
 ('camila',
  'Baixa, educada, talvez uns trinta e cinco anos. Parecia nervoso, não bravo.',
  'Quiet, polite, maybe around thirty-five. He sounded nervous, not angry.'),
 ('jorge',
  'Nervoso por causa de um trenzinho de madeira? Essa história fica mais estranha a cada hora.',
  'Nervous because of a wooden train? This story gets stranger every hour.')]

WALK = [(0,
  None,
  ["'Cashew Tree Guesthouse, good morning! Camila speaking.' On the phone, ",
   (None, 'É a Camila falando.'),
   " literally says 'it is Camila speaking', natural and clear for business calls."]),
 (1,
  None,
  ["'Who is it? Another booking for the weekend?' The three-word ",
   (None, 'fim de semana?'),
   " literally says 'end of week' for 'weekend'."]),
 (4,
  None,
  ["'Yes, sir, we kept your suitcase in the closet. What is your name, please?' Asking someone's name uses ",
   (None, 'Qual é o seu nome,'),
   " literally 'which is your name?', rather than 'what'."]),
 (6,
  None,
  ["'Sir? He said: Please do not open the white parcel. I will stop by Friday at noon.' Casual ",
   (None, 'Eu passo aí'),
   " literally says 'I pass there' to mean 'I'll drop by', and ",
   (None, "ao meio-dia.'"),
   " means 'at midday'."]),
 (8,
  None,
  ["'Too late! He said Thank you and hung up!' Dramatic ",
   (None, 'Tarde demais!'),
   " flips English word order to 'late too much', and ",
   (None, 'desligou!'),
   " means both 'hung up' and 'switched off'."]),
 (9,
  None,
  ["'Polite voice? Young or older?' Watch false friend ",
   (None, 'educada?'),
   " here: it means 'polite and well-mannered', not school-educated!"]),
 (10,
  None,
  ["'Quiet, polite, maybe around thirty-five. He sounded nervous, not angry.' Putting ",
   (None, 'uns'),
   " before a number means 'roughly' or 'about' thirty-five."]),
 (11,
  None,
  ["'Nervous because of a wooden train? This story gets stranger every hour.' Useful connector ",
   (None, 'por causa de'),
   " means 'because of'."])]
