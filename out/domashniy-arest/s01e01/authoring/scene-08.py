# Authoring module for domashniy-arest-s01e01-scene-08.
ID = 'domashniy-arest-s01e01-scene-08'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 1
SCENE = 8
TITLE = 'Кофе и кластер  (Coffee and the Cluster)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'lydia': 'Лидия Алексеевна', 'pasha': 'Паша'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.01'
SOURCE_FILE = 'sources/domashniy-arest/s01/e01.ru.dual.srt'
INTRO = "The next morning, back in the mayor's office. Last time, Arkady named a humiliating condition for the job, a silly kiss, to pay Samson back for his childhood, and Samson stormed out. Now Arkady is in a fine mood: he orders coffee, and his deputy Pasha comes in with news and a big money idea. Let's listen in Russian first."
OPENER = "Let's go through it slowly. It's a sunny morning, and Arkady is very pleased with himself."
TRANSITION = "Now let's hear the whole conversation again."
OUTRO = "And that's the morning meeting: coffee, a quick 'no', and a joke at Pasha's expense. Listen out for 'room temperature' and 'if I were you' when you watch. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('arkady', 'Какое хорошее утро! Лидия Алексеевна, чашку кофе, пожалуйста.', 'What a lovely morning! Lidia Alekseyevna, a cup of coffee, please.', [(323, 'Какое хорошее утро'), (324, 'Лидия Алексеевна'), (324, 'пожалуйста')], "'чашечку Американо' -> 'чашку кофе'"),
    ('lydia', 'Хорошо, Аркадий Борисович.', 'Of course, Arkady Borisovich.', [(325, 'Хорошо, Аркадий Борисович')], ''),
    ('pasha', 'Аркаш, можно?', 'Arkasha, may I come in?', [(326, 'Аркаш, можно')], ''),
    ('arkady', 'Заходи.', 'Come in.', [(327, 'Заходи')], ''),
    ('pasha', 'Реакция положительная. Людям нравится.', 'The reaction is positive. People like it.', [(328, 'Реакция'), (328, 'положительная')], "'на вступление' dropped; 'Людям нравится' new, after cue 329 (the voters are in a good mood)"),
    ('arkady', 'Хорошо. А что с торговым центром?', 'Good. And what about the shopping centre?', [(330, 'с торговым центром что')], "word order made standard, 'у нас' dropped, 'Хорошо' added"),
    ('pasha', 'Аракелян просит время. Сумма очень большая.', 'Arakelyan is asking for more time. The sum is very large.', [(331, 'просит'), (331, 'сумма очень большая')], "name normalised (Саракелян -> Аракелян); 'отсрочек' -> 'время'"),
    ('arkady', 'Три дня ему даём. Всё.', "We give him three days. That's it.", [(332, 'три дня ему даем'), (333, 'Все')], ''),
    ('pasha', 'Аркаш, мне москвичи звонят каждый день. Может, всё-таки передумаем?', 'Arkasha, the people from Moscow call me every day. Maybe we should reconsider after all?', [(337, 'мне москвичи звонят каждый день'), (339, 'все-таки передумаем')], "'слушай' and 'мы' dropped"),
    ('arkady', 'Я же сказал: нет.', 'I told you: no.', [(341, 'сказал нет')], "'чётко' (clearly) dropped"),
    ('pasha', 'Там такие деньги! Деньги рекой потекут.', "There's so much money in it! Money will flow like a river.", [(342, 'там такие'), (344, 'рекой потекут')], "'суммы' -> 'деньги', slang 'бабки' -> 'деньги'"),
    ('arkady', 'А потом отходы потекут.', 'And then waste will flow.', [(345, 'А потом отходы потекут')], ''),
    ('pasha', 'Мы же бизнесом здесь занимаемся.', "But we're in business here.", [(346, 'бизнесом здесь занимаемся')], "'вроде как' dropped, 'же' added"),
    ('arkady', 'Жадность, Паша, должна быть умеренная. Комнатной температуры.', 'Greed, Pasha, should be moderate. Room temperature.', [(359, 'Жадность, Паша, должна быть умеренная'), (360, 'Комнатной температуры')], ''),
    ('arkady', 'Посмотри, какой у нас город прекрасный. Озёра, луга.', 'Look what a beautiful town we have. Lakes, meadows.', [(349, 'посмотри, какой у нас'), (349, 'прекрасный'), (350, 'Озера, луга')], "'городок' -> 'город'"),
    ('arkady', 'Мы же здесь выросли. И о людях тоже надо думать.', 'After all, we grew up here. And you have to think about people too.', [(352, 'здесь выросли'), (354, 'И о людях тоже')], "'все-таки' -> 'же'; 'думать надо' -> 'надо думать', 'Паш' dropped"),
    ('pasha', 'Я бы на твоём месте подумал.', "If I were you, I'd think about it.", [(361, 'я бы на твоем месте подумал')], ''),
    ('arkady', 'Вот поэтому ты и не на моём месте.', "And that's exactly why you're not in my place.", [(362, 'Вот поэтому'), (362, 'ты и не на моём месте')], "'Паш' dropped"),
]
WALK = [
    (0, 'Какое хорошее утро!', "'What a lovely morning!' \"Kakoye\" and \"khorosheye\" both take '-oye' endings to match \"utro\" ('morning'). Then he calls his secretary."),
    (0, 'Лидия Алексеевна, чашку кофе, пожалуйста.', "'Lidia Alekseyevna, a cup of coffee, please.' \"Chashka\" ('cup') shifts to \"chashku\" because he's asking for it, while \"kofe\" never changes its ending at all."),
    (1, None, "'Of course, Arkady Borisovich.' \"Khorosho\" ('good' or 'all right') doubles as a polite 'certainly' when answering a request. Then Pasha pokes his head round the door."),
    (2, None, "'Arkasha, may I come in?' One-word \"mozhno?\" ('is it allowed?') is what Russians say as they knock at an office door."),
    (3, None, "'Come in.' \"Zakhodi\" is the casual 'step inside!' for a close colleague; to a stranger he'd add '-te' as \"zakhodite\". Pasha starts with campaign news."),
    (4, None, "'The reaction is positive. People like it.' Notice \"lyudyam nravitsya\" — literally 'to people it is pleasing', which is how Russian says 'people like it'."),
    (5, None, "'Good. And what about the shopping centre?' \"A chto s...?\" — literally 'and what with...?' — is a brisk way to ask for an update on any project."),
    (6, None, "'Arakelyan is asking for more time. The sum is very large.' \"Prosit vremya\" literally says 'asks for time', and \"bolshaya\" ('large') matches \"summa\". Arkady is not impressed."),
    (7, None, "'We give him three days. That's it.' present-form \"dayom\" ('we give') lays down an ultimatum, sealed by crisp \"vsyo\" ('that's final'). Now Pasha pitches what he really wants."),
    (8, 'Аркаш, мне москвичи звонят каждый день.', "'Arkasha, the people from Moscow call me every day.' \"Moskvichi\" means 'Muscovites', built straight from \"Moskva\", and \"kazhdy den\" is 'every day'."),
    (8, 'Может, всё-таки передумаем?', "'Maybe we should reconsider after all?' \"Vsyo-taki\" means 'all the same' or 'after all', nudging someone to relent, before \"peredumayem\" ('we'll rethink it')."),
    (9, None, "'I told you: no.' Tiny \"zhe\" after \"ya\" adds exasperated weight — 'I already told you: no'. Pasha tries the money argument."),
    (10, None, "'There's so much money in it! Money will flow like a river.' \"Rekoy\" puts \"reka\" ('river') into a single 'like-a-river' form, paired with \"potekut\" ('will start flowing')."),
    (11, None, "'And then waste will flow.' Arkady echoes \"potekut\" right back at him, swapping in \"otkhody\" ('industrial waste') for the money."),
    (12, None, "'But we're in business here.' \"Zanimayemsya biznesom\" literally says 'we occupy ourselves with business' — Pasha's polite code for taking kickbacks."),
    (13, None, "'Greed, Pasha, should be moderate. Room temperature.' \"Zhadnost\" ('greed', cousin to childhood \"zhadina\"!) should stay \"komnatnoy temperatury\" — 'of room temperature'."),
    (14, None, "'Look what a beautiful town we have. Lakes, meadows.' \"Sineozersk\" itself is built from 'blue lakes', matching \"ozyora\" ('lakes') and \"luga\" ('meadows') outside the window."),
    (15, None, "'After all, we grew up here. And you have to think about people too.' Impersonal \"nado dumat\" ('one ought to think') covers everyone; in the show he grins and adds 'not often, mind you'."),
    (16, None, "'If I were you, I'd think about it.' \"Na tvoyom meste\" literally says 'on your place', combined with \"by\" ('would') for 'if I were in your shoes'."),
    (17, None, "'And that's exactly why you're not in my place.' \"Vot poetomu\" ('that's precisely why') flips \"na tvoyom meste\" into \"ne na moyom meste\" ('not in my place')."),
]
