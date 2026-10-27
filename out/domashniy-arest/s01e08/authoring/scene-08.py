ID = "domashniy-arest-s01e08-scene-08"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 8
SCENE = 8
TITLE = "Путь к сердцу Марины  (The Way to Marina's Heart)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "guard": "anja", "lyosha": "angelina"}
LABELS = {"anya": "Аркадий", "guard": "Охранник", "lyosha": "Лёша"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.08"
SOURCE_FILE = "sources/domashniy-arest/s01/e08.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 101-134. Arkady complains to his bodyguard about Marina's rejection. "
    "When young Lyosha asks to fix his toy tank, the guard gives Arkady practical advice: "
    "win over the child to win the mother. Rude words ('Сдрись', 'баба', 'Они тупые') softened for A1."
)

INTRO = (
    "Welcome back to Domashniy Arest! While mayoral candidate Ivan Samsonov is missing, "
    "disgraced mayor Arkady Anikeyev is completely distracted by his romantic obsession with Marina. "
    "When Marina's young son Lyosha stops by asking for help fixing a broken toy tank, "
    "Arkady's guard gives him unexpected advice: to win the mother's heart, you must win over the child. "
    "Let's listen to the scene in Russian first."
)

STORY = [
    ("guard", "Аркадий, что делать будем? Самсонов пропал.",
     "Arkady, what are we going to do? Samsonov is missing.",
     [(101, "что делать-то будем")], ""),
    ("anya", "Она меня ненавидит! Не хочет разговаривать.",
     "She hates me! She doesn't want to talk.",
     [(102, "Она меня ненавидит"), (104, "Не хочет со мной разговаривать")], ""),
    ("guard", "Кто? Марина? У нас кампания валится!",
     "Who? Marina? Our campaign is falling apart!",
     [(103, "Кто"), (104, "Марина"), (106, "У нас все валится")], ""),
    ("anya", "Посоветуй мне что-нибудь полезное.",
     "Give me some useful advice.",
     [(112, "посоветовала бы мне что-нибудь")], ""),
    ("lyosha", "Здравствуйте! Вы можете починить мой танк?",
     "Hello! Can you fix my tank?",
     [(114, "Здрасте")], "cue 116 garbled 'танец' corrected to 'танк'"),
    ("guard", "Не могу. Уходи отсюда и закрой дверь!",
     "I can't. Get out of here and close the door!",
     [(117, "Не могу"), (117, "и дверь закрой")], "crude insult 'Сдрись' replaced with clean 'Уходи'"),
    ("anya", "Зачем ты его прогнал? Это ошибка.",
     "Why did you chase him away? That is a mistake.",
     [], ""),
    ("guard", "Это ведь её сын.",
     "After all, that is her son.",
     [(121, "Это ведь не просто ребенок"), (122, "Это ее сын")], ""),
    ("guard", "Хочешь понравиться женщине? Подружись с её ребёнком.",
     "Want a woman to like you? Make friends with her child.",
     [(125, "Если ты хочешь, чтобы баба тебя полюбила"), (126, "подружись с ее ребенком")], "'баба' -> polite 'женщина'"),
    ("anya", "Я не люблю детей. С ними скучно.",
     "I do not like children. It is boring with them.",
     [(127, "Я ненавижу детей"), (128, "с ними скучно")], "'ненавижу' -> 'не люблю'"),
    ("guard", "Но мальчик идёт с ней в комплекте.",
     "But the boy comes with her in the package.",
     [(129, "что этот идет с ней в комплекте")], ""),
    ("anya", "Ладно. Потом отправлю его учиться в Англию.",
     "Fine. Later I will send him to study in England.",
     [(131, "Отправлю в Англию учиться")], ""),
    ("guard", "Англия — это слишком дорого.",
     "England is too expensive.",
     [(132, "в Англию жирно")], "colloquial 'жирно' glossed as expensive"),
    ("anya", "Тогда поедет учиться в Болгарию.",
     "Then he will go study in Bulgaria.",
     [(133, "В Болгарию поедем")], ""),
    ("guard", "Сначала почини его игрушечный танк.",
     "First fix his toy tank.",
     [], ""),
    ("anya", "Хорошая идея! Я сейчас же попробую.",
     "Good idea! I will try right now.",
     [], ""),
]

OPENER = (
    "Now let's examine Arkady's conversation with his guard line by line. "
    "They discuss relationship strategies and how to win Marina's affection."
)

WALK = [
    (0, None,
     "'Arkady, what are we going to do? Samsonov is missing.' The guard asks Arkady how to handle the political crisis."),
    (1, None,
     "'She hates me! She doesn't want to talk.' Arkady complains bitterly about Marina ignoring his romantic advances."),
    (2, None,
     "'Who? Marina? Our campaign is falling apart!' The guard is shocked that Arkady cares more about romance than the election."),
    (3, None,
     "'Give me some useful advice.' Arkady demands practical advice and asks what he ought to do."),
    (4, None,
     "'Hello! Can you fix my tank?' Young Lyosha peeks into the room holding his broken toy tank."),
    (5, None,
     "'I can't. Get out of here and close the door!' The gruff guard snaps at the child and tells him to leave."),
    (6, None,
     "'Why did you chase him away? That is a mistake.' Arkady realizes that offending the child could harm his chances with Marina."),
    (7, None,
     "'After all, that is her son.' The particle emphasizes that the boy is the key to Marina's affection."),
    (8, None,
     "'Want a woman to like you? Make friends with her child.' The guard shares a piece of folk wisdom about winning a mother's heart."),
    (9, None,
     "'I do not like children. It is boring with them.' Arkady cynically admits his distaste for kids."),
    (10, None,
     "'But the boy comes with her in the package.' The idiomatic phrase describes the child as part of a package deal."),
    (11, None,
     "'Fine. Later I will send him to study in England.' Arkady daydreams about shipping the boy abroad to boarding school."),
    (12, None,
     "'England is too expensive.' The guard notes that high-end foreign schooling costs far too much money."),
    (13, None,
     "'Then he will go study in Bulgaria.' Arkady quickly downgrades his lavish plan to a cheaper alternative."),
    (14, None,
     "'First fix his toy tank.' The guard advises starting with a small immediate gesture rather than grand foreign plans."),
    (15, None,
     "'Good idea! I will try right now.' Arkady eagerly decides to try his hand at toy repair."),
]

TRANSITION = "Now let's listen to the conversation in the communal apartment once more in Russian."

OUTRO = (
    "Arkady now has a new mission: repairing young Lyosha's plastic toy tank. "
    "Next, we see a feverish dream in which Ivan Samsonov crawls across a muddy battlefield; join us there."
)

CLOSING = ("anya", "Хорошая идея! Я сейчас же попробую.")
