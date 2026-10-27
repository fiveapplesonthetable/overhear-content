"""s01e12 scene 28: Всё за пост министра (All for the Minister Post)."""

ID = "domashniy-arest-s01e12-scene-28"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 12
SCENE = 28
TITLE = "Всё за пост министра  (All for the Minister Post)"
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
SOURCE_NOTE = "Cues 713-732. Arkady watches the money bags being loaded for the minister post; Viktor Stepanovich promises to make him the next governor."

INTRO = (
    "At the governor's residence, Arkady Borisovich watches with amazement as millions of rubles are "
    "loaded into heavy bags. Viktor Stepanovich reassures Arkady that the money is an investment and "
    "promises him the governorship of the region. Let's listen in Russian first."
)

STORY = [
    ("anya", "Это всё только за пост министра?",
     "Is all of this only for the post of minister?",
     [(713, "Это все за министра?")], ""),

    ("governor", "А ты как думал? Там всё серьёзно.",
     "And what did you think? Everything is serious there.",
     [(714, "А ты что хотел?"), (715, "Там все по-взрослому.")], ""),

    ("anya", "Может быть, стоит немного поторговаться?",
     "Maybe it is worth bargaining a little?",
     [(717, "Может, как-то поторговаться?")], ""),

    ("governor", "Аркаша, в Москве никогда не торгуются.",
     "Arkasha, they never bargain in Moscow.",
     [(718, "Аркаш, там не торгуются.")], ""),

    ("governor", "Я быстро отобью все эти деньги.",
     "I will quickly win all this money back.",
     [(720, "Это я за полгода отобью.")], ""),

    ("anya", "Сумма действительно кажется огромной.",
     "The sum really seems enormous.",
     [], ""),

    ("governor", "Я решил сделать тебя губернатором области.",
     "I decided to make you governor of the region.",
     [(725, "Губернатором тебе сделаю.")], ""),

    ("anya", "Вы действительно говорите совершенно серьёзно?",
     "Are you really speaking completely seriously?",
     [], ""),

    ("governor", "Ты молодой и очень перспективный руководитель.",
     "You are a young and very promising leader.",
     [(727, "Молодой, перспективный.")], ""),

    ("governor", "Я не отдам область чужим людям.",
     "I will not give the region to strangers.",
     [(728, "Думаешь, я кому-нибудь другому"), (729, "область отдам? Сейчас.")], ""),

    ("governor", "Грузите скорее все сумки в багажник.",
     "Load all the bags into the trunk quickly.",
     [(730, "Грузите, ребята.")], ""),

    ("anya", "Виктор Степанович, огромное спасибо за доверие.",
     "Viktor Stepanovich, huge thanks for your trust.",
     [(731, "Виктор Степанович, спасибо.")], ""),

    ("governor", "Всё, расслабься, теперь ты под защитой.",
     "That's it, relax, now you are under protection.",
     [(732, "Все. Заслабься.")], ""),

    ("anya", "Я вас никогда не подведу.",
     "I will never let you down.",
     [], ""),
]

OPENER = (
    "Let's examine the dialogue line by line. Notice the expressions used to discuss financial "
    "negotiations, political promises, and personal loyalty."
)

WALK = [
    (0, None,
     "'Is all of this only for the post of minister?' Interrogative question with demonstrative pronoun and prepositional purpose phrase."),
    (1, None,
     "'And what did you think? Everything is serious there.' Conversational question followed by a short predicative clause."),
    (2, None,
     "'Maybe it is worth bargaining a little?' Modal phrase governing an impersonal predicative and reflexive infinitive."),
    (3, None,
     "'Arkasha, they never bargain in Moscow.' Direct address with locative prepositional phrase and negative reflexive present verb."),
    (4, None,
     "'I will quickly win all this money back.' First person future perfective verb with manner adverb and demonstrative object."),
    (5, None,
     "'The sum really seems enormous.' Nominative feminine subject with modal adverb and instrumental predicate adjective."),
    (6, None,
     "'I decided to make you governor of the region.' Past perfective transitive verb with infinitive governing instrumental title."),
    (7, None,
     "'Are you really speaking completely seriously?' Interrogative question with second person plural present verb and two manner adverbs."),
    (8, None,
     "'You are a young and very promising leader.' Descriptive predicate noun phrase with two coordinated qualifying adjectives."),
    (9, None,
     "'I will not give the region to strangers.' Negative future transitive verb with direct object and dative recipient phrase."),
    (10, None,
     "'Load all the bags into the trunk quickly.' Imperative plural verb with comparative adverb and prepositional destination."),
    (11, None,
     "'Viktor Stepanovich, huge thanks for your trust.' Polite gratitude formula with patronymic address and prepositional object."),
    (12, None,
     "'That's it, relax, now you are under protection.' Interjection with imperative verb and prepositional state expression."),
    (13, None,
     "'I will never let you down.' Negative future perfective transitive verb with temporal adverb and accusative pronoun."),
]

TRANSITION = "Now let's listen to Arkady and the governor's grand bargain once again."

OUTRO = (
    "Thrilled by the promise of becoming regional governor, Arkady trusts Viktor Stepanovich completely, "
    "blind to the betrayal in store. See you next time!"
)

CLOSING = ("governor", "Я решил сделать тебя губернатором области.")
