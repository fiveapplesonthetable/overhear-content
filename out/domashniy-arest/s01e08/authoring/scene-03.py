# Authoring module for domashniy-arest-s01e08-scene-03.
ID = 'domashniy-arest-s01e08-scene-03'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 3
TITLE = 'Куда пропал кандидат?  (Where Did the Candidate Go?)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ilona': 'Илона', 'nina': 'Нина', 'slavik': 'Славик'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.08'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = "In our last scene, acting mayor Pasha Osipenko recorded a smear video branding candidate Ivan Samsonov the grandson of a wartime collaborator. Now back at the communal apartment, Nina, campaign manager Ilona, and young Slavik realise that Samsonov has gone missing on the very eve of the decisive mayoral debates. Let's hear the scene in Russian first; don't worry about catching every word."
OPENER = "Now let's follow the frantic search for Samsonov line by line. Nina hangs up the kitchen telephone with a trembling hand."
TRANSITION = "Now let's listen to the scene in the communal flat again without interruption."
OUTRO = 'While Samsonov wanders the town in despair, life in the communal flat goes on. See you next time!'
CLOSING = ('nina', 'Пока!')
STORY = [
    ('nina', 'Славик, выключи телевизор, пожалуйста!', 'Slavik, turn off the television, please!', [(47, 'Слав, да выключишь')], ''),
    ('slavik', 'Да, мама. Я выключил.', 'Yes, Mama. I turned it off.', [(48, 'Да')], ''),
    ('nina', 'Я позвонила в больницы. В морге его нет.', 'I called the hospitals. He is not in the morgue.', [(49, 'Спасибо'), (50, 'Морги его нет')], "cue 50 restored to 'В морге его нет'"),
    ('ilona', 'В каком смысле его нет?', 'In what sense is he not there?', [(52, 'В смысле')], ''),
    ('nina', 'В том смысле, что его нигде нет!', 'In the sense that he is nowhere to be found!', [(53, 'В смысле, что его нигде нет')], ''),
    ('ilona', 'Ну и что теперь делать?', 'Well, and what are we to do now?', [(54, 'Ну и что')], "'теперь делать' added"),
    ('nina', 'Я не знаю, где он сейчас.', "I don't know where he is right now.", [(55, 'Я не знаю, где он')], ''),
    ('ilona', 'А в каких местах он обычно пьёт?', 'And in what places does he usually drink?', [(56, 'А в каких местах он обычно пьет')], ''),
    ('nina', 'Я везде уже была!', 'I have already been everywhere!', [(57, 'Везде была')], ''),
    ('slavik', 'Мама, надо звонить в полицию!', 'Mama, we need to call the police!', [(58, 'надо звонить в полицию')], ''),
    ('slavik', 'Я серьёзно говорю, кроме шуток!', 'I am speaking seriously, no joking!', [(59, 'шутки')], "cue 59 garbled 'Треть шутки' -> 'кроме шуток'"),
    ('ilona', 'Нет, в полицию нам звонить нельзя.', 'No, we must not call the police.', [(60, 'Нет, туда нам сейчас не надо')], ''),
    ('ilona', 'Если кандидат в полиции, кампания проиграна!', 'If the candidate is in the police station, the campaign is lost!', [], 'added for context on campaign stakes'),
    ('nina', 'Подождём ещё немного. Он должен вернуться!', "Let's wait a little longer. He must return!", [(61, 'Подождем еще немного')], "'Он должен вернуться' added"),
]
WALK = [
    (0, None, "'Slavik, turn off the television, please!' Nina tells her son to shut off the embarrassing campaign broadcast."),
    (1, None, "'Yes, Mama. I turned it off.' Slavik answers obediently with a past masculine single-action form."),
    (2, None, "'I called the hospitals. He is not in the morgue.' Nina lists the grim places she has already phoned."),
    (3, None, "'In what sense is he not there?' Ilona asks in surprise, using the location form with 'sense'."),
    (4, None, "'In the sense that he is nowhere to be found!' The negative adverb means 'nowhere' for location."),
    (5, None, "'Well, and what are we to do now?' An action verb question expressing helplessness."),
    (6, None, "'I don't know where he is right now.' Nina admits she has run out of ideas."),
    (7, None, "'And in what places does he usually drink?' Ilona tries to guess where a working-class man might drown his sorrows."),
    (8, None, "'I have already been everywhere!' The adverb means 'everywhere'."),
    (9, None, "'Mama, we need to call the police!' Slavik suggests calling law enforcement."),
    (10, None, "'I am speaking seriously, no joking!' The idiom with the preposition for 'besides' means 'all joking aside'."),
    (11, None, "'No, we must not call the police.' Ilona immediately vetos the idea with the adverb for 'prohibited'."),
    (12, None, "'If the candidate is in the police station, the campaign is lost!' The short passive form marks the election effort as finished."),
    (13, None, "'Let's wait a little longer. He must return!' Nina hopes her husband will come to his senses soon."),
]
