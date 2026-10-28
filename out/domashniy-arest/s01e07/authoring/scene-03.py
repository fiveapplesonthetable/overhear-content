# domashniy-arest/s01e07/scene-03.py
ID = "domashniy-arest-s01e07-scene-03"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 3
TITLE = "Все говорят, а я делаю  (Everyone Talks, I Act)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.07"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"
VOICES = {"narrator": "sky", "ilona": "angelina", "samson": "anja"}
LABELS = {"ilona": "Илона", "samson": "Самсон"}
INTRO = "Meanwhile on a residential courtyard street, campaign strategist Ilona directs a television report as candidate Ivan Samsonov personally paves a pothole with a heavy hand roller, until a passing driver stops to complain about the uneven asphalt. Let's listen in Russian first."
STORY = [
    ("ilona", "Мы ведём наш репортаж с улицы Красноармейской.", "We are broadcasting our report from Krasnoarmeyskaya Street.", [(101, 'Мы ведем наш репортаж с улицы')], "cue 101 TV reporter folded into Ilona's role; garbled 'Кристофорнейская' -> 'Красноармейской'"),
    ("ilona", "Кандидат Иван Самсонов вышел во двор. Он сегодня сам закатал старую яму!", "Candidate Ivan Samsonov came out into the courtyard. Today he paved over an old pothole himself!", [(102, 'кандидат'), (102, 'Иван Самсонов сегодня'), (102, 'закатал яму'), (105, 'во дворе')], "'собственноручно' -> 'сам'"),
    ("ilona", "Дорожная служба обещала закатать её десять лет назад.", "The road service promised to pave it over ten years ago.", [(103, 'службе обещали закатать еще'), (103, 'лет назад')], "cue 103 garbled 'на подорожной службе' -> 'Дорожная служба'; '10' -> 'десять'"),
    ("ilona", "Иван, ваши конкуренты проводят встречи и дают обещания.", "Ivan, your rivals hold meetings and make promises.", [(104, 'Иван'), (104, 'ваши конкуренты проводят встречи, дают обещания')], ""),
    ("ilona", "А вы сегодня закатали яму во дворе. Вы не зря тратите время?", "And today you paved a pothole in a courtyard. Aren't you wasting your time in vain?", [(105, 'а вы сегодня закатали яму во дворе'), (106, 'тратите время')], "cue 106 garbled 'в фокусе тратите время' -> 'не зря тратите время'"),
    ("samson", "А что болтать? Все говорят, а я делаю!", "What is the point of chattering? Everyone talks, and I act!", [(107, 'А что болтать'), (108, 'Все говорят, а я делаю')], ""),
    ("ilona", "Стоп, снято! Молодец, Самсон!", "Stop, that's a wrap! Good job, Samson!", [(110, 'Стоп'), (111, 'Молодец')], "cue 111 garbled 'Сансон' -> 'Самсон'"),
    ("samson", "Эй, я вот тут машину чуть не сломал!", "Hey, I almost broke my car right here!", [(112, 'Я вот тут')], "cue 112 slang 'ходовую убил' simplified to 'машину чуть не сломал'"),
    ("samson", "Ты вон там неровно положил! Там теперь лужица будет!", "You laid it unevenly over there! Now there will be a little puddle there!", [(113, 'Вон там неровно положил, лужица будет')], ""),
    ("samson", "Лужица?! Я тобой сейчас эту лужицу заровняю! Понял?", "A little puddle?! I will level out that puddle with you right now! Understood?", [(114, 'Лужица'), (115, 'Я тобой сейчас эту лужицу'), (116, 'Понял')], "cue 115 spelling 'заравняю' -> 'заровняю'"),
    ("samson", "Я за тебя голосовать не буду! Ухожу отсюда!", "I am not going to vote for you! I am leaving here!", [(117, 'Я за тебя'), (117, 'не буду')], "cue 117 garbled 'танцевать' -> 'голосовать'; cue 118 'И пошел нахрен' cleaned to 'Ухожу отсюда!'"),
    ("samson", "А я буду! Ну, Илона, что дальше?", "Well, I will! So, Ilona, what is next?", [(119, 'А я буду'), (122, 'Ну что дальше')], ""),
    ("ilona", "Ну всё, рабочие могут забирать свой валик.", "All right, the workers can take their roller back.", [(120, 'Ну все, можете забирать свой валик')], ""),
    ("ilona", "Всё отлично, отдыхай! Сегодня выходные, всё круто!", "Everything is great, get some rest! It is the weekend today, everything is cool!", [(123, 'Все отлично, отдыхай'), (125, 'Выходные, все круто')], ""),
]
OPENER = "Now let's break down Samsonov's campaign shoot in the courtyard line by line. The television camera rolls as the report begins."
WALK = [
    (0, None, "'We are broadcasting our report from Krasnoarmeyskaya Street.' Literally 'we lead our report from the street', with the street name in the 'of' form."),
    (1, 'Кандидат Иван Самсонов вышел во двор.', "'Candidate Ivan Samsonov came out into the courtyard.' Notice the direct-object form after 'into' for motion."),
    (1, 'Он сегодня сам закатал старую яму!', "'Today he paved over an old pothole himself!' The emphatic pronoun means 'himself' or 'with his own hands'."),
    (2, None, "'The road service promised to pave it over ten years ago.' With numbers from five upward, 'years' takes the special plural 'of' form form."),
    (3, None, "'Ivan, your rivals hold meetings and make promises.' Both plural verbs are in the present tense."),
    (4, 'А вы сегодня закатали яму во дворе.', "'And today you paved a pothole in a courtyard.' Here 'in the courtyard' is stationary, so it takes the location form."),
    (4, 'Вы не зря тратите время?', "'Aren't you wasting your time in vain?' The short adverb means 'in vain' or 'for nothing'."),
    (5, 'А что болтать?', "'What is the point of chattering?' An action verb question dismissing empty talk."),
    (5, 'Все говорят, а я делаю!', "'Everyone talks, and I act!' Samson delivers the punchy campaign slogan Ilona wrote for him."),
    (6, None, "'Stop, that's a wrap! Good job, Samson!' Literally 'stop, filmed!' — the standard director's call when a take is finished."),
    (7, None, "'Hey, I almost broke my car right here!' A passing driver stops by the fresh patch of asphalt; 'almost' is expressed with 'barely not' plus a past verb."),
    (8, 'Ты вон там неровно положил!', "'You laid it unevenly over there!' The adverb comes from 'not-even'."),
    (8, 'Там теперь лужица будет!', "'Now there will be a little puddle there!' He uses the diminutive of 'puddle'."),
    (9, None, "'A little puddle?! I will level out that puddle with you right now! Understood?' Samson forgets the cameras and threatens to use the driver as a roller, putting 'you' in the 'with/as' form."),
    (10, None, "'I am not going to vote for you! I am leaving here!' The compound ongoing-action form future is formed with 'I will not' plus the basic verb form 'to vote'."),
    (11, None, "'Well, I will! So, Ilona, what is next?' Samson shouts back like a schoolboy and asks Ilona for his next assignment."),
    (12, None, "'All right, the workers can take their roller back.' The real road crew had lent Samson their hand roller for the camera shot."),
    (13, None, "'Everything is great, get some rest! It is the weekend today, everything is cool!' The plural noun for 'days off' means 'the weekend'."),
]
TRANSITION = "Now let's listen to the whole courtyard scene again from beginning to end."
OUTRO = "Samsonov's campaign slogan is 'Everyone talks, I act' — even if he threatens to flatten voters into the fresh asphalt. See you next time!"
CLOSING = ("samson", "Пока!")
