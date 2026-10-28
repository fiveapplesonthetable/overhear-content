# Authoring module for kukhnya-s01e07-scene-16.
ID = 'kukhnya-s01e07-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 7
SCENE = 16
TITLE = 'Предложение соседа  (A Roommate Offer)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.07'
SOURCE_FILE = 'sources/kukhnya/s01/e07.ru.dual.srt'
INTRO = 'Late in the day at Claude Monet, Max still has nowhere to sleep. The bartender, Kostya, has cooled down after their row, and at the bar he offers Max a room in his new flat. There are some useful housing phrases in the Russian.'
OPENER = "Let's go through the offer. Kostya is generous, and Max is suspicious of luck."
TRANSITION = 'Now the offer from beginning to end.'
OUTRO = "Two phrases to keep from this one: 'I have nowhere to live' and 'around ten in the evening'. Bye for now."
CLOSING = ('max', 'Пока!')
STORY = [
    ('kostya', 'Макс, я слышал, у тебя проблема с жильём.', 'Max, I heard you have a problem with housing.', [(319, 'А я слышал, у тебя с жильем проблема')], ''),
    ('max', 'Да, мне совсем негде жить в Москве.', 'Yes, I have nowhere to live in Moscow at all.', [], ''),
    ('kostya', 'Хочешь пожить у меня пару недель?', 'Do you want to live at my place for a couple of weeks?', [(320, 'Хочешь, поживи у меня пару недель')], ''),
    ('max', 'Ты говоришь абсолютно серьёзно, Костя?', 'Are you speaking completely seriously, Kostya?', [(321, 'Серьезно')], ''),
    ('kostya', 'Конечно, без всяких проблем, мой друг!', 'Of course, without any problems, my friend!', [(321, 'Ну, конечно, без')], ''),
    ('kostya', 'Вот точный адрес моей новой квартиры.', 'Here is the exact address of my new apartment.', [(322, 'вот тут адрес')], ''),
    ('kostya', 'Я приеду домой около десяти вечера.', 'I will arrive home around ten in the evening.', [(323, 'к десяти уже буду дома')], ''),
    ('max', 'Отлично, я приду туда прямо вовремя.', 'Excellent, I will come right on time there.', [(324, 'Давай подтягивайся')], ''),
    ('max', 'Может, мне купить что-нибудь вкусное к чаю?', 'Maybe I should buy something tasty for tea?', [(325, 'Слушай, а может, что купить надо')], ''),
    ('kostya', 'Купи лучше красивый букет цветов.', 'Better buy a pretty bouquet of flowers.', [(326, 'цветок букетик купи')], ''),
    ('max', 'Зачем нам с тобой нужны цветы?', 'Why do you and I need flowers?', [], ''),
    ('kostya', 'В этой квартире живёт пожилая хозяйка.', 'An elderly landlady lives in this apartment.', [(326, 'я за бабулей живу просто')], ''),
    ('max', 'Понял, я куплю самые свежие цветы!', 'Understood, I will buy the freshest flowers!', [], ''),
    ('kostya', 'Тогда договорились, жду тебя сегодня вечером!', 'Then agreed, I am waiting for you tonight!', [(328, 'Спасибо')], ''),
]
WALK = [
    (0, None, '\'Max, I heard you have a problem with housing.\' U tebya problema, \'at you a problem\', is the Russian \'you have a problem\'. "Zhil\'yo", housing, becomes zhil\'yom after s, \'with\'.'),
    (1, None, '\'Yes, I have nowhere to live in Moscow at all.\' "Negde", \'nowhere\', with mne, \'to me\', and an infinitive makes \'I have nowhere to live\'. For movement it would be nekuda, \'nowhere to go\'.'),
    (2, None, '\'Do you want to live at my place for a couple of weeks?\' "Paru nedel\'", \'a couple of weeks\', puts nedelya into its \'of\' plural after para. "Pozhit\'", to live for a while, is what Kostya once offered Nastya.'),
    (3, None, '\'Are you speaking completely seriously, Kostya?\' "Ser\'yozno", \'seriously\', on its own is the everyday \'really?\'. "Absolyutno" is easy to recognise as \'absolutely\'.'),
    (4, None, '\'Of course, without any problems, my friend!\' "Bez", \'without\', takes the \'of\' form, so problemy becomes problem. "Vsyakikh", \'any kind of\', is from vsyakiy.'),
    (5, None, '\'Here is the exact address of my new apartment.\' "Vot", \'here is\', points at something with no verb needed. "Moyey novoy kvartiry" all take the feminine \'of\' ending, since kvartira is feminine.'),
    (6, None, '\'I will arrive home around ten in the evening.\' "Okolo", \'around\', changes desyat\' to desyati, the \'of\' ending. "Priedu" is for arriving by transport; on foot it would be pridu.'),
    (7, None, '\'Excellent, I will come right on time there.\' "Pridu" is the on-foot partner of Kostya\'s priedu. "Tuda", \'there\', means \'to there\', with movement.'),
    (8, None, '\'Maybe I should buy something tasty for tea?\' "Chto-nibud\'", \'something\', is chto plus -nibud\', \'anything at all\'. K chayu, \'for tea\', uses k, \'toward\'.'),
    (9, None, '\'Better buy a pretty bouquet of flowers.\' "Kupi luchshe", \'buy better\', means \'you\'d better buy\'. In buket tsvetov, \'a bouquet of flowers\', tsvety becomes tsvetov.'),
    (10, None, '\'Why do you and I need flowers?\' "Nam" s toboy, \'to us with you\', means \'you and I\'. "Nuzhny", \'needed\', is plural to match tsvety.'),
    (11, None, '\'An elderly landlady lives in this apartment.\' "Pozhilaya", \'elderly\', is a polite word for old. "Khozyayka" is the landlady, as in Nastya\'s story.'),
    (12, None, '\'Understood, I will buy the freshest flowers!\' "Kuplyu", \'I will buy\', adds an l that kupit\' doesn\'t have. "Samye svezhie", \'the freshest\', uses samyy for \'most\'.'),
    (13, None, '\'Then agreed, I am waiting for you tonight!\' "Dogovorilis\'", \'agreed\', closes the plan, as it did for Nagiyev. "Zhdu tebya", \'I wait for you\', means \'I\'ll be expecting you\'.'),
]
