# Authoring module for kukhnya-s06e16-scene-03.
ID = 'kukhnya-s06e16-scene-03'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 16
SCENE = 3
TITLE = 'Концерт в Кремле  (Concert in the Kremlin)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.16'
SOURCE_FILE = 'sources/kukhnya/s06/e16.ru.srt'
INTRO = "The designer's translator explains that Olaf only dresses big celebrities in Russia so he can build his brand in the new market. Thinking fast after the translator steps away for coffee, Chef Barinov claims that his fiancée Elena is a famous Russian pop star!"
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Intrigued by the mention of a Kremlin concert, Olaf calls his translator back to verify if Elena is truly a superstar. Until next time!'
CLOSING = ('guest', 'Пока!')
STORY = [
    ('guest', 'Это бесполезно, он ничего не продаст.', 'It is useless, he will not sell anything.', [(33, 'Бесполезно. Он вам ничего не продаст')], 'adapted'),
    ('guest', 'Россия для него совсем новый рынок.', 'Russia is a brand-new market for him.', [(34, 'Россия для него новый рынок')], 'adapted'),
    ('guest', 'В его платьях ходят только звёзды.', 'Only stars wear his dresses.', [(35, 'в его платьях')], 'adapted'),
    ('guest', 'Будь добр, принеси мне горячий кофе.', 'Be so kind, bring me a hot coffee.', [(36, 'будь добр, принеси мне кофе')], 'adapted'),
    ('guest', 'Извините, но мои платья не продаются.', 'Excuse me, but my dresses are not for sale.', [(37, 'Извините, но мои платья не продаются')], 'adapted'),
    ('barinov', 'Очень жаль, что платья не продаются.', 'It is a great pity that the dresses are not for sale.', [(38, 'Очень жаль')], 'adapted'),
    ('barinov', 'Моя жена хотела дать большой концерт.', 'My wife wanted to give a big concert.', [(39, 'Моя жена хотела дать концерт')], 'adapted'),
    ('barinov', 'Она мечтала петь именно в вашем платье.', 'She dreamed of singing in your dress specifically.', [(39, 'именно в вашем платье')], 'adapted'),
    ('guest', 'Подождите, ваша жена большая знаменитость?', 'Wait, is your wife a big celebrity?', [(40, 'Она знаменитость')], 'adapted'),
    ('barinov', 'Да, её зовут певица Елена.', 'Yes, her name is the singer Elena.', [(41, 'Да. Как вы сказали, Елена')], 'adapted'),
    ('barinov', 'Она у нас очень известная певица.', 'She is a very famous singer in our country.', [(44, 'Очень известная')], 'adapted'),
    ('guest', 'Прошу прощения, никогда о ней не слышал.', 'I beg your pardon, I have never heard of her.', [(46, 'Прошу прощения, никогда о ней не слышал')], 'adapted'),
]
WALK = [
    (0, None, "'It is useless, he will not sell anything.' The guest follows up lightly hearing Barinov, letting the remark speak for itself."),
    (1, None, '\'Russia is a brand-new market for him.\' Focusing on the market right here, the guest puts the emphasis on "novyy" ("new") in the middle of the talk.'),
    (2, None, '\'Only stars wear his dresses.\' Bringing up the dress at once, the guest centers the thought on "platyakh" ("dress, gown", from "platye") without wasting a word.'),
    (3, None, "'Be so kind, bring me a hot coffee.' The guest weighs in evenly around Barinov, shifting the mood of the conversation in a single beat."),
    (4, None, '\'Excuse me, but my dresses are not for sale.\' Addressing the dress to Barinov, the guest puts the weight on "prodayutsya" ("to be sold", from "prodavatsya") as the exchange unfolds.'),
    (5, None, '\'It is a great pity that the dresses are not for sale.\' Pointing to the dress with the guest, Barinov leans on "zhal" ("it is a pity"), which carries the whole predicate in Russian without needing "it is".'),
    (6, None, "'My wife wanted to give a big concert.' Barinov jumps in honestly without any doubt, watching the guest's face to see how the news lands."),
    (7, None, '\'She dreamed of singing in your dress specifically.\' Talking about the dress beside the guest, Barinov reaches for the Russian word "platye" ("a dress") right at the heart of the line.'),
    (8, None, "'Wait, is your wife a big celebrity?' Stressing how large things are at once, the guest keeps normal statement word order here, turning the line into a question for Barinov purely through rising pitch."),
    (9, None, "'Yes, her name is the singer Elena.' Barinov proceeds decisively hearing the guest, grounding the moment in plain reality."),
    (10, None, '\'She is a very famous singer in our country.\' Noting how famous she is with the guest, Barinov leans on "izvestnaya" ("famous, well-known", a form of "izvestnyy") to give the remark its edge.'),
    (11, None, '\'I beg your pardon, I have never heard of her.\' Pointing to the forgiveness right here, the guest pairs the negative word with "ne" ("not"), since Russian naturally doubles its negatives for emphasis.'),
]
