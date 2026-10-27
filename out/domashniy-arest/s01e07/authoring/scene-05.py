# Authoring module for domashniy-arest s01e07 scene 05.

ID = "domashniy-arest-s01e07-scene-05"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 5
TITLE = "Два дня в Плёсе  (Two Days in Plyos)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "dean": "anja",
    "marina": "angelina",
}
LABELS = {
    "anya": "Аркадий",
    "dean": "Эдуард Валентинович",
    "marina": "Марина",
}

SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.07"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 204–239 (00:10:43–00:11:58). In the courtyard Ilona congratulates Arkady that Samsonov's poll ratings have "
    "caught up with Osipenko's, and inside Marina's room Eduard explains why he ran home to his wife Alla Evgenyevna "
    "the night before. For the three-role limit, Ilona's brief greeting and question in cues 204–210 are narrated in "
    "WALK and echoed by Arkady, while Arkady, Eduard Valentinovich, and Marina hold the three voices. ASR 'со "
    "сибирскими' (205) is restored to 'с Осипенко', and 'А что ты сейчас нес Алла Евгеньевна?' (218) is restored to "
    "'А почему ты сейчас не с Аллой Евгеньевной?'. Graphic details about stomach flu and basins in 212–214 are "
    "simplified to clean A1 ('Алла Евгеньевна вчера заболела'), 'дурак' (216) -> 'глупый', 'на симпозиум' (222) -> "
    "'Там научная встреча', and 'мне плевать' (226–227) -> 'Мне всё равно'."
)

INTRO = (
    "In the courtyard and inside Marina's room. Last time, Arkady snatched Eduard Valentinovich's bouquet on the stairs "
    "and claimed he and Marina were a couple until fed-up Marina threw both bouquets down the stairwell. Now Ilona "
    "brings Arkady good news that Samsonov's poll ratings have caught up with Osipenko's, while upstairs in Marina's "
    "room Eduard begs Marina for forgiveness and explains that he told his sick wife Alla Evgenyevna he is away at a "
    "two-day academic conference in the Volga town of Plyos. We'll hear it in Russian first; don't worry about catching "
    "every word."
)

# (role, ru, en, [(cue, frag), ...], note)
STORY = [
    ("anya", "У нас рейтинги сравнялись с Осипенко? Прекрасно, пойдём!",
     "Our ratings have caught up with Osipenko's? Wonderful, let's go!",
     [(205, "у нас"), (205, "рейтинги сравнялись"), (207, "Прекрасно. Ну, пойдем")],
     "Ilona's news in 204-206 echoed by Arkady; ASR 'со сибирскими' (205) -> 'с Осипенко'"),
    ("anya", "Забудь про эти цветы. Сейчас сама всё увидишь.",
     "Forget about these flowers. You'll see everything yourself right now.",
     [(209, "Забудь про")],
     "answers Ilona's question in 208-210 about the discarded bouquets"),
    ("dean", "Марина, это было что-то ужасное! Алла Евгеньевна вчера заболела.",
     "Marina, it was something awful! Alla Evgenyevna got sick yesterday.",
     [(211, "Это было что-то ужасное"), (212, "Алла Евгеньевна"), (217, "она заболела")],
     "'подхватила кишечный грипп' (212) and basins (213) simplified to clean A1"),
    ("marina", "Не хочу слышать об Алле Евгеньевне!",
     "I don't want to hear about Alla Evgenyevna!",
     [(214, "Не хочу слышать"), (214, "об Алле Евгеньевне")],
     "'ни об её тазах' omitted"),
    ("dean", "Да, конечно. Прости меня, Марина, прости.",
     "Yes, of course. Forgive me, Marina, forgive me.",
     [(215, "Да, конечно. Прости меня"), (215, "прости")],
     "diminutive 'Мариночка' -> 'Марина'"),
    ("dean", "Я просто глупый. Она целый день лежит дома.",
     "I'm just foolish. She is lying at home all day.",
     [(216, "Я просто"), (217, "она целый день лежит дома")],
     "'дурак' (216) -> 'глупый'"),
    ("marina", "А почему ты сейчас не с Аллой Евгеньевной?",
     "Then why aren't you with Alla Evgenyevna right now?",
     [(218, "А"), (218, "ты сейчас")],
     "ASR 'что ты сейчас нес Алла Евгеньевна' (218) restored to 'почему ты сейчас не с Аллой Евгеньевной'"),
    ("dean", "Потому что я тебя люблю! Я всю ночь не спал.",
     "Because I love you! I didn't sleep all night.",
     [(219, "Потому что я"), (219, "я тебя люблю"), (220, "Я всю ночь не спал")],
     ""),
    ("dean", "Я так хотел к тебе! И утром я всё придумал.",
     "I wanted to come to you so badly! And in the morning I thought of everything.",
     [(220, "я так хотел к тебе"), (221, "И утром")],
     "'когда я проснулся' simplified"),
    ("dean", "Я сказал жене, что еду в Плёс. Там научная встреча.",
     "I told my wife that I'm going to Plyos. There is an academic conference there.",
     [(221, "я сказал"), (222, "в Плёс")],
     "'уезжаю на два дня в Плёс на симпозиум' split into two short A1 sentences"),
    ("dean", "Я уехал на два дня. Поэтому мы два дня будем вместе!",
     "I left for two days. So we will be together for two days!",
     [(222, "на два дня"), (223, "Поэтому мы два дня будем вместе")],
     ""),
    ("marina", "Ты какой смелый! А что ты будешь делать, если она узнает?",
     "How brave you are! And what will you do if she finds out?",
     [(224, "Ты какой смелый"), (225, "А что ты будешь делать, если она узнает")],
     ""),
    ("dean", "Мне всё равно! Я хочу быть только с тобой, понимаешь?",
     "I don't care! I want to be only with you, do you understand?",
     [(228, "Я хочу быть с тобой"), (229, "С тобой, понимаешь")],
     "colloquial 'мне плевать' (226-227) -> 'Мне всё равно'"),
    ("marina", "И с Аллой Евгеньевной.",
     "And with Alla Evgenyevna.",
     [(230, "И с Аллой Евгеньевной")],
     ""),
    ("dean", "Нет, я всё решил! Мы с ней точно расстанемся.",
     "No, I have decided everything! She and I will definitely break up.",
     [(231, "Нет"), (234, "Точно расстанемся"), (239, "Я всё решил")],
     ""),
    ("dean", "И всё изменится! Марина, ну послушай меня!",
     "And everything will change! Marina, just listen to me!",
     [(235, "И всё изменится"), (236, "Марина, ну послушай меня")],
     ""),
]

