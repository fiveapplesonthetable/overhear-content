ID = "domashniy-arest-s01e05-scene-02"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 5
SCENE = 2
TITLE = "Пьяный за рулём  (Drunk at the Wheel)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nina": "anja", "ilona": "angelina"}
LABELS = {"anya": "Аркадий", "nina": "Нина", "ilona": "Илона"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.05"
SOURCE_FILE = "sources/domashniy-arest/s01/e05.ru.dual.srt"
SOURCE_NOTE = ("Cues 57-82. Morning TV news (57-60), Yulia's dishwashing complaint (67-68), and Danila's remark "
               "(69) are folded into narrator context. Crude words ('дебил' in 70, 'помрет' in 80, 'бухать' in 81) "
               "and the brand name 'БМВ' in 73 are cleaned up or omitted.")

INTRO = ("It's the next morning in the communal kitchen, and the television news is still reporting that the "
         "drunk people's candidate crashed a luxury car into the Society for the Blind, right alongside a story "
         "about three unknown men robbing a cash machine on Garibaldi Street. "
         "Listen as Arkady scolds Samson's wife Nina for drinking wine with Samson instead of keeping an eye on "
         "him, Ilona despairs over their ruined campaign, and Nina warns them what will happen when Samson wakes up.")

STORY = [
 ("anya", "Ну он-то понятно! От него я ничего больше не ждал.",
  "Well, with him it's obvious! I didn't expect anything more from him.",
  [(61, "Ну он-то понятно"), (62, "От него я ничего больше не ждал")], ""),
 ("anya", "Но вы, Нина! Я же просил вас всё проконтролировать!",
  "But you, Nina! I asked you to keep everything under control!",
  [(63, "Но вы, Нина, я же просил вас проконтролировать")],
  "'всё' added; split into two short sentences"),
 ("nina", "Я пыталась!",
  "I tried!",
  [(65, "Пыталась")], "'Я' added"),
 ("anya", "Пыталась? С бутылкой вина в руке?",
  "You tried? With a bottle of wine in your hand?",
  [(66, "Пыталась? С бутылкой вина в руке")], ""),
 ("anya", "У нас выборы, ты понимаешь?",
  "We have an election, do you understand?",
  [(70, "У нас выборы, ты понимаешь")], "insult 'дебил' in cue 70 omitted"),
 ("anya", "Надо придумать какую-то другую версию событий.",
  "We need to think up some other version of events.",
  [(71, "надо придумать какую-то"), (71, "версию событий")],
  "'альтернативную' simplified to 'другую'"),
 ("ilona", "А что тут придумывать? Всё, приехали, это финиш!",
  "And what is there to think up? That's it, we've arrived, this is the finish!",
  [(72, "А что тут придумывать? Все, приехали, это финиш")], ""),
 ("ilona", "Пьяный за рулём врезался в общество слепых! В инвалидов!",
  "Drunk at the wheel, he crashed into the Society for the Blind! Into disabled people!",
  [(73, "Пьяный за рулем"), (74, "Врезался"), (74, "в общество слепых, в инвалидов")],
  "brand name 'БМВ' in cue 73 omitted"),
 ("anya", "Нет, отступать некуда! Впереди тюрьма!",
  "No, there is nowhere to retreat! Ahead is prison!",
  [(76, "Нет, отступать некуда"), (76, "впереди"), (76, "тюрьма")], ""),
 ("anya", "Скажи журналистам. Пресс-конференция будет сегодня вечером.",
  "Tell the journalists. The press conference will be this evening.",
  [(77, "скажи журналистам, пресс-конференция будет сегодня вечером")], ""),
 ("nina", "Слушайте, да забудьте вы уже про свои выборы!",
  "Listen, just forget about your election already!",
  [(78, "Слушайте, да забудьте вы уже про свои выборы")], ""),
 ("ilona", "Это ещё почему?",
  "And why is that?",
  [(79, "Это еще почему")], ""),
 ("nina", "Потому что я знаю Самсонова. Он как всё вспомнит, со стыда умрёт!",
  "Because I know Samsonov. Once he remembers everything, he'll die of shame!",
  [(80, "Потому что я знаю Самсонова. Он как все"), (80, "стыда")],
  "cue 80 'вспомнится, стыда помрет' -> 'вспомнит, со стыда умрёт'; cue 81 'бухать' omitted"),
]

OPENER = ("Let's go back through the scene step by step. While Nina's daughter Yulia washes dishes at the sink, "
          "Arkady glares across the kitchen table at Nina.")

WALK = [
 (0, "Ну он-то понятно!",
  "'Well, with him it's obvious!' The particle attached with a hyphen adds emphasis and contrast: 'as for him, "
  "that's understandable'."),
 (0, "От него я ничего больше не ждал.",
  "'I didn't expect anything more from him.' Notice the double negative with 'nothing' and 'did not wait'."),
 (1, None,
  "'But you, Nina! I asked you to keep everything under control!' Even when scolding her, Arkady addresses Nina "
  "with the polite plural pronoun."),
 (2, None,
  "'I tried!' Nina uses the feminine past tense of the reflexive verb 'to try'. Arkady isn't buying it."),
 (3, None,
  "'You tried? With a bottle of wine in your hand?' Look at the three cases in a row: instrumental 'with a "
  "bottle', genitive 'of wine', and prepositional 'in hand'. When lawyer Danila Golovkin mutters that the car is "
  "insured, Arkady snaps at him."),
 (4, None,
  "'We have an election, do you understand?' Literally 'by us are elections' — the word for an election is "
  "always plural in Russian."),
 (5, None,
  "'We need to think up some other version of events.' The suffix with a hyphen on 'some kind of' means 'some or "
  "other, we don't know which yet'. Ilona throws up her hands."),
 (6, "А что тут придумывать?",
  "'And what is there to think up?' An infinitive question meaning 'what could anyone possibly invent here?'"),
 (6, "Всё, приехали, это финиш!",
  "'That's it, we've arrived, this is the finish!' Saying 'we've arrived' is a classic Russian idiom for 'that's "
  "the end of the road, we're done for'."),
 (7, None,
  "'Drunk at the wheel, he crashed into the Society for the Blind! Into disabled people!' Literally 'behind the "
  "steering wheel', using the instrumental case."),
 (8, None,
  "'No, there is nowhere to retreat! Ahead is prison!' If Samson loses the election to Pasha, Arkady knows he "
  "will go straight back behind bars."),
 (9, None,
  "'Tell the journalists. The press conference will be this evening.' Literally 'today in the evening'. Nina "
  "shakes her head at both of them."),
 (10, None,
  "'Listen, just forget about your election already!' The particle before the imperative softens or hurries the "
  "command along: 'come on, just forget about it'."),
 (11, None,
  "'And why is that?' Ilona asks why Nina thinks the campaign is over."),
 (12, "Потому что я знаю Самсонова.",
  "'Because I know Samsonov.' Nina refers to her husband by his surname in the accusative case."),
 (12, "Он как всё вспомнит, со стыда умрёт!",
  "'Once he remembers everything, he'll die of shame!' Literally 'how he will remember everything, from shame he "
  "will die'."),
]

TRANSITION = "Now let's hear the whole kitchen argument again from the start."
OUTRO = ("So Arkady refuses to give up on the election, while Nina is sure Samson will die of shame as soon as he "
         "remembers what he did. Next we'll see what happens when a hungover Samson walks into the kitchen; see you there.")
CLOSING = ("anya", "Впереди тюрьма!")
