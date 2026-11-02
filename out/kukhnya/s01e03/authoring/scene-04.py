# Authoring module for kukhnya-s01e03-scene-04.
ID = 'kukhnya-s01e03-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 4
TITLE = 'Опасный разговор  (A Dangerous Conversation)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vadim': 'Вадим'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = "A rough-looking man stops Max outside Claude Monet. His name is Vadim, he is a prosecutor, and he wants to know who Vika is seeing these days. Max is not enjoying this. Here's the conversation in Russian first."
OPENER = "Let's go through the threat."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Max promises that Vika is seeing nobody, and Vadim does not look convinced. Take away the phrase for "not with anyone", the double negative with a word wedged in the middle.'
CLOSING = ('max', 'До встречи!')
STORY = [
    ('vadim', 'Слышь, малой, есть разговор.', 'Listen, kid, I want to talk.', [(132, 'разговор есть')], ''),
    ('max', 'Что вам нужно?', 'What do you need?', [], ''),
    ('vadim', 'Тут у вас работает Вика.', 'Vika works here with you.', [(133, 'Тут у вас работает Вика')], ''),
    ('vadim', 'Виктория Сергеевна.', 'Viktoria Sergeyevna.', [(133, 'Виктория Сергеевна')], ''),
    ('vadim', 'С кем она тут встречается?', 'Who is she seeing here?', [(134, 'с кем она у вас тут встречается')], ''),
    ('vadim', 'Ну, почему молчим?', 'Well, why are we silent?', [], ''),
    ('max', 'Почему я должен отвечать?', 'Why should I answer?', [(136, 'я тебе должен отвечать')], ''),
    ('vadim', 'Не хочешь отвечать здесь?', "Don't want to answer here?", [(137, 'Не хочешь отвечать здесь')], ''),
    ('vadim', 'Ответишь у меня в прокуратуре.', "You'll answer in my prosecutor's office.", [(138, 'у меня в прокуратуре')], ''),
    ('vadim', 'Ты меня понял?', 'Did you understand me?', [(139, 'Понял')], ''),
    ('max', 'Понял, всё понял.', 'Understood, understood everything.', [(140, 'Понял, понял')], ''),
    ('max', 'Она ни с кем не встречается.', 'She is not seeing anyone.', [(141, 'она здесь ни с кем не встречается')], ''),
    ('vadim', 'Ну, смотри у меня.', 'Well, you watch yourself.', [(142, 'Ну, смотри')], ''),
    ('max', 'Надо срочно предупредить всех.', 'Must urgently warn everyone.', [(160, 'Надо предупредить')], ''),
]
WALK = [
    (0, None, ['\'Listen, kid, I want to talk.\' ', ('vadim', 'Слышь,'), ' is street speech, built from the word for "do you hear". ', ('vadim', 'малой,'), ' meaning kid, is built from the word for "small", and ', ('vadim', 'есть разговор.'), ' literally translates to "there is a conversation".']),
    (1, None, ['\'What do you need?\' ', ('max', 'Что вам нужно?'), ' literally translates to "what to you needed?". Max uses ', ('max', 'вам'), ', the polite word for "you", with a stranger.']),
    (2, None, ['\'Vika works here with you.\' ', ('vadim', 'у вас'), ' literally translates to "at you", meaning "at your place". ', ('vadim', 'Тут'), ' is an everyday word for "here", and ', ('vadim', 'работает'), ' translates to "works".']),
    (3, None, ['\'Viktoria Sergeyevna.\' A first name plus the father\'s name, ', ('vadim', 'Сергеевна.'), ', meaning daughter of Sergey, built from the name Sergey, is the formal way to name an adult.']),
    (4, None, ['\'Who is she seeing here?\' ', ('vadim', 'встречается?'), ' translates to "meets with", which is the normal way to say you\'re dating someone. ', ('vadim', 'С кем'), ' literally translates to "with whom", built from the word for "who".']),
    (5, None, ['\'Well, why are we silent?\' ', ('vadim', 'молчим?'), ' literally translates to "we are silent", built from the action word for "to be silent". Vadim says "we" when he means "you", the scolding "we" used on children.']),
    (6, None, ['\'Why should I answer?\' ', ('max', 'должен'), ' translates to "should", and has a man\'s ending. ', ('max', 'отвечать?'), ', the action word for "to answer", is built from the naming word for "an answer".']),
    (7, None, ['\'Don\'t want to answer here?\' Vadim has called Max the informal "you" from his first word, and ', ('vadim', 'хочешь'), ' is the matching form of the word for "want". ', ('vadim', 'здесь?'), ' translates to "here".']),
    (8, None, ['\'You\'ll answer in my prosecutor\'s office.\' ', ('vadim', 'Ответишь'), ' is the finished action word, so it translates to "you will answer". ', ('vadim', 'у меня в прокуратуре.'), ' literally translates to "at me in the prosecutor\'s office".']),
    (9, None, ['\'Did you understand me?\' ', ('vadim', 'Ты меня понял?'), ' literally translates to "you me understood?". ', ('vadim', 'понял?'), ' has a man\'s ending because Max is a man.']),
    (10, None, ['\'Understood, understood everything.\' ', ('max', 'Понял, всё понял.'), ' repeats the same word and adds ', ('max', 'всё'), ', the word for "everything".']),
    (11, None, ['\'She is not seeing anyone.\' The pieces of the word for "nobody" come apart around the word for "with", to make ', ('max', 'ни с кем'), '. Then ', ('max', 'не'), ' follows, so the double negative has a connecting word wedged inside it.']),
    (12, None, ['\'Well, you watch yourself.\' ', ('vadim', 'смотри у меня.'), ' literally translates to "look, at me", meaning "careful, or you\'ll answer to me". ', ('vadim', 'смотри'), ' is the informal command built from the action word for "to look".']),
    (13, None, ['\'Must urgently warn everyone.\' ', ('max', 'Надо'), ' translates to a one-word "must". ', ('max', 'предупредить'), ' translates to "to warn", and the word for "everyone" becomes ', ('max', 'всех.'), ' as the target of the action.']),
]
