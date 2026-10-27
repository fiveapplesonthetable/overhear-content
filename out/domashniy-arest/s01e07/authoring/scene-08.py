ID = "domashniy-arest-s01e07-scene-08"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 8
TITLE = "Подняли штангу, поднимем область  (We Lifted the Barbell, We'll Lift the Region)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "byelinkov": "anja", "governor": "angelina"}
LABELS = {"anya": "Паша", "byelinkov": "Беленьков", "governor": "Виктор Степанович"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.07"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"

INTRO = ("Last time, Arkady staged a fall down the communal stairs and talked Marina into accompanying him to the "
         "hospital. Meanwhile, at City Hall, a doctor is checking Acting Mayor Pasha Osipenko's blood pressure when "
         "campaign aide Byelinkov walks in with alarming poll numbers. Let's listen in Russian first.")

STORY = [
 ("byelinkov", "Сто двадцать на восемьдесят, как у космонавта! Сейчас ещё раз померим.",
  "One hundred and twenty over eighty, like a cosmonaut's! Now we'll measure it once more.",
  [(313, "на"), (313, "как у космонавта"), (314, "Сейчас"), (314, "померим")],
  "numbers '120 на 80' written out in words; doctor's line folded into Byelinkov"),
 ("anya", "Ну, что у вас там?",
  "Well, what have you got there?",
  [(315, "Ну"), (315, "у вас там")],
  "'чего' -> 'что'"),
 ("byelinkov", "Павел Юрьевич, вам нельзя нервничать сейчас.",
  "Pavel Yuryevich, you must not get nervous right now.",
  [(316, "Павел"), (316, "вам нельзя нервничать сейчас")],
  "cue 316 ASR slip 'Ильич' -> 'Юрьевич'"),
 ("anya", "Я не нервничаю! Рейтинг Самсонова сравнялся с нашим?",
  "I'm not nervous! Samsonov's rating has caught up with ours?",
  [(317, "Я не нервничаю"), (318, "Рейтинг Самсонова сравнялся с нашим")], ""),
 ("anya", "Почему он вдруг сравнялся? Мы шли впереди на десять процентов!",
  "Why did he suddenly catch up? We were ahead by ten percent!",
  [(319, "он вдруг сравнялся"), (319, "Мы"), (319, "на"), (319, "процентов шли")],
  "'10' written out as 'десять'; 'с опережением' -> 'впереди'"),
 ("byelinkov", "Он этого ребёнка спас! Вы же видели.",
  "He saved that child! You saw it, after all.",
  [(321, "Ребенка этого"), (321, "спас"), (322, "вы же видели")],
  "'дурацкого' omitted"),
 ("byelinkov", "Это эффект снежного кома.",
  "It's the snowball effect.",
  [(323, "Эффект снежного кома")], ""),
 ("anya", "Я слушаю вас, Виктор Степанович.",
  "I'm listening to you, Viktor Stepanovich.",
  [(325, "Я слушаю вас, Виктор Степанович")], ""),
 ("governor", "Паша, а ты вообще знаешь, почему я звоню тебе?",
  "Pasha, do you even know why I'm calling you?",
  [(326, "Паша, а ты вообще"), (327, "почему я звоню тебе")],
  "'в курсе' -> 'знаешь'"),
 ("anya", "Виктор Степанович, да вы не волнуйтесь! Это просто эффект снежного кома.",
  "Viktor Stepanovich, don't worry! It's just the snowball effect.",
  [(328, "Виктор Степанович, да вы не волнуйтесь"), (330, "эффект снежного кома")], ""),
 ("governor", "А теперь послушай меня! Если ты сегодня не решишь вопрос с Самсоновым.",
  "And now listen to me! If you don't settle the issue with Samsonov today.",
  [(331, "теперь послушай меня"), (332, "Если ты сегодня"), (332, "вопрос с Самсоновым")],
  "cue 331 'чучело' omitted"),
 ("governor", "То завтра я буду поддерживать его! Ты меня понял?",
  "Then tomorrow I will support him! Did you understand me?",
  [(333, "я"), (333, "его"), (334, "Ты меня понял")],
  "cue 333 simplified to A1"),
 ("byelinkov", "Двести десять на сто тридцать девять!",
  "Two hundred and ten over one hundred and thirty-nine!",
  [(335, "на")],
  "'210 на 139' written out in words"),
 ("anya", "Двадцать девять! Тридцать! Пиши текст.",
  "Twenty-nine! Thirty! Write down the text.",
  [(342, "Пиши текст")],
  "'29! 30!' written out in words"),
 ("anya", "Подняли штангу, поднимем область! А теперь уберите эту штангу!",
  "We lifted the barbell, we'll lift the region! And now take this barbell away!",
  [(342, "Подняли штангу, поднимем область"), (344, "Уберите эту")],
  "cue 344 crude 'хреновину. Сдохнуть с вами' -> 'штангу'"),
]

OPENER = ("Let's break it down. Pasha is calmly having his blood pressure checked in his office when Byelinkov "
          "hesitates in the doorway.")

WALK = [
 (0, "Сто двадцать на восемьдесят, как у космонавта! Сейчас ещё раз померим.",
  "'One hundred and twenty over eighty, like a cosmonaut's! Now we'll measure it once more.' In Russian, ideal blood "
  "pressure is always compared to a cosmonaut's."),
 (1, "Ну, что у вас там?",
  "'Well, what have you got there?' Pasha sees the folder in Byelinkov's hands."),
 (2, "Павел Юрьевич, вам нельзя нервничать сейчас.",
  "'Pavel Yuryevich, you must not get nervous right now.' Pasha snatches the poll sheet."),
 (3, "Я не нервничаю! Рейтинг Самсонова сравнялся с нашим?",
  "'I'm not nervous! Samsonov's rating has caught up with ours?' He explodes."),
 (4, "Почему он вдруг сравнялся? Мы шли впереди на десять процентов!",
  "'Why did he suddenly catch up? We were ahead by ten percent!' Byelinkov reminds him of yesterday's news broadcast."),
 (5, "Он этого ребёнка спас! Вы же видели.",
  "'He saved that child! You saw it, after all.' When Samsonov jumped off the bridge to save disguised Lieutenant "
  "Lyova, the whole town saw him as a hero."),
 (6, "Это эффект снежного кома.",
  "'It's the snowball effect.' Just then, Pasha's special phone rings — it is Governor Viktor Stepanovich."),
 (7, "Я слушаю вас, Виктор Степанович.",
  "'I'm listening to you, Viktor Stepanovich.' The Governor has seen the same poll numbers."),
 (8, "Паша, а ты вообще знаешь, почему я звоню тебе?",
  "'Pasha, do you even know why I'm calling you?' Pasha tries to repeat Byelinkov's excuse."),
 (9, "Виктор Степанович, да вы не волнуйтесь! Это просто эффект снежного кома.",
  "'Viktor Stepanovich, don't worry! It's just the snowball effect.' The Governor cuts him off coldly."),
 (10, "А теперь послушай меня! Если ты сегодня не решишь вопрос с Самсоновым.",
  "'And now listen to me! If you don't settle the issue with Samsonov today.' And he delivers his ultimatum."),
 (11, "То завтра я буду поддерживать его! Ты меня понял?",
  "'Then tomorrow I will support him! Did you understand me?' As soon as the Governor hangs up, the blood-pressure "
  "monitor beeps again."),
 (12, "Двести десять на сто тридцать девять!",
  "'Two hundred and ten over one hundred and thirty-nine!' Pasha's blood pressure has skyrocketed. Desperate to match "
  "Samsonov's macho image, Pasha goes to a gym to film a campaign video under a heavy barbell."),
 (13, "Двадцать девять! Тридцать! Пиши текст.",
  "'Twenty-nine! Thirty! Write down the text.' Pinned helplessly under the barbell on his chest, Pasha gasps out a "
  "campaign slogan."),
 (14, "Подняли штангу, поднимем область! А теперь уберите эту штангу!",
  "'We lifted the barbell, we'll lift the region! And now take this barbell away!' Notice the past plural 'we lifted' "
  "paired with the future plural 'we will lift'."),
]

TRANSITION = "Now let's listen to the whole scene in Pasha's office and the gym again."

OUTRO = ("So with his blood pressure spiking and the barbell crushing his chest, Pasha realises he can't beat "
         "Samsonov with gym videos — and decides to send his bodyguards after Samsonov instead. See you next time.")
CLOSING = ("anya", "Подняли штангу, поднимем область!")
