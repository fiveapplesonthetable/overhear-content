# Authoring module for dix-pour-cent-s01e06-scene-24.
ID = 'dix-pour-cent-s01e06-scene-24'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 6
SCENE = 24
TITLE = "Le pardon de Sofia et la panique d'Andréa  (Sofia's Forgiveness and Andréa's Panic)"
LEVEL = "A1 — débutant"
PAIR = 'fr-en'
VOICES = {"narrator": "sky", "gabriel": "theo", "lea": "lucie", "sofia": "emilie"}
LABELS = {"gabriel": "Gabriel", "lea": "Andréa", "sofia": "Sofia"}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E06'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e06.fr.dual.srt'
INTRO = "Meanwhile, Colette caught a drunken Andréa kissing another woman at the party and walked away in heartbreak. Feeling guilty about Sofia's ruined callback, Gabriel visits Sofia at her apartment to apologize. Later that night, a panicked visitor knocks at Gabriel's own door. Listen to the scene in French first. Don't worry about catching every word. Let's listen to the scene in French first."
OPENER = "Let's walk through Gabriel's apology and Andréa's midnight panic step by step."
TRANSITION = 'Now listen to the whole scene again at normal speed, and see how much more you catch.'
OUTRO = 'Gabriel smoothed things over with Sofia, but Andréa has hit rock bottom after losing Colette. See you next time!'
CLOSING = ("lea", "Au revoir!")
STORY = [
    ('sofia', 'Oui?', 'Yes?', [(630, 'Oui')], ''),
    ('gabriel', 'Sofia? Excuse-moi, je te dérange?', 'Sofia? Sorry, am I disturbing you?', [(631, 'Sofia'), (632, 'je te dérange')], ''),
    ('sofia', 'Non, tu ne me déranges pas.', 'No, you aren', [(643, 'tu ne me déranges pas')], ''),
    ('gabriel', 'Je devais te voir.', 'I had to see you.', [(634, 'Je devais te voir')], ''),
    ('gabriel', "Je me sens vraiment mal pour tout à l'heure.", 'I feel really bad about earlier.', [(635, "Je me sens vraiment mal pour tout à l'heure")], ''),
    ('sofia', "Ce que j'ai dit était horrible.", 'What I said was horrible.', [(637, "ce que j'ai dit était horrible")], ''),
    ('gabriel', "Non, j'aurais dû te le dire.", 'No, I should have told you.', [(640, "j'aurais dû te le dire")], ''),
    ('sofia', 'Tu veux boire quelque chose?', 'Do you want to drink something?', [(645, 'Tu veux'), (645, 'boire quelque chose')], ''),
    ('gabriel', 'Oui, volontiers.', 'Yes, gladly.', [(646, 'Oui, volontiers')], ''),
    ('sofia', "J'ai du porto.", 'I have some port.', [(647, "J'ai du porto")], ''),
    ('gabriel', "J'adore le porto.", 'I love port.', [(648, "J'adore le porto")], ''),
    ('lea', 'Gabriel!', 'Gabriel! Open up!', [(649, 'Gabriel')], ''),
    ('gabriel', 'Andréa? Tu es blessée?', 'Andréa? Are you hurt?', [(649, 'Andréa'), (650, "t'es blessée")], ''),
    ('lea', "J'ai eu un problème de piscine!", 'I had a pool problem!', [(652, "J'ai eu un"), (652, 'problème de piscine')], ''),
    ('lea', 'Gabriel, épouse-moi!', 'Gabriel, marry me!', [(654, 'Gabriel, épouse-moi')], ''),
    ('lea', 'Protège-moi, sauve-moi!', 'Protect me, save me!', [(655, 'Protège-moi, sauve-moi')], ''),
    ('lea', 'Aide-moi, Gabriel...', 'Help me, Gabriel...', [(656, 'Aide-moi, Gabriel')], ''),
]
WALK = [
    (0, None, "'Yes?' Sofia answers the door with a brief question."),
    (1, None, "'Sofia? Sorry, am I disturbing you?' Gabriel uses the informal pronoun 'you' with the verb 'disturb'."),
    (2, None, "'No, you aren't bothering me.' The standard negation 'not' wraps around the pronoun and verb."),
    (3, None, "'I had to see you.' Gabriel opens with the word for 'had to' and lands on 'to see' at the close."),
    (4, None, "'I feel really bad about earlier.' The key word here means 'feel', paired with 'bad' to make the point clear."),
    (5, None, "'What I said was horrible.' The relative phrase 'that' means 'what' or 'that which'."),
    (6, None, "'No, I should have told you.' Listen for the expression meaning 'no', which leads naturally into 'to tell'."),
    (7, None, "'Do you want to drink something?' The conjugated verb 'want' is followed directly by an infinitive."),
    (8, None, "'Yes, gladly.' The polite adverb 'gladly' accepts an invitation with pleasure."),
    (9, None, "'I have some port.' The partitive article 'some' indicates an unspecified quantity of drink."),
    (10, None, "'I love port.' French verbs of preference take a definite article."),
    (11, None, "'Gabriel! Open up!' Andréa pounds frantically on Gabriel's apartment door late at night."),
    (12, None, "'Andréa? Are you hurt?' The feminine verb form 'hurt' agrees with Andréa."),
    (13, None, "'I had a pool problem!' Andréa explains her drenched clothes with frantic absurdity."),
    (14, None, "'Gabriel, marry me!' Listen for the expression meaning 'marry me!', which leads naturally into 'marry me!'."),
    (15, None, "'Protect me, save me!' Two urgent commands plead for emotional rescue."),
    (16, None, "'Help me, Gabriel...' Andréa whispers her final desperate plea in the hallway."),
]
