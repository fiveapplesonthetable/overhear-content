# Authoring module for kukhnya-s06e17-scene-05.
ID = 'kukhnya-s06e17-scene-05'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 17
SCENE = 5
TITLE = "Жена инспектора  (The Inspector's Wife)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя', 'guest': 'Гость'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.17'
SOURCE_FILE = 'sources/kukhnya/s06/e17.ru.srt'
INTRO = "Fedya argues against opening the cooler door for fear of prison, when the inspector's wife suddenly arrives looking for her husband. Chef Barinov lies that he hasn't seen him and orders Fedya to keep an eye on her."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Chef Barinov sends Fedya to watch the inspector's wife, little suspecting that Fedya will misunderstand that instruction too. Until next time!"
CLOSING = ('fedya', 'До встречи!')
STORY = [
    ('fedya', 'Не открывайте эту дверь сейчас.', 'Do not open this door right now.', [(65, 'Не открывайте')], 'adapted'),
    ('fedya', 'Нас всех за это засудят.', 'They will prosecute all of us for this.', [(65, 'нас всех засудят')], 'adapted'),
    ('fedya', 'А мне в тюрьму нельзя.', 'And I cannot go to prison.', [(65, 'а мне в тюрьму нельзя')], 'adapted'),
    ('barinov', 'Открывайте, он же там замёрзнет.', 'Open up, he will freeze in there.', [(67, 'открывайте, он же'), (68, 'Самерзнет')], 'adapted'),
    ('guest', 'Здравствуйте, сюда заходил мой муж?', 'Hello, did my husband stop by here?', [(69, 'Здравствуйте. К вам не заходил мой муж')], 'adapted'),
    ('guest', 'Он хотел поговорить с шефом.', 'He wanted to speak with the chef.', [(70, 'Он собирался поговорить с')], 'adapted'),
    ('barinov', 'Нет, он сюда не заходил.', 'No, he did not come in here.', [(71, 'Нет, не заходил')], 'adapted'),
    ('fedya', 'Шеф, а если она запаникует?', 'Chef, what if she panics?', [(72, 'Шеф, а если она запаникует')], 'adapted'),
    ('fedya', 'Она же сразу полицию вызовет.', 'She will call the police right away.', [(72, 'и полицию вызовет')], 'adapted'),
    ('barinov', 'Надо тихо проследить за ней.', 'We need to quietly keep an eye on her.', [(73, 'Надо за ней проследить')], 'adapted'),
    ('barinov', 'Федя, его жена на тебе.', 'Fedya, his wife is your responsibility.', [(74, 'Федя, жена на тебе')], 'adapted'),
    ('barinov', 'А с ним попробуем договориться.', 'And we will try to reach an agreement with him.', [(76, 'мы попробуем договориться')], 'adapted'),
]
WALK = [
    (0, None, "'Do not open this door right now.' Adding that do not open this door right now fills in the missing piece for Barinov."),
    (1, None, '\'They will prosecute all of us for this.\' Saying that they will prosecute all of them for this is how Fedya sets the tone with Barinov. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (2, None, "'And I cannot go to prison.' Since he cannot go to prison, Fedya does not waste words on excuses."),
    (3, None, "'Open up, he will freeze in there.' By telling Fedya to open up he will freeze in there, Barinov keeps his side of the story grounded."),
    (4, None, '\'Hello, did my husband stop by here?\' By checking whether his husband stop by here, the guest presses Barinov for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (5, None, "'He wanted to speak with the chef.' Because he wanted to speak, the guest treats the matter as settled."),
    (6, None, "'No, he did not come in here.' Explaining that he did not come in here lays the cards on the table for Fedya."),
    (7, None, '\'Chef, what if she panics?\' With the plan and inspector hanging in the air, Fedya puts Barinov on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (8, None, "'She will call the police right away.' Claiming that she will call the police right away sounds confident, even if Barinov has doubts."),
    (9, None, "'We need to quietly keep an eye on her.' Needing to quietly keep an eye moves the conversation forward without extra drama. Russian packs the whole idea of what is allowed or needed into one impersonal word at the front."),
    (10, None, '\'Fedya, his wife is your responsibility.\' Barinov explains that his wife is Fedya\'s responsibility, keeping his voice calm and direct. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (11, None, "'And we will try to reach an agreement with him.' Realizing that they will try to reach an agreement with him changes how Barinov handles the situation."),
]
