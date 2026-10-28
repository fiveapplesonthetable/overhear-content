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
    (0, None, "'Hello, did you like our restaurant today?' Vika politely asks the guest if they enjoyed the restaurant today. She is checking on their experience."),
    (1, None, "'Please forgive us, for the love of God.' The guest apologizes profusely to the staff. They literally ask for forgiveness for the sake of goodness."),
    (2, None, "'Did something happen with your wife?' Vika is concerned and asks if something happened to the guest's wife. She wants to know why they are apologizing."),
    (3, None, "'My wife told me everything in detail.' The guest explains that his wife told him everything in detail. He knows the whole story now."),
    (4, None, "'Did she get poisoned by some dish of ours?' Vika worries that the woman got food poisoning from their dish. She is trying to find the problem."),
    (5, None, "'No, she was not poisoned by food at all.' The guest reassures her that it is not food poisoning at all. The food is perfectly fine."),
    (6, None, "'Why then did she feel so ill?' Vika is confused about why the woman felt so bad then. She wants to understand the situation."),
    (7, None, "'She is pregnant, already in the third month.' The guest reveals the secret that she is actually pregnant. She is already three months along."),
    (8, None, "'So she just has bad morning sickness?' Vika realizes the woman just has severe morning sickness. It was never about the restaurant food."),
    (9, None, "'Yes, the smells of food make her nauseous.' The guest confirms this by saying food smells make her sick. It is a normal pregnancy symptom."),
    (10, None, "'We were very worried about her health.' Vika expresses relief and mentions how worried they were. They really cared about her well-being."),
    (11, None, "'Thank you for your understanding and care.' The guest thanks her for being so understanding and caring. They appreciate the restaurant's kind attitude."),
    (12, None, "'So this woman is definitely not the critic.' Vika concludes that this woman is definitely not the restaurant critic. They were panicking over nothing."),
]
