# Authoring module for dix-pour-cent-s02e04-scene-18.
ID = 'dix-pour-cent-s02e04-scene-18'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 4
SCENE = 18
TITLE = 'Nouveau rendez-vous  (Rescheduling the Meeting)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'sacha': 'Sacha'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E04'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e04.fr.dual.srt'
INTRO = 'In her office, Andrea meets with German film director Sacha Hartman, who is furious because he believes superstar Isabelle Adjani is ignoring him. Andrea decides to take control of the situation and calls Isabelle directly. Listen to the scene in French first.'
OPENER = "Let's examine how Andrea calms down an angry film director."
TRANSITION = "Now let's hear the negotiation once more at normal pace."
OUTRO = 'With a single phone call, Andrea fixes the misunderstanding and confirms the meeting with Isabelle Adjani. See you next time!'
CLOSING = ('sacha', 'Bonne journée!')
STORY = [
    ('sacha', 'Comment ça, Isabelle est indisponible?', 'What do you mean, Isabelle is unavailable?', [(481, 'Comment ça, indisponible ?')], ''),
    ('andrea', 'Elle a un défilé et des essayages.', 'She has a fashion show and costume fittings.', [(482, 'Rien. Elle a des essayages'), (483, 'puis un défilé Chanel')], ''),
    ('sacha', 'Je suis resté à Paris exprès pour elle!', 'I stayed in Paris specially for her!', [(485, "Mais je suis resté exprès. Qu'est-ce qu'elle fait ?")], ''),
    ('sacha', 'Elle me séduit, puis elle me snobe.', 'She charms me, then she snubs me.', [(487, 'Elle vous séduit, puis vous snobe')], ''),
    ('andrea', 'Sacha, ne soyez pas si paranoïaque.', 'Sacha, do not be so paranoid.', [(489, 'Sacha, ne soyez pas si paranoïaque')], ''),
    ('sacha', "Je n'ai pas besoin d'Adjani pour mon film.", 'I do not need Adjani for my movie.', [(492, "Je n'ai pas besoin d'Adjani !")], ''),
    ('sacha', "Il y a d'autres grandes actrices.", 'There are other great actresses.', [(493, 'Il y a plein de grandes actrices')], ''),
    ('andrea', "Attendez, je vais l'appeler tout de suite.", 'Wait, I am going to call her right away.', [(494, "Attendez, je vais l'appeler")], ''),
    ('andrea', "Allô Isabelle? C'est Andréa Martel.", 'Hello Isabelle? It is Andréa Martel.', [(497, "Isabelle, c'est Andréa Martel d'ASK")], ''),
    ('andrea', 'Sacha Hartman aimerait beaucoup vous voir.', 'Sacha Hartman would really like to see you.', [(498, "J'appelle de la part de Sacha Hartman"), (499, 'Souhaitez-vous le rencontrer ?')], ''),
    ('andrea', 'Seriez-vous libre demain matin au bureau?', 'Would you be free tomorrow morning at the office?', [(501, 'Demain, au bureau ?')], ''),
    ('andrea', 'Parfait, rendez-vous demain à onze heures!', "Perfect, see you tomorrow at eleven o'clock!", [(504, 'Demain à 11h'), (505, 'Parfait, à demain, Isabelle')], ''),
    ('andrea', "Vous voyez, Sacha? C'est réglé.", 'You see, Sacha? It is settled.', [(510, "Alors, c'est réglé !")], ''),
    ('sacha', 'Elle a vraiment accepté de me voir?', 'She really agreed to see me?', [(506, 'Indisponible ?')], ''),
    ('andrea', 'Oui, elle essaie de vous joindre depuis deux jours.', 'Yes, she has been trying to reach you for two days.', [(499, 'Depuis deux jours'), (500, "j'essaie !")], ''),
    ('sacha', "D'accord, alors je serai là demain.", 'Alright, then I will be there tomorrow.', [(504, "D'accord, merci"), (511, 'Très bien')], ''),
]
WALK = [
    (0, None, "'What do you mean, Isabelle is unavailable?' Built word-for-word as 'how that?', those opening two words challenge surprising news just like 'what do you mean?' in English."),
    (1, None, "'She has a fashion show and costume fittings.' Related to 'filing past' on a runway, the first item means 'fashion show', paired with a word built from 'try on'."),
    (2, None, "'I stayed in Paris specially for her!' Watch two false friends in French: the action means 'stayed' rather than 'rested', and the word before 'for her' means 'on purpose'."),
    (3, None, "'She charms me, then she snubs me.' French turns borrowed 'snob' into an everyday action meaning 'to snub', placing 'me' ahead of both actions."),
    (4, None, "'Sacha, do not be so paranoid.' Wrapping the polite 'be' command in the negative softens Andrea's scolding, followed by 'so' before the cognate 'paranoid'."),
    (5, None, "'I do not need Adjani for my movie.' Even in the negative, 'have need of' keeps its 'of' shortened before Adjani's vowel in French."),
    (6, None, "'There are other great actresses.' Opening with a handy chunk meaning 'there are', French links 'others' using a shortened 'of' up front."),
    (7, None, "'Wait, I am going to call her right away.' Notice 'her' shrinks to a single letter attached to 'call' rather than standing after it as in English."),
    (8, None, "'Hello Isabelle? It is Andrea Martel.' That telephone-only greeting comes from 'halloo', and Andrea gives both her first name and surname for professional poise."),
    (9, None, "'Sacha Hartman would really like to see you.' Placing 'a lot' right after 'would like' builds 'would really like', with polite 'you' tucked ahead of 'see'."),
    (10, None, "'Would you be free tomorrow morning at the office?' Inverting 'would be' and polite 'you' sounds extra courteous, while 'tomorrow morning' needs no connector in French."),
    (11, None, "'Perfect, see you tomorrow at eleven o'clock!' Clock times in French say 'at eleven hours', always keeping 'hours' where English uses 'o'clock'."),
    (12, None, "'You see, Sacha? It is settled.' Related to a 'ruler' that straightens lines, that closing expression means 'sorted out' or 'settled'."),
    (13, None, "'She really agreed to see me?' Agreeing 'to do' something takes 'of' after 'accepted' in French, with 'me' sitting right ahead of 'see'."),
    (14, None, "'Yes, she has been trying to reach you for two days.' Present action plus 'since two days' expresses an effort still underway now, where English says 'has been trying'."),
    (15, None, "'Alright, then I will be there tomorrow.' Pairing 'then' with one-word future 'will be' seals Sacha's promise cleanly in French."),
]
