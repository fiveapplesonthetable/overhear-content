"""s01e08 scene 09: Секрет в раздевалке (A Secret in the Locker Room)."""

ID = "kukhnya-s01e08-scene-09"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 9
TITLE = "Секрет в раздевалке  (A Secret in the Locker Room)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja"}
LABELS = {"anya": "Макс", "vika": "Вика"}
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"

INTRO = (
    "In the restaurant locker room, Max and art director Victoria desperately try to hide Dmitry Nagiyev's unconscious dog after a freak accident with a hot dog. "
    "Victoria is terrified of Dmitry's fury, while Max tries to keep calm despite standing in his underwear. "
    "Let's listen to their frantic conversation in Russian first."
)

STORY = [
    ("vika", "Осторожней, куда ты прячешь бедную собаку?",
     "Careful, where are you hiding the poor dog?",
     [(116, "Осторожней"), (117, "Куда ты ее прячешь")], "panicking over the pet"),
    ("anya", "Здесь в раздевалке её никто не найдёт.",
     "Here in the locker room nobody will find her.",
     [(117, "Здесь все найдут")], "seeking a hidden place"),
    ("vika", "Боже мой, что я скажу Дмитрию?",
     "My God, what will I tell Dmitry?",
     [(110, "Боже мой, что я скажу Дмитрию Владимировну")], "fearing the owner's anger"),
    ("anya", "Скажи ему правду, что собака просто убежала.",
     "Tell him the truth, that the dog simply ran away.",
     [(113, "скажешь, что сбежала твоя собака")], "suggesting a cover story"),
    ("vika", "Дмитрий Владимирович будет просто в ярости!",
     "Dmitry Vladimirovich will be simply furious!",
     [], "dreading Nagiyev's reaction"),
    ("anya", "Успокойся, она скоро сама придёт в себя.",
     "Calm down, she will soon come to her senses herself.",
     [], "trying to comfort her"),
    ("vika", "Ты почему стоишь передо мной без штанов?",
     "Why are you standing in front of me without pants?",
     [(98, "Где форма"), (123, "Без штанов разговор лучше клеится")], "noticing his state"),
    ("anya", "Мои джинсы сейчас стираются в машинке.",
     "My jeans are being washed in the machine right now.",
     [(99, "А джинсы стираются")], "explaining his lack of clothes"),
    ("vika", "Надень скорее хоть что-нибудь на себя!",
     "Put at least something on yourself quickly!",
     [], "urging him to cover up"),
    ("anya", "Сначала давай аккуратно положим собаку сюда.",
     "First let us carefully put the dog here.",
     [(120, "Подожди, ты на сюда")], "focusing on the priority"),
    ("vika", "Ладно, положи её тихо на нижнюю полку.",
     "Fine, put her quietly on the bottom shelf.",
     [(118, "Пусть пока здесь полежит")], "agreeing on the spot"),
    ("anya", "Всё будет хорошо, никто ничего не узнает!",
     "Everything will be fine, nobody will find out anything!",
     [(122, "Ничем. Просто разговариваем")], "reassuring her with confidence"),
]

OPENER = "Let's review this frantic locker room exchange line by line."

WALK = [
    (0, None,
     "'Careful, where are you hiding the poor dog?' Victoria panics as Max moves the limp pet."),
    (1, None,
     "'Here in the locker room nobody will find her.' Max suggests a temporary hiding spot among the staff lockers."),
    (2, None,
     "'My God, what will I tell Dmitry?' Victoria worries about facing the furious restaurant owner."),
    (3, None,
     "'Tell him the truth, that the dog simply ran away.' Max devises a quick cover story to buy them time."),
    (4, None,
     "'Dmitry Vladimirovich will be simply furious!' Victoria anticipates an explosive reaction from Nagiyev."),
    (5, None,
     "'Calm down, she will soon come to her senses herself.' Max reassures her that the animal is merely stunned."),
    (6, None,
     "'Why are you standing in front of me without pants?' Victoria suddenly notices Max's complete lack of trousers."),
    (7, None,
     "'My jeans are being washed in the machine right now.' Max explains his awkward state of undress."),
    (8, None,
     "'Put at least something on yourself quickly!' Victoria demands that he cover up immediately."),
    (9, None,
     "'First let us carefully put the dog here.' Max prioritizes concealing the unconscious pet."),
    (10, None,
     "'Fine, put her quietly on the bottom shelf.' Victoria points out an out-of-the-way locker."),
    (11, None,
     "'Everything will be fine, nobody will find out anything!' Max offers confident comfort to calm her nerves."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal conversational speed."

OUTRO = (
    "Hiding the little dog on a locker shelf, Max and Victoria hope their secret stays safe from the rest of the staff. "
    "See you next time!"
)

CLOSING = ("anya", "Всё будет хорошо, никто ничего не узнает!")
