# Authoring module for domashniy-arest-s01e07-scene-06.
ID = 'domashniy-arest-s01e07-scene-06'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 7
SCENE = 6
TITLE = "Приёмчик губернатора  (The Governor's Trick)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'dean': 'Эдуард Владимирович', 'ilona': 'Илона'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.07'
SOURCE_FILE = 'sources/domashniy-arest/s01/e07.ru.dual.srt'
INTRO = "In the communal flat corridor right outside Marina's door. Now Arkady begs Ilona to help him separate Marina and Eduard, and when she refuses, he resorts to a shameless trick he learned from the regional governor. Let's listen in Russian first."
OPENER = "Let's break the scene down piece by piece. Outside Marina's room, Ilona refuses to get dragged into Arkady's romantic jealousy:"
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = "Marina and Eduard rush out of the room toward the stairs, where Arkady and Ilona have just staged a dramatic accident on the landing to ruin Eduard's romantic getaway. Here's one last line from the scene:. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('ilona', 'Я не буду тебе помогать! Ты понимаешь, что это детский сад?', 'I am not going to help you! Do you understand that this is kindergarten?', [(240, 'Я не буду тебе помогать'), (242, 'Ты понимаешь, что это детский сад')], ''),
    ('arkady', 'Нашёл время и место! Какая тебе разница?', 'You found a fine time and place! What difference does it make to you?', [(242, 'Нашел время и место'), (244, 'Какая'), (244, 'разница')], "word order in 244 smoothed to 'Какая тебе разница?'"),
    ('arkady', 'Я не могу спать спокойно! Этот старик крадёт у девушки лучшие годы.', "I cannot sleep in peace! This old man is stealing the girl's best years.", [(245, 'я не могу спать спокойно'), (246, 'крадет у девушки')], "crude 'старый урод' (245) and slip in 246-247 cleaned to 'старик ... лучшие годы'"),
    ('ilona', 'Ты что, влюбился в неё?', 'What, did you fall in love with her?', [(248, 'влюбился')], "colloquial 'Че, влюбился?' -> 'Ты что, влюбился в неё?'"),
    ('arkady', 'Нет! Или да. Какая разница? Помоги мне, я прошу тебя.', 'No! Or yes. What difference does it make? Help me, I beg you.', [(249, 'Нет'), (251, 'Или да. Какая разница? Помоги мне'), (253, 'Помоги мне, я прошу тебя')], ''),
    ('ilona', 'Нет, я сказала нет.', 'No, I said no.', [(252, 'Нет'), (254, 'Нет')], ''),
    ('arkady', 'Смотри, я на колени встал! Я ноги твои целую.', 'Look, I got down on my knees! I am kissing your feet.', [(255, 'Я на колени встал, я ноги твои целую')], ''),
    ('ilona', 'Не надо мне ничего целовать! Аркадий, перестань, я с улицы пришла!', "Don't kiss anything of mine! Arkady, stop it, I just came in from the street!", [(256, 'не надо мне ничего целовать'), (258, 'перестань'), (258, 'с улицы')], "'Аркаш ... они с улицы пришли' (about her boots) -> 'Аркадий ... я с улицы пришла'"),
    ('arkady', 'Ну пожалуйста, помоги мне! Я всё равно буду целовать.', 'Please, help me! I will keep kissing them anyway.', [(257, 'Ну пожалуйста. Ну помоги мне'), (259, 'буду целовать')], ''),
    ('ilona', 'Фу, отдай ноги, говорю! Всё, хватит, стоп! Я согласна.', "Ugh, give me my feet back, I say! That's it, enough, stop! I agree.", [(260, 'Фу'), (262, 'Отдай ноги, говорю'), (265, 'Все, хватит, стоп')], "'Я согласна' from 266-268 'Согласилась? Хватит, да'"),
    ('arkady', 'Ура, работает приёмчик! Это меня губернатор научил.', 'Hooray, the little trick works! The governor taught me this.', [(269, 'Работает приемчик'), (271, 'губернатор научил')], "ASR 'Это мне губернатор научил' -> 'Это меня губернатор научил'"),
    ('arkady', 'Он так каждый раз президента просит. Чтобы его с работы не сняли.', "He begs the president like that every time. So that they don't fire him from his job.", [(272, 'Он каждый раз так президента')], "'уговаривает его с должности не снимать' split and simplified for A1"),
    ('dean', 'Марина, иди ко мне! Я сегодня принял одну таблетку.', 'Marina, come to me! I took a pill today.', [(274, 'Иди ко мне'), (277, 'я сегодня принял')], "diminutive 'таблеточку' -> 'таблетку'"),
    ('dean', 'Так что сегодня я буду как молодой герой!', 'So today I will be like a young hero!', [(277, 'так что я сегодня буду')], "'Просто Казанова' (278) simplified to A1 'как молодой герой'"),
    ('dean', 'Давление? Ничего, от тебя у меня просто кружится голова.', "Blood pressure? It's nothing, you just make my head spin.", [(279, 'давление'), (280, 'А от тебя')], "echoes Marina's warning in 279; 'головокружение' (280) -> 'кружится голова' (A1)"),
    ('dean', 'Ой, что это там за шум? Я не знаю, пойдём посмотрим.', "Oh, what is that noise out there? I don't know, let's go look.", [(283, 'Что это'), (284, 'Я не знаю')], 'adds context for the loud crash on the stairs in 281-283'),
]
WALK = [
    (0, 'Я не буду тебе помогать!', "'I am not going to help you!' Ilona refuses to get dragged into Arkady's romantic schemes."),
    (0, 'Ты понимаешь, что это детский сад?', "'Do you understand that this is kindergarten?' She calls his romantic jealousy childish nonsense."),
    (1, 'Нашёл время и место!', "'You found a fine time and place!' Here, Ilona reminds him they are in the middle of a serious campaign."),
    (1, 'Какая тебе разница?', "'What difference does it make to you?' She asks why he cares so much about Marina's dating life."),
    (2, 'Я не могу спать спокойно!', "'I cannot sleep in peace!' Arkady tries to sound like a noble protector of innocent youth."),
    (2, 'Этот старик крадёт у девушки лучшие годы.', "'This old man is stealing the girl's best years.' Arkady indignantly protests against Eduard."),
    (3, None, "'What, did you fall in love with her?' Ilona cuts straight through his noble excuses."),
    (4, 'Нет! Или да.', "'No! Or yes.' Arkady stammers and wavers in confusion."),
    (4, 'Какая разница? Помоги мне, я прошу тебя.', "'What difference does it make? Help me, I beg you.' He abandons pride and asks for her help."),
    (5, None, "'No, I said no.' Ilona turns away and refuses to assist him."),
    (6, 'Смотри, я на колени встал!', "'Look, I got down on my knees!' Arkady drops dramatically to the corridor floor."),
    (6, 'Я ноги твои целую.', "'I am kissing your feet.' He grabs her boots and presses his face against them."),
    (7, 'Не надо мне ничего целовать!', "'Don't kiss anything of mine!' Ilona pulls back in disgust."),
    (7, 'Аркадий, перестань, я с улицы пришла!', "'Arkady, stop it, I just came in from the street!' She warns him that her winter boots are filthy."),
    (8, 'Ну пожалуйста, помоги мне!', "'Please, help me!' Arkady begs desperately from the corridor floor."),
    (8, 'Я всё равно буду целовать.', "'I will keep kissing them anyway.' Arkady clings to her ankles and refuses to let go."),
    (9, 'Фу, отдай ноги, говорю!', "'Ugh, give me my feet back, I say!' Ilona tries to shake him off her boots."),
    (9, 'Всё, хватит, стоп! Я согласна.', "'That's it, enough, stop! I agree.' Exhausted by his shameless antics, Ilona finally surrenders."),
    (10, 'Ура, работает приёмчик!', "'Hooray, the little trick works!' Arkady jumps up with a victorious grin."),
    (10, 'Это меня губернатор научил.', "'The governor taught me this.' Notice that in Russian you teach someone in the direct-object form."),
    (11, 'Он так каждый раз президента просит.', "'He begs the president like that every time.' Arkady explains that the governor uses this trick to keep his post."),
    (11, 'Чтобы его с работы не сняли.', "'So that they don't fire him from his job.' The conjunction introduces a clause of purpose."),
    (12, 'Марина, иди ко мне!', "'Marina, come to me!' Inside the room, Eduard tries to entice Marina into bed."),
    (12, 'Я сегодня принял одну таблетку.', "'I took a pill today.' Eduard boasts that he took medication to enhance his romantic performance."),
    (13, None, "'So today I will be like a young hero!' He promises to feel youthful and energetic all evening."),
    (14, 'Давление?', "'Blood pressure?' Eduard waves off the warning and says that it is nothing."),
    (14, 'Ничего, от тебя у меня просто кружится голова.', "'It's nothing, you just make my head spin.' Literally, from you my head spins."),
    (15, 'Ой, что это там за шум?', "'Oh, what is that noise out there?' A sudden loud crash echoes from the stairwell outside."),
    (15, 'Я не знаю, пойдём посмотрим.', "'I don't know, let's go look.' Eduard and Marina rush to the corridor to see what happened to Arkady."),
]
