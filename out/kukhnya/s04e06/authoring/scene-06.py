ID = "kukhnya-s04e06-scene-06"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 6
SCENE = 6
TITLE = "Перенос встречи  (Rescheduling the Visit)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "guest": "anja"}
LABELS = {"anya": "Шеф", "guest": "Гость"}
SOURCE_NAME = "Кухня (Kukhnya) S4.06"
SOURCE_FILE = "sources/kukhnya/s04/e06.ru.srt"
SOURCE_NOTE = "Cues 71-79. Right after Elena leaves for the afternoon spa session, Volodya calls Barinov to cancel lunch and reschedule his visit to Arcobaleno for dinner instead."

INTRO = "Seconds after Elena Pavlovna walks out the door for her afternoon spa appointment, Viktor Barinov's phone rings. It is his friend Volodya calling to say that he cannot make it for lunch after all and will come to Arcobaleno for dinner instead—right when Elena will be back!"

STORY = [
    ("anya", "Да, Володя, привет, я тебя уже жду!", "Yes, Volodya, hi, I am already waiting for you!", [(71, "Да, Володь. Вить, привет.")], "adapted"),
    ("guest", "Витя, у нас не получится зайти на обед.", "Vitya, we will not be able to drop by for lunch.", [(72, "не получится у нас к тебе зайти на обед.")], "adapted"),
    ("guest", "У нас самолёт вечером, а дел ещё много.", "Our plane is in the evening, and there is still much to do.", [(73, "самолет вечером, а еще столько дел сделать надо.")], "adapted"),
    ("anya", "Как же вы так меня подводите, друзья?", "How can you let me down like that, folks?", [(75, "Что же вы так?")], "adapted"),
    ("anya", "Вы меня сейчас просто очень сильно расстроили.", "You have just upset me very much right now.", [(76, "Вы меня очень расстроили.")], "adapted"),
    ("guest", "Прости меня, пожалуйста, мой старый друг.", "Please forgive me, my old pal.", [(77, "Прости, дружище.")], "adapted"),
    ("anya", "Я так старался вас сегодня вкусно удивить.", "I tried so hard to surprise you deliciously today.", [(77, "Я старался вас как-то удивить")], "adapted"),
    ("guest", "Хорошо, тогда мы заедем к тебе на ужин!", "All right, then we will stop by your place for dinner!", [(78, "тогда мы заедем к тебе прямо перед рейсом на ужин")], "adapted"),
    ("guest", "Заедем прямо перед нашим вечерним рейсом.", "We will drop in right before our evening flight.", [(78, "прямо перед рейсом")], "adapted"),
    ("anya", "Подожди, вы хотите приехать вечером на ужин?", "Wait, you want to come in the evening for dinner?", [], "new"),
    ("guest", "Да, вечером мы точно будем у тебя!", "Yes, in the evening we will definitely be at your place!", [], "new"),
    ("anya", "Нет проблем, Володя, буду вас ждать вечером.", "No problem, Volodya, I will wait for you in the evening.", [(79, "Нет проблем, жду.")], "adapted"),
]

OPENER = "Let's break down Volodya's phone call to Barinov line by line."

WALK = [
    (0, None, "'Yes, Volodya, hi, I am already waiting for you!' Present-tense verb 'waiting' governs the accusative pronoun."),
    (1, None, "'Vitya, we will not be able to drop by for lunch.' Impersonal reflexive future verb expresses whether a plan will work out."),
    (2, None, "'Our plane is in the evening, and there is still much to do.' Genitive plural 'of matters' follows the quantity adverb."),
    (3, None, "'How can you let me down like that, folks?' Barinov pretends to be disappointed that they are missing lunch."),
    (4, None, "'You have just upset me very much right now.' Perfective past plural verb describes causing disappointment."),
    (5, None, "'Please forgive me, my old pal.' Singular perfective imperative asks for pardon between close friends."),
    (6, None, "'I tried so hard to surprise you deliciously today.' Barinov lays the guilt on thick, causing his friend to reconsider."),
    (7, None, "'All right, then we will stop by your place for dinner!' To Barinov's horror, Volodya switches the visit to dinnertime."),
    (8, None, "'We will drop in right before our evening flight.' Preposition 'before' governs the instrumental singular of 'flight'."),
    (9, None, "'Wait, you want to come in the evening for dinner?' Barinov realizes he wasted his spa gift on the wrong shift."),
    (10, None, "'Yes, in the evening we will definitely be at your place!' Instrumental singular 'in the evening' marks the time of day."),
    (11, None, "'No problem, Volodya, I will wait for you in the evening.' Forced to agree, Barinov now needs a new plan for tonight."),
]

TRANSITION = "Now let's listen to the phone call about rescheduling the visit again."
OUTRO = "With Volodya now coming at dinnertime instead of lunch, Barinov has to figure out how to keep Elena away from Arcobaleno in the evening too. See you in the next scene."
CLOSING = ("anya", "Вы меня сейчас просто очень сильно расстроили.")
CLOSING_TRANS = "You have just upset me very much right now."
