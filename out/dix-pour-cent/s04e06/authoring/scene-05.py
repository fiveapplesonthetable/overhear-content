# Authoring module for dix-pour-cent-s04e06-scene-05.
ID = 'dix-pour-cent-s04e06-scene-05'
SHOW = 'dix-pour-cent'
SEASON = 4
EPISODE = 6
SCENE = 5
TITLE = "Un pastis matinal  (A Morning Pastis)"
LEVEL = "A1 — débutant"
PAIR = 'fr-en'
VOICES = {"narrator": "sky", "jean": "theo", "lea": "lucie"}
LABELS = {"jean": "Jean", "lea": "Andréa"}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S04E06'
SOURCE_FILE = 'sources/dix-pour-cent/s04/e06.fr.dual.srt'
INTRO = "At a Parisian cafe around ten in the morning, Andrea meets movie star Jean Reno. To her surprise, she finds him already drinking pastis to clear his head. Let's listen to their conversation in French first."
OPENER = "Let's look at Andrea and Jean Reno talking at the cafe step by step."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "Troubled by Jean Reno's morning drinking, Andrea tries to understand why her star client is feeling so overwhelmed and exhausted with his career. When you watch the episode, listen out for the expressions meaning 'pastis' and 'pleases'. You'll catch them now. See you next time."
CLOSING = ("jean", "À bientôt!")
STORY = [
    ('jean', "Un pastis, s'il vous plaît!", 'A pastis, please!', [(199, 'Un pastis')], ''),
    ('lea', 'Mais Jean, il est dix heures.', 'Oh but Jean, it is ten in the morning.', [(200, '10h')], ''),
    ('jean', 'Oui, mais on doit parler.', 'Yes, but we have to talk.', [(201, 'on doit parler')], ''),
    ('lea', 'Pourquoi boire si tôt le matin?', 'Why drink so early in the morning?', [(200, 'matin')], ''),
    ('jean', 'Il faut être à égalité.', 'We must be on equal footing.', [(202, 'égalité')], ''),
    ('lea', 'Tu en es à combien?', 'How many have you had?', [(203, 'combien')], ''),
    ('jean', "C'est seulement le deuxième verre.", 'This is only my second glass.', [(204, 'deuxième')], ''),
    ('lea', 'Ça ne te ressemble pas du tout.', 'That is not like you at all.', [(205, 'ressemble pas')], ''),
    ('jean', "J'avais besoin d'éclaircir mes idées.", 'I needed to clear my thoughts.', [(207, 'idées')], ''),
    ('lea', 'Tu as un problème grave?', 'Do you have a serious problem?', [(201, 'doit parler')], ''),
    ('jean', 'Je suis fatigué de ce métier.', 'I am tired of this profession.', [(207, 'idées')], ''),
    ('lea', 'Tu dois rester calme, Jean.', 'You must stay calm, Jean.', [(205, 'ressemble pas')], ''),
    ('jean', "Remettez-m'en un, s'il vous plaît.", 'Pour me another one, please.', [(208, "Remettez-m'en un")], ''),
    ('lea', "Non, écoute-moi d'abord, Jean.", 'No, listen to me first, Jean.', [(201, 'doit parler')], ''),
]
WALK = [
    (0, None, "'A pastis, please!' Jean orders an aniseed aperitif from the cafe waiter. Jean uses the polite 'you' form alongside 'pleases' to keep a respectful professional tone."),
    (1, None, "'Oh but Jean, it is ten in the morning.' Andrea reminds the actor of the early hour. The key noun here means 'hours', anchored by its matching French article."),
    (2, None, "'Yes, but we have to talk.' Jean emphasizes that they have an important matter to discuss. The clause hinges on the everyday verb meaning 'must'."),
    (3, None, "'Why drink so early in the morning?' Andrea inquires why he is drinking liquor before noon. Notice how 'to drink' leads directly into the noun meaning 'morning'."),
    (4, None, "'We must be on equal footing.' Jean argues that they should share equal conditions for their talk. Notice how 'is necessary' leads directly into the noun meaning 'equality'."),
    (5, None, "'How many have you had?' Andrea asks how many drinks he has already consumed. Andrea uses the casual singular 'you' with 'this line', showing close familiarity."),
    (6, None, "'This is only my second glass.' Jean downplays the amount he has had to drink. The key noun here means 'glass', anchored by its matching French article."),
    (7, None, "'That is not like you at all.' Andrea remarks that heavy morning drinking is out of character for him. The two-part French negation brackets the verb for 'resembles' on both sides."),
    (8, None, "'I needed to clear my thoughts.' Jean confides that his mind felt foggy and overburdened. Notice how 'had' leads directly into the noun meaning 'need'."),
    (9, None, "'Do you have a serious problem?' Andrea probes whether some major crisis has occurred. In everyday spoken French, rising intonation on 'have' at the end is enough to turn the sentence into a question."),
    (10, None, "'I am tired of this profession.' Jean confesses his growing exhaustion with the film industry. The key noun here means 'profession', anchored by its matching French article."),
    (11, None, "'You must stay calm, Jean.' Andrea advises him to maintain his composure. The descriptive adjective for 'calm' agrees in gender and number with its noun."),
    (12, None, "'Pour me another one, please.' Jean signals the waiter to bring another round. The clause hinges on the everyday verb meaning 'pour again'."),
    (13, None, "'No, listen to me first, Jean.' Andrea insists that he stop drinking and pay attention to her. Notice how the short vowel drops before a vowel sound around 'listen', making the phrase flow smoothly as one unit. Now let's hear the whole conversation again."),
]
