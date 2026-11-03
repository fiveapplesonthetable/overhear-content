# Authoring module for kukhnya-s01e08-scene-10.
ID = 'kukhnya-s01e08-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 10
TITLE = 'Шеф на скамейке  (Chef on the Bench)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'passerby': 'Прохожий'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Barinov has been shut out of his own restaurant, Claude Monet, while Elena runs his kitchen for the day. He sits on a bench outside, and a rude stranger sits down next to him. It's in Russian first."
OPENER = 'Slowly now. The stranger starts with an insult, and by the end Barinov is thanking him.'
TRANSITION = 'Now the whole conversation on the bench again.'
OUTRO = "Barinov's vow, 'I'll come back and get my kitchen back', pairs two closely related Russian verbs: 'to return' oneself and 'to take something back'. And 'thanks for the advice' is useful any day. See you next time."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('passerby', 'Эй, дурак, почему ты сидишь здесь?', 'Hey, idiot, why are you sitting here?', [(124, 'Эй, дурак')], ''),
    ('barinov', 'Я великий шеф-повар, а вовсе не дурак!', 'I am a great head chef, not an idiot at all!', [], ''),
    ('passerby', 'Тогда почему ты не готовишь на кухне?', 'Then why are you not cooking in the kitchen?', [], ''),
    ('barinov', 'Меня временно выгнали из собственного ресторана.', 'They temporarily kicked me out of my own restaurant.', [], ''),
    ('passerby', 'Кто посмел выгнать такого строгого повара?', 'Who dared to kick out such a strict chef?', [], ''),
    ('barinov', 'Одна наглая женщина из соседнего ресторана.', 'An insolent woman from a neighboring restaurant.', [], ''),
    ('passerby', 'Женщины всегда приносят мужчинам большие проблемы.', 'Women always bring men big problems.', [], ''),
    ('barinov', 'Ты абсолютно прав, мой случайный собеседник.', 'You are absolutely right, my random conversational partner.', [], ''),
    ('passerby', 'И что ты теперь собираешься делать?', 'And what are you going to do now?', [], ''),
    ('barinov', 'Я вернусь и верну свою кухню!', 'I will return and get my kitchen back!', [], ''),
    ('passerby', 'Вот это правильные слова, смелый повар!', 'Now those are the right words, brave cook!', [], ''),
    ('barinov', 'Спасибо за совет, я иду побеждать!', 'Thank you for the advice, I am going to win!', [], ''),
]
WALK = [
    (0, None, ["'Hey, idiot, why are you sitting here?' The stranger immediately opens with a harsh insult, calling the chef a fool by using ", ('passerby', 'дурак'), '.']),
    (1, None, ["'I am a great head chef, not an idiot at all!' Barinov proudly defends his esteemed reputation as a truly great cook with ", ('barinov', 'великий'), '.']),
    (2, None, ["'Then why are you not cooking in the kitchen?' Curious about his current situation outside the building, the man asks about preparing food using ", ('passerby', 'готовишь'), '.']),
    (3, None, ["'They temporarily kicked me out of my own restaurant.' He explains the humiliating experience of being kicked out of his establishment with ", ('barinov', 'выгнали'), '.']),
    (4, None, ["'Who dared to kick out such a strict chef?' Wondering who would have the courage to do that, the stranger asks who dared with ", ('passerby', 'посмел'), '.']),
    (5, None, ["'An insolent woman from a neighboring restaurant.' The chef blames an incredibly insolent and arrogant woman from next door, describing her as ", ('barinov', 'наглая'), '.']),
    (6, None, ["'Women always bring men big problems.' generalizing about relationships between people, the man claims that women always cause trouble, emphasizing it with ", ('passerby', 'всегда'), '.']),
    (7, None, ["'You are absolutely right, my random conversational partner.' Finding unexpected agreement on the bench, Barinov refers to his random conversation partner as a ", ('barinov', 'собеседник'), '.']),
    (8, None, ["'And what are you going to do now?' Asking about future plans and intentions, the passerby wonders what the chef is going to do using ", ('passerby', 'собираешься'), '.']),
    (9, None, ["'I will return and get my kitchen back!' Filled with renewed determination to take back his kitchen, Barinov vows to get it back with ", ('barinov', 'верну'), '.']),
    (10, None, ["'Now those are the right words, brave cook!' The stranger approves of this brave and courageous attitude, praising him with the word ", ('passerby', 'смелый'), '.']),
    (11, None, ["'Thank you for the advice, I am going to win!' Feeling completely inspired by the chat, the chef declares he is off to win or conquer using ", ('barinov', 'побеждать'), '.']),
]
