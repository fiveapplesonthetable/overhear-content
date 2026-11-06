ID = 'pousada-do-cajueiro-s01e03-scene-07'
SHOW, SEASON, EPISODE, SCENE = 'pousada-do-cajueiro', 1, 3, 7
TITLE = 'Devolvendo o caderno  (Returning the Notebook)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'camila': 'Camila', 'rafael': 'Rafael'}

INTRO = ("Camila climbs up to the third-floor door to return Rafael's forgotten leather notebook, trying hard to act "
 'natural despite thinking he is a secret hotel inspector. Listen first.')
OPENER = "Let's walk through the scene upstairs one line at a time."
TRANSITION = "Now let's listen to the whole third-floor scene again."
OUTRO = ('Rafael got his notebook back without suspecting a thing, yet that cooling hot-water pipe in the bathroom '
 'is a warning sign. One final scene in Episode 3—down to the boiler cellar! See you next time.')
CLOSING = ('rafael', 'Boa noite!')

STORY = [('camila',
  'Com licença, Rafael? Desculpe incomodar a esta hora.',
  'Excuse me, Rafael? Sorry to disturb at this hour.'),
 ('rafael',
  'Ah, o meu caderno de couro! Obrigado! Eu estava procurando agora mesmo.',
  'Oh, my leather notebook! Thank you! I was looking for it right now.'),
 ('camila',
  'O senhor deixou perto da xícara de sopa lá no balcão.',
  'You left it near the soup cup down on the counter.'),
 ('rafael',
  'Todas as minhas anotações desta semana estão aqui. Você me salvou.',
  'All my notes from this week are in here. You saved me.'),
 ('camila',
  'Ficamos felizes que o nosso pátio seja tranquilo para o seu... trabalho.',
  'We are glad that our courtyard is peaceful for your... work.'),
 ('rafael',
  'Muito tranquilo! Mas você ouviu uma batida metálica estranha agora há pouco?',
  'Very peaceful! Though did you hear a strange metallic knock just now?'),
 ('camila',
  'Ouvi, sim! Pareceu vir do cano de água quente ali no banheiro.',
  'I did hear it! It seemed to come from the hot-water pipe there in the bathroom.'),
 ('rafael',
  'Veja a torneira da pia: a água começou morna, mas já está ficando fria.',
  'Check the sink tap: the water started lukewarm, yet it is already turning cool.'),
 ('camila',
  'Ah! Às vezes os canos antigos juntam um pouco de ar à noite.',
  'Oh! Sometimes the old pipes trap a little air at night.'),
 ('rafael',
  'Na noite fresca do Recife, não faz mal nenhum. Já tomei banho antes de sair.',
  'In the breezy Recife evening, it does no harm at all. I already showered before leaving.'),
 ('camila',
  'Obrigada pela paciência! O Jorge vai olhar o aquecedor no porão agora mesmo.',
  'Thank you for your patience! Jorge will check the water heater in the cellar right now.'),
 ('rafael', 'Bom descanso, Camila. Até amanhã no café.', 'Good rest, Camila. See you tomorrow at breakfast.')]

WALK = [(0,
  None,
  ["'Excuse me, Rafael? Sorry to disturb at this hour.' Polite ",
   (None, 'Desculpe incomodar'),
   " means 'sorry to bother you' when knocking on an office or guest-room door."]),
 (5,
  None,
  ["'Very peaceful! Though did you hear a strange metallic knock just now?' Natural time phrase ",
   (None, 'agora há pouco?'),
   " means 'just a moment ago'."]),
 (6,
  None,
  ["'I did hear it! It seemed to come from the hot-water pipe there in the bathroom.' Instead of bare 'yes', "
   'Brazilian speakers answer a question by echoing the action word: ',
   (None, 'Ouvi, sim!'),
   " literally 'I heard, yes!'."]),
 (7,
  None,
  ["'Check the sink tap: the water started lukewarm, yet it is already turning cool.' Between hot and cold "
   'sits ',
   (None, 'morna,'),
   " for 'lukewarm', while ",
   (None, 'a torneira da pia:'),
   ' names the bathroom sink tap.']),
 (8,
  None,
  ["'Oh! Sometimes the old pipes trap a little air at night.' Handy frequency chunk ",
   (None, 'Às vezes'),
   " literally 'at the times', means 'sometimes'."]),
 (9,
  None,
  ["'In the breezy Recife evening, it does no harm at all. I already showered before leaving.' Reassuring ",
   (None, 'não faz mal'),
   " literally says 'it makes no harm'—meaning 'no problem at all'—and ",
   (None, 'tomei banho'),
   " literally says 'took a bath' for taking a shower."]),
 (10,
  None,
  ["'Thank you for your patience! Jorge will check the water heater in the cellar right now.' Central "
   'hot-water showers in a guesthouse run off ',
   (None, 'o aquecedor'),
   " built from the word for 'to heat'."]),
 (3,
  None,
  ["'All my notes from this week are in here. You saved me.' Short ",
   (None, 'desta semana'),
   " blends 'of' and 'this' before 'week'."])]
