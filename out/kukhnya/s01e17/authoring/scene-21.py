# Authoring module for kukhnya-s01e17-scene-21.
ID = 'kukhnya-s01e17-scene-21'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 21
TITLE = 'Конец конфликта  (End of the Conflict)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = "Gathered in the Claude Monet dining room, Victoria and the restaurant staff approach Max to apologize for ruining his birthday celebration. Chef Viktor steps in to ensure peace is restored, bringing the long day of intense conflicts to an end. Let's listen to their conversation in Russian first."
OPENER = "Now let's examine this reconciliation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Relieved that the tension has dissipated, Max accepts their apologies as Victoria and Chef Viktor return to their work in the restaurant. Next time you watch the episode, listen for the Russian expressions for 'to forgive' and 'to spoil' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('vika', 'Максим, прости нас, пожалуйста.', 'Maxim, please forgive us.', [(321, 'Максим, прости нас, пожалуйста, что испортили тебе праздник.')], ''),
    ('vika', 'Мы испортили тебе отличный праздник.', 'We ruined a great holiday for you.', [(321, 'что испортили тебе праздник')], ''),
    ('max', 'Я не сержусь на вас.', 'I am not angry at you.', [], ''),
    ('vika', 'Прости их, пожалуйста, от души.', 'Please forgive them from the heart.', [(322, 'Прости их, пожалуйста.')], ''),
    ('barinov', 'Ну и меня тоже прости.', 'Well and forgive me too.', [(323, 'Ну и меня.')], ''),
    ('barinov', 'Так, всё? Конфликт закончился?', 'So, is that all? The conflict is over?', [(323, 'Так все?'), (324, 'Конфликт исчерпан?')], ''),
    ('max', 'Да, шеф, конфликт закончился.', 'Yes, chef, the conflict is over.', [(324, 'Конфликт исчерпан')], ''),
    ('barinov', 'Но только пока кто-то снова не ошибётся.', 'But only until someone makes a mistake again.', [(324, 'Временно, пока кто-нибудь снова не накосячит.')], ''),
    ('vika', 'Мы все хотим мира на кухне.', 'We all want peace in the kitchen.', [], ''),
    ('barinov', 'Мир на кухне — это главное.', 'Peace in the kitchen is key.', [], ''),
    ('max', 'Спасибо всем за добрые слова.', 'Thank you all for the kind words.', [], ''),
    ('vika', 'Теперь мы можем спокойно работать.', 'Now we can work calmly.', [], ''),
    ('max', 'Я очень рад, что мы помирились.', 'I am very glad that we reconciled.', [], ''),
]
WALK = [
    (0, None, "'Maxim, please forgive us.' Vika starts with a sincere plea for forgiveness."),
    (1, None, "'We ruined a great holiday for you.' She admits fault, acknowledging the damage done to the occasion."),
    (2, None, "'I am not angry at you.' Max responds generously, letting go of any resentment."),
    (3, None, "'Please forgive them from the heart.' Vika urges him to extend that same grace to the others."),
    (4, None, "'Well and forgive me too.' Barinov chimes in, casually asking to be included in the pardon."),
    (5, None, "'So, is that all? The conflict is over?' He then asks for confirmation that the drama is officially resolved."),
    (6, None, "'Yes, chef, the conflict is over.' Max agrees respectfully, putting the issue to rest."),
    (7, None, "'But only until someone makes a mistake again.' Barinov adds a cynical caveat, warning that peace is fragile."),
    (8, None, "'We all want peace in the kitchen.' Vika expresses a collective desire for a harmonious work environment."),
    (9, None, "'Peace in the kitchen is key.' Barinov reinforces this, stating it as a fundamental requirement."),
    (10, None, "'Thank you all for the kind words.' Max shows appreciation for their willingness to make amends."),
    (11, None, "'Now we can work calmly.' Vika looks forward to resuming normal operations without the tension."),
    (12, None, "'I am very glad that we reconciled.' Max concludes by sharing his genuine relief at the reconciliation."),
]
