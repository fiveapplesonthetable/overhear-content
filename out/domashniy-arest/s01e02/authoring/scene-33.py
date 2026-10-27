ID = "domashniy-arest-s01e02-scene-33"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 2
SCENE = 33
TITLE = "Охрана говорит нет  (The Guards Say No)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "pasha": "anja", "vitalik": "angelina"}
LABELS = {"anya": "Аркадий", "pasha": "Паша", "vitalik": "Виталик"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.02"
SOURCE_FILE = "sources/domashniy-arest/s01/e02.ru.dual.srt"
SOURCE_NOTE = ("Arkady is the viewpoint character (`anya`). The guards speak as one role, Vitalik. Merged scene 34 "
               "(a stranger's 'business proposal'; Marina phones the agents and agrees; closing song) is told in "
               "the OUTRO. «Денег нет, но вы держитесь» is a famous quoted phrase, explained neutrally. Insults "
               "(дебильные, к чёртовой матери) are left out.")

INTRO = ("Later that night, in the same flat, Arkady has a visitor. Last time, he told little Lyosha there would be "
         "no console and took his iPhone back from Slavik. Now Pasha arrives with Arkady's old guards, led by "
         "Vitalik, to get the money out of him; we'll hear it in Russian first, so don't worry about catching "
         "every word.")

STORY = [
 ("pasha", "Ну что, Аркаша? Наступила ночь, просыпается мафия.",
  "So, Arkasha? Night has fallen, the mafia wakes up.",
  [(1195, "наступила ночь, просыпается мафия")], "Аркашенька -> Аркаша"),
 ("anya", "Что за шутки?", "What kind of jokes are these?",
  [(1196, "Что за шутки")], "'дебильные' (stupid, rude) left out"),
 ("pasha", "Нормальные шутки. Где деньги?", "Normal jokes. Where's the money?",
  [(1197, "Нормальные шутки"), (1200, "Где деньги")], "the back-and-forth of 1198-1199 left out"),
 ("anya", "Денег нет, но вы держитесь.", "There's no money, but hang in there.",
  [(1201, "Денег нет, но вы держитесь")], ""),
 ("pasha", "Это ты держись.", "You're the one who should hang in there.",
  [(1202, "Это ты держись")], ""),
 ("pasha", "Виталик, поговорите с ним.", "Vitalik, have a word with him.",
  [(1203, "Виталик")], "«пообщайтесь-ка» -> «поговорите» (plural: to all the guards)"),
 ("vitalik", "Павел Юрьевич, мы с Аркадием Борисовичем говорить не будем.",
  "Pavel Yuryevich, we're not going to have a word with Arkady Borisovich.",
  [(1204, "Павел Юрьевич"), (1204, "мы с Аркадием Борисовичем")],
  "'посовещались, решили' left out; общаться не станем -> говорить не будем"),
 ("vitalik", "Он нашей сестре квартиру дал.", "He gave our sister a flat.",
  [(1206, "Он нашей сестре квартиру дал")], ""),
 ("vitalik", "И бабушку на лечение в Израиль отправил.", "And he sent our grandmother to Israel for treatment.",
  [(1207, "И бабушку на лечение в Израиль отправил")], ""),
 ("pasha", "Но она всё равно умерла.", "But she died anyway.",
  [(1208, "Но она все равно умерла")], "speaker of cue 1208 not marked; given to Pasha (a sneer)"),
 ("vitalik", "Но он же отправил.", "But he did send her.",
  [(1209, "Но он же отправил")], ""),
 ("anya", "Добро возвращается к отправителю.", "Good deeds come back to the sender.",
  [(1211, "Добро возвращается к отправителю")], ""),
 ("anya", "А теперь сломайте Павлу Юрьевичу руку.", "And now break Pavel Yuryevich's arm.",
  [(1213, "А теперь сломайте"), (1213, "Павлу Юрьевичу руку")], "'-ка' dropped"),
 ("vitalik", "Тоже не можем. Мы на вас больше не работаем.", "We can't do that either. We don't work for you any more.",
  [(1215, "Тоже не можем. Мы на вас больше не работаем")], ""),
 ("vitalik", "Мы работаем на него.", "We work for him.",
  [(1216, "Мы работаем на него")], ""),
 ("pasha", "Тогда я вас уволю.", "Then I'll fire you.",
  [(1218, "уволю")], "«Иначе уволю к чёртовой матери» -> «Тогда я вас уволю»"),
 ("vitalik", "Хотите, увольняйте. Лучше всё равно не найдёте.", "Fire us if you like. You won't find better anyway.",
  [(1219, "Хотите, увольняйте"), (1220, "Лучше все равно не найдете")], ""),
 ("pasha", "Цирк какой-то.", "What a circus.",
  [(1221, "какой-то")], "«Шапито какой-то» -> «Цирк какой-то» (plain word; speaker not marked, given to Pasha)"),
]

OPENER = "Let's walk through it slowly. Pasha starts with a joke that every Russian knows."

WALK = [
 (0, "Ну что, Аркаша?",
  "'So, Arkasha?' Arkasha is the childhood form of Arkady, and from Pasha it sounds mocking. Then comes the joke."),
 (0, "Наступила ночь, просыпается мафия.",
  "'Night has fallen, the mafia wakes up.' These are the words of the host in a popular party game called Mafia, "
  "where the 'mafia' players secretly wake up at night. Arkady is not amused."),
 (1, None,
  "'What kind of jokes are these?' The two little words at the start together mean 'what kind of', and they "
  "often sound annoyed. Pasha brushes it off and gets to the point."),
 (2, None,
  "'Normal jokes. Where's the money?' The word for money only exists in the plural, so it behaves like 'they'. "
  "Arkady answers with a famous phrase."),
 (3, None,
  "'There's no money, but hang in there.' This is a well-known phrase from Russian public life that people quote "
  "all the time as a joke. After 'there's no', money takes the ending for 'of'. Pasha turns it back on him."),
 (4, None,
  "'You're the one who should hang in there.' Arkady used the polite plural form of the command; Pasha uses the "
  "short, familiar one. Then he calls in the muscle."),
 (5, None,
  "'Vitalik, have a word with him.' The command ends the plural way, because Pasha means all the guards, not just "
  "Vitalik. And 'a word' here is not a friendly chat. But Vitalik has news."),
 (6, None,
  "'Pavel Yuryevich, we're not going to have a word with Arkady Borisovich.' First name plus father's name is the "
  "respectful way to address someone. 'We won't' is literally 'we will not be', followed by the verb. Pasha can't "
  "believe it, so Vitalik explains."),
 (7, None,
  "'He gave our sister a flat.' The person who receives something takes the ending meaning 'to': 'to our sister'. "
  "And that's not all."),
 (8, None,
  "'And he sent our grandmother to Israel for treatment.' The verb comes last here, which is very common in "
  "speech. Pasha finds a nasty answer."),
 (9, None,
  "'But she died anyway.' The middle two words mean 'all the same', 'anyway'. Vitalik doesn't back down."),
 (10, None,
  "'But he did send her.' The little word after 'he' adds emphasis, like 'he did'. Arkady is delighted."),
 (11, None,
  "'Good deeds come back to the sender.' Like 'what goes around comes around', with the good, and the last word is "
  "the one used for the sender of a letter. Feeling bold, Arkady gives an order of his own."),
 (12, None,
  "'And now break Pavel Yuryevich's arm.' Again Pasha gets the ending for 'to': literally, 'break to Pavel "
  "Yuryevich the arm'. Russian often shows whose body part it is this way. The guards refuse him too."),
 (13, "Тоже не можем.",
  "'We can't do that either.' Just 'also we can't'. Then the real reason."),
 (13, "Мы на вас больше не работаем.",
  "'We don't work for you any more.' To work for someone is literally to work 'on' them. They nod at Pasha."),
 (14, None,
  "'We work for him.' Pasha is the acting mayor now. So he threatens them."),
 (15, None,
  "'Then I'll fire you.' This verb is in the future tense, a single finished action. The guards are not worried."),
 (16, "Хотите, увольняйте.",
  "'Fire us if you like.' Literally, 'you want, fire'. The command is in the polite plural form. And they add one "
  "more thing."),
 (16, "Лучше всё равно не найдёте.",
  "'You won't find better anyway.' The same two words for 'anyway' we heard a moment ago. Pasha gives up."),
 (17, None,
  "'What a circus.' Literally, 'some kind of circus'. A good word for this whole evening."),
]

TRANSITION = "Now listen to the whole scene once more."

OUTRO = ("Afterwards a stranger comes up to Arkady, asks if he's the mayor who broke his finger, and says he has a "
         "business proposal; and Marina phones the agents to say she has changed her mind and agrees. That's the end "
         "of the second episode, with the song about how much money it takes to be happy; well done, and see you in "
         "the next one.")
CLOSING = ("anya", "Спокойной ночи!")
