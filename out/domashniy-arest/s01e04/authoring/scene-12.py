# domashniy-arest/s01e04/scene-12.py
ID = "domashniy-arest-s01e04-scene-12"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 4
SCENE = 12
TITLE = "Пресс-конференция во дворе  (Courtyard Press Conference)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.04"
SOURCE_FILE = "sources/domashniy-arest/s01/e04.ru.dual.srt"
VOICES = {"narrator": "sky", "anya": "alisa", "reporter": "angelina", "samson": "anja"}
LABELS = {"anya": "Аркадий", "reporter": "Журналистка", "samson": "Самсон"}
INTRO = "Last time, Arkady showed Samson and Nina the comments calling Samson a people's hero and promised Nina she would be the mayor's wife in two months. Now Arkady has gathered reporters in the courtyard outside the communal flat for a press conference with Samson. Let's listen in Russian first; don't worry about catching every word."
STORY = [
    ("anya", "Я получил урок. Я благодарен Ивану Васильевичу за честное мнение.", "I learned a lesson. I am grateful to Ivan Vasilyevich for his honest opinion.", [(384, 'Я получил урок'), (384, 'благодарен Ивану Васильевичу за честное мнение')], "split into two short sentences"),
    ("reporter", "То есть вы признаёте, что брали взятки?", "So you admit that you took bribes?", [(385, 'То есть вы признаете, что брали взятки')], ""),
    ("anya", "Нет, взяток я не брал. Но я мало думал о людях.", "No, I didn't take bribes. But I thought too little about people.", [(386, 'Нет, взяток я не брал'), (387, 'Но я мало думал о людях')], ""),
    ("anya", "Я попал в беду. И понял, как тяжело живётся народу.", "I got into trouble. And I understood how hard life is for the people.", [(389, 'в беду'), (389, 'как'), (389, 'тяжело живется народу')], "cue 389 'попав в беду, ты по-настоящему понимаешь' simplified into two A1 sentences"),
    ("reporter", "Иван Васильевич, выбрасывать человека в окно нормально?", "Ivan Vasilyevich, is throwing a person out the window normal?", [(393, 'Иван Васильевич'), (393, 'выбрасывать человека в окно это нормально')], "'это' dropped for brevity"),
    ("samson", "А что с ними делать? Они совсем совесть потеряли!", "And what are we supposed to do with them? They've completely lost their conscience!", [(394, 'А что с ними делать'), (395, 'они совсем'), (396, 'потеряли')], "slang 'нюх потеряли, оборзели' -> 'совесть потеряли'; crude 391 dropped"),
    ("reporter", "А что вы предлагаете? Всех чиновников в окно выбрасывать?", "And what do you propose? Throwing all officials out the window?", [(398, 'А что вы предлагаете'), (398, 'всех чиновников в окно')], "'выкидывать' -> 'выбрасывать'"),
    ("samson", "Можно и всех! Но только это не поможет.", "Could do all of them! Only that won't help.", [(399, 'и всех'), (400, 'Но только это не поможет')], "cue 399 'Да не бешало бы и всех' -> 'Можно и всех'"),
    ("anya", "Правильно, это не поможет! Уже нужно самим.", "Right, that won't help! People need to do it themselves now.", [(401, 'Правильно, это не поможет. Уже нужно самим')], ""),
    ("samson", "Что самим?", "Do what themselves?", [(402, 'Что самим')], ""),
    ("reporter", "Самим идти во власть? Что это значит?", "Go into government themselves? What does that mean?", [(404, 'Идти во власть'), (406, 'что это значит')], ""),
    ("anya", "Иван Васильевич от слов переходит к делу.", "Ivan Vasilyevich is moving from words to action.", [(407, 'Иван Васильевич от слов переходит к делу')], ""),
    ("anya", "Он выдвигает свою кандидатуру на пост мэра города!", "He is putting forward his candidacy for the post of mayor of the city!", [(408, 'Он выдвигает свою кандидатуру на пост мэра города')], ""),
    ("reporter", "Вы подтверждаете это, Иван Васильевич?", "Do you confirm this, Ivan Vasilyevich?", [(409, 'Вы подтверждаете'), (409, 'Иван Васильевич')], "'эту информацию' -> 'это'"),
    ("samson", "Да, да! Я выдвигаю свою кандидатуру.", "Yes, yes! I am putting forward my candidacy.", [(410, 'Да, да. Я выдвигаю свою кандидатуру')], ""),
    ("anya", "У Самсонова главное — честность и порядочность. Все говорят, а он делает!", "Samsonov has the main thing — honesty and decency. Everyone talks, while he gets things done!", [(413, 'главное'), (413, 'порядочность'), (419, 'Все говорят, а он делает')], "'честность и' added; cue 419 from Nina folded into Arkady's closing line"),
]
OPENER = "Let's go through the press conference. Arkady stands beside Samson in front of the microphones and puts on his most humble voice."
WALK = [
    (0, 'Я получил урок.', "'I learned a lesson.' Literally 'I received a lesson'."),
    (0, 'Я благодарен Ивану Васильевичу за честное мнение.', "'I am grateful to Ivan Vasilyevich for his honest opinion.' 'Grateful' is a short masculine adjective, followed by the 'to/for' form for the person and 'for' plus the object-form for the reason. A reporter jumps in."),
    (1, None, "'So you admit that you took bribes?' The pair of words at the start means 'that is, so'. Arkady quickly corrects her."),
    (2, 'Нет, взяток я не брал.', "'No, I didn't take bribes.' With the negated verb, 'bribes' goes into the plural 'of' form and moves to the front for emphasis."),
    (2, 'Но я мало думал о людях.', "'But I thought too little about people.' Then he plays for sympathy."),
    (3, None, "'I got into trouble. And I understood how hard life is for the people.' Literally 'how hard it is lived to the people', an impersonal self-action verb form with the 'to/for' form. The reporter turns to Samson."),
    (4, None, "'Ivan Vasilyevich, is throwing a person out the window normal?' Notice how 'into the window' uses the direct-object form, which is how Russian says 'out of the window'. Samson answers bluntly."),
    (5, 'А что с ними делать?', "'And what are we supposed to do with them?' Russian forms this yes-or-no question without a question word, relying on rising pitch on 'to do'."),
    (5, 'Они совсем совесть потеряли!', "'They've completely lost their conscience!' Meaning the town officials. The reporter presses him."),
    (6, None, "'And what do you propose? Throwing all officials out the window?' Samson starts to agree, then remembers what Arkady coached him to say."),
    (7, 'Можно и всех!', "'Could do all of them!' The key word here means 'one could', anchored at the close by 'one could'."),
    (7, 'Но только это не поможет.', "'Only that won't help.' Arkady jumps in on cue to steer the conversation."),
    (8, None, "'Right, that won't help! People need to do it themselves now.' Samson forgets his next line."),
    (9, None, "'Do what themselves?' Luckily, the reporter guesses it for him."),
    (10, None, "'Go into government themselves? What does that mean?' Literally 'go into power'. Arkady makes the big announcement."),
    (11, None, "'Ivan Vasilyevich is moving from words to action.' Literally 'from words crosses over to deed'. And then the headline."),
    (12, None, "'He is putting forward his candidacy for the post of mayor of the city!' The reporters gasp and ask Samson directly."),
    (13, None, "'Do you confirm this, Ivan Vasilyevich?' Prompted by a nod from Arkady, Samson repeats the long phrase."),
    (14, None, "'Yes, yes! I am putting forward my candidacy.' And Arkady wraps up with a campaign pitch and their new slogan."),
    (15, 'У Самсонова главное — честность и порядочность.', "'Samsonov has the main thing — honesty and decency.' Listen for the word meaning 'there is', which leads straight into 'decency'."),
    (15, 'Все говорят, а он делает!', "'Everyone talks, while he gets things done!' Nina immediately steps up to give reporters the phone number of their campaign headquarters, and soon the news is on every screen in town."),
]
TRANSITION = "Let's hear the whole press conference again from start to finish."
OUTRO = "So Ivan Samsonov is officially running for mayor of Sineozersk, with Arkady as his secret campaign boss and Nina taking calls. Even the security agents Lavrov and Zavarzin see the news in their car. See you next time!"
CLOSING = ("samson", "Пока!")
