ID = "kukhnya-s01e14-scene-06"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 6
TITLE = "Нервы су-шефа  (The Sous-Chef's Nerves)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja"}
LABELS = {"anya": "Сеня", "leva": "Лёва"}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 65-76. In the kitchen, a nervous Leva panics at the thought of temporarily "
    "replacing the drunk Chef Barinov. His friend Senya gives him an encouraging pep talk."
)

INTRO = (
    "In the kitchen, a nervous Leva panics at the thought of temporarily replacing "
    "the drunk Chef Barinov. Seeing his friend struggle, Senya gives him an encouraging pep talk, "
    "trying to teach the mild-mannered sous-chef how to shout like a true boss. "
    "Let us listen to their conversation in Russian first."
)

STORY = [
    ("leva", "Я не смогу управлять всей кухней!",
     "I cannot manage the whole kitchen!",
     [(65, "Я не смогу.")], "adapted"),
    ("anya", "У тебя обязательно всё отлично получится!",
     "You will definitely do absolutely great!",
     [(68, "У тебя все получится.")], "adapted"),
    ("leva", "Я никогда раньше не заменял шефа.",
     "I have never replaced the chef before.",
     [], "new"),
    ("anya", "Ведь ты наш су-шеф, то есть супер-шеф!",
     "Because you are our sous-chef, that is super-chef!",
     [(69, "Ведь ты же су-шеф, а это значит супер-шеф.")], "adapted"),
    ("leva", "Но шеф всегда так сильно кричит.",
     "But the chef always shouts so loudly.",
     [], "new"),
    ("anya", "А ты просто кричи на всех громче.",
     "And you simply shout at everyone louder.",
     [], "new"),
    ("leva", "Я совсем не умею страшно кричать.",
     "I completely do not know how to shout terribly.",
     [], "new"),
    ("anya", "Давай, попробуй громко накричать на меня.",
     "Come on, try to shout loudly at me.",
     [], "new"),
    ("leva", "Сеня, немедленно иди резать эти овощи!",
     "Senya, go cut these vegetables immediately!",
     [], "new"),
    ("anya", "Очень слабо, Лёва, нужно больше злости!",
     "Very weak, Leva, we need more anger!",
     [], "new"),
    ("leva", "Хорошо, сейчас я соберусь с силами.",
     "All right, now I will gather my strength.",
     [], "new"),
    ("anya", "Ты наш самый лучший главный повар сегодня!",
     "You are our absolute best head chef today!",
     [], "new"),
    ("leva", "Да, я смогу, я точно смогу!",
     "Yes, I can do it, I definitely can!",
     [(70, "Да, я смогу."), (71, "Я точно смогу.")], "adapted"),
    ("anya", "Вот теперь я вижу настоящего шефа!",
     "Now I see a real chef!",
     [], "new"),
]

OPENER = "Now let us examine Senya's pep talk line by line."

WALK = [
    (0, None,
     "'I cannot manage the whole kitchen!' -- Leva panics at the huge responsibility of leading the team."),
    (1, None,
     "'You will definitely do absolutely great!' -- Senya encourages him to believe in his own abilities."),
    (2, None,
     "'I have never replaced the chef before.' -- Leva admits his lack of experience in the top role."),
    (3, None,
     "'Because you are our sous-chef, that is super-chef!' -- Senya cleverly motivates him with a pun."),
    (4, None,
     "'But the chef always shouts so loudly.' -- Leva points out Barinov's aggressive management style."),
    (5, None,
     "'And you simply shout at everyone louder.' -- Senya advises him to adopt the same fierce behavior."),
    (6, None,
     "'I completely do not know how to shout terribly.' -- The gentle sous-chef confesses he cannot act mean."),
    (7, None,
     "'Come on, try to shout loudly at me.' -- Senya offers himself as a practice target."),
    (8, None,
     "'Senya, go cut these vegetables immediately!' -- Leva makes a timid attempt at giving a strict order."),
    (9, None,
     "'Very weak, Leva, we need more anger!' -- Senya rejects the polite command and demands more aggression."),
    (10, None,
     "'All right, now I will gather my strength.' -- Leva promises to focus and act tougher."),
    (11, None,
     "'You are our absolute best head chef today!' -- Senya continues to boost his friend's confidence."),
    (12, None,
     "'Yes, I can do it, I definitely can!' -- Leva finally believes in himself and accepts the challenge."),
    (13, None,
     "'Now I see a real chef!' -- Senya proudly congratulates him on his new boss attitude."),
]

TRANSITION = "Now let us listen to Leva and Senya once more."
OUTRO = (
    "With a little help from Senya, the timid Leva finally finds his inner boss, "
    "ready to take charge of Claude Monet's chaotic kitchen for the day."
)
CLOSING = ("anya", "Вот теперь я вижу настоящего шефа!")
