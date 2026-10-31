# Authoring module for dix-pour-cent-s01e01-scene-02.
ID = 'dix-pour-cent-s01e01-scene-02'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 1
SCENE = 2
TITLE = "Je vais déjeuner deux fois  (I'll Have Lunch Twice)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'magali': 'Magali', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E01'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e01.fr.dual.srt'
INTRO = ('After the photo shoot, the story moves to the talent agency. Andrea arrives with her assistant Magali, who '
 "is trying to organise a very crowded diary. Another agent, Mathias, is already discussing an actor's fee "
 'on the phone. Listen to the French first, and follow the appointments even if some names are new.')
OPENER = "Let's slow that morning down. The greetings are friendly, but the diary is already causing trouble."
TRANSITION = 'Hear the whole exchange again. Listen for the days, the two lunches and the requests to make a phone call.'
OUTRO = ('You have heard plans, times and several short instructions. Try following the diary on a second listen; '
 'repeated words will help you find your place. See you next time.')
CLOSING = ('andrea', 'Bonne journée!')
STORY = [('andrea',
  'Bonjour! Salut, Mathias.',
  'Morning! Hi, Mathias.',
  [(74, 'Bonjour'), (75, 'Salut, Mathias')],
  ''),
 ('mathias',
  'Oui, trois cent mille. Je parle de ses vingt ans de carrière.',
  "Yes, three hundred thousand. I'm talking about his twenty years in the business.",
  [(75, 'Oui, 300 000'), (78, 'Je parle de ses 20 ans de carrière')],
  'Digits written as words for speech.'),
 ('andrea',
  'Magali, je dois voir la pièce de Koltès cette semaine.',
  'Magali, I have to see the Koltès play this week.',
  [(79, 'Je dois voir la pièce de Koltès cette semaine')],
  ''),
 ('andrea', 'Deux places pour mardi?', 'Two tickets for Tuesday?', [(80, 'Deux places pour mardi')], ''),
 ('magali',
  'Mardi, tu as le film de Kechiche.',
  "On Tuesday you've got the Kechiche film.",
  [(81, 'Mardi tu as le film de Kechiche')],
  ''),
 ('andrea', 'Jeudi, alors.', 'Thursday, then.', [(82, 'Jeudi, alors')], ''),
 ('magali',
  'Et demain, tu déjeunes avec Audiard.',
  "And tomorrow you're having lunch with Audiard.",
  [(83, 'déjeuner avec Audiard'), (83, 'demain')],
  ''),
 ('andrea', 'Je prends ça. Merci.', "I'll take that. Thanks.", [(84, 'Je prends ça. Merci')], ''),
 ('magali',
  'Tu déjeunes aussi avec Dany Boon demain.',
  "You're also having lunch with Dany Boon tomorrow.",
  [(85, 'Tu déjeunes avec Dany Boon demain')],
  ''),
 ('andrea', 'Tu es pénible, Magali.', "You're a pain, Magali.", [(86, 'Tu es pénible, Magali')], ''),
 ('andrea',
  "L'un à midi, l'autre à quatorze heures. Je vais déjeuner deux fois.",
  "One at noon, the other at two. I'm going to have lunch twice.",
  [(89, "l'un à midi, l'autre à quatorze heures"), (89, 'deux fois')],
  ''),
 ('andrea',
  'Appelle Clémentine. Dis-lui que je ne peux pas venir ce soir.',
  "Call Clementine. Tell her I can't come tonight.",
  [(90, 'Appelle Clémentine'), (90, 'dis-lui que je ne peux pas venir ce soir')],
  ''),
 ('magali',
  'Clémentine? Celle de la semaine dernière?',
  'Clémentine? The one from last week?',
  [(91, 'Clémentine ? Celle de la semaine dernière ?')],
  ''),
 ('andrea',
  'Il y a une autre Clémentine?',
  'Is there another Clémentine?',
  [(91, 'une autre Clémentine')],
  ''),
 ('magali', "Qu'est-ce que je lui dis?", 'What do I tell her?', [(94, "Qu'est-ce que je lui dis ?")], ''),
 ('andrea',
  'Je ne sais pas. Trouve quelque chose.',
  "I don't know. Think of something.",
  [(93, 'Je ne sais pas'), (97, 'Trouve quelque chose')],
  ''),
 ('andrea',
  "Dis que j'ai une réunion. Improvise!",
  "Say I've got a meeting. Improvise!",
  [(98, 'une réunion'), (98, 'Improvise !')],
  ''),
 ('andrea',
  'Gabriel. Tu ne rappelles pas Cécile de France?',
  "Gabriel. Aren't you calling Cécile de France back?",
  [(99, 'Gabriel.'), (100, 'Tu ne rappelles pas Cécile de France ?')],
  '')]
