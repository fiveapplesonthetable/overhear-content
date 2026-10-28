# Authoring module for domashniy-arest-s01e01-scene-18.
ID = 'domashniy-arest-s01e01-scene-18'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 1
SCENE = 18
TITLE = 'Течёт труба  (The Leaking Pipe)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'nina': 'Нина', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.01'
SOURCE_FILE = 'sources/domashniy-arest/s01/e01.ru.dual.srt'
INTRO = "We're still in the communal flat. Last time, Arkady offered Samson peace, Samson broke his finger with a handshake, and announced that the mayor would now be the family's servant. Now Samson drags him to the shared toilet, where an old pipe is leaking, and Arkady has an idea. We'll hear it in Russian first; don't worry about catching every word."
OPENER = "Let's go back through it slowly. Samson pushes Arkady into the little room he knows from his childhood."
TRANSITION = 'Now the whole scene once more, in Russian.'
OUTRO = 'The pipe is still leaking, but Arkady has talked his way out of the repair job, at least for today. Next time the family writes its wish list; see you then. See you next time!'
CLOSING = ('nina', 'Пока!')
STORY = [
    ('samson', 'Узнаёшь? У нас здесь ничего не изменилось.', 'Recognise it? Nothing has changed here.', [(695, 'Узнаёшь'), (697, 'у нас здесь ничего не изменилось')], ''),
    ('arkady', 'Пусти меня, Самсон!', 'Let me go, Samson!', [(694, 'Пусти меня')], "'Самсон' added as address"),
    ('samson', 'Сейчас будешь чинить трубу. И унитаз не забудь помыть.', "Now you're going to fix the pipe. And don't forget to wash the toilet.", [(698, 'Сейчас будешь'), (703, 'Унитаз не забудь помыть')], "698 'стоять, чинить' simplified to 'чинить трубу'; the detailed repair orders (699-702) summarised"),
    ('arkady', 'Послушай, Самсон, я это делать не буду.', "Listen, Samson, I'm not going to do this.", [(705, 'Послушай, Самсон')], "706 retold cleanly: the crude refusal becomes 'я это делать не буду'"),
    ('arkady', 'Я выйду отсюда через две недели. Я решу все ваши проблемы.', "I'll be out of here in two weeks. I'll solve all your problems.", [(709, 'Я выйду отсюда через две недели'), (710, 'Я решу все ваши проблемы')], "'максимум' dropped"),
    ('arkady', 'У вас будет всё, что захотите.', "You'll have everything you want.", [(711, 'У вас будет все, что захотите')], ''),
    ('nina', 'Всё, что захотим, говоришь?', 'Everything we want, you say?', [(716, 'Все, что захотим, говоришь')], 'given to Nina'),
    ('arkady', 'Всё, что захотите. Клянусь!', 'Everything you want. I swear!', [(717, 'Все, что захотите'), (719, 'клянусь')], "'Мама' dropped from 719"),
    ('samson', 'Нина, не слушай. Это опять обман.', "Nina, don't listen. It's another trick.", [], "retells 720-721 ('разводняк очередной' -> 'опять обман')"),
    ('arkady', 'Нет, это не обман. В этот раз всё будет официально.', "No, it's not a trick. This time everything will be official.", [(722, 'это не'), (723, 'В этот раз все будет официально')], "722 'разводняк' -> 'обман'"),
    ('nina', 'Пока всё не подпишешь, отсюда не выйдешь.', "You're not leaving here until you sign everything.", [(726, 'Пока все не подпишешь, отсюда не выйдешь')], ''),
    ('arkady', 'Вот, сразу видно, деловая женщина.', "Now there's a businesswoman, you can see it at once.", [(727, 'Вот, сразу видно, деловая женщина')], ''),
    ('nina', 'Юля, неси ручку и листик.', 'Yulia, bring a pen and a piece of paper.', [(730, 'неси ручку и листик')], "'Юля' written in its standard form"),
    ('arkady', 'Послушайте, а можно в другое место? Здесь плохо пахнет.', 'Listen, could we go somewhere else? It smells bad in here.', [(731, 'Послушайте'), (733, 'в другое место')], "732-735 simplified: 'можем мы переместиться' -> 'можно'; the smell line retold"),
    ('nina', 'Ладно, пойдём в комнату.', "All right, let's go to our room.", [], "added: the next scene takes place in the Samsonovs' room"),
]
WALK = [
    (0, 'Узнаёшь?', "'Recognise it?' One word does the whole job: the verb ends in the 'you' form, so no pronoun is needed. Then Samson looks around."),
    (0, 'У нас здесь ничего не изменилось.', "'Nothing has changed here.' Notice the double negative: literally 'nothing not changed'. In Russian that's normal, and it doesn't cancel out. Arkady struggles."),
    (1, None, "'Let me go, Samson!' A short command, in the casual form he uses with his old neighbour. Samson gives him his orders."),
    (2, 'Сейчас будешь чинить трубу.', "'Now you're going to fix the pipe.' The word for 'you will be', plus a verb, is the simplest way to talk about the future. The pipe is wrapped in old rags, and it leaks."),
    (2, 'И унитаз не забудь помыть.', "'And don't forget to wash the toilet.' The order is upside down compared with English: toilet first, then 'don't forget', then 'wash'. Arkady refuses."),
    (3, None, "'Listen, Samson, I'm not going to do this.' Again the word for 'I will be', now with 'not'. In the show he says it a lot less politely. Then he changes tactics."),
    (4, 'Я выйду отсюда через две недели.', "'I'll be out of here in two weeks.' The verb is a completed action, so in the present form it points to the future. That's the second way to talk about the future, and you'll hear it everywhere."),
    (4, 'Я решу все ваши проблемы.', "'I'll solve all your problems.' Same thing: a completed-action verb, so it means 'I will solve'. Spoken like a true politician."),
    (5, None, "'You'll have everything you want.' Literally 'at you will be everything'. That's how Russians say someone has something. Nina is interested."),
    (6, None, "'Everything we want, you say?' She repeats his words, but changes 'you want' to 'we want'. Arkady insists."),
    (7, None, "'Everything you want. I swear!' Right then, Samson isn't convinced at all."),
    (8, None, "'Nina, don't listen. It's another trick.' The word for 'again' makes it clear: he has tricked them before. Arkady has an answer for that."),
    (9, None, "'No, it's not a trick. This time everything will be official.' The last word sounds like the English, so you can guess it. Nina knows what she wants."),
    (10, None, "'You're not leaving here until you sign everything.' Literally 'while you don't sign everything, you won't leave'. A useful pattern for setting conditions. Arkady likes her style."),
    (11, None, "'Now there's a businesswoman, you can see it at once.' The middle phrase means 'it's immediately visible'. Nina calls her daughter."),
    (12, None, "'Yulia, bring a pen and a piece of paper.' The verb is a command, and both things are in the object form, because Yulia is to bring them. Arkady has one more request."),
    (13, 'Послушайте, а можно в другое место?', "'Listen, could we go somewhere else?' This time he uses the polite or plural form of 'listen', because he's speaking to the whole family. The word in the middle is very handy: it means 'is it possible' or 'may we'."),
    (13, 'Здесь плохо пахнет.', "'It smells bad in here.' Literally 'here badly smells'. No 'it' is needed. And Nina agrees, for once."),
    (14, None, "'All right, let's go to our room.' The second word means 'let's go'. And so the negotiations move next door."),
]
