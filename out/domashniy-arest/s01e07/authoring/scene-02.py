# Authoring module for domashniy-arest-s01e07-scene-02.
ID = 'domashniy-arest-s01e07-scene-02'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 7
SCENE = 2
TITLE = "Бабушкина брошь  (Grandmother's Brooch)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'danya': 'Даня', 'grandma': 'Бабушка'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.07'
SOURCE_FILE = 'sources/domashniy-arest/s01/e07.ru.dual.srt'
INTRO = "Now inside his tiny room, Arkady rummages through his late grandmother's jewelry box for a vintage brooch to give Marina, arguing aloud with his grandmother's sharp-tongued imagined voice until lawyer Danya knocks for their legal consultation. Let's listen in Russian first."
OPENER = "Now let's go through Arkady's imagined argument with his grandmother and Danya's visit step by step. Arkady opens an old jewelry box in his room."
TRANSITION = "Let's hear the entire scene again in Russian without interruption."
OUTRO = 'While Arkady polishes a factory-made brooch for Marina, polite lawyer Danya is already having tea and pastries with Nina in the kitchen. See you next time!'
CLOSING = ('danya', 'Пока!')
STORY = [
    ('grandma', 'Смотри, куда полез, внучек!', 'Watch where you are reaching, grandson!', [(71, 'Смотри, куда полез')], "cue 71 'ублюдок' -> 'внучек'"),
    ('arkady', 'Бабушка, тихо! Не мешай мне искать подарок!', "Grandma, quiet! Don't bother me while I look for a present!", [(73, 'не мешай')], "cues 72-73 cleaned up to 'Бабушка, тихо! Не мешай мне искать подарок!'"),
    ('grandma', 'Ты что, влюбился? И кому ты такой нужен?', 'What, did you fall in love? And who needs you like this?', [(75, 'И кому ты такой нужен')], "cue 74 slang 'Втрескался' -> 'Ты что, влюбился?'; 'лузер' omitted in Ru line"),
    ('arkady', 'Что? В твоё время даже слов таких не было!', "What? In your day there weren't even words like that!", [(76, 'В твоё время даже слов таких не было')], "colloquial 'Чё' -> 'Что'"),
    ('grandma', 'Эта старая брошь никому не понравится! Даже Клавдии Викторовне!', 'Nobody will like this old brooch! Not even Klavdia Viktorovna!', [(77, 'брошь'), (77, 'даже')], "cue 77 'не даст' cleaned to 'никому не понравится'"),
    ('arkady', 'Но тебе же дед её подарил! Значит, что-то в ней есть, так?', 'But Grandpa gave it to you! So there is something special about it, right?', [(79, 'Значит, что-то в ней есть, так')], "cue 78 'Ну ты же дала деду' cleaned to 'Но тебе же дед её подарил'"),
    ('grandma', 'Ничего в ней нет! Дед работал на заводе, где эти брошки делали.', 'There is nothing special about it! Grandpa worked at the factory where they made these brooches.', [(80, 'ничего в ней нет'), (81, 'дед на заводе работал, где эти брошки делали')], "cue 80 'Жопа я в косяк' omitted"),
    ('grandma', 'Он их с завода брал и дарил! Я эту брошку не носила!', 'He took them from the factory and gave them to everyone! I never wore this brooch in my life!', [(82, 'Он их'), (82, 'дарил'), (83, 'я эту'), (83, 'не носила')], "cue 82 'воровал и всем своим шлюхам дарил' -> 'с завода брал и всем дарил'; cue 83 'дешёвку' -> 'брошку'"),
    ('arkady', 'А вот сюда я её и положу! Отличный подарок будет!', 'Right here is where I will put it! It will be an excellent gift!', [(84, 'А вот сюда я её и положу')], 'cues 85-87 cleaned'),
    ('arkady', 'Да, чего тебе?', 'Yes, what do you want?', [(89, 'Да'), (90, 'Чего тебе')], ''),
    ('danya', 'Аркадий Борисович, сейчас время нашей консультации.', 'Arkady Borisovich, it is time for our consultation now.', [(91, 'Время нашей консультации')], ''),
    ('arkady', 'Давай позже, я занят! Подожди на кухне.', "Let's do it later, I'm busy! Wait in the kitchen.", [(92, 'Давай позже')], "'я занят! Подожди на кухне' added for context"),
    ('danya', 'Прекрасно, я подожду.', 'Wonderful, I will wait.', [(93, 'Прекрасно. Я подожду')], ''),
    ('danya', 'Нина, привет! Я к Аркадию Борисовичу зашёл, а он занят.', 'Nina, hi! I stopped by to see Arkady Borisovich, but he is busy.', [(96, 'Привет'), (97, 'к Аркадию Борисовичу'), (97, 'зашел'), (98, 'а он занят')], ''),
    ('danya', 'Я пирожные принёс! Может, мы пока чаю попьём?', 'I brought pastries! Maybe we could have some tea in the meantime?', [(99, 'Я пирожные принес'), (99, 'может, мы пока чаю')], "cue 99 'чаю пьем' -> 'чаю попьём'"),
]
WALK = [
    (0, None, "'Watch where you are reaching, grandson!' As Arkady reaches for an old brooch, his late grandmother's voice scolds him from her portrait."),
    (1, None, "'Grandma, quiet! Don't bother me while I look for a present!' Notice the negative command with the 'to me/you' word 'to me'."),
    (2, 'Ты что, влюбился?', "'What, did you fall in love?' The '-sya' form is masculine singular."),
    (2, 'И кому ты такой нужен?', "'And who needs you like this?' Literally 'and to whom are you needed like this?'"),
    (3, None, "'What? In your day there weren't even words like that!' In the original she even calls him a 'loser', and Arkady points out that word didn't exist in her time."),
    (4, None, "'Nobody will like this old brooch! Not even Klavdia Viktorovna!' Both 'nobody' and the neighbour's name are in the 'to/for' form."),
    (5, None, "'But Grandpa gave it to you! So there is something special about it, right?' Literally 'something in her there is'."),
    (6, 'Ничего в ней нет!', "'There is nothing special about it!' Literally 'nothing in her there is not'."),
    (6, 'Дед работал на заводе, где эти брошки делали.', "'Grandpa worked at the factory where they made these brooches.' Notice 'at the factory' uses the little word for 'on'."),
    (7, 'Он их с завода брал и дарил!', "'He took them from the factory and gave them away!' Ongoing-action form action words show a repeated habit."),
    (7, 'Я эту брошку не носила!', "'I never wore this brooch!' Literally 'in life I did not wear this brooch'."),
    (8, None, "'Right here is where I will put it! It will be an excellent gift!' Unbothered, Arkady places the brooch into a velvet gift box just as someone knocks."),
    (9, None, "'Yes, what do you want?' Literally 'what to you', a blunt colloquial way to answer the door."),
    (10, None, "'Arkady Borisovich, it is time for our consultation now.' It is Nina's polite lawyer friend Danya."),
    (11, None, "'Let's do it later, I'm busy! Wait in the kitchen.' Arkady is too focused on his romantic plan to talk about his court case."),
    (12, None, "'Wonderful, I will wait.' Danya is only too happy to wait in the kitchen, where Nina is making tea."),
    (13, None, "'Nina, hi! I stopped by to see Arkady Borisovich, but he is busy.' Notice the prefixed past word for 'stopped by on the way'."),
    (14, None, "'I brought pastries! Maybe we could have some tea in the meantime?' Notice the partitive 'of'-form form of 'tea', and Nina gladly accepts."),
]
