ID = 'pousada-do-cajueiro-s01e01-scene-03'
SHOW, SEASON, EPISODE, SCENE = 'pousada-do-cajueiro', 1, 1, 3
TITLE = 'Cadê os meus óculos?  (Where Are My Glasses?)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'otavio': 'Otávio', 'camila': 'Camila', 'jorge': 'Jorge'}

INTRO = ('Before the first guest arrives, guesthouse owner Otavio hurries in from the courtyard looking flustered. '
 'Camila and Jorge watch as Otavio pats his pockets in a panic. Listen to the whole scene first.')
OPENER = "Let's go back through the scene line by line."
TRANSITION = "Now let's listen to the whole exchange once more."
OUTRO = ('Otavio found his glasses perched on his own forehead right as a taxi pulled up at the gate. Let the rhythm '
 'of the Portuguese sink in, and see you next time.')
CLOSING = ('otavio', 'Até mais!')

STORY = [('otavio',
  'Bom dia, pessoal! Bem-vinda, Camila. Está tudo pronto?',
  'Good morning, everyone! Welcome, Camila. Is everything ready?'),
 ('camila',
  'Bom dia, Seu Otávio! Sim, o balcão está limpo e as chaves estão prontas.',
  'Good morning, Mr Otavio! Yes, the counter is clean and the keys are ready.'),
 ('otavio',
  'A hóspede do quarto quatro fica a semana toda. Tudo precisa estar perfeito!',
  'The guest in room four stays all week. Everything needs to be perfect!'),
 ('jorge',
  'Calma, chefe. O quarto está limpo e as toalhas estão frescas.',
  'Easy, boss. The room is clean and the towels are fresh.'),
 ('otavio',
  'Eu preciso ler o caderno de reservas, mas cadê os meus óculos?',
  'I need to read the reservation book, but where are my glasses?'),
 ('camila', 'Eles estão no bolso do seu paletó?', 'Are they in your jacket pocket?'),
 ('otavio',
  'Não, só tem uma caneta e três recibos velhos!',
  'No, there is only a pen and three old receipts!'),
 ('jorge', 'Olhe no espelho atrás do balcão, chefe.', 'Look in the mirror behind the counter, boss.'),
 ('otavio',
  'Por que os meus óculos estariam no... ah! Estão na minha cabeça!',
  'Why would my glasses be in the... oh! They are on my head!'),
 ('camila', 'Bem aí na sua testa, sãos e salvos.', 'Right there on your forehead, safe and sound.'),
 ('otavio',
  'Não contem para ninguém! Agora, um sorriso bonito quando a campainha tocar.',
  'Do not tell anyone! Now, a nice smile when the bell rings.'),
 ('jorge', 'Olha só, um táxi acabou de parar no portão.', 'Look there, a taxi just stopped at the gate.')]

WALK = [(0,
  None,
  ["'Good morning, everyone! Welcome, Camila. Is everything ready?' Otavio greets the team with ",
   (None, 'pessoal!'),
   " literally 'staff' or 'folks', and uses ",
   (None, 'Bem-vinda,'),
   " with a feminine 'a' because he is welcoming Camila."]),
 (1,
  None,
  ["'Good morning, Mr Otavio! Yes, the counter is clean and the keys are ready.' Calling an older man or "
   'boss ',
   (None, 'Seu'),
   ' before his first name is warm, respectful Brazilian politeness—never stiff, just courteous.']),
 (4,
  None,
  ["'I need to read the reservation book, but where are my glasses?' Short, punchy ",
   (None, 'cadê'),
   " is the favourite Brazilian everyday word for 'where is?' or 'where did I put?'."]),
 (5,
  None,
  ["'Are they in your jacket pocket?' Notice ",
   (None, 'no bolso'),
   " squeezing 'in' and 'the' into a single two-letter word before 'pocket'."]),
 (6,
  None,
  ["'No, there is only a pen and three old receipts!' Once again ",
   (None, 'só tem'),
   " literally says 'only has' to mean 'there is only'—a pattern you will hear every single day in Recife."]),
 (8,
  None,
  ["'Why would my glasses be in the... oh! They are on my head!' Glasses are plural in Portuguese just like "
   'in English, so ',
   (None, 'Estão'),
   " means 'they are' for a temporary spot like Otavio's forehead."]),
 (10,
  None,
  ["'Do not tell anyone! Now, a nice smile when the bell rings.' Because Otavio is addressing both Camila "
   'and Jorge, ',
   (None, 'Não contem'),
   ' takes the plural command ending.']),
 (11,
  None,
  ["'Look there, a taxi just stopped at the gate.' Combining ",
   (None, 'acabou de parar'),
   " literally says 'finished stopping', which is how Portuguese cleanly expresses 'just stopped'."])]
