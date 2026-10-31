SOURCE_NOTE = 'French dialogue is an A1 abridgment. Original video confirms speakers and setting; unprompted original-audio transcription confirms the address forms. Dual subtitles provide scene locators.'
# Authoring module for dix-pour-cent-s01e01-scene-14.
ID = 'dix-pour-cent-s01e01-scene-14'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 1
SCENE = 14
TITLE = "Je suis bien ici  (I'm Fine Here)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'camille': 'Camille', 'mathias': 'Mathias', 'noemie': 'Noémie'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E01'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e01.fr.dual.srt'
INTRO = ("Camille has found work as Andrea's assistant, despite Mathias's refusal to help her. He is startled to "
 'find her at his own agency and tries to persuade her to leave. Listen to the argument, and then to '
 "Noemie's mistaken warning about Mathias.")
OPENER = "Let's take it slowly. Mathias stops dead when he sees Camille in the corridor, and his first words are not exactly a warm hello."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = ('You have heard an offer of help, a refusal and a warning. The familiar and polite forms of you change with '
 'the relationship between the speakers. See you next time.')
CLOSING = ('camille', 'À bientôt!')
STORY = [('mathias',
  "Qu'est-ce que tu fais là?",
  'What are you doing here?',
  [(443, "Qu'est-ce que tu fais là ?")],
  ''),
 ('camille',
  "J'ai trouvé un travail. Super, non?",
  "I've found a job. Great, isn't it?",
  [(443, "J'ai trouvé un travail"), (444, 'Super, non ?')],
  ''),
 ('mathias', 'Un travail?', 'A job?', [(445, 'Un travail ?')], ''),
 ('camille',
  "Je suis la nouvelle assistante d'Andréa Martel.",
  "I'm Andréa Martel's new assistant.",
  [(446, "Je suis la nouvelle assistante d'Andréa Martel")],
  ''),
 ('mathias',
  "Écoute, j'ai mal réagi ce matin.",
  'Listen, I reacted badly this morning.',
  [(449, "Écoute, j'ai"), (450, "J'ai mal réagi ce matin")],
  ''),
 ('mathias',
  "Je ne m'attendais pas à te voir.",
  "I wasn't expecting to see you.",
  [(450, "je ne m'attendais pas à te voir")],
  ''),
 ('mathias',
  "Si tu veux, je peux t'aider à trouver un poste.",
  'If you want, I can help you find a job.',
  [(451, 'si tu veux'), (452, 'trouver un poste dans le cinéma')],
  ''),
 ('camille',
  "C'est gentil, mais je suis bien ici.",
  "That's kind, but I'm fine here.",
  [(453, "C'est gentil, mais je suis bien ici")],
  ''),
 ('mathias',
  "Non, Camille! Ce n'est pas possible.",
  "No, Camille! It's not possible.",
  [(454, 'Camille'), (455, 'pas possible')],
  ''),
 ('camille', 'Pourquoi?', 'Why?', [(455, 'Pourquoi ?')], ''),
 ('mathias',
  "Parce que tu ne peux pas. C'est ma vie!",
  "Because you can't. It's my life!",
  [(456, 'Parce que tu ne peux pas'), (456, "c'est ma vie")],
  ''),
 ('camille', 'Tu ne me donnes rien.', 'You give me nothing.', [(457, 'Tu ne me donnes rien')], ''),
 ('camille',
  'Alors je me débrouille seule, comme toujours!',
  "So I'll manage on my own, as always!",
  [(457, 'alors je me débrouille seule, comme toujours')],
  ''),
 ('noemie',
  'Bonjour. En fait, toi et lui...',
  'Hello. Actually, you and him...',
  [(458, 'Bonjour'), (459, 'En fait, vous'), (460, 'vous et lui')],
  'The familiar address is confirmed by original French audio.'),
 ('noemie',
  'Mathias, tu sais, est marié.',
  'Mathias, you know, is married.',
  [(461, 'Mathias, vous savez'), (462, 'est marié')],
  'The familiar address is confirmed by original French audio.'),
 ('noemie', 'Il est très, très marié.', "He's very, very married.", [(463, 'Il est très, très marié')], '')]
WALK = [(0,
  None,
  "'What are you doing here?' He uses the casual 'you', the one for family and friends, so we already sense "
  'these two know each other well. Camille answers brightly.'),
 (1,
  "J'ai trouvé un travail.",
  "'I found a job.' This is the past French uses most in conversation: a helper word, 'have', plus the "
  "action. Literally 'I have found a job'."),
 (1,
  'Super, non?',
  "'Great, isn't it?' Adding the little word for 'no' with a question mark at the end is an easy way to ask "
  'for agreement. Mathias can only repeat her words.'),
 (3,
  None,
  "'I'm Andrea Martel's new assistant.' The description 'new' has a feminine form to match 'assistant'. "
  "French names the owner after a short linking word, which loses its vowel before Andrea's name."),
 (4,
  None,
  "'Listen, I reacted badly this morning.' He starts with a casual command, 'listen', to calm things down. "
  "It's almost an apology."),
 (5,
  None,
  "'I wasn't expecting to see you.' The expression meaning 'expect' is followed by a short linking word and "
  "the action 'see'. The small word for 'you' comes just before that action."),
 (6,
  None,
  "'If you want, I can help you find a job.' The offer begins with 'if' and a present form. After 'can', "
  "'help' stays in its plain form, followed by another link to 'find'."),
 (7,
  None,
  "'That's kind, but I'm fine here.' French literally says 'I am well here'. Camille uses the description "
  "'kind' to acknowledge his offer before 'but' turns it down."),
 (8,
  None,
  "'No, Camille! It's not possible.' Here is that negative wrap again, around the verb 'is'. In fast speech "
  "the French often drop the first little word, and you'll hear exactly that in the episode."),
 (9, None, "'Why?' One short word, and Camille stands her ground."),
 (10,
  'Parce que tu ne peux pas.',
  "'Because you can't.' The verb here means 'to be able to', and it often stands alone like this."),
 (10,
  "C'est ma vie!",
  "'It's my life!' The possessive is feminine because 'life' is a feminine noun. Mathias's own gender does "
  'not choose its form.'),
 (11,
  None,
  "'You give me nothing.' Another negative wrap, this time with a different second word, the one that means "
  "'nothing'. Camille fires back."),
 (12,
  None,
  "'So I'll manage on my own, as always!' That verb in the middle is a very French one: to get by, to sort "
  "yourself out. The word for 'alone' is feminine here, because she is talking about herself. Then Mathias "
  'walks off.'),
 (13,
  None,
  "'Hello. Actually, you and him...' After 'and', French uses the separate form of 'you', just as it uses a "
  "separate form of 'him'. Noemie is hinting at a relationship she has misunderstood."),
 (14,
  None,
  "'Mathias, you know, is married.' The little aside 'you know' directly addresses Camille. It has the "
  'familiar form and interrupts the statement about Mathias.'),
 (15,
  None,
  "'He's very, very married.' Repeating 'very' strengthens Noemie's warning. The description of Mathias has "
  'a masculine form; its feminine form would sound the same.')]
