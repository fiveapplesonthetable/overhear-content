# Authoring module for kukhnya-s06e11-scene-04.
ID = 'kukhnya-s06e11-scene-04'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 11
SCENE = 4
TITLE = 'Устрицы в России  (Oysters in Russia)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.11'
SOURCE_FILE = 'sources/kukhnya/s06/e11.ru.srt'
INTRO = 'In his office, Barinov immediately suspects that his brother Valentin flew ten thousand kilometers to ask for money again. Valya pitches his latest venture—oyster farming in Russia—and promises to pay back his old debt with interest, just not right now.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Valya explains why he is temporarily short on cash right now: he left his entire suitcase in a random taxi from the airport. See you next time!'
CLOSING = ('barinov', 'До свидания!')
STORY = [
    ('guest', 'И с тех пор даже учителя называли его Зюзей.', 'And since then even the teachers called him Zyuzya.', [(69, 'И с тех пор даже учителя стали его называть Зюзей')], 'adapted'),
    ('barinov', 'Ладно, пойдём скорее ко мне в кабинет.', 'Alright, let us go quickly to my office.', [(70, 'Ладно, пойдём')], 'adapted'),
    ('guest', 'Я пролетел десять тысяч километров, ты не рад?', 'I flew ten thousand kilometers, are you not glad?', [(74, 'Я пролетел 10 тысяч километров'), (75, 'Неужели совсем не рад видеть')], 'adapted'),
    ('barinov', 'Очень рад, но ты прилетел только меня повидать?', 'Very glad, but did you fly in just to see me?', [(76, 'Очень рад. А ты прилетел только что, чтобы меня повидать')], 'adapted'),
    ('guest', 'Не только, у меня есть отличная идея.', 'Not only that, I have an excellent idea.', [(77, 'Не только. Есть отличная бизнес-идея')], 'adapted'),
    ('barinov', 'Я всё понял, сразу говорю, денег не дам.', 'I understood everything, I am telling you right away, I will not give you money.', [(78, 'Все понял. Сразу говорю, денег не дам')], 'adapted'),
    ('guest', 'Подожди, на этот раз это реально работает!', 'Wait, this time it really works!', [(79, 'Да это реально работает')], 'adapted'),
    ('barinov', 'Скажи, что ты придумал на этот раз?', 'Tell me, what did you come up with this time?', [(81, 'Что на этот раз')], 'adapted'),
    ('guest', 'Мы будем разводить свежих устриц здесь, в России.', 'We will raise fresh oysters here in Russia.', [(83, 'Здесь, в России')], 'adapted'),
    ('barinov', 'Валя, ты повторяешься, устриц ты уже разводил.', 'Valya, you are repeating yourself, you already raised oysters.', [(84, 'Валя, ты повторяешься'), (84, 'ты разводил два года назад')], 'adapted'),
    ('guest', 'Витя, в Америке у меня всё отлично работает.', 'Vitya, in America everything works great for me.', [(87, 'Витя, в Америке все'), (88, 'Все работает')], 'adapted'),
    ('guest', 'Я скоро отдам всё, что тебе должен, с процентами.', 'I will soon pay back everything I owe you, with interest.', [(89, 'Я скоро отдам все, что тебе должен'), (90, 'Даже с процентами')], 'adapted'),
    ('barinov', 'Но я так понимаю, ты отдашь не сейчас.', 'But as I understand it, you will not pay it back right now.', [(91, 'Но я так понимаю, не сейчас')], 'adapted'),
]
WALK = [
    (0, None, '\'And since then even the teachers called him Zyuzya.\' The guest chooses this telling detail in reply: "uchitelya" means "the teachers" (from "uchitel"), giving the line its exact edge.'),
    (1, None, '\'Alright, let us go quickly to my office.\' Barinov hands over this update right away: tacking on "ladno" ("okay, fine, deal") softens the edge and checks that the guest is on board.'),
    (2, None, "'I flew ten thousand kilometers, are you not glad?' The guest checks skeptically to see how Barinov will answer on the spot."),
    (3, None, '\'Very glad, but did you fly in just to see me?\' Barinov underscores one key word in earnest: "priletel" means "flew" (from "priletet"), giving the line its exact edge.'),
    (4, None, '\'Not only that, I have an excellent idea.\' The guest states that point briskly now: Russian phrases this around "u menya" (literally "by me") rather than "I have", a pattern you will hear in almost every scene.'),
    (5, None, "'I understood everything, I am telling you right away, I will not give you money.' Barinov steps in right away with the guest, before the guest can change the subject."),
    (6, None, '\'Wait, this time it really works!\' The guest features this sharp term in earnest: "rabotayet" means "works" (from "rabotat"), giving the line its exact edge.'),
    (7, None, '\'Tell me, what did you come up with this time?\' Barinov sends that answer frankly here: putting the question word "chto" right at the front of the line lets the guest hear the point of the question on the very first beat.'),
    (8, None, "'We will raise fresh oysters here in Russia.' The guest speaks sharply with a nod, so Barinov knows he is not just making small talk."),
    (9, None, '\'Valya, you are repeating yourself, you already raised oysters.\' Barinov chooses one colorful word in earnest: "povtoryayeshsya" means "you are repeating yourself" (from "povtoryatsya"), giving the line its exact edge.'),
    (10, None, '\'Vitya, in America everything works great for me.\' The guest voices this statement for Barinov: Russian phrases this around "u menya" (literally "by me") rather than "I have", a pattern you will hear in almost every scene.'),
    (11, None, "'I will soon pay back everything I owe you, with interest.' The guest follows up wryly hearing Barinov, before Barinov can change the subject."),
    (12, None, '\'But as I understand it, you will not pay it back right now.\' Barinov underscores one practical touch in reply: "ponimayu" means "understand" (from "ponimat"), giving the line its exact edge.'),
]
