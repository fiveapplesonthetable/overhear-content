# Authoring module for boris-s01e01-scene-02.
ID = 'boris-s01e01-scene-02'
SHOW = 'boris'
SEASON = 1
EPISODE = 1
SCENE = 2
TITLE = 'Cambiare mentalità  (Change Your Mindset)'
LEVEL = 'A1 — beginner'
PAIR = 'it-en'
LABELS = {'lopez': 'Lopez', 'biascica': 'Biascica', 'sergio': 'Sergio'}
SOURCE_NAME = 'Boris S01E01'
SOURCE_FILE = 'sources/boris/s01/e01.it.srt'
INTRO = (
    'Inside Studio 2, network executive Lopez gathers the crew to defend making a second season of their cancelled soap opera. '
    'His grand pep talk is immediately punctured when chief electrician Biascica asks production manager Sergio about unpaid overtime from April. '
    'Listen to the Italian exchange first without worrying about every detail.'
)
OPENER = (
    "Let's go back through Lopez's speech and Biascica's blunt question about money."
)
TRANSITION = 'Now hear the whole Studio 2 exchange again, from the pep talk to the overtime dispute.'
OUTRO = (
    'You have heard how "bisogna" expresses what needs to be done, and how Biascica and Sergio argue over old pay. '
    'See you next time.'
)
CLOSING = ('biascica', 'Buona giornata!')
STORY = [
    ('lopez', 'Tutti dicono che questa serie è una pazzia.', 'Everyone says that this series is madness.', [(32, 'Tutti dicono che'), (32, 'pazzia')], 'Shortened from the full soap-opera title for A1 clarity.'),
    ('lopez', 'No, non è andata male.', 'No, it did not go badly.', [(39, 'no non è andato male')], 'Feminine agreement matching "la serie".'),
    ('lopez', 'Non era giusta la fascia oraria.', 'The time slot was not right.', [(40, 'non era giusta la fascia oraria')], ''),
    ('lopez', 'Però bisogna cambiare mentalità.', 'However, we need to change our mindset.', [(43, 'però bisogna cambiare mentalità')], ''),
    ('lopez', 'René non è un regista.', 'Rene is not a director.', [(50, 'René non è un regista')], ''),
    ('lopez', 'René è la regia.', 'Rene is directing itself.', [(51, 'René è la regia')], ''),
    ('lopez', 'Vi chiedo di mettere il cuore. Buon lavoro a tutti!', 'I ask you to put your heart into it. Good work, everyone!', [(56, 'vi chiedo di mettere il cuore'), (58, 'Buon lavoro a tutti')], ''),
    ('biascica', 'Dottore, con tutto il rispetto.', 'Sir, with all due respect.', [(61, 'tutto rispetto')], 'Standardised from colloquial rapid speech.'),
    ('biascica', 'C\'è ancora la questione degli straordinari di aprile.', 'There is still the issue of the April overtime.', [(66, 'questione'), (66, 'straordinari')], 'Standardised article "degli" for Romanesco "dei".'),
    ('sergio', 'Ma quella è una storia di un anno e mezzo fa!', 'But that is a story from a year and a half ago!', [(69, 'ma quella è una storia di un anno e mezzo fa')], ''),
    ('biascica', 'Appunto, è un anno e mezzo che aspettiamo.', 'Exactly, we have been waiting for a year and a half.', [(70, 'Appunto, un anno e mezzo che aspettiamo')], ''),
    ('sergio', 'Biascica, quei soldi non li vedrete mai.', 'Biascica, you will never see that money.', [(71, 'quei soldi'), (72, 'Non li vedrete mai')], ''),
    ('biascica', 'No, non è giusto. Non si fa così.', 'No, it is not fair. That is no way to behave.', [(73, 'No, non è giusto'), (75, 'Non si fa così')], ''),
    ('sergio', 'È sempre uguale.', 'It is always the same.', [(90, 'sempre uguale')], ''),
]
WALK = [
    (0, None, [
        '\'Everyone says that this series is madness.\' "Tutti" means "everyone", and "pazzia" is "madness" or "folly", built from "pazzo", the word for "crazy".'
    ]),
    (1, None, [
        '\'No, it did not go badly.\' Lopez defends the flop. In Italian, "andare male" literally says "to go badly", a handy everyday way to describe something failing.'
    ]),
    (2, None, [
        '\'The time slot was not right.\' Television people call a broadcast slot a "fascia oraria", literally an "hourly band" in the schedule.'
    ]),
    (3, None, [
        '\'However, we need to change our mindset.\' "Bisogna" is a wonderfully useful impersonal word meaning "it is necessary" or "one must", without naming who has to do the work.'
    ]),
    (4, None, [
        '\'Rene is not a director.\' Notice that "regista" ends in "-a" even when describing a man, just like "stagista" in the first scene.'
    ]),
    (5, None, [
        '\'Rene is directing itself.\' Lopez flatters him by swapping the person word "regista" for the craft itself, "la regia", meaning the art of directing.'
    ]),
    (6, None, [
        '\'I ask you to put your heart into it. Good work, everyone!\' Italians say "buon lavoro" to wish colleagues a productive day, where English might say "good luck".'
    ]),
    (7, None, [
        '\'Sir, with all due respect.\' In Rome and across Italy, calling a boss "dottore" shows polite deference even when nobody in the room is a medical doctor.'
    ]),
    (8, None, [
        '\'There is still the issue of the April overtime.\' "Straordinari" literally means "extraordinary hours", the standard workplace word for overtime pay.'
    ]),
    (9, None, [
        '\'But that is a story from a year and a half ago!\' Little "fa" at the very end works just like English "ago", placed after "un anno e mezzo", a year and a half.'
    ]),
    (10, None, [
        '\'Exactly, we have been waiting for a year and a half.\' "Appunto" is a sharp single-word comeback for "precisely" or "that\'s my point". Notice Italian uses present "aspettiamo" because they are still waiting.'
    ]),
    (11, None, [
        '\'Biascica, you will never see that money.\' Where English treats "money" as singular, Italian "soldi" is plural, so Sergio echoes it with "li" for "them".'
    ]),
    (12, None, [
        '\'No, it is not fair. That is no way to behave.\' "Non si fa cosi" literally says "one does not do like this", a classic everyday protest when someone breaks the rules.'
    ]),
    (13, None, [
        '\'It is always the same.\' Sergio sighs as Biascica walks off. "Uguale" means "equal" or "the same", and you will hear this three-word shrug constantly in Italian.'
    ]),
]

