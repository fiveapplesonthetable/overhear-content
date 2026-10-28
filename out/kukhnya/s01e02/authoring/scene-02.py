# Authoring module for kukhnya-s01e02-scene-02.
ID = 'kukhnya-s01e02-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 2
TITLE = "Опоздание на смену  (Late for the Shift)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
LABELS = {"barinov": "Шеф", "max": "Макс"}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = "Max arrives two hours late for his shift at Claude Monet, and head chef Viktor Barinov could not be happier. He bet the other cooks that Max would be late, and he has just won. As Max's \"reward\", he sends him off to unload deliveries all day. Here is their exchange in Russian first."
OPENER = "Now let's take it again slowly, and watch Barinov enjoy himself."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "You'll hear Barinov call Max \"oguzok\" many more times in the series. See you next time!"
CLOSING = ("barinov", "Пока!")
STORY = [
    ('barinov', 'Лавров, ты опоздал на два часа!', 'Lavrov, you are two hours late!', [(9, 'ты опоздал на два часа')], ''),
    ('barinov', 'Он опоздал, значит, я выиграл спор!', 'He is late, meaning I won the bet!', [(12, 'Он опоздал, я выиграл')], ''),
    ('barinov', 'Все, кто ставил, скидывайтесь быстро!', 'Everyone who bet, pay up quickly!', [(13, 'Все, кто ставил, скидывайтесь'), (14, 'Быстро, быстро')], ''),
    ('max', 'Шеф, простите, я попал в пробку.', 'Chef, forgive me, I got stuck in a traffic jam.', [], ''),
    ('barinov', 'Ты поднял мне настроение сегодня утром.', 'You lifted my mood this morning.', [(15, 'ты мне поднял настроение')], ''),
    ('barinov', 'Поэтому я награждаю тебя важным делом.', 'Therefore I reward you with an important task.', [(16, 'я тебя награждаю очень важным')], ''),
    ('barinov', 'Ты будешь целый день разгружать продукты!', 'You will unload groceries the whole day!', [(17, 'Ты будешь разгружать продукты')], ''),
    ('max', 'Шеф, но я думал, я буду готовить.', 'Chef, but I thought I would be cooking.', [(19, 'Шеф, я думал, я буду готовить')], ''),
    ('barinov', 'Ты приписал себе две несуществующие способности!', 'You credited yourself with two non-existent abilities!', [(20, 'приписал себе две несуществующие способности')], ''),
    ('barinov', 'Способность думать и способность готовить!', 'The ability to think and the ability to cook!', [(21, 'Думать и готовить')], ''),
    ('max', 'Я очень хорошо учился в кулинарном колледже.', 'I studied very well at the culinary college.', [], ''),
    ('barinov', 'А здесь ресторан, а не твой колледж!', 'And here is a restaurant, not your college!', [], ''),
    ('barinov', 'А ну живо иди работать, огузок!', 'Now go to work immediately, oguzok!', [(22, 'А ну, мах')], ''),
]
WALK = [
    (0, None, "'Lavrov, you are two hours late!' Barinov doesn't say \"Max\". He uses the surname, the way a stern boss puts you in your place. The two hours are the whole problem."),
    (1, None, "'He is late, meaning I won the bet!' He isn't even angry yet: the chef had money on this."),
    (2, None, "'Everyone who bet, pay up quickly!' Now he turns to the rest of the kitchen to collect. The word he uses means \"chip in\", and it's what you'd shout at a group who all owe you money."),
    (3, None, "'Chef, forgive me, I got stuck in a traffic jam.' Max tries the oldest excuse there is. \"Forgive me\" is the polite, formal version, the kind you say to a boss and not to a friend."),
    (4, None, "'You lifted my mood this morning.' Sarcasm, and not very hidden. A bad morning for Max is good news for Barinov, and he says it with a straight face."),
    (5, None, "'Therefore I reward you with an important task.' Notice how grand he makes it sound. \"Reward\" is a prize word, and the prize is a chore. That gap is the joke."),
    (6, None, "'You will unload groceries the whole day!' And there is the reward: unloading deliveries from morning to night. After \"important task\" it lands like a punchline."),
    (7, None, "'Chef, but I thought I would be cooking.' Max dares to say what he hoped for. \"I thought\" is a handy way to point out, politely, that your expectations were different."),
    (8, None, "'You credited yourself with two non-existent abilities!' Barinov turns Max's words into a joke at his expense. Literally it's close to \"you wrote them down for yourself\", as if Max had padded his CV."),
    (9, None, "'The ability to think and the ability to cook!' He says \"ability\" twice, once for each skill, so the insult lands twice, like a drum beat."),
    (10, None, "'I studied very well at the culinary college.' Max defends himself with his one card, school. It's a weak answer and he knows it."),
    (11, None, "'And here is a restaurant, not your college!' Barinov shuts that down fast. In Russian the same small word can mean \"and\" or \"but\", and here it means \"but\"."),
    (12, None, "'Now go to work immediately, oguzok!' \"Oguzok\" is Barinov's nickname for Max. It's actually a cut of meat from the rear of the animal, so the chef is calling him scraps."),
]
