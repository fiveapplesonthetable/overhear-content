# Authoring module for domashniy-arest-s01e04-scene-11.
ID = 'domashniy-arest-s01e04-scene-11'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 4
SCENE = 11
TITLE = 'Шанс всей жизни  (The Chance of a Lifetime)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'nina': 'Нина', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.04'
SOURCE_FILE = 'sources/domashniy-arest/s01/e04.ru.dual.srt'
INTRO = "Last time, after the video of Samson throwing the mayor out the window gained four million views, Arkady declared Samson the future mayor of Sineozersk. Samson storms into his room and tries to throw Arkady out, blaming him for ruining his quiet life, while Arkady tries to win over Nina and Samson with the online comments. Let's listen in Russian first."
OPENER = "Let's walk through it. Samson wants nothing to do with politics, and Arkady follows him right into the Samsonovs' room."
TRANSITION = "Now let's hear the whole conversation again from the beginning."
OUTRO = "So with the promise of becoming the mayor's wife in two months — and glowing comments calling Samson the pride of Russia — Nina convinces Samson to hear Arkady out. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('arkady', 'Ваня, да пойми ты наконец! Это настоящий успех.', 'Vanya, understand at last! This is real success.', [(332, 'Ваня, да пойми ты, наконец'), (334, 'Это настоящий успех')], ''),
    ('samson', 'Уходи отсюда, я тебе сказал! Оставь нас в покое.', 'Get out of here, I told you! Leave us in peace.', [(336, 'я тебе сказал'), (337, 'Оставь нас в покое')], "crude 335-336 'Пошел ты нахрен ... вали отсюда' -> 'Уходи отсюда'"),
    ('arkady', 'Ваня, это самый лучший шанс в твоей жизни!', 'Vanya, this is the very best chance of your life!', [(338, 'Ваня'), (339, 'самый лучший шанс')], "cue 339 'в своей жизни' -> 'в твоей жизни'"),
    ('samson', 'Я как тебя встретил, вся жизнь пошла плохо.', 'Ever since I met you, my whole life has gone badly.', [(342, 'Я как тебя'), (342, 'вся жизнь')], "'повстречал' -> 'встретил'; idiom 'псу под хвост' -> 'пошла плохо'; crude 341 dropped"),
    ('samson', 'Работы нет, денег нет! А без тебя я прекрасно жил.', "There's no job, no money! And without you I lived wonderfully.", [(343, 'Работы нет, денег нет'), (345, 'без тебя'), (345, 'прекрасно жил')], ''),
    ('samson', 'Там твоя комната, а здесь наша. Между нами стена, понял?', 'There is your room, and here is ours. Between us is a wall, got it?', [(352, 'там твоя комната, а здесь наша. Между нами стена, понял')], ''),
    ('arkady', 'Сейчас всё в твоих руках! Ты можешь изменить жизнь своей семьи.', "Right now everything is in your hands! You can change your family's life.", [(355, 'сейчас все в твоих руках'), (356, 'можешь изменить'), (357, 'жизнь своей семьи')], ''),
    ('nina', 'А что, шансы правда хорошие?', 'Wait, are the chances really good?', [(359, 'А что, шансы правда хорошие')], ''),
    ('arkady', 'Вы сами подумайте. Он самый известный человек в Синеозерске!', 'Think about it yourselves. He is the most famous man in Sineozersk!', [(360, 'вы сами'), (362, 'самый известный человек в Синеозерске')], "'посудите' -> 'подумайте'"),
    ('arkady', 'Вы почитайте про него комментарии. Это народный герой!', "Read the comments about him. He's a people's hero!", [(363, 'Вы почитайте. Это народный герой'), (364, 'комментарии')], "'про себя' -> 'про него'"),
    ('arkady', 'Всё пойдёт хорошо. Через два месяца вы будете женой мэра!', "Everything will go well. In two months you will be the mayor's wife!", [(367, 'Все пойдет хорошо. Через два месяца вы будете женой мэра')], ''),
    ('samson', 'А тебе это зачем?', "And what's in it for you?", [(368, 'А тебе это зачем')], ''),
    ('arkady', 'Он станет мэром и меня вытащит. Я скажу ему как.', "He will become mayor and get me out. I'll tell him how.", [(369, 'Он станет мэром и меня вытащит. Я скажу ему как')], ''),
    ('nina', 'Слушай, тут пишут: «Гордость России! Наконец-то кто-то за народ!»', "Listen, here they write: 'Pride of Russia! Finally someone is for the people!'", [(373, 'Гордость России'), (374, 'Наконец-то кто-то'), (374, 'за народ')], "Yulia reading comments folded into Nina's role; insults/crude comments 370-372, 375, 377 omitted"),
    ('nina', 'А что от нас нужно?', 'And what is needed from us?', [(381, 'А что от нас')], "'потребуется' -> 'нужно'"),
    ('arkady', 'Я вам сейчас всё объясню.', 'I will explain everything to you right now.', [(383, 'Я вам все объясню')], "'сейчас' added"),
]
WALK = [
    (0, None, "'Vanya, understand at last! This is real success.' That little particle before the command adds impatience: 'come on, understand!'. Samson has had enough."),
    (1, 'Уходи отсюда, я тебе сказал!', "'Get out of here, I told you!' The line opens with 'get out' and lands on 'told' at the end for emphasis."),
    (1, 'Оставь нас в покое.', "'Leave us in peace.' A very common set phrase: literally 'leave us in calm'. Arkady keeps pushing."),
    (2, None, "'Vanya, this is the very best chance of your life!' 'The very best' combines 'most' with 'best'. Samson lists what Arkady's arrival has actually brought him."),
    (3, None, "'Ever since I met you, my whole life has gone badly.' Literally 'how I met you, all life went badly'. He continues."),
    (4, 'Работы нет, денег нет!', "'There's no job, no money!' Both nouns are in the 'of' form because of the negative word 'there is no'."),
    (4, 'А без тебя я прекрасно жил.', "'And without you I lived wonderfully.' Samson points at the wall between their rooms."),
    (5, None, "'There is your room, and here is ours. Between us is a wall, got it?' Samson uses the adverb for 'there' right alongside the verb meaning 'got it?'."),
    (6, None, "'Right now everything is in your hands! You can change your family's life.' And that catches Nina's ear."),
    (7, None, "'Wait, are the chances really good?' The noun for 'truth' is used right in the middle of the sentence to mean 'really, truly'. Arkady turns to Nina with his smoothest smile."),
    (8, 'Вы сами подумайте.', "'Think about it yourselves.' Listen for the word meaning 'think', which leads straight into 'think'."),
    (8, 'Он самый известный человек в Синеозерске!', "'He is the most famous man in Sineozersk!' That superlative word 'most' in front of any adjective makes it 'the most...'. He hands them the tablet."),
    (9, None, "'Read the comments about him. He's a people's hero!' And then he gives Nina the clincher."),
    (10, 'Всё пойдёт хорошо.', "'Everything will go well.' Arkady uses the adverb for 'well' right alongside the verb meaning 'will go'."),
    (10, 'Через два месяца вы будете женой мэра!', "'In two months you will be the mayor's wife!' After 'will be', the noun 'wife' goes into the 'with/as' form. Even Samson stops and asks the key question."),
    (11, None, "'And what's in it for you?' Literally 'and to you this what for?'. Arkady answers Nina honestly, as if Samson weren't even in the room."),
    (12, 'Он станет мэром и меня вытащит.', "'He will become mayor and get me out.' Again, 'become' takes the 'with/as' form: 'will become mayor'."),
    (12, 'Я скажу ему как.', "'I'll tell him how.' Meanwhile, Nina and their daughter Yulia look at the comments under the video."),
    (13, None, "'Listen, here they write: Pride of Russia! Finally someone is for the people!' Ignoring a few rude comments about Arkady, the internet loves Samson. Nina is sold."),
    (14, None, "'And what is needed from us?' Right then, Arkady rubs his hands together."),
    (15, None, "'I will explain everything to you right now.' Arkady uses the adverb for 'right now' right alongside the verb meaning 'will explain'."),
]
