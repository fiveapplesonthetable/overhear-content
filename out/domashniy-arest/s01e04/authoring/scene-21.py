# Authoring module for domashniy-arest-s01e04-scene-21.
ID = 'domashniy-arest-s01e04-scene-21'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 4
SCENE = 21
TITLE = 'Задание для адвоката  (A Task for the Lawyer)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'golovkin': 'Головкин'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.04'
SOURCE_FILE = 'sources/domashniy-arest/s01/e04.ru.dual.srt'
INTRO = "Out in the corridor of the communal flat, a moment later. Last time, Arkady stopped Klavdia Viktorovna from giving her phone to Ilona by promising her a cemetery plot beside her late husband Grisha. Now Arkady pulls his nervous lawyer Danila Golovkin into the hallway to explain how to buy that plot from the cemetery administrator. Let's listen in Russian first."
OPENER = "Let's take the conversation line by line. Arkady leads Golovkin out into the hallway to give him his instructions."
TRANSITION = "Let's listen to the whole scene again from start to finish."
OUTRO = 'So poor Golovkin is off to the cemetery with another hundred and fifty thousand roubles of his own savings, all for the sake of seeing Nina in the corridor. Great job following that scene in Russian. See you next time!'
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('arkady', 'Данила, пойдём. Смотри, ничего сложного.', "Danila, let's go. Look, there's nothing complicated.", [(825, 'Данила, пойдем'), (826, 'Смотри'), (826, 'ничего сложного')], ''),
    ('arkady', 'Там на кладбище центральный вход.', 'There at the cemetery is the main entrance.', [(826, 'Там на кладбище центральный вход')], ''),
    ('arkady', 'Входишь сразу налево, к администратору. Там сидит такой Лисицын.', 'You go in and turn straight left, to the administrator. A fellow named Lisitsyn sits there.', [(827, 'Входишь сразу налево, к администратору'), (828, 'Там'), (828, 'лисицын такой сидит')], "'мордатый' dropped"),
    ('arkady', 'Он тебе сразу грубо скажет: мест нет, уходите.', "He'll tell you rudely right away: there are no plots, go away.", [(829, 'Он тебе сразу грубо'), (829, 'скажет, мест нет, уходите')], "'так' dropped"),
    ('arkady', 'А ты скажи: куда же я пойду? Понимаешь?', 'And you say: where am I supposed to go? Understand?', [(830, 'А ты'), (830, 'куда же я пойду'), (831, 'Понимаешь')], "'ему,' -> 'скажи:'"),
    ('arkady', 'А сам конверт ему двигай. И главное, в глаза ему смотри.', 'And slide the envelope over to him yourself. And above all, look him in the eyes.', [(832, 'А сам конверт ему'), (833, 'И главное, в глаза ему'), (833, 'смотри')], "'пододвигай' -> 'двигай'; 'так' dropped"),
    ('golovkin', 'А по-моему, это гадость! Я не буду давать взятку.', "In my opinion, this is disgusting! I won't pay a bribe.", [(835, 'А')], "garbled cue 835 ('А я мне мерзость') retold cleanly at A1"),
    ('arkady', 'Пошёл вон! Ты больше не мой адвокат.', "Get out! You're no longer my lawyer.", [(836, 'Пошел вон'), (837, 'Ты больше не мой адвокат')], ''),
    ('arkady', 'И Нину свою ты больше не увидишь!', "And you'll never see your Nina again!", [(838, 'И Нину свою ты больше не увидишь')], ''),
    ('golovkin', 'Согласен! Согласен!', 'I agree! I agree!', [(839, 'Согласен'), (840, 'Согласен')], ''),
    ('arkady', 'Тогда смотри. В конверте должно быть сто пятьдесят тысяч.', 'Then listen. There must be a hundred and fifty thousand in the envelope.', [(841, 'Тогда смотри'), (842, 'В конверте должно быть'), (842, 'тысяч')], "'150' written out as 'сто пятьдесят'"),
    ('golovkin', 'Вы пользуетесь моей слабостью!', "You're taking advantage of my weakness!", [(844, 'мой')], "garbled cue 844 ('Пользуйтесь, мой слабый') restored"),
    ('arkady', 'Конечно, пользуюсь. Это шантаж.', "Of course I am. It's blackmail.", [(845, 'Конечно, пользуюсь. Это шантаж')], ''),
    ('arkady', 'Давай, Даня, иди. Действуй!', 'Come on, Danya, go. Get to work!', [(846, 'Давай'), (847, 'Иди. Действуй')], "'Данечка' -> 'Даня'; 'злодействуй' dropped"),
]
WALK = [
    (0, None, "'Danila, let's go. Look, there's nothing complicated.' After 'nothing', the adjective takes the 'of'-form ending: 'nothing of complicated'."),
    (1, None, "'There at the cemetery is the main entrance.' After 'at', the word for 'cemetery' is in the location form."),
    (2, None, "'You go in and turn straight left, to the administrator. A fellow named Lisitsyn sits there.' Russian uses the present tense 'you go in' to give step-by-step directions, just like English."),
    (3, None, "'He'll tell you rudely right away: there are no plots, go away.' With 'there are no', the word for 'places' takes the plural 'of' form, which has no ending at all."),
    (4, None, "'And you say: where am I supposed to go? Understand?' That helpless question is the signal that you are ready to pay."),
    (5, None, "'And slide the envelope over to him yourself. And above all, look him in the eyes.' Literally, 'and yourself move the envelope to him'. Honest Golovkin is horrified."),
    (6, None, "'In my opinion, this is disgusting! I won't pay a bribe.' Literally, 'to give a bribe'. Arkady doesn't argue; he simply pulls the lever he has over the lovesick lawyer."),
    (7, None, "'Get out! You're no longer my lawyer.' Literally, 'no more my lawyer'."),
    (8, None, "'And you'll never see your Nina again!' Because Golovkin only comes to the flat to catch a glimpse of his childhood sweetheart Nina, he caves in within half a second."),
    (9, None, "'I agree! I agree!' The short masculine form matches a male speaker. Arkady doesn't miss a beat."),
    (10, None, "'Then listen. There must be a hundred and fifty thousand in the envelope.' And of course, since Arkady has no money, Golovkin has to pay that out of his own pocket too."),
    (11, None, "'You're taking advantage of my weakness!' The verb for 'making use of' takes the 'with/as' form: 'with my weakness'. Arkady grins."),
    (12, None, "'Of course I am. It's blackmail.' He admits it cheerfully."),
    (13, None, "'Come on, Danya, go. Get to work!' The last command literally means 'act!' or 'take action!'."),
]
