ID = 'kukhnya-s03e07-scene-09'
SHOW = "kukhnya"
SEASON = 3
EPISODE = 7
SCENE = 9
TITLE = 'Журналист и таракан  (The Journalist and the Cockroach)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'guest': 'anja'}
LABELS = {'anya': 'Шеф', 'guest': 'Гость'}
SOURCE_NAME = "Кухня (Kukhnya) S3.07"
SOURCE_FILE = 'sources/kukhnya/s03/e07.ru.srt'

INTRO = "Chef Barinov approaches the guest's table and pretends not to see any cockroach. The diner warns that he is a journalist and is about to photograph the plate for all of Moscow."

STORY = [
    ('anya', 'Добрый день, я шеф-повар ресторана.', 'Good afternoon, I am the head chef of the restaurant.', [(118, 'Добрый день. Я шеф-повар')], 'adapted'),
    ('anya', 'Скажите, это вы меня сейчас звали?', 'Tell me, was it you who called for me just now?', [(119, 'Вы меня звали')], 'adapted'),
    ('guest', 'Да, звал, я у себя в тарелке нашёл таракана.', 'Yes, I called, I found a cockroach in my plate.', [(120, 'Я у себя в тарелке нашел таракан')], 'adapted'),
    ('guest', 'Вы понимаете, что я могу вас за это засудить?', 'Do you understand that I can sue you for this?', [(121, 'Вы понимаете, что я могу вас за это засудить')], 'adapted'),
    ('anya', 'Я вас не понимаю, я не вижу тут таракана.', 'I do not understand you, I do not see a cockroach here.', [(122, 'Я вас не понимаю. Я не вижу тут таракана')], 'adapted'),
    ('guest', 'Вот как вы со мной разговариваете, да?', 'So that is how you talk to me, yes?', [(123, 'Вот как, да')], 'adapted'),
    ('guest', 'Между прочим, я известный журналист.', 'By the way, I am a well-known journalist.', [(124, 'Между прочим, я журналист')], 'adapted'),
    ('guest', 'И об этом скоро узнает вся Москва.', 'And all of Moscow will soon find out about this.', [(125, 'И об этом узнает вся Москва')], 'adapted'),
    ('guest', 'Я вам это твёрдо обещаю.', 'I firmly promise you that.', [(126, 'Я вам это обещаю')], 'adapted'),
    ('guest', 'Я сейчас собираюсь его сфотографировать.', 'Right now I am going to photograph it.', [(127, 'Я сейчас собираюсь его сфотографировать')], 'adapted'),
    ('anya', 'А, так вы говорите про это?', 'Ah, so you are talking about this?', [(128, 'А, вы про это')], 'adapted'),
    ('anya', 'Послушайте, так это вовсе не таракан.', 'Listen, this is not a cockroach at all.', [(128, 'Так это не таракан')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Good afternoon, I am the head chef of the restaurant.' Chef Barinov anchors the line on 'good', while 'restaurant' completes the thought."),
    (1, None, "'Tell me, was it you who called for me just now?' Chef Barinov anchors the line on 'say', while 'called for' completes the thought."),
    (2, None, "'Yes, I called, I found a cockroach in my plate.' the guest anchors the line on 'yes', while 'cockroach' completes the thought."),
    (3, None, "'Do you understand that I can sue you for this?' The grammar packs 'you' and 'sue' into a tight, idiomatic kitchen exchange. Chef Barinov answers right away."),
    (4, None, "'I do not understand you, I do not see a cockroach here.' Chef Barinov anchors the line on 'I', while 'cockroach' completes the thought."),
    (5, None, "'So that is how you talk to me, yes?' The grammar packs 'here' and 'yes' into a tight, idiomatic kitchen exchange."),
    (6, None, "'By the way, I am a well-known journalist.' Here the Russian phrasing highlights 'between' before landing on 'journalist'."),
    (7, None, "'And all of Moscow will soon find out about this.' the guest brings out the contrast between 'and' and 'about' in a few short words."),
    (8, None, "'I firmly promise you that.' The meaning hinges on 'I' working together with 'promise' in spoken Russian."),
    (9, None, "'Right now I am going to photograph it.' Notice the reflexive suffix on the verb meaning 'intend', turning the action back on the subject. Chef Barinov answers right away."),
    (10, None, "'Ah, so you are talking about this?' Chef Barinov anchors the line on 'and', while 'this' completes the thought."),
    (11, None, "'Listen, this is not a cockroach at all.' In Russian, the idea of 'listen' flows naturally into 'cockroach' without extra filler words."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'To stop the journalist from taking a photo, Chef Barinov has to prove on the spot that the bug on the plate is edible.'
CLOSING = ('anya', 'Так это не таракан!')