OPENER = "Let's unpack this scene line by line. Down in the courtyard, Ilona tells Arkady that Samsonov's poll numbers have caught up with Osipenko's:"

WALK = [
    (0, "У нас рейтинги сравнялись с Осипенко? Прекрасно, пойдём!",
     "'Our ratings have caught up with Osipenko's? Wonderful, let's go!' Arkady is delighted by the campaign news."),
    (1, "Забудь про эти цветы.",
     "'Forget about these flowers.' Ilona notices the crushed flowers on the stairs, and Arkady waves them off."),
    (1, "Сейчас сама всё увидишь.",
     "'You'll see everything yourself right now.' Arkady leads Ilona up to Marina's door."),
    (2, "Марина, это было что-то ужасное!",
     "'Marina, it was something awful!' Eduard explains his sudden disappearance the evening before."),
    (2, "Алла Евгеньевна вчера заболела.",
     "'Alla Evgenyevna got sick yesterday.' Notice that the adjective stands in the neuter singular after 'something'."),
    (3, None,
     "'I don't want to hear about Alla Evgenyevna!' Before a vowel sound, the preposition adds an extra consonant."),
    (4, None,
     "'Yes, of course. Forgive me, Marina, forgive me.' Eduard apologizes humbly for bringing up his wife."),
    (5, "Я просто глупый.",
     "'I'm just foolish.' He admits that he handled the situation terribly."),
    (5, "Она целый день лежит дома.",
     "'She is lying at home all day.' His wife is too sick to leave the house."),
    (6, None,
     "'Then why aren't you with Alla Evgenyevna right now?' Marina points out his glaring hypocrisy."),
    (7, "Потому что я тебя люблю!",
     "'Because I love you!' Eduard protests passionately in her room."),
    (7, "Я всю ночь не спал.",
     "'I didn't sleep all night.' He claims he tossed and turned thinking only of her."),
    (8, "Я так хотел к тебе!",
     "'I wanted to come to you so badly!' Russian often leaves out the verb of motion when the direction is clear."),
    (8, "И утром я всё придумал.",
     "'And in the morning I thought of everything.' Eduard explains his elaborate cover story."),
    (9, "Я сказал жене, что еду в Плёс.",
     "'I told my wife that I'm going to Plyos.' Plyos is a scenic town on the Volga where academic conferences are held."),
    (9, "Там научная встреча.",
     "'There is an academic conference there.' He invented a symposium to explain his absence."),
    (10, "Я уехал на два дня.",
     "'I left for two days.' He told his wife he would be away for the entire weekend."),
    (10, "Поэтому мы два дня будем вместе!",
     "'So we will be together for two days!' Eduard beams with pride at his clever plan."),
    (11, "Ты какой смелый!",
     "'How brave you are!' Marina remarks with biting sarcasm."),
    (11, "А что ты будешь делать, если она узнает?",
     "'And what will you do if she finds out?' Marina asks what will happen when his wife discovers the truth."),
    (12, "Мне всё равно!",
     "'I don't care!' Literally, to me it is all the same."),
    (12, "Я хочу быть только с тобой, понимаешь?",
     "'I want to be only with you, do you understand?' Eduard insists that he has made up his mind."),
    (13, None,
     "'And with Alla Evgenyevna.' Marina adds dryly, reminding him that he is still married."),
    (14, "Нет, я всё решил!",
     "'No, I have decided everything!' Eduard insists that this time is different."),
    (14, "Мы с ней точно расстанемся.",
     "'She and I will definitely break up.' Notice the Russian phrasing 'we with her' for 'she and I'."),
    (15, "И всё изменится!",
     "'And everything will change!' He promises that their life together will be wonderful."),
    (15, "Марина, ну послушай меня!",
     "'Marina, just listen to me!' Eduard pleads over the roaring sound of Marina's noisy hairdryer."),
]

TRANSITION = "Now let's hear the whole conversation again from beginning to end."

OUTRO = (
    "While Marina drowns out Eduard's promises with her hairdryer inside the room, Arkady and Ilona are listening right "
    "outside her door in the corridor, and Arkady is desperate for a plan to break them up. Here's one last line:"
)

CLOSING = ("marina", "Ты какой смелый!")
