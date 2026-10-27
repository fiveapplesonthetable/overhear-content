ID = "kukhnya-s01e14-scene-07"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 7
TITLE = "Байки Макса  (Max's Tall Tales)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja"}
LABELS = {"anya": "Саша", "max": "Макс"}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 136-148. Max shows off in front of the dining room girls, pretending to be a famous chef "
    "who cooked for Gerard Depardieu in Paris."
)

INTRO = (
    "In the dining room, Max shows off in front of the waitresses, pretending to be a famous chef "
    "who cooked for the actor Gerard Depardieu in Paris. Enchanted by his lies, the girls beg him "
    "for more stories. Let us listen to his tall tales in Russian first."
)

STORY = [
    ("max", "Жерар Депардье доедает моё блюдо и говорит.",
     "Gerard Depardieu finishes my dish and says.",
     [(136, "доедает Депардье ему родоту и говорит.")], "adapted"),
    ("anya", "Неужели ему так сильно всё понравилось?",
     "Did he really like everything so much?",
     [], "new"),
    ("max", "Он сказал, что это просто невероятно вкусно!",
     "He said that it is simply incredibly tasty!",
     [(137, "офигеть!")], "adapted"),
    ("anya", "Что, он прямо так тебе и сказал?",
     "What, did he say it to you exactly like that?",
     [(139, "Что, прям так и сказала?")], "adapted"),
    ("max", "Да, именно так, только на французском языке.",
     "Yes, exactly like that, only in the French language.",
     [(140, "Да. Ну, то по-французски.")], "adapted"),
    ("anya", "Какой же ты талантливый повар, Макс!",
     "What a talented cook you are, Max!",
     [], "new"),
    ("max", "Такую вкусную еду не готовит даже мама!",
     "Even a mother does not cook such tasty food!",
     [(138, "Такой родоту не готовит даже моя мама!")], "adapted"),
    ("anya", "Вы с ним теперь хорошие друзья?",
     "Are you now good friends with him?",
     [], "new"),
    ("max", "С тех пор мы с Жераром дружим.",
     "Since then Gerard and I are friends.",
     [(141, "С тех пор мы с Жераром дружим.")], "adapted"),
    ("anya", "Расскажи нам ещё что-нибудь интересное, пожалуйста!",
     "Tell us something else interesting, please!",
     [(145, "расскажите еще что-нибудь там?")], "adapted"),
    ("max", "С большим удовольствием, милые дамы.",
     "With great pleasure, lovely ladies.",
     [(143, "дамы"), (146, "Удовольствие.")], "adapted"),
    ("max", "Однажды, когда я работал в Париже...",
     "Once, when I worked in Paris...",
     [(146, "Как-то раз в Париже.")], "adapted"),
    ("anya", "Какой чудесный и невероятно красивый город!",
     "What a wonderful and incredibly beautiful city!",
     [], "new"),
    ("max", "Ой, прошу прощения, мне пора бежать.",
     "Oh, I beg your pardon, it is time for me to run.",
     [(147, "Прошу прощения")], "adapted"),
]

OPENER = "Now let us examine Max's fabricated stories line by line."

WALK = [
    (0, None,
     "'Gerard Depardieu finishes my dish and says.' -- Max sets the scene for his fake celebrity encounter."),
    (1, None,
     "'Did he really like everything so much?' -- Sasha eagerly asks about the famous actor's reaction."),
    (2, None,
     "'He said that it is simply incredibly tasty!' -- Max boasts about the overwhelming praise he received."),
    (3, None,
     "'What, did he say it to you exactly like that?' -- The waitress wonders if the star used those exact words."),
    (4, None,
     "'Yes, exactly like that, only in the French language.' -- Max adds an international detail to make it sound authentic."),
    (5, None,
     "'What a talented cook you are, Max!' -- Sasha expresses her deep admiration for his culinary skills."),
    (6, None,
     "'Even a mother does not cook such tasty food!' -- The cook quotes the ultimate compliment from Depardieu."),
    (7, None,
     "'Are you now good friends with him?' -- The girl asks if they stayed in touch after the meal."),
    (8, None,
     "'Since then Gerard and I are friends.' -- Max claims he is on a first-name basis with the celebrity."),
    (9, None,
     "'Tell us something else interesting, please!' -- Sasha begs to hear more glamorous tales from France."),
    (10, None,
     "'With great pleasure, lovely ladies.' -- Max happily agrees to continue his performance for the women."),
    (11, None,
     "'Once, when I worked in Paris...' -- He starts spinning another elaborate lie about his past."),
    (12, None,
     "'What a wonderful and incredibly beautiful city!' -- Sasha sighs dreamily at the mention of the French capital."),
    (13, None,
     "'Oh, I beg your pardon, it is time for me to run.' -- Max suddenly remembers his actual duties and abruptly leaves."),
]

TRANSITION = "Now let us listen to Max and Sasha again."
OUTRO = (
    "Max enjoys the attention of the dining room staff, spinning wild tales about his fake career "
    "until he is suddenly reminded of his real responsibilities in the kitchen."
)
CLOSING = ("max", "Ой, прошу прощения, мне пора бежать.")
