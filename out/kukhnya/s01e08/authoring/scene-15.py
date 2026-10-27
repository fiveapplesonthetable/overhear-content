"""s01e08 scene 15: Звонок Нагиеву (Phone Call to Nagiyev)."""

ID = "kukhnya-s01e08-scene-15"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 15
TITLE = "Звонок Нагиеву  (Phone Call to Nagiyev)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja"}
LABELS = {"anya": "Саша", "max": "Макс"}
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"
SOURCE_NOTE = "Cues 185-202. Sasha talks on the phone with Dmitry Nagiyev about his dog Tyson, realizing she and Max need to buy a replacement."

INTRO = (
    "While standing in Claude Monet, waitress Sasha receives a sudden telephone call from restaurant owner Dmitry Nagiyev. "
    "Nervously pretending that his small dog Tyson is healthy and playing happily, Sasha asks for the exact breed before realizing they must urgently buy a lookalike. "
    "Let's listen to their phone call and aftermath in Russian."
)

STORY = [
    ("anya", "Да, здравствуйте, Дмитрий Владимирович!", "Yes, hello, Dmitry Vladimirovich!",
     [(185, "Да, Дмитрий Владимирович")], ""),
    ("anya", "Тайсон чувствует себя прекрасно.", "Tyson feels great.",
     [(186, "Тайсон? Тайсон хорошо")], ""),
    ("anya", "Он бегает и очень весело играет.", "He runs around and plays very merrily.",
     [(187, "Да, бегает"), (188, "Такой веселый и гривый")], ""),
    ("max", "Зачем ты так нагло врёшь?", "Why are you lying so boldly?",
     [(189, "А, и мертвый")], ""),
    ("anya", "Подскажите, пожалуйста, какая у него порода?", "Could you tell me, please, what breed he is?",
     [(190, "а вы не подскажете, что это за порода?")], ""),
    ("anya", "Я просто влюбилась в эту собаку.", "I simply fell in love with this dog.",
     [(191, "я просто влюблена")], ""),
    ("anya", "Как называется эта порода, ши-тцу?", "What is this breed called, Shih Tzu?",
     [(195, "А, ши-цу"), (196, "Ши-цу")], ""),
    ("anya", "Вы можете совсем не спешить обратно.", "You do not need to rush back at all.",
     [(197, "вы не спешите")], ""),
    ("anya", "Мы с ним отлично ладим.", "He and I get along wonderfully.",
     [(198, "Мы с Таисиным прекрасно ладим")], ""),
    ("anya", "Спасибо вам большое, до свидания!", "Thank you very much, goodbye!",
     [(199, "Да, да, спасибо"), (200, "до свидания")], ""),
    ("max", "И что теперь нам делать?", "And what are we to do now?",
     [], ""),
    ("anya", "Нужно срочно ехать покупать собаку!", "We need to go buy a dog urgently!",
     [(201, "Нужно ехать покупать собаку")], ""),
    ("max", "Но где мы найдём такую собаку?", "But where will we find such a dog?",
     [(202, "Куда?")], ""),
]

OPENER = "Let's follow how Sasha manages a stressful telephone inquiry from the restaurant owner."

WALK = [
    (2, None,
     "'He runs around and plays very merrily.' Two present tense verbs describe continuous active play with an expressive adverb in the sentence."),
    (5, None,
     "'I simply fell in love with this dog.' A reflexive past tense verb paired with a prepositional accusative expresses affectionate admiration."),
    (8, None,
     "'He and I get along wonderfully.' The collaborative plural pronoun construction indicates joint activity and mutual harmony."),
    (11, None,
     "'We need to go buy a dog urgently!' A modal predicative construction combined with multiple dependent infinitives conveys immediate urgency."),
]

TRANSITION = "Now, let's hear Sasha's deceptive phone conversation once more."

OUTRO = (
    "Now you know how to talk about pets, handle nervous phone inquiries, and discuss urgent problem-solving in Russian. "
    "Listen for these lively expressions in the next scene."
)

CLOSING = ("anya", "Мы должны обойти все зоомагазины города.")
