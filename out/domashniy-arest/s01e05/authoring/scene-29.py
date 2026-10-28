# Authoring module for domashniy-arest-s01e05-scene-29.
ID = 'domashniy-arest-s01e05-scene-29'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 5
SCENE = 29
TITLE = 'Любая обезьяна выиграет  (Any Monkey Could Win)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'governor': 'Губернатор', 'pasha': 'Паша'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.05'
SOURCE_FILE = 'sources/domashniy-arest/s01/e05.ru.dual.srt'
INTRO = "Late at night in Pasha's office and at the governor's steam bath. Meanwhile, regional governor Viktor Stepanovich has seen the TV news turning Samson's crash at the Society of the Blind into a heroic drug bust, and he calls Pasha from the steam bath. Let's listen in Russian first."
OPENER = "Let's take the scene line by line. Pasha answers the governor's phone call at his desk."
TRANSITION = "Now let's hear the whole scene once more, start to finish."
OUTRO = "So while the governor is whipped with birch branches in the steam bath, Pasha has to hold the receiver tightly to his ear and admit that he is only slightly better than a monkey. Next time, in our final scene of the episode, Marina comes to Arkady's room late at night to thank him. See you then. See you next time!"
CLOSING = ('pasha', 'Пока!')
STORY = [
    ('pasha', 'Да, Виктор Степанович, слушаю вас.', "Yes, Viktor Stepanovich, I'm listening to you.", [(1110, 'Да, Виктор Степанович, слушаю вас')], ''),
    ('governor', 'Я тебя предупреждал! Ты опять всё проиграл!', 'I warned you! You lost everything again!', [(1111, 'Я тебя предупреждал'), (1112, 'Ты опять все')], "crude insults in 1111-1116 omitted; 'слил' -> 'проиграл'"),
    ('governor', 'Я даже лицо твоё сейчас представляю! Ты слышишь меня или нет?', 'I can even picture your face right now! Do you hear me or not?', [(1115, 'Я даже'), (1115, 'сейчас твою представляю'), (1117, 'Слышишь меня, нет')], "'рожу... Похожую на жопу' (1115-1116) -> 'лицо твоё'"),
    ('pasha', 'Слушаю, Виктор Степанович, слушаю вас.', "I'm listening, Viktor Stepanovich, I'm listening to you.", [(1118, 'Слушаю, Виктор Степанович, слушаю вас')], ''),
    ('governor', 'Слушай, не делай мне одолжения здесь!', "Listen, don't do me a favour here!", [(1119, 'Слушай, не делай мне одолжения здесь')], ''),
    ('pasha', 'Я не делаю.', "I'm not doing that.", [(1120, 'Я не делаю')], 'crude lines 1121-1122 omitted'),
    ('governor', 'Любая обезьяна эти выборы выиграет! Ты что, хуже обезьяны?', 'Any monkey will win this election! What, are you worse than a monkey?', [(1123, 'Любая обезьяна эти выборы выиграет'), (1124, 'Ты что, хуже обезьяны')], ''),
    ('pasha', 'Нет, я лучше обезьяны.', "No, I'm better than a monkey.", [(1125, 'Нет, я лучше обезьяны')], ''),
    ('governor', 'Ты что там сейчас? Ты со мной шутишь, что ли?', 'What are you doing over there now? Are you joking with me, or what?', [(1126, 'ты'), (1126, 'там сейчас'), (1128, 'Ты со мной'), (1128, 'что ли')], "'ёрничаешь' -> 'шутишь'"),
    ('pasha', 'Нет, я не шучу, Виктор Степанович.', "No, I'm not joking, Viktor Stepanovich.", [(1129, 'Нет, я не'), (1129, 'Виктор Степанович')], "'не ёрничаю' -> 'не шучу'"),
    ('governor', 'Вот и не надо со мной сейчас шутить!', "Then don't joke with me right now!", [(1130, 'Вот и не надо со мной'), (1130, 'сейчас')], "crude insults in 1131-1134 omitted; 'ёрничать' -> 'шутить'"),
    ('governor', 'Тебе ничего нельзя доверить! Ты слушаешь меня?', "You can't be trusted with anything! Are you listening to me?", [(1133, 'доверить'), (1135, 'Ты слушаешь меня')], "clean A1 for 1133-1134 'Что-нибудь просрать, доверить, ты и это просрешь'"),
    ('pasha', 'Слушаю.', "I'm listening.", [(1136, 'Слушаю')], ''),
    ('governor', 'Что слушаешь? Ты по громкой связи со мной говоришь?', 'What do you mean, listening? Are you talking to me on speakerphone?', [(1137, 'Что слушаешь'), (1138, 'Ты'), (1138, 'по громкой связи со мной говоришь')], "'чё там' dropped"),
    ('governor', 'Быстро возьми трубку в руки! Трубку!', 'Quickly take the receiver in your hands! The receiver!', [(1139, 'быстро трубку в руки'), (1140, 'Трубку')], "'А ну-ка взял быстро' -> 'Быстро возьми'"),
    ('pasha', 'Я слушаю возле уха.', "I'm listening right by my ear.", [(1141, 'Я слушаю возле уха')], 'crude lines 1142-1143 omitted'),
    ('governor', 'Ты что, паришься? Сильнее давай!', 'What, are you steaming yourself? Harder, come on!', [(1144, 'Ты что')], "garbled 'пробуешь' -> 'паришься'; 'Сильнее давай!' to bath attendant"),
    ('pasha', 'Да, Виктор Степанович.', 'Yes, Viktor Stepanovich.', [(1145, 'Да')], ''),
]
WALK = [
    (0, None, "'Yes, Viktor Stepanovich, I'm listening to you.' Pasha uses his most respectful tone. On the other end of the line, the governor is sitting in a hot steam bath and shouting."),
    (1, None, "'I warned you! You lost everything again!' Earlier in the episode the governor warned Pasha to watch out for Ilona, and now Ilona has turned Pasha's Blind Society trap into a triumph for Samson."),
    (2, 'Я даже лицо твоё сейчас представляю!', "'I can even picture your face right now!' In the show the governor adds a string of unprintable comparisons."),
    (2, 'Ты слышишь меня или нет?', "'Do you hear me or not?' In this moment, Pasha sits stiffly at his desk, speaking into the speakerphone."),
    (3, None, "'I'm listening, Viktor Stepanovich, I'm listening to you.' His tired tone only makes the governor angrier."),
    (4, None, "'Listen, don't do me a favour here!' The noun for 'a favour' is in the 'of' form after the negative command."),
    (5, None, "'I'm not doing that.' Then the governor sums up the whole election."),
    (6, 'Любая обезьяна эти выборы выиграет!', "'Any monkey will win this election!' With all the administrative resources of city hall, winning should be automatic. So he asks Pasha a pointed question."),
    (6, 'Ты что, хуже обезьяны?', "'What, are you worse than a monkey?' After the comparative word 'worse', 'monkey' takes the 'of'-form ending 'than a monkey'. Pasha answers literally."),
    (7, None, "'No, I'm better than a monkey.' That sounds suspiciously like backtalk to the governor."),
    (8, 'Ты со мной шутишь, что ли?', "'What are you doing over there now? Are you joking with me, or what?' In the show he uses a colourful Russian verb meaning 'are you being cheeky with me?' Pasha quickly backs down."),
    (9, None, "'No, I'm not joking, Viktor Stepanovich.' Notice how the consonant in 'joke' changes to a 'ch' sound in the 'I' form."),
    (10, None, "'Then don't joke with me right now!' Literally, 'there, and one must not joke with me now'."),
    (11, 'Тебе ничего нельзя доверить!', "'You can't be trusted with anything! Are you listening to me?' Literally, 'to you nothing is possible to entrust'."),
    (12, None, "'I'm listening.' Suddenly the governor notices the echo on the line."),
    (13, 'Ты по громкой связи со мной говоришь?', "'What do you mean, listening? Are you talking to me on speakerphone?' Literally, 'by loud connection' — the standard Russian phrase for speakerphone."),
    (14, 'Быстро возьми трубку в руки!', "'Quickly take the receiver in your hands! The receiver!' Even when nobody is in the room, Pasha isn't allowed the dignity of speakerphone. Pasha scrambles to pick up the handset."),
    (15, None, "'I'm listening right by my ear.' After the preposition 'near' or 'right by', 'ear' takes the 'of'-form ending. Then the governor turns to his bath attendant, who is whipping his back with birch branches."),
    (16, None, "'What, are you steaming yourself? Harder, come on!' While the bath attendant beats the governor with leafy birch branches, Pasha has to hold the receiver pressed to his ear and listen to every slap and grunt."),
    (17, None, "'Yes, Viktor Stepanovich.' Humiliated in his own mayor's chair, Pasha can only say yes."),
]
