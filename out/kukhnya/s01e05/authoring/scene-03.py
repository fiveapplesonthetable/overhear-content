ID = "kukhnya-s01e05-scene-03"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 5
SCENE = 3
TITLE = "Операция «Треска»  (Operation Cod)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Саша", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.05"
SOURCE_FILE = "sources/kukhnya/s01/e05.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 38-46. Chef Viktor Barinov holds a staff meeting after someone accidentally thaws five kilograms of cod. "
    "He orders head waitress Sasha to push the cod on dinner guests with a twenty percent discount."
)

INTRO = (
    "Morning briefing in the Claude Monet kitchen takes an urgent turn. "
    "Chef Viktor Barinov discovers that someone improperly thawed five kilograms of fresh cod that must be cooked today. "
    "To avoid a costly loss, Barinov instructs head waitress Sasha to aggressively promote fish specials with a twenty percent discount. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("chef", "Внимание, повара! Начнём наше собрание.",
     "Attention, cooks! Let us begin our meeting.",
     [(38, "начнем собрание")], "adapted"),
    ("anya", "Шеф, что сегодня стряслось на кухне?",
     "Chef, what happened in the kitchen today?",
     [], "new"),
    ("chef", "Кто-то вчера разморозил пять килограммов трески.",
     "Someone thawed five kilograms of cod yesterday.",
     [(39, "разморозил пять килограммов трески")], "adapted"),
    ("anya", "И что нам теперь делать?",
     "And what are we to do now?",
     [], "new"),
    ("chef", "Мы обязаны продать всю рыбу сегодня!",
     "We must sell all the fish today!",
     [(40, "мы должны ее сегодня продать")], "adapted"),
    ("anya", "Гости заказывают только мясо и пасту.",
     "Guests only order meat and pasta.",
     [], "new"),
    ("chef", "Саша, подойди ко мне немедленно.",
     "Sasha, come to me immediately.",
     [(42, "Саша! Зайди сюда")], "adapted"),
    ("anya", "Я слушаю вас внимательно, шеф.",
     "I am listening to you carefully, chef.",
     [(43, "Да, шеф")], "adapted"),
    ("chef", "Передай официантам: сегодня активно предлагаем треску.",
     "Tell the waiters: today we actively offer cod.",
     [(43, "что сегодня продаем треску")], "adapted"),
    ("anya", "Может быть, сделаем специальную скидку?",
     "Maybe we will give a special discount?",
     [], "new"),
    ("chef", "Да, скидка двадцать процентов на рыбу.",
     "Yes, twenty percent discount on fish.",
     [(44, "скидка 20%")], "adapted"),
    ("anya", "Понятно, шеф, мы всё организуем.",
     "Understood, chef, we will organize everything.",
     [(45, "Понятно")], "adapted"),
    ("chef", "Если рыба останется, я вас оштрафую!",
     "If fish remains, I will fine you!",
     [], "new"),
]

OPENER = "Now let's examine Chef Barinov and Sasha's kitchen orders line by line."

WALK = [
    (0, None,
     "'Attention, cooks! Let us begin our meeting.' Barinov calls the staff to order with an imperative phrase."),
    (1, None,
     "'Chef, what happened in the kitchen today?' Sasha asks about the emergency with an informal past verb."),
    (2, None,
     "'Someone thawed five kilograms of cod yesterday.' The chef announces the problem using a past perfective verb."),
    (3, None,
     "'And what are we to do now?' Sasha inquires about the strategy with an infinitive question."),
    (4, None,
     "'We must sell all the fish today!' Barinov delivers the mission using a modal short adjective and infinitive."),
    (5, None,
     "'Guests only order meat and pasta.' Sasha highlights customer preferences with a present imperfective verb."),
    (6, None,
     "'Sasha, come to me immediately.' Barinov summons the head waitress with a direct imperative."),
    (7, None,
     "'I am listening to you carefully, chef.' Sasha answers respectfully using a present active verb."),
    (8, None,
     "'Tell the waiters: today we actively offer cod.' The chef gives marketing instructions with an adverb of manner."),
    (9, None,
     "'Maybe we will give a special discount?' Sasha proposes a price incentive using a future verb and accusative noun."),
    (10, None,
     "'Yes, twenty percent discount on fish.' Barinov approves the promotion using a numerical phrase."),
    (11, None,
     "'Understood, chef, we will organize everything.' Sasha confirms the plan using an adverb and future perfective verb."),
    (12, None,
     "'If fish remains, I will fine you!' Barinov concludes with a stern disciplinary threat in the conditional."),
]

TRANSITION = "Now let's listen to the kitchen briefing again without interruption."
OUTRO = (
    "Sasha heads out to brief the waitstaff on pushing the discounted cod special. "
    "In the next scene, Max attempts to dispel Nastya's romantic illusions during their shift."
)
CLOSING = ("chef", "Если рыба останется, я вас оштрафую!")
