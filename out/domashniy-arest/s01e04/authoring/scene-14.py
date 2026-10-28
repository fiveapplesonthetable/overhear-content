# domashniy-arest/s01e04/scene-14.py
ID = "domashniy-arest-s01e04-scene-14"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 4
SCENE = 14
TITLE = "Приказ губернатора  (The Governor's Order)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.04"
SOURCE_FILE = "sources/domashniy-arest/s01/e04.ru.dual.srt"
VOICES = {"narrator": "sky", "pasha": "anja", "governor": "angelina"}
LABELS = {"pasha": "Паша", "governor": "Губернатор"}
INTRO = "Last time, Moscow strategist Ilona Leonidovna arrived at Pasha's campaign headquarters just as Ksyusha reported that Ivan Samsonov had entered the race for mayor. Moments later, Governor Viktor Stepanovich calls Pasha by video link from a winter park to demand action against Samsonov, and then Pasha takes his temper out on Ilona. We'll hear it in Russian first; don't worry about catching every word."
STORY = [
    ("pasha", "Виктор Степанович, приветствую. Я совсем не радостный.", "Viktor Stepanovich, greetings. I'm not happy at all.", [(478, 'Виктор Степанович, приветствую'), (481, 'Я не радостный'), (481, 'совсем')], ""),
    ("governor", "Ты предпринимаешь что-нибудь?", "Are you doing anything about it?", [(482, 'Ты предпринимаешь что-нибудь')], ""),
    ("pasha", "Конечно, предпринимаю. А как же?", "Of course I am. How else?", [(483, 'Конечно, предпринимаю. А как же')], ""),
    ("governor", "Что-то голос какой-то не очень уверенный. Что конкретно?", "Your voice doesn't sound very confident. What specifically?", [(484, 'Что-то голос какой-то не очень уверенный'), (487, 'Что конкретно')], ""),
    ("pasha", "Ну, мы тут всё обсуждали.", "Well, we've been discussing everything here.", [(486, 'Мы тут'), (489, 'Обсуждали')], ""),
    ("governor", "Ты не обсуждай, ты действуй! Самсонова надо ликвидировать!", "Don't discuss, act! Samsonov must be eliminated!", [(490, 'ты не обсуждай'), (491, 'Ты действуй'), (492, 'Самсонова надо ликвидировать')], "dropped insult 'дятел' in cue 490"),
    ("pasha", "В смысле, Виктор Степанович? Прямо так, да?", "What do you mean, Viktor Stepanovich? Just like that?", [(493, 'В смысле, Виктор Степанович'), (495, 'так, да')], "cue 495 'Прям' -> 'Прямо'"),
    ("governor", "Политически!", "Politically!", [(496, 'Политически')], "dropped insult 'чучело'"),
    ("pasha", "А, ну я так и думал. Политически, конечно.", "Ah, well, that's what I thought. Politically, of course.", [(497, 'А, ну я так и думал, политически, конечно')], "split into two short sentences"),
    ("governor", "Произошла накладка. Меня никто не встретил на вокзале.", "There was a mix-up. Nobody met me at the station.", [(515, 'произошла накладка'), (516, 'меня никто не встретил на вокзале')], "split into two short sentences"),
    ("pasha", "Это не накладка. Вас и не должны были встречать.", "That's not a mix-up. Nobody was supposed to meet you.", [(517, 'Это не накладка'), (518, 'Вас и не должны были встречать')], ""),
    ("governor", "Как так?", "How so?", [(519, 'Как так')], ""),
    ("pasha", "А вот так. Потому что у нас бюджет урезан.", "Just like that. Because our budget has been cut.", [(520, 'А вот так'), (520, 'Потому что у нас бюджет урезан')], ""),
    ("pasha", "Вы теперь работаете не на своего дружка Аникеева. Вы работаете на меня.", "You no longer work for your friend Anikeev. You work for me.", [(521, 'вы теперь работаете не на своего дружка'), (522, 'а на меня')], "cue 522 mistranscribes 'Аникеева' as 'а не Киева'; split into two short sentences"),
    ("pasha", "Я жду только одного — результатов от вас. Работайте!", "I expect only one thing: results from you. Get to work!", [(528, 'Я жду только одного. Результатов от вас'), (529, 'Работайте')], ""),
    ("governor", "Хорошо. Хорошо.", "Fine. Fine.", [(530, 'Хорошо. Хорошо')], ""),
]
OPENER = "Let's go back through the scene line by line. Pasha stands nervously in front of the wall screen as the governor's face appears."
WALK = [
    (0, 'Виктор Степанович, приветствую.', "'Viktor Stepanovich, greetings.' A formal, slightly stiff greeting to his boss."),
    (0, 'Я совсем не радостный.', "'I'm not happy at all.' The governor has just asked why Pasha looks so cheerful when Samsonov is on television all day. The adjective has the masculine ending '-iy'. The governor gets straight to the point."),
    (1, None, "'Are you doing anything about it?' Literally 'are you undertaking anything?'. Notice the informal 'you': the governor talks down to Pasha."),
    (2, None, "'Of course I am. How else?' Pasha repeats the same verb in the 'I' form to sound keen. The governor does not believe him."),
    (3, 'Что-то голос какой-то не очень уверенный.', "'Your voice doesn't sound very confident.' Literally 'somehow the voice is kind of not very confident'."),
    (3, 'Что конкретно?', "'What specifically?' Two sharp words, and Pasha stammers."),
    (4, None, "'Well, we've been discussing everything here.' Past tense plural: 'we were discussing'. That sets the governor off."),
    (5, 'Ты не обсуждай, ты действуй!', "'Don't discuss, act!' Two imperatives side by side: first a negative command, 'don't discuss', and then a positive one, 'take action!'."),
    (5, 'Самсонова надо ликвидировать!', "'Samsonov must be eliminated!' The surname takes the object-form '-a' ending. Pasha takes the verb way too literally."),
    (6, None, "'What do you mean, Viktor Stepanovich? Just like that?' The opening two-word phrase literally means 'in the sense?' and is the everyday Russian way to ask 'what do you mean?'. The governor yells into the camera."),
    (7, None, "'Politically!' Just one adverb, ending in '-ski'. Pasha wipes his brow."),
    (8, None, "'Ah, well, that's what I thought. Politically, of course.' Out in the snowy park, the governor finishes staging a photo of himself in a tracksuit claiming he just ran ten kilometres, then demands cognac because he is freezing. Meanwhile, in Pasha's office, Ilona steps forward."),
    (9, 'Произошла накладка.', "'There was a mix-up.' The noun means an overlap or a hitch in plans, and the verb has the feminine past ending '-a'."),
    (9, 'Меня никто не встретил на вокзале.', "'Nobody met me at the station.' Notice the double negation: 'nobody did not meet me'. Pasha doesn't apologise."),
    (10, 'Это не накладка.', "'That's not a mix-up.' Short and cold."),
    (10, 'Вас и не должны были встречать.', "'Nobody was supposed to meet you.' Literally 'they were not even supposed to meet you'."),
    (11, None, "'How so?' Two tiny words of surprise."),
    (12, None, "'Just like that. Because our budget has been cut.' Remember, Arkady is still holding the forty million roubles Pasha counted on. Then Pasha reminds Ilona who is in charge."),
    (13, 'Вы теперь работаете не на своего дружка Аникеева.', "'You no longer work for your friend Anikeev.' Working 'for' someone uses the preposition 'onto' plus the object-form. He uses a dismissive word for 'little friend'."),
    (13, 'Вы работаете на меня.', "'You work for me.' Same preposition, followed by the object-form of 'I'. Then his final order."),
    (14, 'Я жду только одного — результатов от вас.', "'I expect only one thing: results from you.' After 'wait for' or 'expect', both 'one thing' and 'results' take the 'of' case."),
    (14, 'Работайте!', "'Get to work!' A plural formal command. Ilona swallows her anger."),
    (15, None, "'Fine. Fine.' She repeats the word calmly, but she will not forget how Pasha treated her."),
]
TRANSITION = "Let's listen to the whole conversation again from start to finish."
OUTRO = "So the governor orders Pasha to eliminate Samsonov politically, and Pasha foolishly antagonises his own Moscow strategist on her first day. Listen for 'act', 'politically', and 'results' when you watch. See you next time!"
CLOSING = ("pasha", "Пока!")
