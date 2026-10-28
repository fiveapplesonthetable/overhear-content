# Authoring module for kukhnya-s04e20-scene-02.
ID = 'kukhnya-s04e20-scene-02'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 20
SCENE = 2
TITLE = 'Роковая ошибка у бара  (A Fatal Mistake at the Bar)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'kostya': 'Костя'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.20'
SOURCE_FILE = 'sources/kukhnya/s04/e20.ru.srt'
INTRO = "With his broken arm in a cast, Denis stops by the bar and explains to Kostya why he jumped out of Vika's office window yesterday. As Denis vividly describes his dream about Vika kissing him on the couch, Katya walks up behind him and hears only the worst part. Let's listen to the misunderstanding in Russian."
OPENER = "Now let's trace how Katya overhears Denis's story out of context line by line."
TRANSITION = "Let's hear the conversation at the bar again from start to finish."
OUTRO = 'Believing that Denis actually slept with Vika in the office, a heartbroken Katya refuses to listen and storms away. Listen for the action words meaning frightened, happened, and explain. See you next time!'
CLOSING = ('denis', 'Пока!')
STORY = [
    ('kostya', 'Здорово, ну ты нас вчера напугал!', 'Hey there, you really scared us yesterday!', [(22, 'Здорово. Слушай, ну ты нас вчера, конечно, напугал')], 'adapted'),
    ('denis', 'Костя, я вчера и сам испугался.', 'Kostya, I got scared myself yesterday too.', [(23, 'Я сам напугался')], 'adapted'),
    ('kostya', 'Расскажи, как всё это вчера произошло?', 'Tell me, how did all of this happen yesterday?', [(24, 'Как все это произошло-то')], 'adapted'),
    ('denis', 'Помнишь, я рассказывал про свои сны?', 'Do you remember I told you about my dreams?', [(25, 'Помнишь, я тебе рассказывал, что я во сне')], 'adapted'),
    ('denis', 'Так вот, этой женщиной была Вика.', 'Well then, that woman was Vika.', [(26, 'Так вот это была Вика')], 'adapted'),
    ('kostya', 'Подожди, ты про Вику во сне?', 'Wait, you mean Vika in your dream?', [(27, 'Во сне, во сне')], 'adapted'),
    ('kostya', 'Ну расскажи мне об этом подробнее.', 'Well, tell me about that in more detail.', [(29, 'Расскажи подробнее')], 'adapted'),
    ('denis', 'Она позвала меня в кабинет помочь.', 'She called me into the office to help.', [(30, 'она меня позвала в кабинет')], 'adapted'),
    ('denis', 'Там она целует меня на диване.', 'In there she kisses me on the couch.', [(31, 'целует меня, заваливает на диван')], 'adapted'),
    ('denis', 'Я говорю ей: Вика, не надо!', 'I say to her: Vika, do not do that!', [(32, 'Я говорю, Вика, не надо')], 'adapted'),
    ('denis', 'Катя, мне нужно с тобой поговорить!', 'Katya, I need to talk with you!', [(36, 'Ой, Катя, мне нужно с тобой поговорить')], 'adapted'),
    ('denis', 'Катя, постой, я всё тебе объясню!', 'Katya, wait, I will explain everything to you!', [(37, 'Катя, я все объясню')], 'adapted'),
]
WALK = [
    (0, None, "'Hey there, you really scared us yesterday!' Kostya weighs in evenly toward Denis, refusing to let the moment slip past."),
    (1, None, "'Kostya, I got scared myself yesterday too.' Denis speaks plainly across the room, testing Kostya's reaction in the middle of the exchange."),
    (2, None, '\'Tell me, how did all of this happen yesterday?\' Kostya pushes back directly before Denis and chooses "proizoshlo" ("happened", from the root "proizoyti") so Denis hears the exact meaning.'),
    (3, None, "'Do you remember I told you about my dreams?' Discussing his dreams in the exchange, Denis keeps normal statement word order here, turning the line into a question for Kostya purely through rising pitch."),
    (4, None, "'Well then, that woman was Vika.' Denis weighs in right away during the talk, so Kostya knows he is not just making small talk."),
    (5, None, '\'Wait, you mean Vika in your dream?\' Underscoring the dream beside Denis, Kostya brings in "podozhdi" ("wait", from "podozhdat") as the key Russian word here.'),
    (6, None, '\'Well, tell me about that in more detail.\' Kostya cuts in promptly in front of Denis and lands on "podrobneye" ("detail", built on "podrobniy") to keep the statement grounded.'),
    (7, None, "'She called me into the office to help.' Denis opens up right away without holding back, making his position completely clear."),
    (8, None, '\'In there she kisses me on the couch.\' Turning to the sofa during the talk, Denis brings in "divane" ("sofa", from "divan") as the key Russian word here.'),
    (9, None, '\'I say to her: Vika, do not do that!\' Replying quietly during the talk, Denis leans on "nado" ("it is necessary, one needs to"), which carries the whole predicate in Russian without needing "it is".'),
    (10, None, "'Katya, I need to talk with you!' Denis opens up earnestly facing Kostya, before Kostya can change the subject."),
    (11, None, '\'Katya, wait, I will explain everything to you!\' Denis jumps in evenly during the talk and chooses "obyasnyu" ("I\'ll explain", from the root "obyasnit") so Kostya hears the exact meaning.'),
]
