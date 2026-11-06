# Authoring module for dvorik-u-mosta-s01e01-scene-06.
ID = 'dvorik-u-mosta-s01e01-scene-06'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 1
SCENE = 6
TITLE = 'Бирка на чемодане  (The Luggage Tag)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'larisa': 'Лариса', 'yaroslav': 'Ярослав'}
INTRO = 'Back at the front desk, Kira, Larisa Borisovna, and Yaroslav lean over the blue suitcase under the desk lamp. Yaroslav finally puts his glasses to good use. Listen to the Russian scene first.'
OPENER = "Let's go back through the scene one line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "No luck at the train station yet, and the mysterious owner lives just five minutes away. Next time, Zoya steps in to rescue Larisa's evening."
CLOSING = ('yaroslav', 'Всего хорошего!')
STORY = [
    ('yaroslav', 'Вот это путаница! Дайте мне посмотреть на бирку в очках.', 'What a mix-up! Let me look at the tag with my glasses on.'),
    ('larisa', 'Там есть фамилия или номер телефона?', 'Is there a surname or a phone number there?'),
    ('yaroslav', 'Телефона, к сожалению, нет. Только две буквы и старое название улицы.', 'No phone number, unfortunately. Only two letters and an old street name.'),
    ('kira', 'Подождите — эта улица совсем рядом, пять минут пешком!', 'Wait — that street is right nearby, five minutes on foot!'),
    ('larisa', 'Как странно! Мы ехали на одном утреннем поезде в один район.', 'How strange! We rode the same morning train to the same district.'),
    ('yaroslav', 'Кира, срочно позвоните на вокзал в бюро находок.', 'Kira, call the station lost-and-found office urgently.'),
    ('kira', 'Уже набираю... Алло! Кто-нибудь искал синий чемодан?', 'Dialling already... Hello! Was anyone looking for a blue suitcase?'),
    ('larisa', 'Скажите им, что у меня в верхнем кармане красная лента!', 'Tell them that mine has a red ribbon in the top pocket!'),
    ('kira', 'Пока нет? Запишите, пожалуйста, наш телефон и адрес. Спасибо!', 'Not yet? Please write down our phone number and address. Thank you!'),
    ('yaroslav', 'У них пока ничего нет, Лариса Борисовна, мне очень жаль.', 'They have nothing yet, Larisa Borisovna, I am very sorry.'),
    ('larisa', 'Вы ни в чём не виноваты. Просто на мне только одно пальто!', 'It is not your fault at all. It is just that I only have this one coat on!'),
    ('kira', 'Минутку — Зоя из кафе машет мне рукой, у неё есть идея!', 'One moment — Zoya from the café is waving at me, she has an idea!'),
]
WALK = [
    (0, None, ["'What a mix-up! Let me look at the tag with my glasses on.' Wearing glasses is expressed as 'in glasses' — ", (None, 'в очках.'), ' just like standing inside clothes.']),
    (1, None, ["'Is there a surname or a phone number there?' On luggage tags and hotel forms, ", (None, 'фамилия'), ' means family surname, never your whole family.']),
    (2, None, ["'No phone number, unfortunately. Only two letters and an old street name.' Slip ", (None, 'к сожалению,'), " into a sentence whenever you want to soften bad news with 'unfortunately'."]),
    (3, None, ["'Wait — that street is right nearby, five minutes on foot!' Walking distance uses the handy one-word expression ", (None, 'пешком!'), " meaning 'on foot'."]),
    (4, None, ["'How strange! We rode the same morning train to the same district.' Notice how ", (None, 'в один район.'), " uses the number 'one' to mean 'the very same' neighbourhood."]),
    (5, None, ["'Kira, call the station lost-and-found office urgently.' That station office has a memorable name, ", (None, 'бюро находок.'), " — literally 'office of finds', focusing on finding rather than losing!"]),
    (6, None, ["'Dialling already... Hello! Was anyone looking for a blue suitcase?' Answering or starting a phone call uses ", (None, 'Алло!'), ' while ', (None, 'Кто-нибудь'), " asks 'anyone at all?'."]),
    (7, None, ["'Tell them that mine has a red ribbon in the top pocket!' Again possession sits with the person: ", (None, 'у меня'), ' anchors the red ribbon to Larisa.']),
    (8, None, ["'Not yet? Please write down our phone number and address. Thank you!' Two tiny words, ", (None, 'Пока нет?'), " capture 'not yet?' — literally 'for now, no?'."]),
    (9, None, ["'They have nothing yet, Larisa Borisovna, I am very sorry.' Expressing sympathy or regret uses ", (None, 'мне очень жаль.'), " — literally 'to me it is a great pity'."]),
    (10, None, "'It is not your fault at all. It is just that I only have this one coat on!' Larisa reassures the anxious owner graciously, reminding us she is still standing there in her travel coat."),
    (11, None, ["'One moment — Zoya from the café is waving at me, she has an idea!' Asking someone to pause for a second shrinks 'minute' into warm, diminutive ", (None, 'Минутку'), " — 'just a little minute'."]),
]
