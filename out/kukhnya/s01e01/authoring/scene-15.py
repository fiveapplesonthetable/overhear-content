# Authoring module for kukhnya-s01e01-scene-15.
ID = 'kukhnya-s01e01-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 15
TITLE = 'Собеседование на кухне  (Interview in the Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "Max has been sent into a room by a couple of cooks who were pulling his leg, and it turns out to be the chef's office. Then the real head chef, Viktor Barinov, walks in and wants to know who this stranger is. Here's the confrontation in Russian first."
OPENER = "Let's go through their exchange."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Barinov is going to test him, and the test will be a hard one. You\'ve heard how a chef says "here, only I command", which is a good line to remember.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('max', 'Здравствуйте, я пришёл сюда на важное собеседование.', 'Hello, I came here for an important interview.', [(123, 'Я на собеседовании')], ''),
    ('barinov', 'Ты кто такой и как сюда попал?', 'Who are you and how did you get in here?', [(141, 'Ты кто такой')], ''),
    ('max', 'Я принёс своё резюме для шеф-повара.', 'I brought my résumé for the head chef.', [(129, 'Вот мое резюме')], ''),
    ('barinov', 'Что ты вообще делаешь в моём кабинете?', 'What are you even doing in my office?', [(142, 'Ты что здесь делаешь')], ''),
    ('max', 'Другой повар сказал, что шеф уже здесь.', 'Another cook said that the chef is already here.', [(124, 'Вот шеф')], ''),
    ('barinov', 'Настоящий главный шеф-повар этого ресторана — я!', 'The real head chef of this restaurant is me!', [(135, 'Виктор Петрович идёт')], ''),
    ('max', 'Тот человек уже принял меня на работу.', 'That person already hired me for the job.', [(144, 'шеф меня уже взял')], ''),
    ('barinov', 'Кто посмел принять тебя без моего разрешения?', 'Who dared hire you without my permission?', [(145, 'Кто')], ''),
    ('max', 'Я мечтаю готовить вкусные блюда на кухне.', 'I dream of cooking delicious dishes in the kitchen.', [(130, 'Настоящему повару')], ''),
    ('barinov', 'Здесь командую только я и никто больше.', 'Only I command here and no one else.', [(143, 'Какое ещё нахрен собеседование')], ''),
    ('max', 'Пожалуйста, дайте мне один маленький шанс.', 'Please, give me one small chance.', [(132, 'твой потенциал')], ''),
    ('barinov', 'Ладно, сейчас проверим твои настоящие кулинарные навыки.', 'Fine, now we will test your real culinary skills.', [(132, 'увидел твой потенциал')], ''),
]
WALK = [
    (0, None, '\'Hello, I came here for an important interview.\' "Syuda" is "to here", the same word that told Max not to come back. "Vazhnoye" ends in "-oye" because "sobesedovaniye" is neuter.'),
    (1, None, '\'Who are you and how did you get in here?\' "Ty kto takoy" is "you who such", a blunt way to say "who do you think you are?". The "ty" is rude from a stranger. "Popal" means "ended up", as if by chance.'),
    (2, None, '\'I brought my résumé for the head chef.\' "Prinyos" is "brought", carried by a man; a woman would say "prinesla". "Svoyo" is "my own". "Rezyume" never changes.'),
    (3, None, '\'What are you even doing in my office?\' "Voobshche" means "at all" or "even", and it adds irritation. "V moyom kabinete" is "in my office", and both "moyom" and "kabinete" take endings after "v".'),
    (4, None, '\'Another cook said that the chef is already here.\' "Drugoy" is "another", which looks like "drug", friend, with an ending. "Skazal, chto" is "said that", and Russian always puts a comma before "chto".'),
    (5, None, '\'The real head chef of this restaurant is me!\' The dash stands for "is", and "ya" comes last for punch. "Etogo restorana" is "of this restaurant", with "-ogo" and "-a" showing "of".'),
    (6, None, '\'That person already hired me for the job.\' "Prinyal" is "accepted", a second way to say "hired", after "vzyat\' na rabotu". "Tot chelovek" is "that person".'),
    (7, None, '\'Who dared hire you without my permission?\' "Posmel" is "dared", with -l. "Bez" is "without", the same one as in "bez gaza". "Razresheniya" is "of permission", with an "of" ending.'),
    (8, None, '\'I dream of cooking delicious dishes in the kitchen.\' "Mechtayu" is "I dream", from "mechta". "Vkusnyye blyuda" is plural, "tasty dishes", so the describing word ends in "-ye".'),
    (9, None, '\'Only I command here and no one else.\' "Komanduyu" is borrowed from "commander". "Nikto bol\'she" is "nobody more", the Russian for "no one else", with the "ni-" word again.'),
    (10, None, '\'Please, give me one small chance.\' "Dayte" is the formal "give". "Odin malen\'kiy shans" is "one small chance", and "shans" is borrowed.'),
    (11, None, '\'Fine, now we will test your real culinary skills.\' "Ladno" is "fine" or "okay", the same word as in "da ladno". "Tvoi" is "your" in the friendly form, which tells Max the chef talks down to him.'),
]
