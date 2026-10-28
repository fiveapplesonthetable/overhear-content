# Authoring module for kukhnya-s04e17-scene-03.
ID = 'kukhnya-s04e17-scene-03'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 17
SCENE = 3
TITLE = 'Подруга детства  (Childhood Friend)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.17'
SOURCE_FILE = 'sources/kukhnya/s04/e17.ru.srt'
INTRO = "While walking through the dining room, Chef Barinov's daughter Katya spots her childhood friend Lilya. The two women have competed fiercely since kindergarten, so when Lilya introduces her wealthy husband, Katya invents a fiancé on the spot. Let's listen to their rivalry in Russian."
OPENER = "Let's examine Katya and Lilya's competitive reunion line by line."
TRANSITION = "Let's listen to their dining room conversation again without interruption."
OUTRO = "Katya's pride traps her into promising to bring her non-existent fiancé to dinner the very next evening. Listen for the feminine phrase for getting married in Russian. Until next time!"
CLOSING = ('katya', 'До свидания!')
STORY = [
    ('guest', 'Привет, это моя подруга Катя.', 'Hello, this is my friend Katya.', [(22, 'Привет'), (23, 'Это Катя, моя подруга детства')], 'adapted'),
    ('guest', 'Мы вместе в садик ходили.', 'We went to kindergarten together.', [(24, 'Мы с ней еще в садик вместе ходили')], 'adapted'),
    ('katya', 'Мы всегда спорили с детства.', 'We always argued since childhood.', [], 'new'),
    ('guest', 'Меня тогда в университет взяли.', 'They accepted me into the university back then.', [(32, 'а меня в МГУ взяли')], 'adapted'),
    ('katya', 'А я во Францию поехала.', 'And I went to France.', [(33, 'А я во Францию еду учиться')], 'adapted'),
    ('guest', 'Катя, это мой муж Эрнест.', 'Katya, this is my husband Ernest.', [(34, 'Кать, а это Эрнест, мой муж')], 'adapted'),
    ('katya', 'Здравствуйте, мне очень приятно познакомиться.', 'Hello, it is very nice to meet you.', [(35, 'Очень приятно')], 'adapted'),
    ('guest', 'Ну, а ты замуж вышла?', 'Well, and did you get married?', [(36, 'Ну, а ты замуж вышла')], ''),
    ('katya', 'Нет, но скоро обязательно выйду.', 'No, but I will definitely get married soon.', [(36, 'Да нет'), (37, 'Но скоро выйду')], 'adapted'),
    ('katya', 'Через месяц у нас свадьба.', 'Our wedding is in a month.', [(37, 'Через месяц свадьба')], 'adapted'),
    ('guest', 'Тогда завтра вечером поужинаем вместе!', "Then let's have dinner together tomorrow evening!", [(38, 'тогда завтра поужинаем вместе')], 'adapted'),
    ('katya', 'Не знаю, он очень занят.', 'I do not know, he is very busy.', [(40, 'Ну, не знаю, он так занят')], 'adapted'),
    ('guest', 'Отлично, во сколько завтра встречаемся?', 'Great, what time are we meeting tomorrow?', [(42, 'Во сколько встречаемся')], 'adapted'),
]
WALK = [
    (0, None, '\'Hello, this is my friend Katya.\' The guest mentions that this is his friend Katya so Katya sees what is at stake. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (1, None, "'We went to kindergarten together.' Claiming that they went to kindergarten together sounds confident, even if Katya has doubts."),
    (2, None, "'We always argued since childhood.' Around the conversation and friend, Katya sets a calm, everyday tone with the guest."),
    (3, None, "'They accepted me into the university back then.' Around the moment and plan, the guest sets a calm, everyday tone with Katya."),
    (4, None, "'And I went to France.' Realizing that she went to France changes how Katya handles the situation."),
    (5, None, '\'Katya, this is my husband Ernest.\' Noting that this is his husband Ernest keeps the guest\'s side of the story simple and clear. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (6, None, "'Hello, it is very nice to meet you.' Even though it is very nice to meet the guest, Katya keeps a steady face in front of the guest."),
    (7, None, "'Well, and did you get married?' Checking whether Katya gets married cuts straight through the tension between the guest and Katya."),
    (8, None, "'No, but I will definitely get married soon.' Saying that she will definitely get married soon is how Katya sets the tone with the guest."),
    (9, None, '\'Our wedding is in a month.\' Once their wedding is in a month, Katya can finally tell the guest what she means. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
    (10, None, "'Then let's have dinner together tomorrow evening!' Declaring that they should have dinner together tomorrow evening brings the guest's temper right to the surface."),
    (11, None, "'I do not know, he is very busy.' Adding that she does not know he is very busy fills in the missing piece for the guest."),
    (12, None, '\'Great, what time are we meeting tomorrow?\' Wondering if great what time are they meeting tomorrow shows the guest caught off guard. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
]
