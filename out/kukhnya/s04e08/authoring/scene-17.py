ID = "kukhnya-s04e08-scene-17"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 8
SCENE = 17
TITLE = "Погоня за дизайнером  (Chasing the Designer)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "lyova": "anja", "guest": "angelina"}
LABELS = {"anya": "Шеф", "lyova": "Лёва", "guest": "Гость"}
SOURCE_NAME = "Кухня (Kukhnya) S4.08"
SOURCE_FILE = "sources/kukhnya/s04/e08.ru.srt"
SOURCE_NOTE = "Cues 283-300. When the young man returns to Arcobaleno to tell the owner he refuses to work there, Viktor Barinov and Lyova chase him into the kitchen, where the owner catches them in the act."

INTRO = "The next day at Arcobaleno, the young man Roman comes to the owner's office to say he cannot continue working on the project. Spotting Roman through the doorway, Viktor Barinov assumes he ignored yesterday's warning and chases him right into the kitchen!"

STORY = [
    ("guest", "Роман, в чём дело, куда же вы пропали?", "Roman, what is the matter, where did you disappear to?", [(284, "в чем дело? Роман, куда вы пропали?")], "adapted"),
    ("guest", "Понимаете, я не смогу дальше с вами работать.", "You understand, I will not be able to work with you any further.", [(286, "Понимаете, я не смогу с вами дальше работать.")], "adapted"),
    ("guest", "Подождите, но мы же обо всём уже договорились!", "Wait, but we already agreed on everything!", [(287, "Нет, секундочку, мы же обо всем договорились.")], "adapted"),
    ("guest", "Мы с вами утвердили основные цвета и стиль!", "We approved the main colors and style with you!", [(288, "Мы утвердили основные цвета, стиль.")], "adapted"),
    ("anya", "Смотри, Лёва, значит, этот парень нас не понял!", "Look, Lyova, so that guy did not understand us!", [(293, "Значит, ты не понял.")], "adapted"),
    ("anya", "Ладно, тогда мы сейчас объясним ему по-другому!", "Fine, then right now we will explain it to him differently!", [(294, "Ладно, объясним по-другому.")], "adapted"),
    ("anya", "А ну иди сюда, пойдём ещё раз поговорим!", "Come over here, let's go have another talk!", [(295, "Пойдем поговорим."), (296, "Иди сюда!")], "adapted"),
    ("guest", "Подождите, вы неправильно поняли, я просто ухожу!", "Wait, you misunderstood, I am simply leaving!", [(295, "А вы не поняли, я просто...")], "adapted"),
    ("anya", "Я что, вчера тебе неясно всё выразился?", "Did I not express myself clearly to you yesterday?", [(299, "неясно выразился?")], "adapted"),
    ("anya", "Я же сказал, ты здесь работать не будешь!", "I told you, you are not going to work here!", [(299, "Ты здесь работать не будешь!")], "adapted"),
    ("guest", "Да я и не собираюсь здесь больше работать!", "Why, I am not even planning to work here anymore!", [(300, "Да я не собираюсь.")], "adapted"),
    ("lyova", "Виктор Петрович, остановитесь, сюда идёт хозяин ресторана!", "Viktor Petrovich, stop, the owner of the restaurant is coming here!", [(300, "Так, Виктор Петрович, что происходит?")], "adapted"),
]

OPENER = "Let's break down the chase through the Arcobaleno kitchen line by line."

WALK = [
    (0, None, "'Roman, what is the matter, where did you disappear to?' The owner of Arcobaleno wonders why Roman stopped answering calls."),
    (1, None, "'You understand, I will not be able to work with you any further.' Shaken by yesterday's car ambush, Roman wants out."),
    (2, None, "'Wait, but we already agreed on everything!' Reflexive past verb 'agreed' governs the preposition 'about' plus prepositional."),
    (3, None, "'We approved the main colors and style with you!' Notice the clue that Barinov missed: Roman was hired for colors and interior style!"),
    (4, None, "'Look, Lyova, so that guy did not understand us!' Seeing Roman in the hallway, Barinov assumes he came to take Elena's job."),
    (5, None, "'Fine, then right now we will explain it to him differently!' Adverb 'in another way' signals another round of intimidation."),
    (6, None, "'Come over here, let's go have another talk!' Barinov and Lyova corner Roman and drag him into the kitchen."),
    (7, None, "'Wait, you misunderstood, I am simply leaving!' Roman tries in vain to explain why he came to the office."),
    (8, None, "'Did I not express myself clearly to you yesterday?' Reflexive past verb 'expressed oneself' pairs with the adverb 'unclearly'."),
    (9, None, "'I told you, you are not going to work here!' Barinov roars at the terrified young man across the kitchen."),
    (10, None, "'Why, I am not even planning to work here anymore!' Reflexive verb 'am intending/planning' confirms he is quitting."),
    (11, None, "'Viktor Petrovich, stop, the owner of the restaurant is coming here!' The owner walks in and demands to know what is going on."),
]

TRANSITION = "Now let's hear the kitchen chase scene at Arcobaleno again."
OUTRO = "Caught red-handed by the restaurant owner and Elena Pavlovna, Viktor Barinov finally learns the shocking truth about who is really leaving. See you in the next scene."
CLOSING = ("anya", "Я же сказал, ты здесь работать не будешь!")
CLOSING_TRANS = "I told you, you are not going to work here!"
