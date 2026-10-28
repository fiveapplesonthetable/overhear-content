# Authoring module for domashniy-arest-s01e05-scene-09.
ID = 'domashniy-arest-s01e05-scene-09'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 5
SCENE = 9
TITLE = 'В обществе слепых  (At the Society of the Blind)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'gennady': 'Геннадий Андреевич', 'ilona': 'Илона'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.05'
SOURCE_FILE = 'sources/domashniy-arest/s01/e05.ru.dual.srt'
INTRO = "Last time, in the kitchen, Arkady told Marina to ask her friend the dean for money to pay off the debt collectors. Meanwhile, Ilona visits the damaged building of the Society of the Blind, where workers are sorting soaked boxes of dried herbs after Samson's crash, and tries to apologise to chairman Gennady Andreyevich. Let's listen in Russian first."
OPENER = "Let's walk through it. Amid the rubble and soaked boxes at the Society of the Blind, Ilona introduces herself to chairman Gennady Andreyevich."
TRANSITION = "Now let's listen to the whole scene at the Society of the Blind again."
OUTRO = "So Ilona's visit uncovers a crucial secret: Arkady really did sign the order for the blind society's new building two years ago, and Pasha stole the money himself. Now they just have to prove it. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('ilona', 'Здравствуйте! Я не журналистка. Я руководитель штаба Ивана Самсонова.', "Hello! I'm not a journalist. I'm the head of Ivan Samsonov's campaign.", [(310, 'Здравствуйте'), (313, 'Я не журналистка'), (315, 'Я руководитель штаба Ивана Самсонова')], ''),
    ('ilona', 'Я пришла принести вам наши самые глубокие извинения.', "I've come to bring you our deepest apologies.", [(316, 'я пришла'), (316, 'принести вам наши самые'), (316, 'извинения')], "'глубочайшие' -> A1 'глубокие'"),
    ('gennady', 'Вот это уже наглость! Вы же не слепая.', 'Now that is nerve! You are not blind, after all.', [(317, 'Вот это уже наглость'), (318, 'Вы же не слепая')], ''),
    ('gennady', 'Вы видите, что он тут сделал? Он теперь проиграет выборы!', 'Do you see what he did here? He will lose the election now!', [(318, 'Вы видите, что он'), (324, 'Он же теперь'), (324, 'выборы')], "'натворил' -> 'сделал', 'провалит' -> 'проиграет'"),
    ('ilona', 'Нет, нашему кандидату за это очень стыдно.', 'No, our candidate is very ashamed of this.', [(325, 'Нет'), (327, 'нашему кандидату за это очень стыдно')], ''),
    ('gennady', 'Да кого мы слушаем? С ними же этот взяточник Аникеев!', 'Why are we even listening? That bribe-taker Anikeev is with them!', [(328, 'Да кого мы слушаем'), (328, 'взяточник с ними')], "cue 328 slip 'а не Кей' -> 'Аникеев'"),
    ('ilona', 'Аркадий Борисович — очень опытный политик. И он взяток не брал.', "Arkady Borisovich is a very experienced politician. And he didn't take bribes.", [(329, 'Аркадий Борисович'), (329, 'очень опытный политик'), (330, 'И он взяток не брал')], ''),
    ('ilona', 'Он всегда поддерживал инвалидов!', 'He always supported disabled people!', [(337, 'Всегда'), (337, 'он поддерживал'), (337, 'инвалидов')], ''),
    ('gennady', 'Пятнадцать лет мы просим новое здание! Аникеев лично сюда приезжал, и что?', "For fifteen years we've been asking for a new building! Anikeev came here in person, and what?", [(333, 'Пятнадцать лет мы'), (333, 'просим'), (334, 'Аникеев'), (334, 'лично'), (334, 'сюда приезжал'), (335, 'И что')], ''),
    ('gennady', 'Павел Юрьевич нам помог! Он пообещал построить нам новое здание.', 'Whereas Pavel Yuryevich helped us! Today he promised to build us a new building.', [(343, 'Павел'), (343, 'пообещал нам'), (343, 'построить новое здание')], "cue 343 slip 'Юрий Часипенко' -> 'Юрьевич', split into two short sentences"),
    ('gennady', 'Поэтому мы будем поддерживать его!', 'Therefore we will support him!', [(344, 'Поэтому мы будем поддерживать его')], ''),
    ('ilona', 'Аркадий, слепые тебя ненавидят! Куда ты дел деньги на новое здание?', 'Hello, Arkady! The blind people hate you. Where did you put their money for the new building?', [(346, 'Слепые тебя ненавидят'), (348, 'деньги на новое здание')], ''),
    ('arkady', 'Я их ещё два года назад им выделил! Я сам приказ подписывал!', 'I allocated it to them two years ago! I signed the order myself!', [(349, 'Я их еще два года назад им выделил'), (352, 'Я сам приказ подписывал')], ''),
    ('ilona', 'Почему они в старом здании? Осипенко сказал, что деньги забрал ты!', 'Then why are they in the old building? Osipenko said that you took the money!', [(350, 'Осипенко'), (350, 'сказал, что'), (353, 'почему они'), (353, 'в старом здании')], 'cues 350 and 353 combined into two short A1 sentences'),
    ('arkady', 'Что за глупости? Значит, Осипенко сам эти деньги украл!', 'What nonsense? That means Osipenko stole that money himself!', [(351, 'Что за'), (354, 'значит, Осипенко сам эти')], "cue 351 'бред' -> 'глупости', cue 354 slang 'бабки спер' -> 'деньги украл'"),
]
WALK = [
    (0, None, "'Hello! I'm not a journalist. I'm the head of Ivan Samsonov's campaign.' Literally 'leader of the headquarters'. Then she offers an apology."),
    (1, None, "'I've come to bring you our deepest apologies.' Chairman Gennady Andreyevich is furious."),
    (2, None, "'Now that is nerve! You are not blind, after all.' He points his white cane toward the hole in the wall where Samson's car crashed through."),
    (3, None, "'Do you see what he did here? He will lose the election now!' Right then, Ilona tries to soften his anger."),
    (4, None, "'No, our candidate is very ashamed of this.' Literally 'to our candidate for this it is very shameful'. Then one of the workers mentions Arkady."),
    (5, None, "'Why are we even listening? That bribe-taker Anikeev is with them!' In this moment, Ilona loyally defends Arkady."),
    (6, None, "'Arkady Borisovich is a very experienced politician. And he didn't take bribes.' Notice the plural 'of' form 'of bribes' after the negative verb."),
    (7, None, "'He always supported disabled people!' That makes Gennady Andreyevich laugh bitterly."),
    (8, None, "'For fifteen years we've been asking for a new building! Anikeev came here in person, and what?' Then he reveals who already visited them that morning."),
    (9, None, "'Pavel Yuryevich helped us! He promised to build us a new building.' Right then, Pasha Osipenko beat them to it."),
    (10, None, "'Therefore we will support him!' Stepping outside, Ilona immediately phones Arkady, who is hiding in the communal flat's bathroom while old Klavdia bangs on the door."),
    (11, None, "'Arkady, the blind people hate you! Where did you put the money for the new building?' In this moment, Arkady is genuinely shocked."),
    (12, None, "'I allocated it to them two years ago! I signed the order myself!' For once, Arkady actually did something good as mayor."),
    (13, None, "'Why are they in the old building? Osipenko said that you took the money!' In the show Osipenko told them Arkady used their money to build himself a hunting lodge. Arkady puts two and two together."),
    (14, None, "'What nonsense? That means Osipenko stole that money himself!' While working as Arkady's deputy, Pasha quietly stole the money meant for the blind society's new building."),
]
