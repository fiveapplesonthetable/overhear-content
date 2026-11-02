# Authoring module for kukhnya-s01e14-scene-03.
ID = 'kukhnya-s01e14-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 3
TITLE = 'Серьёзный парень  (A Serious Guy)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'eleonora': 'Элеонора', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = 'Vika has a visitor at the restaurant: a woman she calls Mum. The woman has plenty to say about Max. Hear their talk before we look closer.'
OPENER = "Now slowly, with Vika's mother doing most of the talking."
TRANSITION = 'The whole scene once more, in one piece.'
OUTRO = "Vika's mother backs off for now, but she hasn't changed her mind about Max. Listen for the difference between the short and long names for mother. See you in the next scene."
CLOSING = ('eleonora', 'Пока!')
STORY = [
    ('vika', 'Мам, зачем ты пришла сюда сегодня?', 'Mom, why did you come here today?', [], ''),
    ('eleonora', 'Зачем тебе этот странный тинейджер?', 'What do you want with that strange teenager?', [(7, 'Зачем тебе этот тинейджер?')], ''),
    ('vika', 'Макс серьёзный парень и хороший повар.', 'Max is a serious guy and a good cook.', [(11, 'Макс серьёзный парень.')], ''),
    ('eleonora', 'Почему ты вечно впадаешь в крайности?', 'Why do you always go to extremes?', [(9, 'Вика, ну почему ты вечно впадаешь в какие-то крайности?')], ''),
    ('vika', 'Это моя жизнь, и я сама решаю.', 'This is my life, and I decide myself.', [], ''),
    ('eleonora', 'То женатики, то дети, сразу дети.', 'First married men, then kids, kids right away.', [(10, 'То женатики, то дети. В общем, сразу дети.')], ''),
    ('vika', 'Хватит критиковать меня каждый день!', 'Stop criticizing me every single day!', [], ''),
    ('eleonora', 'Скажи, а ты записала парня в школу?', 'Tell me, did you enroll the guy in school?', [(13, 'Скажи, а ты успела записать серьёзного парня в школу?')], ''),
    ('vika', 'Я не хочу это обсуждать сейчас.', 'I do not want to discuss this now.', [], ''),
    ('eleonora', 'А то я могла бы вам помочь.', 'Otherwise I could have helped you.', [(14, 'А то я могу бы хлопотать.')], ''),
    ('vika', 'Мама, пожалуйста, просто уходи отсюда.', 'Mom, please, just leave from here.', [], ''),
    ('eleonora', 'Ладно, я оставлю вас в покое пока.', 'Alright, I will leave you in peace for now.', [], ''),
]
WALK = [
    (0, None, ["'Mom, why did you come here today?' Now let's inspect the words: ", ('vika', 'Мам'), ' is a clipped form used to call your mother. ', ('vika', 'пришла'), ", meaning 'came', has a feminine ending."]),
    (1, None, ["'What do you want with that strange teenager?' We will break down the dialogue: ", ('eleonora', 'Зачем'), ('eleonora', 'тебе'), " asks 'what for to you?', the usual way to ask why someone needs something. ", ('eleonora', 'тинейджер'), " is just the English 'teenager' in the local alphabet."]),
    (2, None, ["'Max is a serious guy and a good cook.' Let's analyze the speech: ", ('vika', 'серьёзный'), ('vika', 'парень'), " reads as 'serious guy', leaving out 'is'. It uses an everyday word for a young man."]),
    (3, None, ["'Why do you always go to extremes?' Let us break down the sentence: ", ('eleonora', 'впадаешь'), ('eleonora', 'в'), ('eleonora', 'крайности'), " reads as 'fall into extremes', coming from a word for 'the edge'. ", ('eleonora', 'вечно'), ", meaning 'eternally', is a grumbling way to say 'always'."]),
    (4, None, ["'This is my life, and I decide myself.' The term for life, ", ('vika', 'жизнь'), ", is feminine, so 'my' is ", ('vika', 'моя'), '. ', ('vika', 'сама'), ", meaning 'by myself', has a feminine ending."]),
    (5, None, ["'First married men, then kids, kids right away.' Let's break down this part: ", ('eleonora', 'То'), " used twice means 'one minute ..., the next ...'. ", ('eleonora', 'женатики'), ' is a slightly mocking word built on a word for a married man.']),
    (6, None, ["'Stop criticizing me every single day!' Now let's look at the words: ", ('vika', 'Хватит'), " means 'that is enough', and with a verb after it, ", ('vika', 'критиковать'), ", it works as 'stop criticizing'. The verb keeps a native ending that turns many borrowed words into verbs."]),
    (7, None, ["'Tell me, did you enroll the guy in school?' The term for guy becomes ", ('eleonora', 'парня'), ' as the one being enrolled. ', ('eleonora', 'записала'), ' along with ', ('eleonora', 'в'), ('eleonora', 'школу'), " reads as 'wrote into school', which is how you sign a child up."]),
    (8, None, ["'I do not want to discuss this now.' We can inspect the sentence: ", ('vika', 'не'), ('vika', 'хочу'), ('vika', 'обсуждать'), " means 'I do not want to discuss'. The language naturally puts ", ('vika', 'сейчас'), ", meaning 'now', at the very end."]),
    (9, None, ["'Otherwise I could have helped you.' Let's focus on this line: ", ('eleonora', 'А'), ('eleonora', 'то'), " at the start means 'because otherwise'. ", ('eleonora', 'могла'), ('eleonora', 'бы'), " combines a past form with a short word that turns it into 'would'. ", ('eleonora', 'вам'), ' is plural, addressing both of them.']),
    (10, None, ["'Mom, please, just leave from here.' Now she uses the full ", ('vika', 'Мама'), '. ', ('vika', 'уходи'), ' is an order to go away, and ', ('vika', 'отсюда'), " means 'from here', so no separate 'from' is needed."]),
    (11, None, ["'Alright, I will leave you in peace for now.' Now let's look at this line: ", ('eleonora', 'оставлю'), ('eleonora', 'вас'), ('eleonora', 'в'), ('eleonora', 'покое'), " reads as 'leave you in calm', which is the set phrase for leaving someone alone. ", ('eleonora', 'пока'), " here means 'for now', matching the usual word for goodbye."]),
]
