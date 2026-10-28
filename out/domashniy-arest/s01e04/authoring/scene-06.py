# Authoring module for domashniy-arest-s01e04-scene-06.
ID = 'domashniy-arest-s01e04-scene-06'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 4
SCENE = 6
TITLE = "Тайна Головкина  (Golovkin's Secret)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'golovkin': 'Головкин', 'pasha': 'Паша'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.04'
SOURCE_FILE = 'sources/domashniy-arest/s01/e04.ru.dual.srt'
INTRO = "In the corridor outside the investigator's office. Last time, Nina dragged Samson out of the car showroom, and Ilona escaped from the rude taxi driver by driving off in his car. Now Arkady is waiting for his interrogation when his stuttering public defender Danila Golovkin walks up to apologise for speaking against him in court yesterday. Let's listen in Russian first."
OPENER = "Let's take it line by line. Arkady is sitting in the corridor with a bandaged head when Golovkin walks up, and Arkady can't believe his eyes."
TRANSITION = "Now let's hear the whole scene again from the beginning."
OUTRO = "So Arkady discovers that his lawyer is secretly in love with Samson's wife Nina, giving Arkady the leverage he needs before he steps in to face Pasha. Next we check back on Samson and Nina at the job centre; see you then. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('arkady', 'Ты что здесь делаешь? После вчерашнего!', 'What are you doing here? After yesterday!', [(144, 'Ты что здесь делаешь'), (146, 'После вчерашнего')], 'insult in cue 144 dropped'),
    ('golovkin', 'Был неправ. Простите. Я хочу закончить начатое.', 'I was wrong. Forgive me. I want to finish what I started.', [(148, 'Был неправ'), (149, 'Простите'), (150, 'Я хочу закончить'), (151, 'Начатое')], ''),
    ('arkady', 'Чтобы мне ещё десять лет дали? Уходи отсюда!', 'So they give me another ten years? Get out of here!', [(152, 'мне еще')], "cue 152 'Чтоб мне еще десятку припаяли' -> 'Чтобы мне ещё десять лет дали'; rude cue 153 -> 'Уходи отсюда!'"),
    ('golovkin', 'Я не могу.', "I can't.", [(154, 'Я не могу')], ''),
    ('arkady', 'А что такое? Иди отсюда!', "And what's the matter? Go away from here!", [(155, 'А что такое'), (156, 'отсюда')], "'Вон, пошел отсюда' (156) softened to 'Иди отсюда!'"),
    ('golovkin', 'Хорошо. Я люблю женщину в вашей квартире.', 'All right. I love a woman in your flat.', [(158, 'Хорошо. Люблю женщину'), (158, 'в вашей квартире')], "'Я' added; participle 'живущую' dropped"),
    ('arkady', 'Клавдию Викторовну, что ли? Или Марину?', 'Klavdia Viktorovna, or what? Or Marina?', [(159, 'Клавдию Викторовну, что ли? Марину')], 'crude guess about Yulia in cue 159 dropped'),
    ('golovkin', 'Нет, Нину.', 'No, Nina.', [(160, 'Нет')], "'Нину' added so the listener knows whom he means"),
    ('arkady', 'Она же замужем! Ты любишь чужую жену!', "But she's married! You love another man's wife!", [(160, 'Она же замужем')], "crude 'Ты развратник' in cue 160 -> 'Ты любишь чужую жену!'"),
    ('golovkin', 'Я влюблён в неё с первого класса.', "I've been in love with her since first grade.", [(160, 'Я влюблен в нее с первого класса')], ''),
    ('golovkin', 'Прошу оставить это в тайне.', 'I ask you to keep this a secret.', [(161, 'Прошу оставить это в тайне')], ''),
    ('arkady', 'В тайне? А ты мою тайну вчера сохранил?', 'A secret? And did you keep my secret yesterday?', [(162, 'В тайне')], "clean stand-in for cue 162 ('Я тебе, сука, не просил кое-что в тайне оставить')"),
    ('arkady', 'Я сегодня же расскажу всё Самсону!', "I'll tell Samson everything this very day!", [(163, 'я сегодня же расскажу все Самсону')], 'crude second half of cue 163 omitted'),
    ('arkady', 'Он тебя найдёт! Посмотри, что он со мной сделал.', "He'll find you! Look what he did to me.", [(164, 'Он тебя найдет'), (164, 'посмотри'), (164, 'что он')], "adapted from cue 164 ('посмотри на меня, что он с тобой сделает')"),
    ('golovkin', 'Пожалуйста, не надо!', "Please, don't!", [(167, 'Пожалуйста')], "'не надо' added"),
    ('pasha', 'Доброе утро, Аркадий Борисович. Проходи, присядь, перекуси.', 'Good morning, Arkady Borisovich. Come in, sit down, have a bite to eat.', [(173, 'Доброе утро, Аркадий Борисович'), (174, 'Проходи, присядь, перекуси')], ''),
]
WALK = [
    (0, None, "'What are you doing here? After yesterday!' Remember, at yesterday's hearing Golovkin testified against his own client. After the preposition 'after', 'yesterday's' takes the 'of' ending. Golovkin looks sheepish."),
    (1, 'Был неправ.', "'I was wrong.' He uses the masculine past 'was' and then asks Arkady to forgive him."),
    (1, 'Я хочу закончить начатое.', "'I want to finish what I started.' The last word literally means 'the started thing', a past verbal adjective used as a noun. Arkady is horrified."),
    (2, 'Чтобы мне ещё десять лет дали?', "'So they give me another ten years?' Literally, 'in order that to me still ten of years they gave?'. After numbers from five upwards, 'years' changes to the special word for 'summers' in the plural 'of' form."),
    (2, 'Уходи отсюда!', "'Get out of here!' An informal command to leave. But Golovkin doesn't move."),
    (3, None, "'I can't.' If he stops being Arkady's lawyer, he can't visit the communal flat any more. Arkady demands to know why."),
    (4, None, "'And what's the matter? Go away from here!' Cornered, Golovkin blurts out his secret."),
    (5, None, "'All right. I love a woman in your flat.' 'Woman' takes the object ending in 'u', while 'in your flat' uses the location form for location. Arkady starts guessing which neighbour he means."),
    (6, None, "'Klavdia Viktorovna, or what? Or Marina?' Both women's names are in the direct-object form, matching 'I love'. Golovkin shakes his head."),
    (7, None, "'No, Nina.' Also in the object form: 'I love Nina'. Arkady is stunned."),
    (8, 'Она же замужем!', "'But she's married!' The Russian word for a woman being married literally means 'behind a husband', and never changes its ending."),
    (8, 'Ты любишь чужую жену!', "'You love another man's wife!' And she happens to be Samson's wife. Golovkin defends his feelings."),
    (9, None, "'I've been in love with her since first grade.' Russian uses the present state 'I am in love with her' because it is still true today. Then he begs Arkady for silence."),
    (10, None, "'I ask you to keep this a secret.' Literally, 'to leave this in secret'. Arkady's eyes light up with revenge."),
    (11, None, "'A secret? And did you keep my secret yesterday?' In court yesterday, Golovkin revealed Arkady's housing fraud. Now Arkady has the perfect weapon over his lawyer."),
    (12, None, "'I'll tell Samson everything this very day!' Adding the emphatic particle right after 'today' means 'today of all days, this very day'. And he points to his own bandaged head."),
    (13, 'Он тебя найдёт!', "'He'll find you!' future-tense form: one quick, painful result."),
    (13, 'Посмотри, что он со мной сделал.', "'Look what he did to me.' Literally, 'what he with me did'. Golovkin panics."),
    (14, None, "'Please, don't!' Just then, the investigator's door opens and Arkady is called inside, where Pasha is waiting at a table full of food."),
    (15, None, "'Good morning, Arkady Borisovich. Come in, sit down, have a bite to eat.' Notice the mockery: Pasha greets him by his polite name and patronymic, and then gives him three informal commands in a row."),
]
