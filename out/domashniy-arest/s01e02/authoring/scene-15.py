ID = "domashniy-arest-s01e02-scene-15"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 2
SCENE = 15
TITLE = "Меняю айфон  (Swapping the iPhone)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "slavik": "anja", "lyosha": "angelina"}
LABELS = {"anya": "Аркадий", "slavik": "Славик", "lyosha": "Лёша"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.02"
SOURCE_FILE = "sources/domashniy-arest/s01/e02.ru.dual.srt"

INTRO = ("Back in the communal flat now. Last time, at security headquarters, the local chief mocked the two agents "
         "from Moscow and put a call through to their general. Meanwhile Arkady badly needs to make a phone call of "
         "his own, but his own iPhone is blocked, so he goes to the Samsonovs' room, where Slavik and Lyosha are "
         "playing a game on Slavik's old phone. We'll hear it in Russian first; don't worry about catching every word.")

STORY = [
 ("lyosha", "Дай поиграть!", "Let me have a go!", [(428, "Дай поиграть")], ""),
 ("slavik", "Уровень пройду и дам.", "I'll finish the level and then I'll give it to you.",
  [(429, "Уровень пройду и дам")], ""),
 ("anya", "Соседи, привет! Слушай, дружок, дай свой телефон на минутку.",
  "Hi, neighbours! Listen, buddy, lend me your phone for a minute.",
  [(431, "Соседи, привет"), (432, "Слушай, дружок, дай свой телефон на минутку")], ""),
 ("slavik", "Зачем?", "What for?", [(433, "Зачем")], ""),
 ("anya", "Позвонить нужно.", "I need to make a call.", [(434, "Позвонить нужно")], ""),
 ("slavik", "У вас свой есть.", "You've got your own.", [(435, "У вас свой есть")], ""),
 ("anya", "Его в суде заблокировали.", "The court had it blocked.",
  [(436, "Его в суде заблокировали")], "the garbled first half of the cue left out"),
 ("slavik", "Не дам.", "I won't give it to you.", [(439, "Не дам")], ""),
 ("anya", "Ах ты, жадина! А у тебя есть телефон?", "Oh, you greedy thing! And have you got a phone?",
  [(443, "у тебя есть телефон")],
  "'жлоб какой' (cue 440) -> the milder 'жадина'; the question goes to Lyosha (cue 443: 'Слышь, мелкий' dropped); "
  "Yulia's 'no credit' reply (442) is told by the narrator"),
 ("lyosha", "Нет. Вы взяточник.", "No. You take bribes.",
  [(448, "Нет"), (445, "Вы взяточник")], "the two replies swapped round and joined"),
 ("anya", "Тогда не разговаривай.", "Then don't talk.", [(449, "Тогда не разговаривай")], ""),
 ("anya", "Славик, смотри сюда. Меняю свой новый айфон на твой старый телефон.",
  "Slavik, look here. I'll swap my new iPhone for your old phone.",
  [(451, "смотри сюда"), (452, "Меняю свой новый айфон на")],
  "'Жлоб' -> 'Славик'; 'твоё фуфло' (your junk) -> 'твой старый телефон'"),
 ("slavik", "Ага, как с Кайеном, да?", "Yeah, right, like with the Cayenne?",
  [], "cue 453 'Угу, как с Каеном, да?': 'Угу' -> 'Ага', the car spelled Кайен as in s01e01, so not cited"),
 ("anya", "На этот раз по-честному. В крокодиловом чехле!", "This time it's a fair deal. In a crocodile-skin case!",
  [(454, "На этот раз по-честному"), (455, "крокодиловом чехле")], "the cue's 'На' corrected to 'В'"),
 ("anya", "Ну, как знаешь. Продам его Клавдии Викторовне.",
  "Well, suit yourself. I'll sell it to Klavdia Viktorovna.",
  [(458, "как знаешь")], "slangy 'загоню' (459) -> 'Продам'; the cue's case slip 'Клавдию' -> 'Клавдии'"),
 ("slavik", "Постойте!", "Wait!", [(460, "Постойте")], ""),
]

OPENER = ("Let's take it slowly. The two boys are sharing one phone, and the younger one wants a turn.")

WALK = [
 (0, None,
  "'Let me have a go!' Literally, 'give to play'. The command 'give' plus another verb is a handy way to say "
  "'let me'. Slavik is in the middle of a game."),
 (1, None,
  "'I'll finish the level and then I'll give it to you.' Both verbs are perfective, so in this form they point to "
  "the future: first one thing, then the next. Then Arkady comes in."),
 (2, "Соседи, привет!",
  "'Hi, neighbours!' He's all smiles. Then he gets to the point."),
 (2, "Слушай, дружок, дай свой телефон на минутку.",
  "'Listen, buddy, lend me your phone for a minute.' The word for buddy is a friendly little form of 'friend', the "
  "way adults talk to kids, and 'a minute' is also a little form. He's being extra sweet. Slavik isn't fooled."),
 (3, None,
  "'What for?' A short, suspicious question."),
 (4, None,
  "'I need to make a call.' Literally, 'to call is needed'. There's no 'I' at all: Russian often says 'it's "
  "needed' instead of 'I need'. Slavik points out the obvious."),
 (5, None,
  "'You've got your own.' Notice the polite 'you': the boy speaks politely to a grown-up neighbour, while Arkady "
  "speaks to the kids in the friendly form. Arkady explains."),
 (6, None,
  "'The court had it blocked.' Word for word, 'it in the court they blocked'. The verb has no subject, which means "
  "'somebody did it'. Remember, Arkady is under house arrest. But Slavik still says no."),
 (7, None,
  "'I won't give it to you.' Just 'not' and 'I'll give'. Short and final. Arkady tries Slavik's sister Yulia, but she has "
  "no money on her phone, so he turns to Lyosha."),
 (8, "Ах ты, жадина!",
  "'Oh, you greedy thing!' A mild telling-off, the kind you'd say to a child who won't share. Then the question for "
  "Lyosha."),
 (8, "А у тебя есть телефон?",
  "'And have you got a phone?' Literally, 'at you is there a phone?'. This is how Russian says 'to have': "
  "'at me', 'at you', plus the word for 'there is'. Lyosha, Marina's son, has an answer ready."),
 (9, None,
  "'No. You take bribes.' Literally, 'you are a bribe-taker'. One word in Russian for the person who takes bribes. "
  "Everybody in town has seen the news about the mayor. Arkady is not amused."),
 (10, None,
  "'Then don't talk.' A negative command in the friendly form. Arkady goes back to Slavik with a new idea."),
 (11, "Славик, смотри сюда.",
  "'Slavik, look here.' The word at the end means 'to here', with movement, as in 'look over this way'. And then "
  "the offer."),
 (11, "Меняю свой новый айфон на твой старый телефон.",
  "'I'll swap my new iPhone for your old phone.' The present tense can make an offer: 'I swap' means 'I'm offering "
  "to swap, right now'. And the word for 'for' in a swap is the little word that also means 'on'. Slavik has heard "
  "this kind of thing before."),
 (12, None,
  "'Yeah, right, like with the Cayenne?' In the last episode Arkady gave the family his wife's car, a Porsche "
  "Cayenne, and then took it back. Arkady swears it's different now."),
 (13, "На этот раз по-честному.",
  "'This time it's a fair deal.' Literally, 'this time, honestly'. And then he adds a sweetener."),
 (13, "В крокодиловом чехле!",
  "'In a crocodile-skin case!' After the word for 'in', both words get the ending for place. Slavik says nothing, "
  "so Arkady plays his last card."),
 (14, "Ну, как знаешь.",
  "'Well, suit yourself.' Literally, 'as you know'. It's what you say when you pretend not to care."),
 (14, "Продам его Клавдии Викторовне.",
  "'I'll sell it to Klavdia Viktorovna.' She's the old neighbour down the corridor. 'To' someone is shown only by "
  "the endings of her name, the case for giving something to somebody. That does it."),
 (15, None,
  "'Wait!' A polite command to a grown-up. The deal is done: the boy gets the shiny new phone, and Arkady gets a "
  "phone that works."),
]

TRANSITION = "And now the whole scene again, all the way through."

OUTRO = ("So Slavik ends up with the shiny new iPhone, and Arkady finally has a phone he can call from. You did well "
         "to keep up with that one; see you next time.")
CLOSING = ("slavik", "Договорились!")
