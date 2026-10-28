# Authoring module for domashniy-arest-s01e12-scene-07.
ID = 'domashniy-arest-s01e12-scene-07'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 12
SCENE = 7
TITLE = 'Машина Фронтера  (The Frontera Car)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'customs': 'Таможенник', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.12'
SOURCE_FILE = 'sources/domashniy-arest/s01/e12.ru.dual.srt'
INTRO = "Right after that, Samson arrives at a highway checkpoint driving an imported foreign SUV. The customs officer asks about the vehicle's model year and admires its build quality. Explaining that he is pressed for time, Samson asks to be let through promptly. Let's listen to their brief exchange in Russian first."
OPENER = "Now let's examine Samson's border check line by line. Notice the conversational car vocabulary and polite road etiquette."
TRANSITION = "Now let's listen to Samson and the customs officer's conversation once more without pauses."
OUTRO = 'Clearing the checkpoint without delay, Samson continues his journey toward the transit airfield. See you next time!'
CLOSING = ('customs', 'Пока!')
STORY = [
    ('customs', 'Здравствуйте, покажите ваши документы на машину.', 'Hello, show your documents for the car.', [], ''),
    ('samson', 'Пожалуйста, вот все нужные бумаги.', 'Please, here are all the necessary papers.', [], ''),
    ('customs', 'Скажите, какого года эта Фронтера?', 'Tell me, what year is this Frontera?', [(128, 'Какого года Фронтера')], ''),
    ('samson', 'Эта машина две тысячи восьмого года.', 'This car is from the year 2008.', [(129, 'Восьмого')], ''),
    ('customs', 'Да, это действительно очень хорошая машина.', 'Yes, this is truly a very good car.', [(130, 'Хорошая машина')], ''),
    ('samson', 'Мы пригоняем только самые надёжные автомобили.', 'We bring in only the most reliable cars.', [], ''),
    ('customs', 'Куда вы сейчас направляетесь на ней?', 'Where are you heading in it now?', [], ''),
    ('samson', 'Мы сейчас спешим в город Синеозёрск.', 'We are hurrying to the town of Sineozersk now.', [], ''),
    ('samson', 'Слышишь, братан, пропусти нас скорее вперёд.', 'Listen, bro, let us through forward quickly.', [(131, 'Слышь, братан')], ''),
    ('samson', 'Мы очень сильно торопимся по делам.', 'We are in a very big hurry on business.', [(131, 'торопимся')], ''),
    ('customs', 'Хорошо, с документами всё в порядке.', 'Alright, everything is in order with the documents.', [], ''),
    ('samson', 'Большое спасибо за вашу быструю помощь!', 'Thank you very much for your quick help!', [(132, 'Спасибо')], ''),
    ('customs', 'Давай, счастливого пути и хорошей дороги!', 'Go ahead, safe travels and have a good road!', [(133, 'Давай')], ''),
    ('samson', 'Спасибо, друг, мы поехали дальше!', 'Thanks, friend, we drove on further!', [], ''),
]
WALK = [
    (0, None, '\'Hello, show your documents for the car.\' Routine highway stop: a polite "zdravstvuyte" followed immediately by the demand for paperwork.'),
    (1, None, '\'Please, here are all the necessary papers.\' When handing something over, Russians say "pozhaluysta" ("please") where English speakers say "here you go".'),
    (2, None, '\'Tell me, what year is this Frontera?\' Instead of grilling him, the officer is eyeing the foreign SUV—an "Opel Frontera"—with genuine curiosity.'),
    (3, None, '\'This car is from the year 2008.\' In Russian, you give a vehicle\'s model year by saying it is "of the two-thousand-eighth year".'),
    (4, None, "'Yes, this is truly a very good car.' For a provincial checkpoint officer, a sturdy imported four-by-four is something to admire."),
    (5, None, '\'We bring in only the most reliable cars.\' The word he uses for "bring in" specifically means driving vehicles across a border for sale.'),
    (6, None, "'Where are you heading in it now?' Still making small talk, the officer asks about their destination while leafing through the registration."),
    (7, None, '\'We are hurrying to the town of Sineozersk now.\' Samson slips the word for "hurrying" into his answer as a polite hint that he has a schedule to keep.'),
    (8, None, '\'Listen, bro, let us through forward quickly.\' Switching from formal talk to "bratan" ("bro"), Samson appeals to him man-to-man to wave them past the line.'),
    (9, None, "'We are in a very big hurry on business.' He has a plane to catch and a buyer waiting, so every minute at the barrier counts."),
    (10, None, '\'Alright, everything is in order with the documents.\' "V poryadke" literally means "in order", the phrase you always hope to hear from an official holding your papers.'),
    (11, None, "'Thank you very much for your quick help!' Relieved not to be held up for a bribe or an inspection, Samson thanks him warmly."),
    (12, None, '\'Go ahead, safe travels and have a good road!\' "Schastlivogo puti" ("happy journey") is the classic Russian send-off for anyone hitting the road.'),
    (13, None, '\'Thanks, friend, we drove on further!\' Once again Russian uses the past—"we drove on"—for an action that is starting right this second.'),
]
