ID = "domashniy-arest-s01e03-scene-19"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 19
TITLE = "Ревнивый Самсон  (Jealous Samson)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nina": "angelina"}
LABELS = {"anya": "Самсон", "nina": "Нина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"

INTRO = ("Last time, the dean stormed out of Marina's room and left his Chilean wine and fruit with Arkady. Out in the "
         "corridor, Samson calls Arkady a thief and takes the bottle off him, then marches into his own room to have "
         "it out with Nina over her friendly chat with her old classmate, the lawyer Danila Golovkin. We'll hear the "
         "conversation in Russian first; don't worry about catching every word.")

STORY = [
 ("anya", "Ну и что это такое?",
  "Well, and what is all this?",
  [(628, "Ну и что это такое")], ""),
 ("nina", "Чего? Ты же сам всё покупал.",
  "What? You bought everything yourself.",
  [(629, "Чего")],
  "cue 629 'При тебе же все покупало' simplified to 'Ты же сам всё покупал' (the tools on the table)"),
 ("anya", "Да я не про это. Кто этот тип в коридоре?",
  "That's not what I mean. Who was that guy in the corridor?",
  [(630, "Да я не про это")],
  "cue 631 'какого урожая здесь этот ущербный нарисовался' retold cleanly"),
 ("nina", "Какой? Даня, что ли? Ну, он же адвокат Аникеева.",
  "Which one? You mean Danya? Well, he's Anikeev's lawyer.",
  [(632, "Какой"), (634, "что ли"), (635, "Ну, он же адвокат Аникеева")],
  "cue 634 mistranscribes 'Даня' as 'Дальше'"),
 ("anya", "Даня, Данюша! Какая ты стала красивая!",
  "Danya, Danyusha! Look how beautiful you've become!",
  [(636, "Даня, Данюша"), (637, "стала, какая красивая")],
  "Samson mimics Golovkin's compliment from the corridor"),
 ("nina", "Ты что, Самсонов? Мы просто одноклассники.",
  "What's wrong with you, Samsonov? We're just classmates.",
  [(639, "Самсонов"), (639, "мы одноклассники")],
  "dropped 'придурок'"),
 ("anya", "Одноклассники, ага! Я не понимаю, как ты с ним могла.",
  "Classmates, right! I don't understand how you could be with him.",
  [(640, "Я"), (640, "не понимаю, как ты с ним могла")],
  "'Одноклассник' -> plural; 'вообще' trimmed"),
 ("nina", "Чего могла? Он мне как подружка был.",
  "Could what? He was like a girlfriend to me.",
  [(641, "Чего могла"), (643, "Он мне как подружка был")], ""),
 ("anya", "Подружка! Знаем мы таких подружек.",
  "A girlfriend! We know that kind of girlfriend.",
  [(644, "Подружка, знаем таких подружек")], "'мы' added"),
 ("anya", "Я тебе серьёзно говорю. Пусть только ещё раз здесь появится!",
  "I'm telling you seriously. Let him just show up here one more time!",
  [(645, "Я тебе серьёзно говорю, ещё раз здесь появится")],
  "split into two short sentences"),
 ("anya", "Он у меня не только заикаться будет! Вот.",
  "Stuttering won't be his only problem with me! So there.",
  [(645, "он не только заикаться будет"), (647, "Вот")],
  "crude cue 646 dropped"),
 ("nina", "Чего?",
  "What?",
  [(648, "Чего")], ""),
 ("nina", "Вот с таким настроением и иди к Аникееву. Паяльник проверь.",
  "Go to Anikeev in just that mood. Check the soldering iron.",
  [(649, "Вот с таким настроением и"), (650, "Паяльник проверь")],
  "cue 649 'надо идти к Винникееву-то' -> 'иди к Аникееву'"),
]

OPENER = ("Let's walk through it together. Samson comes into the room where the hardware-shop tools are laid out, "
          "fuming with jealousy.")

WALK = [
 (0, None,
  "'Well, and what is all this?' A classic angry opening question. Nina thinks he is looking at the tools on the table."),
 (1, "Чего? Ты же сам всё покупал.",
  "'What? You bought everything yourself.' The little word after 'you' means 'after all', and 'yourself' is masculine "
  "for Samson. Samson waves that away."),
 (2, "Да я не про это.",
  "'That's not what I mean.' Word for word: 'yes I am not about this'."),
 (2, "Кто этот тип в коридоре?",
  "'Who was that guy in the corridor?' Literally 'who is this type in the corridor'. Russian drops 'was' and uses the "
  "prepositional ending '-e' after 'in'. Nina works out whom he means."),
 (3, "Какой? Даня, что ли?",
  "'Which one? You mean Danya?' Adding the two little words at the end turns a name into 'do you mean Danya?'."),
 (3, "Ну, он же адвокат Аникеева.",
  "'Well, he's Anikeev's lawyer.' The surname takes the '-a' ending to mean 'of Anikeev'. Samson mocks the sweet names "
  "and compliments he heard in the hall."),
 (4, "Даня, Данюша!",
  "'Danya, Danyusha!' Both are affectionate short forms of the name Danila."),
 (4, "Какая ты стала красивая!",
  "'Look how beautiful you've become!' Both 'what a' and 'beautiful' have feminine endings for Nina. Nina rolls her eyes "
  "and calls her husband by his surname."),
 (5, None,
  "'What's wrong with you, Samsonov? We're just classmates.' The word for 'classmates' is built from 'one' and 'class': "
  "people from the same class. Samson does not buy it."),
 (6, "Одноклассники, ага!",
  "'Classmates, right!' He repeats the word sarcastically."),
 (6, "Я не понимаю, как ты с ним могла.",
  "'I don't understand how you could be with him.' Literally 'how you with him could', with the feminine past ending "
  "'-la'. Nina is baffled."),
 (7, "Чего могла?",
  "'Could what?' In casual speech, 'what' often appears in its 'of' form."),
 (7, "Он мне как подружка был.",
  "'He was like a girlfriend to me.' Notice the feminine word for a female friend: she means Danila was like one of the "
  "girls at school, never a boyfriend. Samson scoffs."),
 (8, None,
  "'A girlfriend! We know that kind of girlfriend.' In the second sentence the noun is in the accusative plural, which "
  "for animate nouns looks just like the genitive plural. Then he makes a threat."),
 (9, "Я тебе серьёзно говорю.",
  "'I'm telling you seriously.' Word for word: 'I to you seriously speak'."),
 (9, "Пусть только ещё раз здесь появится!",
  "'Let him just show up here one more time!' The first word makes a third-person command: 'let him appear'."),
 (10, None,
  "'Stuttering won't be his only problem with me! So there.' Literally 'he with me not only to stutter will'. And he "
  "finishes with a satisfied 'there!'. Nina sees a way to put her husband's temper to use."),
 (11, None,
  "'What?' She pauses for a second as the idea clicks."),
 (12, "Вот с таким настроением и иди к Аникееву.",
  "'Go to Anikeev in just that mood.' After 'with', both 'such' and 'mood' take the instrumental ending. And after "
  "'towards', Anikeev's surname takes the '-u' ending. Then the practical reminder."),
 (12, "Паяльник проверь.",
  "'Check the soldering iron.' A brisk imperative at the end. Remember, they only want to scare Arkady into telling "
  "where the forty million roubles are."),
]

TRANSITION = "Let's listen to the whole exchange again from the top."

OUTRO = ("So Nina channels Samson's jealousy straight into their plan to scare the mayor with a soldering iron. "
         "Listen for 'classmates' and 'girlfriend' when you watch; see you next time.")
CLOSING = ("anya", "Сейчас всё проверим.")
