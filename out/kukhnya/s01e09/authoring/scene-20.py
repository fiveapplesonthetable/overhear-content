"""Scene 20 — New Discoveries (s01e09, 00:22:51–00:23:22)."""

ID = "kukhnya-s01e09-scene-20"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 9
SCENE = 20
TITLE = "Новые открытия  (New Discoveries)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.09"
SOURCE_FILE = "sources/kukhnya/s01/e09.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "louis": "anja",
}

LABELS = {
    "anya": "Макс",
    "louis": "Луи",
}

INTRO = (
    "Late at night in the quiet kitchen of Claude Monet, Max watches Louis patiently crafting delicate desserts. "
    "Reflecting on how easily we misjudge people, Max apologizes to the pastry chef and discovers the profound art behind his culinary craft."
)

STORY = [
    ("anya", "Луи, ты всё ещё работаешь на кухне?",
     "Louis, are you still working in the kitchen?",
     [], "Max approaches"),

    ("louis", "Да, я делаю нежный шоколадный крем.",
     "Yes, I am making delicate chocolate cream.",
     [], "Louis explains"),

    ("anya", "Тебе кажется, что он ко всему равнодушен.",
     "It seems to you that he is indifferent to everything.",
     [(350, "Тебе кажется, что он ко всему равнодушен.")], "Max begins reflection"),

    ("anya", "Но понимаешь, что мало знаешь о нём.",
     "Then you realize you know little about him.",
     [(351, "Но понимаешь, что мало знаешь о нем.")], "Max reconsiders"),

    ("anya", "Луи, не обижайся на мои глупые слова.",
     "Louis, do not take offense at my silly words.",
     [(352, "Слушай, Луи, ты, если что, не обижайся на меня.")], "Max apologizes"),

    ("anya", "Я был совсем не прав насчёт тебя.",
     "I was completely wrong about you.",
     [(353, "Я не прав был.")], "Max admits error"),

    ("louis", "Ничего страшного, Макс, я понимаю.",
     "Nothing terrible, Max, I understand.",
     [(355, "О, ну.")], "Louis forgives"),

    ("anya", "Готовить такие десерты — это реально сложно.",
     "Cooking such desserts is really difficult.",
     [(354, "То, что ты делаешь, это реально сложно.")], "Max compliments"),

    ("louis", "Многие думают, что это простые сладости.",
     "Many think that these are simple sweets.",
     [(356, "Первым, да. Подумаешь, какие-то десертики.")], "Louis comments"),

    ("louis", "Но кондитерское искусство требует большого терпения.",
     "But confectionery art requires great patience.",
     [], "Louis shares philosophy"),

    ("anya", "Теперь я очень уважаю твой труд.",
     "Now I respect your work very much.",
     [], "Max expresses respect"),

    ("louis", "Спасибо, Макс, попробуй этот свежий десерт.",
     "Thank you, Max, try this fresh dessert.",
     [], "Louis offers dessert"),

    ("anya", "Как много открытий нам ещё предстоит.",
     "How many discoveries still lie ahead for us.",
     [(357, "Как много открытий нам предстоит.")], "Max looks forward"),

    ("anya", "И это по-настоящему здорово для нас!",
     "And this is truly wonderful for us!",
     [(358, "И это здорово.")], "Max concludes"),
]

OPENER = "Let's explore Max's sincere apology to Louis and his thoughtful reflections on discovering the true depth of others."

WALK = [
    (0, None,
     "'Louis, are you still working in the kitchen?' Max approaches the pastry station late at night."),
    (1, None,
     "'Yes, I am making delicate chocolate cream.' Louis concentrates carefully on his sweet creation."),
    (2, None,
     "'It seems to you that he is indifferent to everything.' Max reflects quietly on his past assumptions."),
    (3, None,
     "'Then you realize you know little about him.' Max admits that first impressions are often mistaken."),
    (4, None,
     "'Louis, do not take offense at my silly words.' Max speaks with sincere regret to his coworker."),
    (5, None,
     "'I was completely wrong about you.' Max openly acknowledges his mistake to the pastry chef."),
    (6, None,
     "'Nothing terrible, Max, I understand.' Louis smiles warmly and accepts the heartfelt apology."),
    (7, None,
     "'Cooking such desserts is really difficult.' Max expresses newfound admiration for pastry skills."),
    (8, None,
     "'Many think that these are simple sweets.' Louis explains the common misconception about his work."),
    (9, None,
     "'But confectionery art requires great patience.' The pastry chef describes the dedication demanded by his craft."),
    (10, None,
     "'Now I respect your work very much.' Max shows genuine appreciation for his colleague."),
    (11, None,
     "'Thank you, Max, try this fresh dessert.' Louis generously offers a sweet sample to taste."),
    (12, None,
     "'How many discoveries still lie ahead for us.' Max reflects on the endless lessons learned from people."),
    (13, None,
     "'And this is truly wonderful for us!' Max smiles with gratitude as the night shift concludes."),
]

TRANSITION = "Now let's listen to the quiet kitchen exchange between Max and Louis one more time."

OUTRO = "As the shift ends with mutual respect and a taste of fresh dessert, Max realizes that understanding other people is a lifelong journey of wonderful discoveries."

CLOSING = ("anya", "И это по-настоящему здорово для нас!")
