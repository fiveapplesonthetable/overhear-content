"""s01e12 scene 29: Рыбалка на озере (Fishing at the Lake)."""

ID = "domashniy-arest-s01e12-scene-29"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 12
SCENE = 29
TITLE = "Рыбалка на озере  (Fishing at the Lake)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "governor": "anja",
}
LABELS = {
    "anya": "Аркадий",
    "governor": "Губернатор",
}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.12"
SOURCE_FILE = "sources/domashniy-arest/s01/e12.ru.dual.srt"
SOURCE_NOTE = "Cues 733-757. Viktor Stepanovich takes Arkady out on a frozen lake for fishing and celebratory drinks, promising confidentiality."

INTRO = (
    "Claiming fatigue and the need for absolute secrecy, Governor Viktor Stepanovich drives Arkady out "
    "to a frozen lake for an impromptu winter fishing trip. Bundled against the cold, they share a toast "
    "to their shared political future. Let's listen in Russian first."
)

STORY = [
    ("governor", "Поехали скорее со мной на зимнее озеро.",
     "Come quickly with me to the winter lake.",
     [(734, "Уж поехали на озеро.")], ""),

    ("anya", "На улице сейчас очень сильный холод.",
     "There is very severe cold outside right now.",
     [(736, "Так холодно же.")], ""),

    ("governor", "Мы посидим на льду и половим рыбу.",
     "We will sit on the ice and catch fish.",
     [(735, "Посидим, рыбку"), (736, "половим.")], ""),

    ("governor", "Заодно без лишних ушей обсудим твоё назначение.",
     "At the same time without extra ears we will discuss your appointment.",
     [(739, "А заодно и обсудим назначение твое"), (740, "Без лишних ушей")], ""),

    ("anya", "Хорошо, Виктор Степанович, я с удовольствием поеду.",
     "Fine, Viktor Stepanovich, I will go with pleasure.",
     [], ""),

    ("governor", "Давай нальём в рюмки хорошей водки.",
     "Let's pour good vodka into the shot glasses.",
     [(748, "Ну давай, Аркаш"), (752, "Очень хорошая водка")], ""),

    ("governor", "Поднимем этот тост за твой будущий успех!",
     "Let's raise this toast to your future success!",
     [(749, "За тебя")], ""),

    ("anya", "За ваше высокое министерское назначение!",
     "To your high ministerial appointment!",
     [(750, "За вас, Виктор Степанович"), (751, "Ваше назначение")], ""),

    ("governor", "Только почему-то рыба здесь совсем не клюёт.",
     "Only for some reason the fish do not bite here at all.",
     [(753, "Чего-то рыба-то и не клюет совсем.")], ""),

    ("anya", "Это же теперь ваше профильное министерство.",
     "This is your specialized ministry now after all.",
     [(754, "Так это же теперь ваше министерство.")], ""),

    ("anya", "Вы сможете строго наказать местных чиновников.",
     "You will be able to punish local officials strictly.",
     [(755, "Настучите им по голове")], ""),

    ("governor", "Да, я наведу здесь железный порядок.",
     "Yes, I will establish iron order here.",
     [(757, "Да-да-да.")], ""),

    ("anya", "Мы создадим идеальную команду для работы.",
     "We will create an ideal team for work.",
     [], ""),

    ("governor", "Сначала выслушай меня очень внимательно, Аркаша.",
     "First listen to me very carefully, Arkasha.",
     [], ""),
]

OPENER = (
    "Let's examine the dialogue line by line. Notice the conversational idioms used to suggest "
    "informal get-togethers, toast promotions, and discuss bureaucratic influence."
)

WALK = [
    (0, None,
     "'Come quickly with me to the winter lake.' Imperative verb of motion with comparative adverb and prepositional destination."),
    (1, None,
     "'There is very severe cold outside right now.' Locative adverbial phrase followed by temporal adverb and descriptive nominative noun phrase."),
    (2, None,
     "'We will sit on the ice and catch fish.' Two coordinated future perfective verbs with prepositional location and direct object."),
    (3, None,
     "'At the same time without extra ears we will discuss your appointment.' Temporal adverb with negative prepositional phrase and future transitive verb."),
    (4, None,
     "'Fine, Viktor Stepanovich, I will go with pleasure.' Conversational agreement formula with patronymic address and future verb of motion."),
    (5, None,
     "'Let's pour good vodka into the shot glasses.' Cohortative imperative with prepositional goal and descriptive genitive object."),
    (6, None,
     "'Let's raise this toast to your future success!' Future cohortative verb governing accusative noun with prepositional beneficiary."),
    (7, None,
     "'To your high ministerial appointment!' Elliptical toast prepositional phrase with two qualifying adjectives."),
    (8, None,
     "'Only for some reason the fish do not bite here at all.' Particle phrase with indefinite adverb and negative present imperfective verb."),
    (9, None,
     "'This is your specialized ministry now after all.' Demonstrative pronoun with emphatic particle and descriptive predicate noun phrase."),
    (10, None,
     "'You will be able to punish local officials strictly.' Future modal verb with manner adverb and perfective infinitive governing accusative."),
    (11, None,
     "'Yes, I will establish iron order here.' Affirmative particle with future perfective verb and figurative accusative object."),
    (12, None,
     "'We will create an ideal team for work.' First person plural future perfective verb with descriptive object and purpose phrase."),
    (13, None,
     "'First listen to me very carefully, Arkasha.' Temporal adverb with imperative verb, accusative pronoun, and manner adverb."),
]

TRANSITION = "Now let's listen to their cordial exchange on the frozen lake once more."

OUTRO = (
    "Under the guise of friendly fishing and celebration, Viktor Stepanovich is preparing to "
    "deliver a devastating ultimatum to Arkady. See you next time!"
)

CLOSING = ("governor", "Поднимем этот тост за твой будущий успех!")
