# Authoring module for domashniy-arest-s01e09-scene-26.
ID = 'domashniy-arest-s01e09-scene-26'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 9
SCENE = 26
TITLE = 'Звонок Заварзину  (Call to Zavarzin)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'sanya': 'Саня'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.09'
SOURCE_FILE = 'sources/domashniy-arest/s01/e09.ru.dual.srt'
INTRO = 'Realizing that Marina was questioning him on behalf of his political enemy Osipenko, Arkady contacts his reliable friend Sanya Zavarzin. Arkady tells him about the false kindergarten story he planted and instructs Sanya to stake out the location. Listen to their Russian conversation first, and do not worry about catching every word.'
OPENER = "Let's examine how Arkady coordinates with Zavarzin line by line."
TRANSITION = "Now listen to Arkady and Zavarzin's phone call once again."
OUTRO = 'Zavarzin rushes out to monitor the kindergarten as instructed. See you next time!'
CLOSING = ('sanya', 'Пока!')
STORY = [
    ('arkady', 'Саня, срочно ответь мне!', 'Sanya, answer me urgently!', [], 'Arkady dials Zavarzin'),
    ('sanya', 'Саня, у меня выходной.', 'Sanya, I have a day off.', [(721, 'Саня, у меня выходной')], ''),
    ('arkady', 'Плюй на выходной!', 'Forget the day off!', [(722, 'Плюй на выходной')], ''),
    ('arkady', 'Марина работает на Осипенко.', 'Marina works for Osipenko.', [(722, 'Марина работает на')], ''),
    ('sanya', 'С чего ты это взял?', 'What makes you think that?', [], 'Zavarzin is skeptical'),
    ('arkady', 'Всё меня про деньги выспрашивала.', 'She kept questioning me about the money.', [(723, 'Все меня про деньги')], 'adapted to standard spelling выспрашивала'),
    ('sanya', 'Твоя любовь, что ли?', 'Your romantic love or what?', [(724, 'Твоя любовь, что ли')], ''),
    ('arkady', 'Я сказал ей про детский сад.', 'I told her about the kindergarten.', [], 'Arkady explains his bait'),
    ('arkady', 'Якобы спрятал деньги в «Золотом ключике».', 'Supposedly hid the cash in Golden Key.', [(725, 'детском садике «Золотой ключик»')], ''),
    ('sanya', 'И что мне теперь делать?', 'And what should I do now?', [], 'Sanya asks for orders'),
    ('arkady', 'Ты можешь поехать туда и проверить?', 'Can you go there and check?', [(726, 'Ты можешь поехать туда и проверить')], ''),
    ('arkady', 'Надо посмотреть, всё ли там тихо.', 'We need to see if everything is quiet there.', [(726, 'все ли там тихо')], ''),
    ('sanya', 'Понял тебя. Я уже выезжаю.', 'Understood. I am already driving out.', [], 'Sanya gets into gear'),
]
WALK = [
    (0, None, "'Sanya, answer me urgently!' Arkady demands immediate attention over the phone line."),
    (1, None, "'Sanya, I have a day off.' In Russian, the possessive pronoun appears with 'of'-form."),
    (2, None, "'Forget the day off!' A colourful colloquial Russian idiom meaning disregard it."),
    (3, None, "'Marina works for Osipenko.' The preposition with object-form marks who she works for."),
    (4, None, "'What makes you think that?' A set conversational phrase asking for evidence."),
    (5, None, "'She kept questioning me about the money.' The prefix indicates persistent questioning."),
    (6, None, "'Your romantic love or what?' An ironic tag question expressing teasing disbelief."),
    (7, None, "'I told her about the kindergarten.' The preposition with object-form introduces topic."),
    (8, None, "'Supposedly hid the cash in Golden Key.' The modal particle expresses allegation."),
    (9, None, "'And what should I do now?' An action verb question asking for direction and instructions."),
    (10, None, "'Can you go there and check?' Notice the pair of single-action form infinitives after modal."),
    (11, None, "'We need to see if everything is quiet there.' The particle serves as whether in indirect."),
    (12, 'Понял тебя.', "'Understood.' The masculine past tense verb is used colloquially for message received."),
    (12, 'Я уже выезжаю.', "'I am already driving out.' The prefix indicates motion starting outward by vehicle."),
]
