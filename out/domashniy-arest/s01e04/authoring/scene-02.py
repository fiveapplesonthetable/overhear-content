# Authoring module for domashniy-arest-s01e04-scene-02.
ID = 'domashniy-arest-s01e04-scene-02'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 4
SCENE = 2
TITLE = 'Артурик в такси  (Arturik in the Taxi)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arturik': 'Артурик', 'ilona': 'Илона'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.04'
SOURCE_FILE = 'sources/domashniy-arest/s01/e04.ru.dual.srt'
INTRO = "On the road from the Sineozersk railway station, a few minutes later. Meanwhile, a sharp Moscow political strategist named Ilona Leonidovna is riding in a local taxi toward her hotel when the driver, Arturik, recognises her from her youth in Sineozersk and locks the car doors. Let's listen in Russian first."
OPENER = "Let's go back through the scene. Arturik looks in his mirror, recognises his passenger, and switches straight to the informal 'you'."
TRANSITION = "Let's listen to the whole conversation in the taxi once more."
OUTRO = "So Ilona has talked the pushy taxi driver into pulling over under Devil's Bridge, and he has no idea who he is dealing with. Next we check in on Arkady back in the communal kitchen; see you then. See you next time!"
CLOSING = ('ilona', 'Пока!')
STORY = [
    ('arturik', 'Стой, я тебя узнал! Ты у нас в клубе танцевала!', 'Wait, I recognise you! You used to dance at our club!', [(46, 'я тебя узнал'), (46, 'танцевала')], "'зажигалки стриптиз танцевала' cleaned up to 'у нас в клубе танцевала'"),
    ('arturik', 'А меня не помнишь? Я Артурик, я к вам часто приходил.', "And don't you remember me? I'm Arturik, I used to come see you often.", [(46, 'а меня'), (47, 'не помнишь'), (47, 'я к вам часто приходил')], "cue 47 'артуре' -> 'Я Артурик'"),
    ('arturik', 'Ты в Москву переехала, да? Поедем сейчас в сауну, посидим!', "You moved to Moscow, right? Let's go to a sauna now and sit for a while!", [(48, 'в москву'), (48, 'да'), (49, 'Поедем сейчас в сауну, посидим')], "'перебралась' -> 'переехала'; 'покайфуем' and cue 50 dropped"),
    ('ilona', 'Артурик, я уже давно не танцую. И в сауну не езжу.', "Listen, Arturik, I haven't danced in a long time. And I don't go to saunas.", [(51, 'Артурик, я'), (51, 'уже давно не танцую'), (52, 'в сауну не')], "'во-первых ... во-вторых, даже когда танцевала, в сауну не ездила' simplified"),
    ('ilona', 'Я приехала к очень серьёзному человеку. Он меня ждёт.', 'I have come to see a very important man. He is waiting for me.', [(53, 'я приехала к очень серьезному человеку'), (53, 'он меня ждет')], 'split into two short sentences'),
    ('arturik', 'А почему этот серьёзный человек тебя не встретил?', "Then why didn't this important man meet you at the station?", [(54, 'этот серьезный человек тебя не встретил')], "'Чего же' -> 'А почему'"),
    ('ilona', 'Машину останови!', 'Stop the car!', [(56, 'Машину останови')], "insult 'баран' dropped"),
    ('arturik', 'Ты в Москву переехала и важная стала? Со своими уже не хочешь?', "Did you move to Moscow and get all important? Don't you want to be with your own people anymore?", [(57, 'в Москву переехала'), (57, 'стала'), (58, 'Со своими уже не хочешь')], "'крутая' -> 'важная'"),
    ('ilona', 'Не хочу.', "No, I don't.", [(59, 'Не хочу')], ''),
    ('arturik', 'А придётся! Не бойся, тебе понравится.', "Well, you'll have to! Don't be afraid, you'll like it.", [(60, 'Придётся'), (55, 'тебе понравится')], "'Не боись' -> 'Не бойся'"),
    ('ilona', 'Ладно, Артурик. Послушай, я правда опаздываю.', 'All right, Arturik. Listen, I really am running late.', [(62, 'Ладно, Артурик'), (63, 'Послушай, только я, правда, опаздываю')], "'чёрт с тобой' dropped"),
    ('ilona', 'Давай лучше где-нибудь здесь, а? Зачем нам в сауну ехать?', "Let's stop somewhere around here instead, eh? Why should we drive to a sauna?", [(63, 'давай лучше где-нибудь здесь, а'), (66, 'Зачем нам в сауну ехать')], ''),
    ('arturik', 'Что, серьёзно?', 'What, seriously?', [(64, 'серьёзно')], ''),
    ('ilona', 'Серьёзно. Давай вон под Чёртов мост.', "Seriously. Let's pull under Devil's Bridge over there.", [(65, 'Серьёзно'), (66, 'давай вон'), (66, 'мост')], "cue 66 has the slip 'по чёртов мост' for 'под Чёртов мост'"),
    ('arturik', 'Вот это дело! Потом обратно бесплатно отвезу.', "Now we're talking! Afterwards I'll drive you back for free.", [(67, 'Вот это дело'), (70, 'Обратно бесплатно отвезу')], ''),
]
WALK = [
    (0, None, "'Wait, I recognise you! You used to dance at our club!' Both verbs are in the past tense: 'I recognised' has no ending because Arturik is a man, and 'you danced' ends in '-a' because Ilona is a woman."),
    (1, None, "'And don't you remember me? I'm Arturik, I used to come see you often.' He uses the ongoing-action form verb for something he did repeatedly."),
    (2, None, "'You moved to Moscow, right? Let's go to a sauna now and sit for a while!' And with that, he clicks the door locks shut. Ilona stays ice-cold and uses the formal 'you'."),
    (3, None, "'Arturik, I haven't danced in a long time. And I don't go to saunas.' Russian uses the present tense with 'for a long time not' to mean 'I haven't done this in a long time'."),
    (4, 'Я приехала к очень серьёзному человеку.', "'I have come to see a very important man.' Literally 'a very serious person'. After the preposition 'to', both the adjective and the noun take the masculine the 'to/for' ending."),
    (4, 'Он меня ждёт.', "'He is waiting for me.' That important man, as we will soon learn, is Pasha. Arturik just smirks."),
    (5, None, "'Then why didn't this important man meet you at the station?' Meanwhile, Ilona drops the polite tone."),
    (6, None, "'Stop the car!' She puts 'the car' first, in the direct-object form, followed by a sharp singular command."),
    (7, None, "'Did you move to Moscow and get all important? Don't you want to be with your own people anymore?' The '-a' ending on the past-tense verb for 'became' shows that the subject is feminine."),
    (8, None, "'No, I don't.' Just two words: 'not I-want'."),
    (9, None, "'Well, you'll have to! Don't be afraid, you'll like it.' The first word is an impersonal future verb that means 'it will be necessary, you'll have no choice'. Seeing that the doors are locked, Ilona changes tactics and pretends to play along."),
    (10, None, "'All right, Arturik. Listen, I really am running late.' Notice that she has switched to the informal 'listen' to sound friendly."),
    (11, None, "'Let's stop somewhere around here instead, eh? Why should we drive to a sauna?' Literally 'why to us to drive to a sauna?'."),
    (12, None, "'What, seriously?' Arturik can hardly believe his luck, and he thinks that she has changed her mind."),
    (13, None, "'Seriously. Let's pull under Devil's Bridge over there.' After 'under' for direction, 'Devil's Bridge' stays in the direct-object form."),
    (14, None, "'Now we're talking! Afterwards I'll drive you back for free.' The first sentence is a handy idiom, literally 'here this is business!'. We'll soon see what Ilona really has planned for him under that bridge."),
]
