# Authoring module for kukhnya-s01e11-scene-18.
ID = 'kukhnya-s01e11-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 18
TITLE = 'Неожиданное признание  (An Unexpected Confession)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = 'Near the reception desk of Claude Monet, the husband of the ailing female diner steps up to settle their bill. Expecting an angry complaint or a scandal over food poisoning, Victoria is astonished when the customer offers an earnest apology and reveals a touching personal secret. Let us listen to their conversation in Russian first.'
OPENER = "Now let us examine Victoria and the gentleman's polite discussion line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Deeply relieved to discover that pregnancy rather than food poisoning was the cause, Victoria happily confirms that the restaurant's reputation remains untarnished. Next time you watch the episode, listen for the Russian expressions for 'pregnant' and 'dish' — you will catch every word right away. See you next time!"
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Здравствуйте, вам понравился наш ресторан сегодня?', 'Hello, did you like our restaurant today?', [], ''),
    ('guest', 'Вы уж извините нас, ради бога.', 'Please forgive us, for the love of God.', [(221, 'Вы уж извините нас, ради бога')], ''),
    ('vika', 'Что-то случилось с вашей женой?', 'Did something happen with your wife?', [], ''),
    ('guest', 'Моя жена мне всё подробно рассказала.', 'My wife told me everything in detail.', [(220, 'Мне моя жена все рассказала')], ''),
    ('vika', 'Она отравилась каким-то нашим блюдом?', 'Did she get poisoned by some dish of ours?', [(210, 'после вашего блюда отравилась')], ''),
    ('guest', 'Нет, она вовсе не отравилась едой.', 'No, she was not poisoned by food at all.', [], ''),
    ('vika', 'Почему же ей стало так плохо?', 'Why then did she feel so ill?', [], ''),
    ('guest', 'Она беременна, уже на третьем месяце.', 'She is pregnant, already in the third month.', [(222, 'Она на третьем месяце беременности')], ''),
    ('vika', 'Так у неё просто сильный токсикоз?', 'So she just has bad morning sickness?', [(223, 'токсикоз')], ''),
    ('guest', 'Да, от запахов еды её тошнит.', 'Yes, the smells of food make her nauseous.', [], ''),
    ('vika', 'Мы очень переживали за её здоровье.', 'We were very worried about her health.', [], ''),
    ('guest', 'Спасибо вам за понимание и заботу.', 'Thank you for your understanding and care.', [], ''),
    ('vika', 'Значит, эта женщина точно не критик.', 'So this woman is definitely not the critic.', [(226, 'мы точно знаем, что критик не она')], ''),
]
WALK = [
    (0, None, "'Hello, did you like our restaurant today?' Vika turns a statement into a question purely through rising intonation on the word meaning 'hello', pairing it with 'pleased' and 'restaurant'."),
    (1, None, "'Please forgive us, for the love of God.' the guest leads with the direct command form meaning 'forgive', followed by 'God'."),
    (2, None, "'Did something happen with your wife?' Vika turns a statement into a question purely through rising intonation on the word meaning 'happened', followed by 'wife'."),
    (3, None, "'My wife told me everything in detail.' the guest expresses this naturally by combining the word for 'wife' with 'in detail' and 'told'."),
    (4, None, "'Did she get poisoned by some dish of ours?' Vika turns a statement into a question purely through rising intonation on the word meaning 'got poisoned', followed by 'dish'."),
    (5, None, "'No, she was not poisoned by food at all.' Here the guest anchors the line on the word meaning 'at all' and builds the thought around 'got poisoned' and 'food'."),
    (6, None, "'Why then did she feel so ill?' The phrasing opens with 'why' before bringing in 'became' and 'so' to make the point clear."),
    (7, None, "'She is pregnant, already in the third month.' Russian omits the present-tense verb 'to be' here, linking 'pregnant' directly with 'already', pairing it with 'third' and 'month'."),
    (8, None, "'So she just has bad morning sickness?' Vika turns a statement into a question purely through rising intonation on the word meaning 'so', pairing it with 'simply' and 'strong'."),
    (9, None, "'Yes, the smells of food make her nauseous.' Here the guest anchors the line on the word meaning 'smells' and builds the thought around 'of food' and 'makes nauseous'."),
    (10, None, "'We were very worried about her health.' The phrasing opens with 'very' before bringing in 'worried' and 'health' to make the point clear."),
    (11, None, "'Thank you for your understanding and care.' Russian omits the present-tense verb 'to be' here, linking 'thank you' directly with 'understanding', followed by 'care'."),
    (12, None, "'So this woman is definitely not the critic.' Russian omits the present-tense verb 'to be' here, linking 'it means' directly with 'woman', pairing it with 'definitely' and 'critic'."),
]
