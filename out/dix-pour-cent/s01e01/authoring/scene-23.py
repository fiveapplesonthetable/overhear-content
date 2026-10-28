# Authoring module for dix-pour-cent-s01e01-scene-23.
ID = 'dix-pour-cent-s01e01-scene-23'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 1
SCENE = 23
TITLE = 'Pas de Cécile, pas de Paris  (No Cécile, No Paris)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'mathias': 'Mathias', 'miranda': 'Miranda'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E01'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e01.fr.dual.srt'
INTRO = "Meanwhile, Mathias is back in the elegant tea room with Miranda Jones, Tarantino's producer. She has a new worry: she wants to shoot the film in Paris, and for that she needs permits. Mathias sees his chance. You'll hear it all in French first; don't worry if some words slip past you."
OPENER = "Let's take it slowly. Miranda opens with what she wants, and the verb she uses is the film-world word for shooting a scene."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "That's the end of this scene. When you watch it, listen for the short, punchy line about Cécile and Paris; you'll recognise it straight away. See you next time!"
CLOSING = ('miranda', 'Au revoir, Mathias!')
STORY = [
    ('miranda', 'Mathias, je veux tourner à Paris.', 'Mathias, I want to shoot in Paris.', [(642, 'Tourner à Paris')], ''),
    ('mathias', "Paris? C'est une très bonne idée.", "Paris? That's a very good idea.", [], ''),
    ('miranda', 'Oui, mais il faut des autorisations. Ah, la paperasse française!', 'Ah, French paperwork!', [(629, 'les autorisations'), (631, 'La paperasse française')], ''),
    ('mathias', "C'est plus simple quand on connaît les bonnes personnes.", "It's simpler when you know the right people.", [(633, 'quand on connaît les bonnes personnes')], ''),
    ('miranda', 'Vraiment?', 'Really?', [(634, 'Vraiment')], ''),
    ('mathias', "Si vous avez besoin d'aide, demandez.", 'If you need help, just ask.', [(634, "Si vous avez besoin d'aide, demandez")], ''),
    ('mathias', "Je connais la ministre de la Culture. C'est une jeune femme brillante.", "She's a brilliant young woman.", [(635, 'ministre de la culture'), (637, "C'est une jeune femme brillante")], ''),
    ('mathias', 'Et elle adore Cécile de France!', 'And she loves Cécile de France!', [(639, 'elle adore Cécile de France')], ''),
    ('miranda', "Mais Cécile n'est plus dans le projet.", "But Cécile isn't in the project any more.", [(641, 'projet')], ''),
    ('mathias', 'Je sais. Elle va être très triste.', "I know. She's going to be very sad.", [], ''),
    ('mathias', "Alors, tourner à Paris, c'est peut-être impossible.", 'So shooting in Paris might be impossible.', [(642, 'Tourner à Paris'), (642, 'peut-être impossible')], ''),
    ('miranda', "Elle n'a pas besoin de le savoir.", "She doesn't need to know.", [(643, "Elle n'a pas besoin de le savoir")], ''),
    ('mathias', "Elles sont très proches. C'est difficile de cacher la vérité.", "They're very close.", [(644, 'Elles sont très proches'), (645, "C'est difficile de cacher des choses à ses amies")], ''),
    ('miranda', 'Vous bluffez.', "You're bluffing.", [(647, 'Vous bluffez')], ''),
    ('mathias', 'Pas du tout. Pas de Cécile, pas de Paris.', 'No Cécile, no Paris.', [(647, 'Pas du tout'), (648, 'Pas de Cécile, pas de Paris')], ''),
    ('miranda', 'Bon. Je vais parler à Quentin.', "Fine. I'll talk to Quentin.", [], ''),
    ('mathias', 'Merci, Miranda. Bonne chance!', 'Thank you, Miranda. Good luck!', [(650, 'Bonne chance')], ''),
]
WALK = [
    (0, None, "'Mathias, I want to shoot in Paris.' The first action word means 'I want', and right after it comes an action word in its dictionary form, just like in English. Mathias likes the idea."),
    (1, None, "'Paris? That's a very good idea.' The word for 'idea' is feminine, so the little word before it is the feminine 'a'. Then Miranda sighs."),
    (2, 'Oui, mais il faut des autorisations.', "'Yes, but you need permits.' Here is a really useful expression: those two little words at the start mean 'you need' or 'it takes'. They never change, whoever needs the thing."),
    (2, 'Ah, la paperasse française!', "'Ah, French paperwork!' The French love to complain about their own forms and stamps. Mathias answers with a smooth smile."),
    (3, None, "'It's simpler when you know the right people.' The word in the middle means 'one' or 'people in general'. It sounds like a hint, and it is one."),
    (4, None, "'Really?' Miranda is curious now. One word, rising at the end."),
    (5, None, "'If you need help, just ask.' Notice the polite form of 'you' all through this scene: Mathias and Miranda are business partners, so they stay formal. The last word is a polite command, 'ask'."),
    (6, 'Je connais la ministre de la Culture.', "'I know the Minister of Culture.' The action word means to know a person. And the minister is a woman, so she gets the feminine 'the'."),
    (6, "C'est une jeune femme brillante.", "'She's a brilliant young woman.' A short describing word like 'young' goes before the word; a longer one like 'brilliant' goes after it. Then Mathias plays his card."),
    (7, None, "'And she loves Cécile de France!' The action word is stronger than just 'like': it means 'adore'. Miranda sees the problem coming."),
    (8, None, "'But Cécile isn't in the project any more.' Here is our second language point. The negative in French wraps around the action word, and when the second half is this word, it means 'no longer', 'not any more'."),
    (9, None, "'I know. She's going to be very sad.' To talk about the near future, take the verb 'to go' and add an infinitive, exactly like 'going to be' in English."),
    (12, None, "'They are very close. It is hard to hide the truth.' The word in the middle means 'maybe', and it's a calm way to make a threat. Miranda tries a way out."),
    (11, None, "'She doesn't need to know.' The negative wraps around the verb again, this time with the ordinary 'not'. Mathias doesn't let go."),
    (12, 'Elles sont très proches.', "'They're very close.' The pronoun here is the plural for women, since both are women: the minister and Cécile."),
    (15, None, "'It's hard to hide things from your friends.' Literally 'it is difficult to hide things to one's friends'. Miranda isn't fooled."),
    (13, None, "'You're bluffing.' The same word as in poker, with the polite form of 'you'. And now the line of the scene."),
    (14, 'Pas du tout.', "'Not at all.' Mathias gives a very handy reply when someone accuses you of something."),
    (14, 'Pas de Cécile, pas de Paris.', "'No Cécile, no Paris.' Without a verb, the negative word alone is enough, with a little word linking it to the noun. Short and hard to forget. Miranda gives in."),
    (15, None, "'Fine. I'll talk to Quentin.' The near future again: 'I am going to' plus 'talk'. Quentin is Tarantino, of course."),
    (16, None, "'Thank you, Miranda. Good luck!' Mathias has turned a no into a maybe, and he leaves the table very pleased."),
]
