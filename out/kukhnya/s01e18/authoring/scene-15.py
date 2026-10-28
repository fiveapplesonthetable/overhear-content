# Authoring module for kukhnya-s01e18-scene-15.
ID = 'kukhnya-s01e18-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 18
SCENE = 15
TITLE = 'Ошибочная бутылка  (The Wrong Bottle)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.18'
SOURCE_FILE = 'sources/kukhnya/s01/e18.ru.dual.srt'
INTRO = 'Max discovers Senya was poisoned by their fake cognac. Viktor asks Kostya for a bottle of cognac and accidentally takes the fake one. Let us listen to their conversation in Russian first.'
OPENER = 'Now let us examine the conversation line by line.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max discovers Senya was poisoned by their fake cognac. Viktor asks Kostya for a bottle of cognac and accidentally takes the fake one. Next time you watch the episode, listen for the Russian expressions for 'just' and 'horror' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Костя, это просто ужас!', 'Kostya, this is just a nightmare!', [(285, 'просто')], ''),
    ('max', 'Сеня отравился нашим коньяком.', 'Senya got poisoned by our cognac.', [(281, 'что Сеня отравился этим коньяком.')], ''),
    ('kostya', 'О нет, что делать?', 'Oh no, what to do?', [], ''),
    ('barinov', 'Костя, дай мне бутылку коньяка.', 'Kostya, give me a bottle of cognac.', [(289, 'мне')], ''),
    ('barinov', 'Ту, которая стоит справа.', 'The one that stands on the right.', [], ''),
    ('kostya', 'Вот эту бутылку?', 'This bottle right here?', [(282, 'вот')], ''),
    ('barinov', 'Нет, дай мне другую. Да, эту.', 'No, give me another one. Yes, this one.', [(289, 'мне'), (289, 'мне')], ''),
    ('max', 'Шеф забрал наш коньяк!', 'Chef took our cognac!', [], ''),
    ('max', 'Надо забрать эту бутылку назад.', 'We need to take this bottle back.', [(291, 'Надо забрать бутылку, Костян.')], ''),
    ('kostya', 'Я не могу к нему подойти.', 'I can not approach him.', [(293, 'Я же не могу к ней подойти.')], ''),
    ('max', 'Давай, Костя, ты должен.', 'Come on, Kostya, you must.', [(294, 'Давай, Костян, давай, дружок.')], ''),
    ('max', 'Понятно, давай дальше.', "Got it, let's move on.", [], ''),
]
WALK = [
    (0, None, "'Kostya, this is just a nightmare!' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'Kostya' straight to 'horror'."),
    (1, None, "'Senya got poisoned by our cognac.' Max uses the action verb meaning 'to get poisoned' to focus on the single completed result, pairing it with 'cognac'."),
    (2, None, "'Oh no, what to do?' Kostya delivers a punchy one-word reaction built around the Russian word meaning 'do'."),
    (3, None, "'Kostya, give me a bottle of cognac.' Chef Barinov leads with the direct command form meaning 'give', pairing it with 'a bottle' and 'cognac'."),
    (4, None, "'The one that stands on the right.' Chef Barinov chooses the action verb meaning 'is parked' for the ongoing action, followed by 'to the right'."),
    (5, None, "'This bottle right here?' Kostya turns a statement into a question purely through rising intonation on the word meaning 'a bottle' to make the point directly in conversation."),
    (6, None, "'No, give me another one. Yes, this one.' Chef Barinov leads with the direct command form meaning 'give', followed by 'the other one'."),
    (7, None, "'Chef took our cognac!' Max uses the action verb meaning 'takes it back' to focus on the single completed result, pairing it with 'cognac'."),
    (8, None, "'We need to take this bottle back.' Max puts the word for 'it is necessary' together with 'take' and 'a bottle' in a crisp, natural spoken turn of phrase."),
    (9, None, "'I can not approach him.' Notice how naturally this everyday Russian phrase expresses the speaker's point."),
    (10, None, "'Come on, Kostya, you must.' Max leads with the direct command form meaning 'let's', followed by 'has to'."),
    (11, None, "'Got it, let's move on.' Max leads with the direct command form meaning 'let's', pairing it with 'clear' and 'next'."),
]
