# Authoring module for domashniy-arest-s01e09-scene-25.
ID = 'domashniy-arest-s01e09-scene-25'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 9
SCENE = 25
TITLE = 'Проверка информации  (Testing the Information)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'marina': 'Марина', 'pasha': 'Паша'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.09'
SOURCE_FILE = 'sources/domashniy-arest/s01/e09.ru.dual.srt'
INTRO = 'After her meeting with Arkady, Marina meets Osipenko to pass along the lead. Arkady claimed his hidden millions are tucked away in a local kindergarten called The Golden Key. Osipenko immediately suspects a trap, but prepares to verify it anyway. Listen to their Russian conversation first, and do not worry about catching every word.'
OPENER = "Let's examine line by line how Osipenko evaluates the report from Marina."
TRANSITION = 'Now listen to the interrogation of the information once again.'
OUTRO = 'Osipenko figures that whether it is a real hiding spot or a clever trap, the kindergarten must be secured immediately. See you next time!'
CLOSING = ('pasha', 'Пока!')
STORY = [
    ('pasha', 'Есть контакт? Что он сказал?', 'Is contact made? What did he say?', [(715, 'Есть контакт')], ''),
    ('marina', 'Он назвал место, где лежат деньги.', 'He named the place where the money lies.', [], 'Marina reports on Arkady'),
    ('pasha', 'И где же эти миллионы?', 'And where are these millions?', [], 'Osipenko asks intently'),
    ('marina', 'В детском садике «Золотой ключик».', 'In the Golden Key kindergarten.', [], 'Marina reveals the supposed hiding place'),
    ('pasha', 'Мне кажется, как-то всё очень просто.', 'It seems to me, somehow everything is very simple.', [(716, 'как-то все очень просто')], ''),
    ('marina', 'А он не соврал?', 'And could he have lied?', [(717, 'он не соврал')], ''),
    ('pasha', 'Соврал, конечно!', 'He lied, of course!', [(718, 'Соврал, конечно')], ''),
    ('marina', 'А что же тогда хорошего?', 'So what is good about that then?', [(719, 'А что же тогда хорошего')], ''),
    ('pasha', 'Это была проверка.', 'It was a test.', [(720, 'Это была проверка')], ''),
    ('marina', 'Вы думаете, он нас проверяет?', 'You think he is testing us?', [], 'Marina is surprised'),
    ('pasha', 'Мы всё равно проверим этот детский сад.', 'We will check that kindergarten all the same.', [], 'Osipenko plans to send men'),
    ('marina', 'Будьте осторожны, он очень хитрый.', 'Be careful, he is very cunning.', [], 'Marina gives a final warning'),
]
WALK = [
    (0, 'Есть контакт?', "'Is contact made?' An informal expression meaning successful contact was established."),
    (0, 'Что он сказал?', "'What did he say?' Osipenko demands the exact words from the cafe."),
    (1, None, "'He named the place where the money lies.' The verb of location takes the plural subject."),
    (2, None, "'And where are these millions?' The emphatic particle adds impatience to the question."),
    (3, None, "'In the Golden Key kindergarten.' The location form indicates physical location."),
    (4, None, "'It seems to me, somehow everything is very simple.' The impersonal construction expresses doubt."),
    (5, None, "'And could he have lied?' The negative particle softens the speculative question."),
    (6, None, "'He lied, of course!' Osipenko assumes Arkady is always plotting deceit."),
    (7, None, "'So what is good about that then?' The 'of'-form singular of the adjective follows what."),
    (8, None, "'It was a test.' The past tense feminine noun refers to a probe or trial."),
    (9, None, "'You think he is testing us?' The ongoing-action form denotes an ongoing suspicion."),
    (10, None, "'We will check that kindergarten all the same.' The fixed idiom means regardless."),
    (11, None, "'Be careful, he is very cunning.' The command form plural expresses an urgent warning."),
]