WALK = [(0,
  None,
  "'Morning! Hi, Mathias.' The first greeting works with strangers as well as colleagues. The second is more "
  'familiar; listen for how short it is.'),
 (1,
  'Oui, trois cent mille.',
  "'Yes, three hundred thousand.' A number before 'hundred' can multiply it. The following word means "
  "'thousand', so the whole amount is three hundred thousand."),
 (1,
  'Je parle de ses vingt ans de carrière.',
  "'I'm talking about his twenty years in the business.' The number comes first, followed by 'years'. The "
  "possessive refers to the actor's career, rather than to the agent speaking."),
 (2,
  None,
  "'Magali, I have to see the Koltes play this week.' The word meaning 'have to' comes before the action "
  "'see'. You can reuse that pair with another action you need to do."),
 (3,
  'Deux places pour mardi?',
  "'Two tickets for Tuesday?' A 'place' can mean a seat or ticket at a theatre. Here the two places are for "
  'the play.'),
 (4,
  'Mardi, tu as le film de Kechiche.',
  "'On Tuesday you've got the Kechiche film.' A day named on its own can identify the coming appointment. "
  "There is no separate French word corresponding to English 'on' here."),
 (5,
  None,
  "'Thursday, then.' The last word can help someone draw a conclusion. A new day has solved the first diary "
  'clash.'),
 (6,
  None,
  "'And tomorrow you're having lunch with Audiard.' French has one word for 'have lunch'. Adding 'tomorrow' "
  'lets this present form describe a planned event.'),
 (7,
  None,
  "'I'll take that. Thanks.' The present form of 'take' suits a decision made right now. The small word "
  'after it points to the thing being offered.'),
 (8,
  None,
  "'You're also having lunch with Dany Boon tomorrow.' The extra word meaning 'also' reveals the problem. "
  'Both lunches are on the same day.'),
 (9,
  None,
  "'You're a pain, Magali.' The adjective can describe something difficult or tiresome. Applied to a person "
  'here, it sounds like an irritated complaint.'),
 (10,
  "L'un à midi, l'autre à quatorze heures.",
  "'One at noon, the other at two.' The pair 'one' and 'the other' separates the two appointments. Fourteen "
  'hours on the clock means two in the afternoon.'),
 (10,
  'Je vais déjeuner deux fois.',
  "'I'm going to have lunch twice.' A form of 'go' followed by an action gives a plan for the future. The "
  "last two words literally say 'two times'."),
 (11,
  'Appelle Clémentine.',
  "'Call Clementine.' An instruction can begin straight with the action, without a separate word for 'you'. "
  'This one addresses a familiar person.'),
 (11,
  'Dis-lui que je ne peux pas venir ce soir.',
  "'Tell her I can't come tonight.' In this instruction the little word for 'to her' attaches after 'tell'. "
  'In an ordinary statement it would go before the action.'),
 (12,
  None,
  "'Clementine? The one from last week?' The expression for 'the one' is feminine because it refers to a "
  "woman. The word for 'last' also has a feminine form beside 'week'."),
 (13,
  None,
  "'Is there another Clementine?' French uses a short expression meaning 'there is'. Here the rising "
  'question asks whether a second person with that name exists.'),
 (14,
  None,
  "'What do I tell her?' The opening question expression asks about the message. The small word for 'to her' "
  'identifies who will receive it.'),
 (15,
  None,
  "'I don't know. Think of something.' The first sentence puts two little negative words around 'know'. The "
  'second switches to a direct instruction.'),
 (16,
  None,
  "'Say I've got a meeting. Improvise!' A meeting is described by a feminine noun, so listen to the little "
  'word before it. This is an excuse to invent, rather than a confirmed meeting.'),
 (17,
  None,
  "'Gabriel. Aren't you calling Cecile de France back?' Calling back and calling use related French words. A "
  'short beginning adds the idea of doing it again.')]
