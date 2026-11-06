ID = 'pousada-do-cajueiro-s01e01-scene-08'
SHOW, SEASON, EPISODE, SCENE = 'pousada-do-cajueiro', 1, 1, 8
TITLE = 'Deixada no degrau  (Left on the Step)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'camila': 'Camila', 'jorge': 'Jorge'}

INTRO = ('It is almost nine in the evening, and the courtyard lanterns glow softly as Camila wraps up her first '
 'shift with Jorge. Suddenly, the front gate bell rings once in the quiet Recife night. Listen first.')
OPENER = "Let's replay the cliffhanger one line at a time."
TRANSITION = "Now let's listen to the whole final scene of Episode 1 again."
OUTRO = ("Helena's real suitcase is back on the step, yet the mystery owner vanished into the night asking them to "
 'keep his bag until Friday! Episode 1 is complete—see you next time for Episode 2.')
CLOSING = ('jorge', 'Até amanhã!')

STORY = [('camila',
  'Você ouviu isso, Jorge? Alguém tocou o sino do portão!',
  'Did you hear that, Jorge? Someone rang the gate bell!'),
 ('jorge',
  'Às nove da noite? Fique aqui, vamos abrir a porta juntos.',
  'At nine at night? Stay here, let us open the door together.'),
 ('camila', 'Oi? Boa noite! Não tem ninguém no pátio!', 'Hello? Good evening! Nobody is in the courtyard!'),
 ('jorge', 'Espere. Olhe ali embaixo, no degrau de pedra.', 'Wait. Look down there, on the stone step.'),
 ('camila',
  'Outra mala azul-escura! Será que é a mala da Dona Helena?',
  "Another dark-blue suitcase! Could this be Madam Helena's suitcase?"),
 ('jorge',
  'Veja o zíper... sim, as iniciais dela estão bem aqui!',
  'Check the zipper... yes, her initials are right here!'),
 ('camila',
  'Por que a pessoa correu sem pegar a própria mala de volta?',
  'Why did the person run off without taking their own suitcase back?'),
 ('jorge',
  'Olhe, tem um envelope branco preso com fita na alça.',
  'Look, there is a white envelope taped to the handle.'),
 ('camila',
  "Deixe eu ler: 'Desculpe o engano. Por favor, guardem a minha mala azul até sexta-feira.'",
  "Let me read: 'Sorry for the mistake. Please keep my blue suitcase until Friday.'"),
 ('jorge', 'Até sexta-feira? Sem nome e sem assinatura!', 'Until Friday? No name and no signature!'),
 ('camila',
  'Quem deixa os sapatos e um trenzinho de madeira com estranhos até sexta?',
  'Who leaves their shoes and a wooden train with strangers until Friday?'),
 ('jorge',
  'Bem-vinda à Pousada do Cajueiro, Camila. Seu segundo dia não vai ser chato.',
  'Welcome to the Cashew Tree Guesthouse, Camila. Your second day is not going to be boring.')]

WALK = [(1,
  None,
  ["'At nine at night? Stay here, let us open the door together.' In Portuguese, clock times take ",
   (None, 'Às nove'),
   " with that grave mark showing 'at' and 'the' merged before 'nine'."]),
 (2,
  None,
  ["'Hello? Good evening! Nobody is in the courtyard!' After dark, ",
   (None, 'Boa noite!'),
   " is a single greeting that means both 'good evening' when arriving and 'good night' when heading to "
   'bed.']),
 (4,
  None,
  ["'Another dark-blue suitcase! Could this be Madam Helena's suitcase?' Starting a question with ",
   (None, 'Será que'),
   " literally asks 'will it be that...?', turning any guess into a wondering 'could it be?'."]),
 (5,
  None,
  ["'Check the zipper... yes, her initials are right here!' Instead of a generic 'her', ",
   (None, 'dela'),
   " combines 'of' and 'she' after 'initials' so there is zero doubt it means 'hers', not 'his'."]),
 (6,
  None,
  ["'Why did the person run off without taking their own suitcase back?' Two-word ",
   (None, 'de volta?'),
   " is a handy phrase that means 'back' when returning or retrieving something."]),
 (8,
  None,
  ["'Let me read: Sorry for the mistake. Please keep my blue suitcase until Friday.' Day names from Monday "
   'to Friday count market days, so ',
   (None, "sexta-feira.'"),
   " is literally 'sixth market day'."]),
 (9,
  None,
  ["'Until Friday? No name and no signature!' Repeating ",
   (None, 'Sem'),
   " for 'without' makes Jorge's disbelief crisp: without a name, without a signature."]),
 (11,
  None,
  ["'Welcome to the Cashew Tree Guesthouse, Camila. Your second day is not going to be boring.' Casual ",
   (None, 'chato.'),
   " literally means 'flat', and in Brazilian Portuguese it is the everyday word for 'boring' or "
   "'annoying'."])]
