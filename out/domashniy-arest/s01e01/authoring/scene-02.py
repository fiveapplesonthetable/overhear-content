# Authoring module for domashniy-arest-s01e01-scene-02.
ID = 'domashniy-arest-s01e01-scene-02'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 1
SCENE = 2
TITLE = "Где машинка?  (Where's the Toy Car?)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.01'
SOURCE_FILE = 'sources/domashniy-arest/s01/e01.ru.dual.srt'
INTRO = "We're still in the nineteen eighties, in the same communal flat. Last time, Vanya's father came home from Hungary with gum, markers and a toy car, and told him to share everything; little Arkady only watched. Now Arkady asks Vanya for a piece of gum, and soon the toy car goes missing. We'll hear it in Russian first; don't worry about catching every word."
OPENER = "Let's go through it. The presents have been handed out, and Vanya is enjoying himself in front of Arkady."
TRANSITION = "Here's the whole scene once more."
OUTRO = "That's the promise little Arkady makes, and thirty years later he will get his chance. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('samson', 'Ну что, очкарик? Видишь, ничего не осталось.', "Well, four-eyes? See, there's nothing left.", [(84, 'видишь, ничего не осталось')], "cue 83 'Ну, че, очканак?' -> 'Ну что, очкарик?' (the mild school taunt for a child in glasses)"),
    ('arkady', 'У тебя же есть ещё. Дай хоть одну.', "But you've still got some. Give me just one.", [(85, 'У тебя же есть еще'), (86, 'Дай хоть одну')], ''),
    ('samson', 'Нет. Это моё.', "No. That's mine.", [(87, 'Это')], "'Это НЗ' (my emergency reserve, an abbreviation) -> 'Это моё'; 'Нет' new"),
    ('arkady', 'Жадина!', 'Greedy!', [], "Arkady's reaction to the refusal"),
    ('samson', 'Видишь фломастеры? Это Япония!', "See the markers? They're from Japan!", [(88, 'видишь'), (92, 'это Япония')], "cue 88 'фломики' (slang) -> фломастеры; said to a girl in the source"),
    ('samson', 'А где машинка? Где моя машинка?', "Hey, where's the toy car? Where's my toy car?", [(93, 'машинка')], "'А машинка-то где?' -> standard word order; repeated question new"),
    ('samson', 'Очкарик! Держи его!', 'Four-eyes! Grab him!', [(94, 'Держи его')], "'Очканав' (garbled) -> 'Очкарик'"),
    ('arkady', 'Пусти!', 'Let go!', [(96, 'Пусти')], ''),
    ('samson', 'Ну что, попался?', "Well, well, caught you, didn't we?", [(95, 'Ну что, попался')], ''),
    ('arkady', 'Я только посмотрел!', 'I was only looking!', [], "Arkady wanted to look at the presents: cue 65 'А можно я пойду посмотрю?', cue 67 'Я сам посмотрю'"),
    ('samson', 'Смотрите, какой у нас грязный унитаз!', 'Look, how dirty our toilet is!', [(99, 'смотрите'), (100, 'у нас')], "cue 100 'у нас какой унитаз грязный': word order made standard"),
    ('samson', 'Надо его помыть!', 'It needs a wash!', [(101, 'Надо')], "'Надо бы протереть' (it ought to be wiped) -> 'Надо его помыть'"),
    ('arkady', 'Ты ещё пожалеешь!', "You'll be sorry!", [(105, 'ты еще пожалеешь')], "insult 'Дебил' dropped"),
    ('samson', 'Да ну? Когда?', 'Oh yeah? When?', [(106, 'Да ну, когда')], ''),
    ('arkady', 'Когда вырасту, ты будешь просить у меня прощения!', "When I grow up, you'll be begging me to forgive you!", [(107, 'Когда вырасту')], "the crude rest of cue 107 retold cleanly: 'you'll beg me to forgive you'"),
    ('samson', 'Что ты сказал?', 'What did you say?', [(108, 'Что ты сказал')], ''),
]
WALK = [
    (0, 'Ну что, очкарик?', "'Well, four-eyes?' \"Ochkarik\" comes from \"ochki\" ('glasses'), a classic schoolyard taunt for a kid in specs. Then Vanya shows his empty hands."),
    (0, 'Видишь, ничего не осталось.', "'See, there's nothing left.' Literally, 'nothing didn't remain': in Russian, \"nichego\" ('nothing') always pairs with \"ne\" ('not'). Arkady knows that isn't true."),
    (1, 'У тебя же есть ещё.', "'But you've still got some.' Literally, 'at you there is more', with tiny \"zhe\" adding an insistent 'but you clearly do!'. Then he asks."),
    (1, 'Дай хоть одну.', "'Give me just one.' \"Day\" asks someone casually to hand something over, and \"khot odnu\" pleads for 'at least one'. The answer is short."),
    (2, None, "'No. That's mine.' \"Moyo\" is 'mine' when talking about things in general, even though his father told him to share. Arkady has one word for that."),
    (3, None, "'Greedy!' \"Zhadina\" is what Russian kids shout at anyone who won't share. Vanya doesn't care, and shows off his markers."),
    (4, None, "'See the markers? They're from Japan!' Literally, 'this is Japan' — \"eto Yaponiya\" — which is how a boy boasts about foreign treasure. Suddenly something goes missing."),
    (5, None, "'Hey, where's the toy car? Where's my toy car?' \"Moya\" ends in '-ya' to match \"mashinka\", since cars are feminine in Russian. Right then Vanya spots Arkady."),
    (6, None, "'Four-eyes! Grab him!' \"Derzhi\" is the very same 'hold' Vanya's dad used when handing over gum, except \"derzhi yego!\" means 'hold him — grab him!'. Arkady struggles."),
    (7, None, "'Let go!' \"Pusti!\" is the sharp one-word order to release someone. Vanya grins."),
    (8, None, "'Well, well, caught you, didn't we?' \"Popalsya\" packs 'you got caught!' into a single word. Arkady tries to explain."),
    (9, None, "'I was only looking!' \"Tolko\" means 'only' or 'just', and \"posmotrel\" has no '-a' on the end for a male speaker; a girl would say \"posmotrela\". Vanya gets a nasty idea."),
    (10, None, "'Look, how dirty our toilet is!' \"Smotrite\" adds '-te' onto \"smotri\" because Vanya is calling to all the kids at once. Then he adds something."),
    (11, None, "'It needs a wash!' \"Nado\" means 'it's needed' or 'we ought to', and you'll hear it in almost every Russian conversation. What happens next is cruel: the boys dunk Arkady's head into the toilet bowl, and afterwards he makes a threat."),
    (12, None, "'You'll be sorry!' \"Yeshchyo pozhaleyesh\" literally warns 'you will still regret it!'. Vanya just laughs at him."),
    (13, None, "'Oh yeah? When?' \"Da nu?\" is a scoffing two-word comeback for 'oh really, come off it?'. Arkady answers."),
    (14, None, "'When I grow up, you'll be begging me to forgive you!' Where English uses present in 'when I grow up', Russian uses future \"kogda vyrastu\" — 'when I will grow up'. Remember this line, because the whole series turns on it."),
    (15, None, "'What did you say?' \"Chto ty skazal?\" puts 'what' first and needs no helper like 'did' at all."),
]
