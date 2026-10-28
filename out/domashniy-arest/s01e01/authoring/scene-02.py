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
    (0, 'Ну что, очкарик?', "'Well, four-eyes?' The word is a schoolyard name for a child in glasses, and it's what Vanya always calls him. Then he shows his empty hands."),
    (0, 'Видишь, ничего не осталось.', "'See, there's nothing left.' Literally, 'nothing didn't remain': in Russian, 'nothing' comes with a 'not' as well. Arkady knows that isn't true."),
    (1, 'У тебя же есть ещё.', "'But you've still got some.' Literally, 'at you there is more'. It's the same pattern as 'I have', just with 'you'. Then he asks."),
    (1, 'Дай хоть одну.', "'Give me just one.' The first word is a command: give. The answer is short."),
    (2, None, "'No. That's mine.' Remember, his father told him to share with everyone. Arkady has one word for that."),
    (3, None, "'Greedy!' It's what children shout at someone who won't share. Vanya doesn't care, and shows off his markers."),
    (4, None, "'See the markers? They're from Japan!' Literally, 'this is Japan', which is how a boy boasts. But then something goes missing."),
    (5, None, "'Hey, where's the toy car? Where's my toy car?' The word for 'my' ends in an 'a' to match the car, which is feminine. And then Vanya spots Arkady."),
    (6, None, "'Four-eyes! Grab him!' The verb is the one Dad used when he handed the gum over, 'hold', but here it means 'catch him'. Arkady struggles."),
    (7, None, "'Let go!' A command again, a short one. Vanya grins."),
    (8, None, "'Well, well, caught you, didn't we?' One verb in the past tense says it all. Arkady tries to explain."),
    (9, None, "'I was only looking!' He just wanted to see the car. The verb ends in a plain consonant because Arkady is a boy; a girl would add an 'a'. Vanya has a nasty idea."),
    (10, None, "'Look, how dirty our toilet is!' The word for 'look' ends in the plural, because he's talking to all the children around him. Then he adds something."),
    (11, None, "'It needs a wash!' The first word means 'it is necessary', and you'll hear it everywhere. What happens next is cruel: the boys push Arkady's head into the shared toilet bowl. Afterwards, wet and angry, he makes a threat."),
    (12, None, "'You'll be sorry!' Right then, Vanya just laughs at him."),
    (13, None, "'Oh yeah? When?' The first two words together mean 'oh, really?', said with scorn. And Arkady answers."),
    (14, None, "'When I grow up, you'll be begging me to forgive you!' Both verbs point to the future: 'when I grow up', and 'you will be asking'. Remember this line, because the whole series is about this promise."),
    (15, None, "'What did you say?' The verb ends in a plain consonant again, because the 'you' he's asking is Arkady, a boy."),
]
