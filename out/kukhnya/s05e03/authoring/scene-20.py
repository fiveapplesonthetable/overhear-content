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
    (0, None, "'Mom, let's get out of here quickly.' Katya puts the comment toward Barinov: spoken Russian trims this down to just 4 words, dropping the extra helper words that English has to spell out."),
    (1, None, "'Maybe he is in the shower right now.' Katya stands firm bluntly with a shrug, so Denis knows she is not just making small talk."),
    (2, None, '\'Let him go, they have left already!\' Denis sharpens this vivid expression at once: "otpusti" means "let go, release" (from "otpustit"), giving the line its exact edge.'),
    (3, None, '\'A weakness can turn into a big secret.\' Denis voices that remark for Katya: the "-sya" ending on "prevratitsya" ("to turn into") turns the action inward or makes it happen between people naturally.'),
    (4, None, "'A secret can destroy our whole life.' Denis stands firm pointedly as things stand, saying out loud what both of them already know."),
    (5, None, '\'Congratulations on your housewarming!\' Barinov picks this sharp term for Katya: "pozdravlyayu" means "congratulations" (from "pozdravlyat"), giving the line its exact edge.'),
    (6, None, '\'They do not live long with me.\' Barinov shares the comeback beside Denis: Russian phrases this around "u menya" (literally "by me") rather than "I have", a pattern you will hear in almost every scene.'),
    (7, None, "'Someone keeps secrets for the sake of loved ones.' Denis reacts quietly hearing Katya, testing Katya's reaction in the middle of the exchange."),
    (8, None, '\'For some reason your mom is not firing me.\' Barinov spotlights one clear choice for Denis: "pochemu-to" means "for some reason", and it carries the main weight of what Barinov is saying.'),
    (9, None, '\'She promised to. Do you know why?\' Barinov frames this warning toward Katya: putting the question word "pochemu" right at the front of the line lets Katya hear the point of the question on the very first beat.'),
    (10, None, "'Yes, Dad, I know why.' Katya stands firm wryly during the talk, leaving no doubt about where she stands."),
    (11, None, '\'Because you are a really cool chef.\' Katya chooses one clear word with Denis: "krutoy" means "cool", and it carries the main weight of what Katya is saying.'),
    (12, None, "'Someone is ready to separate close people.' Denis steps in evenly to settle things, watching Barinov's face to see how the news lands."),
    (13, None, "'And someone cannot entrust a secret even to himself.' Denis reacts briskly with a shrug, before Katya can change the subject."),
]
