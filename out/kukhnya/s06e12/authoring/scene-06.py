# Authoring module for kukhnya-s06e12-scene-06.
ID = 'kukhnya-s06e12-scene-06'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 12
SCENE = 6
TITLE = "Подарок для Насти и переезд Лёвы  (A Gift for Nastya and Lyova's Move)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'kostya': 'Костя', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.12'
SOURCE_FILE = 'sources/kukhnya/s06/e12.ru.srt'
INTRO = "At the bar, Kostya explains that tomorrow is his wedding anniversary with Nastya and asks Denis to buy a forty-thousand-ruble ring using the fifty-percent personal discount. That evening, Lyova moves back into his mother's apartment, where she uses superstitions to keep him inside."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "While Lyova is trapped inside his mother's apartment, Denis buys the discounted ring for Kostya—unaware that Marina is reporting the purchase straight to Sveta. See you next time!"
CLOSING = ('denis', 'До завтра!')
STORY = [
    ('denis', 'Ты предлагаешь мне из-за этой скидки жениться?', 'Are you suggesting I get married because of this discount?', [(90, 'Предлагаешь из-за этого жениться')], 'adapted'),
    ('kostya', 'Нет, просто у нас с Настей завтра годовщина.', 'No, it is just that Nastya and I have our anniversary tomorrow.', [(90, 'Нет, это я о своем'), (91, 'Просто у нас с Настей завтра годовщина')], 'adapted'),
    ('kostya', 'И я как раз думаю, что ей подарить.', 'And I am just thinking about what to give her.', [(92, 'Я как раз думаю, что ей подарить')], 'adapted'),
    ('kostya', 'Смотри, вот это красивое кольцо за сорок тысяч.', 'Look, here is this beautiful ring for forty thousand.', [(93, 'Вот это')], 'adapted'),
    ('kostya', 'Со скидкой будет двадцать тысяч, я его беру.', 'With the discount it will be twenty thousand, I am taking it.', [(94, 'Я беру')], 'adapted'),
    ('kostya', 'Точнее, ты его берёшь, ведь скидка твоя.', 'More precisely, you are buying it, since the discount is yours.', [(95, 'Ты, точнее, берешь'), (96, 'Скидка же твоя')], 'adapted'),
    ('denis', 'Ладно, договорились, я сегодня вечером туда заеду.', 'Alright, deal, I will stop by there this evening.', [(97, 'Ладно, я сегодня вечером заеду')], 'adapted'),
    ('lyova', 'Мама, я принёс вещи, прости меня за ссору.', 'Mom, I brought my things, forgive me for the quarrel.', [(99, 'Прости')], 'adapted'),
    ('kostya', 'Как хорошо, что ты снова дома, сынок.', 'How good it is that you are home again, son.', [(98, 'Хорошо, что ты снова дома')], 'adapted'),
    ('kostya', 'Лёва, подожди, ты куда это вечером собрался?', 'Lyova, wait, where are you heading off to in the evening?', [(100, 'ты что, куда-то собрался')], 'adapted'),
    ('lyova', 'Мама, я только быстро пойду мусор вынесу.', 'Mom, I will just quickly go take out the trash.', [(101, 'Мам, пойду мусор вынесу')], 'adapted'),
    ('kostya', 'Вечером мусор выносить — плохая примета, вынесешь завтра!', 'Taking out trash in the evening is a bad omen, take it out tomorrow!', [(102, 'плохая примета'), (103, 'Вынесешь завтра')], 'adapted'),
]
WALK = [
    (0, None, '\'Are you suggesting I get married because of this discount?\' Denis challenges wryly at this point, using "predlagayesh" (from "predlagat", "are suggesting") alongside "skidki" ("discount") to shape the meaning.'),
    (1, None, '\'No, it is just that Nastya and I have our anniversary tomorrow.\' Kostya picks a measured course in the room, putting "prosto" ("just") alongside "zavtra" ("tomorrow") in a tight, everyday turn of phrase.'),
    (2, None, '\'And I am just thinking about what to give her.\' Kostya shows a clear stance for Denis, combining "kak" ("how") and "raz" ("time, once") so the key meaning lands right away.'),
    (3, None, '\'Look, here is this beautiful ring for forty thousand.\' Kostya strikes a resolute approach at once, using "smotri" (from "smotret", "look") alongside "krasivoye" ("beautiful") to shape the meaning.'),
    (4, None, '\'With the discount it will be twenty thousand, I am taking it.\' Kostya shows an emphatic style straight away, linking "skidkoy" ("discount"), "budet" ("will be"), and "tysyach" ("thousand") in one brisk exchange.'),
    (5, None, '\'More precisely, you are buying it, since the discount is yours.\' Kostya takes a sharp note in the scene, using "tochneye" (from "tochno", "definitely") alongside "beryosh" ("do you take") to shape the meaning.'),
    (6, None, '\'Alright, deal, I will stop by there this evening.\' Denis keeps a grounded tempo in the conversation, putting "dogovorilis" ("agreed, deal") alongside "segodnya" ("today") in a tight, everyday turn of phrase.'),
    (7, None, '\'Mom, I brought my things, forgive me for the quarrel.\' Lyova adopts a warm manner for Kostya, anchoring the Russian line on "mama" ("mum, mother") and "prinyos" ("brought") without extra filler.'),
    (8, None, '\'How good it is that you are home again, son.\' Kostya establishes a pointed angle in this beat, joining "kak" ("how") to "khorosho" ("good, fine") so every word pulls its weight.'),
    (9, None, '\'Lyova, wait, where are you heading off to in the evening?\' Kostya quizzes frankly without a pause, anchoring the Russian line on "podozhdi" ("wait") and "kuda" ("where to") without extra filler.'),
    (10, None, '\'Mom, I will just quickly go take out the trash.\' Lyova projects a clear manner straight away, anchoring the Russian line on "mama" ("mum, mother") and "tolko" ("only") without extra filler.'),
    (11, None, '\'Taking out trash in the evening is a bad omen, take it out tomorrow!\' Kostya displays a sharp tempo on the spot, combining "vecherom" ("in the evening") and "musor" ("rubbish") so the key meaning lands right away.'),
]
