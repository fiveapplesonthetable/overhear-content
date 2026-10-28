# Authoring module for kukhnya-s06e05-scene-02.
ID = 'kukhnya-s06e05-scene-02'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 5
SCENE = 2
TITLE = "Проигрыш Михаила  (Mikhail's Gambling Loss)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя', 'mikhail': 'Михаил'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.05'
SOURCE_FILE = 'sources/kukhnya/s06/e05.ru.srt'
INTRO = 'Just as the fortune teller predicted, identical twin bellboys summon Chef Barinov upstairs to room two-oh-seven, where Mikhail Dzhekovich has gambled away everything he owns.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "While Chef Barinov hauls a broke Mikhail out of the card game, Kostya grows suspicious of Nastya's secretive morning errands. See you next time!"
CLOSING = ('kostya', 'Всего хорошего!')
STORY = [
    ('barinov', 'Прошу прощения, здесь мой друг.', 'Excuse me, my friend is in here.', [(25, 'Прошу прощения, у вас здесь мой друг')], 'adapted'),
    ('mikhail', 'Витя, это правда ты пришёл?', 'Vitya, is it really you who came?', [(26, 'Витя, Витенька, это ты')], 'adapted'),
    ('mikhail', 'Ты представляешь, я всё проиграл.', 'Can you imagine, I lost everything.', [(27, 'ты представляешь, я всё проиграл')], 'adapted'),
    ('mikhail', 'Я проиграл всё, что у меня было.', 'I lost everything that I had.', [(28, 'Всё, что у меня было')], 'adapted'),
    ('mikhail', 'Зачем я вообще с ним сел играть?', 'Why did I even sit down to play with him?', [(30, 'Зачем я вообще с ним сел играть')], 'adapted'),
    ('barinov', 'Вы его самого не выиграли?', 'Did you not win him too?', [(31, 'а вы его самого в рабство не выиграли')], 'adapted'),
    ('barinov', 'Жаль, тогда я его забираю.', 'Too bad, then I am taking him away.', [(32, 'Жаль. Ну тогда его забирают')], 'adapted'),
    ('kostya', 'Настя, ты телефон дома забыла.', 'Nastya, you forgot your phone at home.', [(35, 'Настя, а ты телефон дома забыла')], 'adapted'),
    ('barinov', 'Спасибо тебе большое, дорогой.', 'Thank you very much, my dear.', [(36, 'Спасибо')], 'adapted'),
    ('kostya', 'Скажи мне правду, пожалуйста.', 'Tell me the truth, please.', [(37, 'Скажи мне, пожалуйста')], 'adapted'),
    ('barinov', 'Гости за столиком уже ждут.', 'The guests at the table are already waiting.', [(38, 'Гости за восьмым столиком постарели уже')], 'adapted'),
    ('barinov', 'Иди быстрее прими у них заказ.', 'Go quickly and take their order.', [(39, 'Иди прими заказ')], 'adapted'),
]
WALK = [
    (0, None, "'Excuse me, my friend is in here.' Barinov replies pointedly around Kostya, steering the talk right where he wants it."),
    (1, None, "'Vitya, is it really you who came?' Mikhail asks curiously where this conversation is heading next."),
    (2, None, '\'Can you imagine, I lost everything.\' Mikhail focuses on one colorful element for Barinov: "predstavlyayesh" means "can you imagine" (from "predstavlyat"), giving the line its exact edge.'),
    (3, None, '\'I lost everything that I had.\' Mikhail states that point with warmth: Russian phrases this around "u menya" (literally "by me") rather than "I have", a pattern you will hear in almost every scene.'),
    (4, None, "'Why did I even sit down to play with him?' Mikhail questions wryly how Barinov expects that to work in practice."),
    (5, None, '\'Did you not win him too?\' Barinov colors this vivid piece right here: "samogo" means "the very" (from "samyy"), giving the line its exact edge.'),
    (6, None, '\'Too bad, then I am taking him away.\' Barinov frames that point frankly here: the single Russian word "zhal" ("it is a pity") sets up the whole statement without needing a separate word for "it is".'),
    (7, None, "'Nastya, you forgot your phone at home.' Kostya pushes back bluntly as things stand, making his position completely clear."),
    (8, None, '\'Thank you very much, my dear.\' Barinov emphasizes this clear touch in reply: "bolshoye" means "big, very much" (from "bolshoy"), giving the line its exact edge.'),
    (9, None, '\'Tell me the truth, please.\' Kostya aims that thought right away: dropping in "pozhaluysta" ("please") keeps the request polite on the surface even in a brisk exchange.'),
    (10, None, "'The guests at the table are already waiting.' Barinov reacts evenly with a shrug, saying out loud what both of them already know."),
    (11, None, '\'Go quickly and take their order.\' Barinov spotlights one direct word toward Mikhail: "bystreye" means "faster" (from "bystro"), giving the line its exact edge.'),
]
