ID = 'porta-dos-fundos-s01e01-scene-04'
SHOW, SEASON, EPISODE, SCENE = 'porta-dos-fundos', 1, 1, 4
TITLE = 'Estamos livres  (We Are Free)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'colega': 'Colega', 'financeiro': 'Funcionário', 'organizador': 'Organizador'}
SOURCE_NAME = 'Porta dos Fundos — Vem pra reunião (2026-01-05)'
SOURCE_FILE = 'sources/porta-dos-fundos/s01/e01.pt.srt'

INTRO = (
    'Worn down by his colleague, the finance employee finally agrees to step into the marketing meeting. '
    'Right as they settle the ground rules outside the door, an organizer walks out with breaking news. '
    'Listen in Brazilian Portuguese first, and do not worry about catching every word.'
)
OPENER = "Let's go back through the twist one line at a time."
TRANSITION = "Now let's listen to the whole exchange once more."
OUTRO = (
    'The employee escaped the meeting only to get drafted straight into a coffee break. '
    'Stick around for one final scene inside an actual office presentation. See you next time!'
)
CLOSING = ('organizador', 'Até amanhã!')

STORY = [
    ('colega', 'Tá bom. Você vai entrar lá dentro.', "All right. You're going inside there.", [(153, 'Tá bom. Você vai entrar lá dentro')], ''),
    ('colega', 'E você vai ficar sentado esse tempo inteiro.', "And you're going to stay seated that whole time.", [(159, 'e você vai ficar'), (161, 'sentado'), (161, 'esse tempo inteiro')], 'Simplified acenar com a cabeça clause.'),
    ('colega', 'Fechou? Estamos alinhados?', 'Deal? Are we aligned?', [(167, 'Fechou'), (171, 'Estamos alinhados')], 'Turned office buzzwords into quick check questions.'),
    ('financeiro', 'Sim, senhor.', 'Yes, sir.', [(185, 'Sim, senhor')], ''),
    ('organizador', 'Ih, gente! O cara desmarcou a reunião.', 'Oh, folks! The guy canceled the meeting.', [(189, 'Ih, gente'), (197, 'o cara desmarcou a reunião')], ''),
    ('colega', 'Desmarcou? Que que houve?', 'He canceled? What happened?', [(199, 'Desmarcou'), (191, 'que que houve')], ''),
    ('organizador', 'A outra reunião atrasou. Ele não vem mais.', 'The other meeting ran late. He is not coming anymore.', [(205, 'reunião atrasou, ele não')], 'Simplified cues 201-211 scheduling tangle.'),
    ('organizador', 'Estamos livres!', 'We are free!', [(217, 'Estamos livres')], ''),
    ('colega', 'Estamos livres! Vamos tomar um cafezinho?', 'We are free! Shall we grab a little coffee?', [(219, 'Estamos livres'), (223, 'cafezinho'), (229, 'tomar um cafezinho')], 'Replaced caption typo Toar with Vamos tomar.'),
    ('financeiro', 'Eu gostaria, mas agora tenho que resolver umas coisinhas.', 'I would like to, but right now I have to sort out a few little things.', [(225, 'eu gostaria, mas agora'), (227, 'resolver umas coisinhas')], 'Simplified vou ter que to tenho que.'),
    ('colega', 'Vamos tomar um cafezinho com adoçante!', "Let's have a little coffee with sweetener!", [(229, 'tomar um cafezinho'), (231, 'com adoçante')], 'Omitted misheard caption tail no fita.'),
    ('financeiro', 'Oba.', 'Yay.', [(235, 'Oba')], ''),
]

WALK = [
    (0, None, ["'All right. You're going inside there.' ", ('financeiro', 'Tá bom.'), ', literally "it\'s good", is the everyday Brazilian "okay" or "all right", though here the colleague uses it to start giving orders.']),
    (1, None, ["'And you're going to stay seated that whole time.' ", ('colega', 'inteiro.'), ' means "whole" or "entire", and placing it after ', ('colega', 'esse tempo'), ' stresses every single minute he has to sit still.']),
    (2, None, ["'Deal? Are we aligned?' ", ('colega', 'Fechou?'), ' literally means "it closed", like closing a deal, and ', ('colega', 'estamos alinhados?'), ' is classic Brazilian office-speak for "we\'re on the same page".']),
    (3, None, ["'Yes, sir.' Calling a peer ", ('financeiro', 'senhor.'), ' here is pure dry humour, like saluting a drill sergeant just to end the lecture.']),
    (4, None, ["'Oh, folks! The guy canceled the meeting.' The verb means to book or schedule, so adding a prefix flips ", ('colega', 'desmarcou'), ' neatly into "un-booked" or "canceled".']),
    (5, None, ["'He canceled? What happened?' ", ('financeiro', 'Que que houve?'), ' is the go-to spoken question when something unexpected happens, built around the verb meaning "there was".']),
    (6, None, ["'The other meeting ran late. He is not coming anymore.' Adding ", ('colega', 'mais.'), ' right after ', ('colega', 'não vem'), ' gives you "not anymore", where ', ('colega', 'mais.'), ' literally means "more".']),
    (7, None, ["'We are free!' Because ", ('colega', 'livres!'), " describes both of them together, it adds an 's' to match ", ('colega', 'estamos'), ', meaning "we are".']),
    (8, None, ["'We are free! Shall we grab a little coffee?' In Brazil you never just invite someone for the plain drink: adding the warm ending makes ", ('colega', 'cafezinho?'), ' sound quick, friendly, and impossible to refuse.']),
    (9, None, ["'I would like to, but right now I have to sort out a few little things.' Notice the employee fights back with the same affectionate ending: ", ('financeiro', 'coisinhas.'), ' shrinks "things" into "just a few little tasks" to soften his excuse.']),
    (10, None, ["'Let's have a little coffee with sweetener!' ", ('colega', 'adoçante!'), ' comes from a root meaning "sweet", so it literally names the thing that sweetens your cup.']),
    (11, None, ["'Yay.' Normally, ", ('financeiro', 'Oba.'), " is a cheerful Brazilian shout of delight, which makes the employee's flat, defeated delivery even funnier."]),
]
