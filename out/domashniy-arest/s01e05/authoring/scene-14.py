ID = "domashniy-arest-s01e05-scene-14"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 5
SCENE = 14
TITLE = "Трус не играет в хоккей  (A Coward Doesn't Play Hockey)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "pasha": "anja", "governor": "angelina"}
LABELS = {"anya": "Аркадий", "pasha": "Паша", "governor": "Виктор Степанович"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.05"
SOURCE_FILE = "sources/domashniy-arest/s01/e05.ru.dual.srt"

INTRO = (
    "After Danila Golovkin invents a second cover story at his dacha, Ilona sneaks into the City Hall archive. "
    "There archivist Lydia Alexeyevna tries to chase her out, until Ilona whispers that she is secretly working "
    "for Arkady Borisovich, and Lydia gives her five minutes to search. Meanwhile, at the local ice rink, Pasha "
    "tries to reassure Governor Viktor Stepanovich while the governor poses in hockey gear, and Arkady phones Ilona "
    "in the archive. Listen to the Russian first; you don't need to catch every word."
)

STORY = [
    ("pasha", "Виктор Степанович, я вообще не понимаю.",
     "Viktor Stepanovich, I really don't understand.",
     [(501, "Виктор Степанович, я вообще не понимаю")], "split cue 501 into two short lines"),
    ("pasha", "Что вы так переживаете? Самсонов всё, он себя закопал.",
     "Why are you worrying like that? Samsonov is finished, he buried himself.",
     [(501, "что вы так переживаете"), (502, "Самсонов все, он себя закопал")], ""),
    ("governor", "А если Аникеев что-нибудь придумает?",
     "And what if Anikeev comes up with something?",
     [(503, "А если Аникеев что-нибудь придумает?")], "dropped insult 'придурок' in 504"),
    ("pasha", "Да что он придумает?",
     "What could he come up with?",
     [(505, "Да что он придумает?")], ""),
    ("governor", "Вот со слепыми договорится и всё.",
     "He'll just make a deal with the blind people, and that's it.",
     [(506, "вот со слепыми"), (506, "и все")], "cue 506 'договориться' -> 'договорится'"),
    ("pasha", "Не договорится, слепые его ненавидят. Они же думают, что виноват он.",
     "He won't make a deal, the blind people hate him. They think that he is to blame.",
     [(507, "слепые его ненавидят"), (508, "Они же думают, что")], "simplified slang 'мариновал-то' in 508"),
    ("governor", "А на самом деле?",
     "And in reality?",
     [(509, "А на самом деле?")], ""),
    ("pasha", "А на самом деле это сделал я. Мне там нужно было перехватить постройки.",
     "And in reality I did it. I needed to grab the construction contracts there.",
     [(510, "А на самом деле мне там нужно было"), (510, "перехватить постройки")], "split into two short sentences"),
    ("governor", "Приказ Аникеева о выделении средств остался?",
     "Is Anikeev's order on allocating the funds still there?",
     [(511, "Приказ"), (511, "о выделении средств остался?")], "cue 511 'Анифеева' -> 'Аникеева'"),
    ("pasha", "Ну, наверное, в архиве где-то.",
     "Well, probably somewhere in the archive.",
     [(512, "Ну, наверное"), (513, "в архиве где-то")], ""),
    ("governor", "Смотри, они его увидят!",
     "Watch out, they'll see it!",
     [(514, "они его увидят")], "garbled 'уторяйся' -> 'Смотри'"),
    ("pasha", "Как же они его увидят, если они слепые?",
     "How will they see it if they are blind?",
     [(515, "Как же они его увидят, если они слепые?")], ""),
    ("governor", "Ты всё шуточки, что ли, шутишь? Поезжай в мэрию и в шредер всё это!",
     "Are you still cracking jokes? Drive to City Hall and put all of it in the shredder!",
     [(516, "Ты все шуточки, что ли, шутишь?"), (517, "в мэрию и в Шреддер все это")], "cleaned up 'Вези свою жопу' in 517"),
    ("pasha", "Я понял. Всё, уже еду!",
     "I understand. Right, I'm on my way!",
     [(518, "Я понял. Все")], "cleaned up 'везу жопу' in 518 and 'Дебил' in 519"),
    ("governor", "Хорошая фотография! Напиши: трус не играет в хоккей.",
     "Good photo! Write: a coward doesn't play hockey.",
     [(525, "Хорошая фотография"), (527, "Трус не играет в хоккей")], ""),
    ("anya", "Алло, Илона! Почему не звонишь? Ты нашла?",
     "Hello, Ilona! Why aren't you calling? Did you find it?",
     [(538, "Алло, Илона"), (539, "Почему не звонишь?"), (539, "Ты нашла?")], ""),
    ("anya", "Как не нашла? Послушай, в чёрном шкафу посмотри. Там справа от двери!",
     "What do you mean you didn't find it? Listen, look in the black cabinet. There to the right of the door!",
     [(540, "Как не нашла?"), (541, "Послушай"), (542, "В черном шкафу посмотри. Там справа от двери")], ""),
]

OPENER = "Now let's walk through what happens at the ice rink and in the archive."

WALK = [
    (0, None,
     "Standing by the boards of the ice rink, Pasha tells the governor that he really does not understand."),
    (1, "Что вы так переживаете?",
     "'Why are you worrying like that?' Notice the polite plural 'you' as Pasha addresses his boss."),
    (1, "Самсонов всё, он себя закопал.",
     "'Samsonov is finished, he buried himself' by crashing a luxury car into the Society of the Blind."),
    (2, None,
     "'And what if Anikeev comes up with something?' The perfective verb with the prefix 'pri-' means to think up or invent a plan."),
    (3, None,
     "'What could he come up with?' Pasha brushes the worry aside."),
    (4, None,
     "'He'll just make a deal with the blind people, and that's it.' Notice the instrumental plural ending '-ymi' after the preposition 'with'."),
    (5, "Не договорится, слепые его ненавидят.",
     "'He won't make a deal, the blind people hate him.' Here 'will make a deal' sets up the idea, while 'hate' comes at the end for emphasis."),
    (5, "Они же думают, что виноват он.",
     "'They think that he is to blame' for delaying their new building."),
    (6, None,
     "'And in reality?' Literally 'and on the actual matter?', the standard Russian phrase for 'in fact' or 'actually'."),
    (7, "А на самом деле это сделал я.",
     "'And in reality I did it.' Pasha admits the truth."),
    (7, "Мне там нужно было перехватить постройки.",
     "'I needed to grab the construction contracts there.' That prompts a sharp question from the governor."),
    (8, None,
     "'Is Anikeev's order on allocating the funds still there?' If that signed order exists, it proves Anikeev gave the money and Pasha diverted it."),
    (9, None,
     "'Well, probably somewhere in the archive.' The governor immediately sees the danger."),
    (10, None,
     "'Watch out, they'll see it!' Here 'watch out' sets up the idea, while 'will see' comes at the end for emphasis."),
    (11, None,
     "Pasha makes a clumsy joke: 'How will they see it if they are blind?' The governor explodes."),
    (12, "Ты всё шуточки, что ли, шутишь?",
     "'Are you still cracking jokes?' The key word here means 'you', which the speaker combines with 'still'."),
    (12, "Поезжай в мэрию и в шредер всё это!",
     "'Drive to City Hall and put all of it in the shredder!' Notice how Russian drops the second verb and says simply 'and into the shredder all this!'."),
    (13, None,
     "'I understand. Right, I'm on my way!' As Pasha hurries off, the governor poses on the ice for a campaign photograph and approves the caption."),
    (14, "Хорошая фотография!",
     "'Good photo!' Feminine adjective and noun."),
    (14, "Напиши: трус не играет в хоккей.",
     "'Write: a coward doesn't play hockey' — a famous line from a classic Soviet hockey song. Meanwhile, back in the flat, Arkady anxiously phones Ilona in the City Hall archive."),
    (15, None,
     "'Hello, Ilona! Why aren't you calling? Did you find it?' Notice the feminine past-tense ending '-la' because he is speaking to Ilona."),
    (16, "Как не нашла?",
     "'What do you mean you didn't find it?' Listen for the word meaning 'how' right alongside 'found' in this line."),
    (16, "Послушай, в чёрном шкафу посмотри.",
     "'Listen, look in the black cabinet.' The noun for cabinet takes the special prepositional ending '-u' when expressing location."),
    (16, "Там справа от двери!",
     "'There to the right of the door!'"),
]

TRANSITION = "Now listen to the whole scene again from start to finish."

OUTRO = (
    "While Ilona opens the black cabinet in the archive and Pasha races to City Hall to shred the folder, "
    "another pair of uninvited guests returns to the communal flat. Listen for 'in reality', 'order', and "
    "'in the archive' when you watch; see you next time."
)
CLOSING = ("anya", "Да, хорошо. Хорошо!")
