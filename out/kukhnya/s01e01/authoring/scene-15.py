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
INTRO = "Max arrives in the bustling kitchen of Claude Monet for a job interview, where pranksters trick him into the back office. Moments later, the fiery and imposing head chef Viktor Barinov bursts in, furiously demanding to know who this intruder is. Let's listen to their confrontation in Russian."
OPENER = "Let's examine the dialogue sentence by sentence. Notice the workplace confrontation vocabulary and assertive speech."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Viktor Barinov angrily reprimands Max for entering his office, but agrees to test his cooking skills on the line. Great work practicing emotional and professional Russian dialogue! Next time you watch the episode, listen for the Russian expressions for 'dish' and 'more' — you will catch every word right away. See you next time!"
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
    (0, None, "'Hello, I came here for an important interview.' Max greets the room, announcing his formal purpose while hoping to make a good impression."),
    (1, None, "'Who are you and how did you get in here?' Barinov explodes with suspicion, demanding immediate answers about the stranger trespassing in his sanctuary."),
    (2, None, "'I brought my résumé for the head chef.' Holding up his paperwork, the naive candidate tries to legitimize his presence in the back room."),
    (3, None, "'What are you even doing in my office?' The furious boss zeroes in on the inappropriate location chosen for this impromptu meeting."),
    (4, None, "'Another cook said that the chef is already here.' Explaining his mistake, the young man blames a colleague for misdirecting him into the trap."),
    (5, None, "'The real head chef of this restaurant is me!' Asserting his absolute dominance, the veteran cook makes his supreme identity known with forceful pride."),
    (6, None, "'That person already hired me for the job.' Still confused by the prank, the newcomer claims he has already been granted a position."),
    (7, None, "'Who dared hire you without my permission?' Outraged by the idea of bypassed authority, the head honcho demands the name of the traitor."),
    (8, None, "'I dream of cooking delicious dishes in the kitchen.' Max pivots to his passion, sharing his heartfelt desire to create amazing food."),
    (9, None, "'Only I command here and no one else.' A stern reminder of the hierarchy is delivered to ensure the rookie understands who holds power."),
    (10, None, "'Please, give me one small chance.' Begging for an opportunity, the underdog pleads for just a moment to demonstrate his worth."),
    (11, None, "'Fine, now we will test your real culinary skills.' Reluctantly agreeing, the master cook declares that a practical trial will determine the boy's fate."),
]
