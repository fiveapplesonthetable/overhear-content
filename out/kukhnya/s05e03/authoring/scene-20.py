# Authoring module for kukhnya-s05e03-scene-20.
ID = 'kukhnya-s05e03-scene-20'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 3
SCENE = 20
TITLE = 'Спасение Дениса и новый Аркадий  (Saving Denis and the New Arkady)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'denis': 'Денис', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.03'
SOURCE_FILE = 'sources/kukhnya/s05/e03.ru.srt'
INTRO = 'In the closing scene of Episode 3, Kostya and Nastya smuggle Denis out of room 205 on a laundry cart just before Eleonora opens the door, and Katya tells her father why Eleonora decided to keep him on. Listen to the finale.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that brings Episode 3 to a close as Denis narrowly escapes Eleonora's trap, though his guilty secret still weighs on him. See you in Episode 4. See you next time!"
CLOSING = ('katya', 'Пока!')
STORY = [
    ('katya', 'Мама, пойдём скорее отсюда.', "Mom, let's get out of here quickly.", [(351, 'Мам, пойдем?')], 'adapted'),
    ('katya', 'Может быть, он сейчас в душе.', 'Maybe he is in the shower right now.', [(352, 'Может быть, он в душе')], 'verbatim'),
    ('denis', 'Отпусти его, они уже ушли!', 'Let him go, they have left already!', [(353, 'его, они ушли!')], 'adapted'),
    ('denis', 'Слабость может превратиться в большую тайну.', 'A weakness can turn into a big secret.', [(355, 'слабость'), (355, 'тайну')], 'adapted'),
    ('denis', 'Тайна может разрушить нам всю жизнь.', 'A secret can destroy our whole life.', [(356, 'разрушить нам жизнь')], 'adapted'),
    ('barinov', 'Поздравляю тебя с новосельем!', 'Congratulations on your housewarming!', [(357, 'С новосельем!')], 'adapted'),
    ('barinov', 'Они у меня долго не живут.', 'They do not live long with me.', [(359, 'Да, они у меня долго не живут')], 'verbatim'),
    ('denis', 'Кто-то хранит тайны ради своих близких.', 'Someone keeps secrets for the sake of loved ones.', [(360, 'Кто-то хранит тайны ради своих близких')], 'verbatim'),
    ('barinov', 'Твоя мама меня почему-то не увольняет.', 'For some reason your mom is not firing me.', [(361, 'меня не увольняет')], 'adapted'),
    ('barinov', 'Она обещала. Не знаешь почему?', 'She promised to. Do you know why?', [(362, 'Обещала. Не знаешь почему?')], 'verbatim'),
    ('katya', 'Да, папа, я это знаю.', 'Yes, Dad, I know why.', [(363, 'Знаю')], 'adapted'),
    ('katya', 'Потому что ты очень крутой шеф.', 'Because you are a really cool chef.', [(364, 'Ты крутой шеф')], 'adapted'),
    ('denis', 'Кто-то готов разлучить близких людей.', 'Someone is ready to separate close people.', [(366, 'Кто-то готов разлучить близких людей')], 'verbatim'),
    ('denis', 'А кто-то не может доверить тайну себе.', 'And someone cannot entrust a secret even to himself.', [(368, 'кто-то не может доверить тайну'), (368, 'себе')], 'adapted'),
]
WALK = [
    (0, None, "'Mom, let's get out of here quickly.' Turning to the mum in the exchange, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (1, None, "'Maybe he is in the shower right now.' Katya proceeds bluntly without a pause, shifting the mood of the conversation in a single beat."),
    (2, None, '\'Let him go, they have left already!\' Denis fires back smoothly during the talk and reaches for the Russian word "otpusti" ("let go, release", built from "otpustit") right at the center of the line.'),
    (3, None, '\'A weakness can turn into a big secret.\' Mentioning a weakness around Katya, the "-sya" ending on "prevratitsya" ("to turn into") marks an action that unfolds mutually or turns back on the speaker.'),
    (4, None, "'A secret can destroy our whole life.' Denis weighs in pointedly on the spot, refusing to let the moment slip past."),
    (5, None, '\'Congratulations on your housewarming!\' Pointing to the housewarming in the exchange, Barinov centers the thought on "novoselyem" ("housewarming", from "novoselye") without wasting a word.'),
    (6, None, "'They do not live long with me.' Barinov opens up dryly toward Denis, keeping the focus on what actually matters here."),
    (7, None, "'Someone keeps secrets for the sake of loved ones.' Denis responds quietly around Barinov, testing Barinov's reaction in the middle of the exchange."),
    (8, None, '\'For some reason your mom is not firing me.\' Talking about the mum beside Denis, Barinov chooses "pochemu-to" ("for some reason") so Denis gets the point right away.'),
    (9, None, '\'She promised to. Do you know why?\' Speaking dryly in this beat, Barinov puts the question word "pochemu" right at the start so Katya hears the focus immediately.'),
    (10, None, "'Yes, Dad, I know why.' Katya counters wryly facing Barinov, testing Barinov's reaction in the middle of the exchange."),
    (11, None, '\'Because you are a really cool chef.\' Insisting on how cool Barinov is beside Barinov, Katya puts the emphasis on "krutoy" ("cool") in the middle of the talk.'),
    (12, None, '\'Someone is ready to separate close people.\' Pointing out how ready things are at once, Denis reaches for the Russian word "blizkikh" ("close, near", built from "blizkiy") right at the center of the line.'),
    (13, None, "'And someone cannot entrust a secret even to himself.' Denis cuts in briskly without holding back, shifting the mood of the conversation in a single beat."),
]
