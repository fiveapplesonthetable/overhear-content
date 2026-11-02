# Authoring module for kukhnya-s01e05-scene-19.
ID = 'kukhnya-s01e05-scene-19'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 19
TITLE = 'Хитрый план  (A Cunning Plan)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "At the Claude Monet bar, Kostya the bartender and Sasha the waitress compare notes. They've been staging a little game to make Max jealous, and Sasha has just told Max a story of her own. Kostya wants to make the fake plan look more real. Listen in Russian first."
OPENER = "Let's go slowly. They're plotting, so the lines come out quick and low."
TRANSITION = 'Now the whole plot again, without breaks.'
OUTRO = 'Listen for the words that mean "listen", "maybe" and "agreed". Those three little words are how Russians float a plan to a friend and then seal it.'
CLOSING = ('sasha', 'Пока!')
STORY = [
    ('kostya', 'Саша, ну что, ты сказала Максу?', 'Sasha, well, did you tell Max?', [(278, 'ты сказала Максу')], ""),
    ('sasha', 'Да, я сказала, что забыла его.', "Yes, I said I'd forgotten him.", [(264, 'я тебя уже забыла'), (279, 'Сказала')], ""),
    ('kostya', 'И как он на это отреагировал?', 'And how did he react to that?', [(280, 'Ну и что он')], ""),
    ('sasha', 'Он очень сильно удивился и расстроился.', 'He was very surprised and upset.', [(281, 'Расплакался')], ""),
    ('kostya', 'Мне даже немного жалко его стало.', 'I even felt a little sorry for him.', [(282, 'Мне даже его жалко стало')], ""),
    ('sasha', 'Ты только никому не рассказывай правду.', 'Just do not tell anyone the truth.', [(286, 'не говорили, что мы')], ""),
    ('kostya', 'Конечно, никто ничего не узнает.', 'Of course, no one will find out anything.', [(287, 'Понятное дело')], ""),
    ('sasha', 'Спасибо, ты настоящий верный друг!', "Thank you, you're a true, loyal friend!", [], ""),
    ('kostya', 'Слушай, а может мы сходим куда-нибудь?', 'Listen, maybe we should go somewhere?', [(288, 'а может мы с тобой повстречаемся')], ""),
    ('sasha', 'Куда именно ты предлагаешь пойти?', 'Where exactly do you suggest going?', [], ""),
    ('kostya', 'Давай сходим в кино вместе.', 'Let us go to the movies together.', [(290, 'в кино, я не знаю, сходим')], ""),
    ('kostya', 'Это нужно для правдоподобности нашего плана.', 'This is needed for the believability of our plan.', [(289, 'Для правдоподобности')], ""),
    ('sasha', 'Отличная идея, пойдём сегодня вечером!', 'Great idea, let us go tonight!', [(291, 'ну давай')], ""),
    ('kostya', 'Договорились, тогда встретимся после работы.', 'Agreed, then let us meet after work.', [(291, 'Так точно никто не догадается')], ""),
]
WALK = [
    (0, None, ["'Sasha, well, did you tell Max?' is a casual ", ('kostya', 'ну'), ('kostya', 'что,'), " 'so?'. ", ('kostya', 'сказала'), ' has the feminine past ending because Sasha is a woman, and ', ('kostya', 'Максу?'), ", meaning 'to Max', takes the dative ending."]),
    (1, None, ["'Yes, I said I'd forgotten him.' and ", ('sasha', 'сказала,'), ('sasha', 'забыла'), ' share the feminine past ending, because Sasha is talking about herself. ', ('sasha', 'что'), " here implies 'that', acting as the word that joins the two halves."]),
    (2, None, ["\'And how did he react to that?\' is built from the English \'react\' with a Russian prefix and ending. ", ('kostya', 'отреагировал?'), " Russians react \'on\' something: ", ('kostya', 'на'), ('kostya', 'это'), ", \'on that\'."]),
    (3, None, ["'He was very surprised and upset.' and ", ('sasha', 'удивился'), ('sasha', 'расстроился.'), " both carry the reflexive suffix, to express 'got surprised' and 'got upset'. ", ('sasha', 'очень'), ('sasha', 'сильно'), ", 'very strongly', together just translates to 'really'."]),
    (4, None, ["'I even felt a little sorry for him.' is literally 'to me pity him ", ('kostya', 'Мне'), ('kostya', 'жалко'), ('kostya', 'его'), ('kostya', 'стало.'), " became'. The one who feels sorry is ", ('kostya', 'Мне'), ", 'to me', and the one pitied is ", ('kostya', 'его'), '.']),
    (5, None, ["'Just do not tell anyone the truth.' literally translates to 'don't tell', and ", ('sasha', 'не'), ('sasha', 'рассказывай'), " Sasha is used for it as a plea. The word for 'truth' becomes ", ('sasha', 'правду.'), ' because it is the thing not told.']),
    (6, None, ["'Of course, no one will find out anything.' stacks three negatives, and Russian needs ", ('kostya', 'никто'), ('kostya', 'ничего'), ('kostya', 'не'), ('kostya', 'узнает.'), ' all of them. ', ('kostya', 'узнает.'), " implies completion, so it forms the future: 'will find out'."]),
    (7, None, ["'Thank you, you're a true, loyal friend!' can translate to 'true' or 'real', ", ('sasha', 'настоящий'), " and ", ('sasha', 'верный'), " translates to 'loyal' or 'faithful'. Both have the masculine endings to match ", ('sasha', 'друг!'), '.']),
    (8, None, ["'Listen, maybe we should go somewhere?' A ", ('kostya', 'может'), " is a casual 'or maybe', used to suggest something. ", ('kostya', 'куда-нибудь?'), " translates to 'somewhere', and the suffix implies 'some place or other'."]),
    (9, None, ["'Where exactly do you suggest going?' literally translates to 'where to', for ", ('sasha', 'Куда'), " movement. ", ('sasha', 'предлагаешь'), ", 'you suggest', leads straight into ", ('sasha', 'пойти?'), ", 'to go'."]),
    (10, None, ["'Let us go to the movies together.' , 'cinema', is borrowed and never ", ('kostya', 'кино'), " changes its ending. ", ('kostya', 'Давай'), ('kostya', 'сходим'), " literally translates to 'let's go', for a trip there and back."]),
    (11, None, ["'This is needed for the believability of our plan.' joins the words for 'truth' and ", ('kostya', 'правдоподобности'), " 'similar', so literally 'truth-likeness'. After ", ('kostya', 'для'), ", 'for', it changes form."]),
    (12, None, ["'Great idea, let us go tonight!' is 'today in the evening', and ", ('sasha', 'сегодня'), ('sasha', 'вечером!'), " the ending on the word for 'evening' does the work of 'in'. ", ('sasha', 'пойдём'), ", 'let's go', is a common way to say yes to a plan."]),
    (13, None, ["'Agreed, then let us meet after work.' , 'agreed', literally 'we've talked it ", ('kostya', 'Договорились,'), " erally 'we've talked it into an agreement', closes the deal. After ", ('kostya', 'после'), ", 'after', the word for 'work' becomes ", ('kostya', 'работы.'), '.']),
]
