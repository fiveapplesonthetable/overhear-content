# Authoring module for domashniy-arest-s01e04-scene-16.
ID = 'domashniy-arest-s01e04-scene-16'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 4
SCENE = 16
TITLE = "Компромат Клавдии  (Klavdia's Kompromat)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'klavdia': 'Клавдия Викторовна'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.04'
SOURCE_FILE = 'sources/domashniy-arest/s01/e04.ru.dual.srt'
INTRO = "Last time, Arkady dressed Samson in a simple sweater and work jacket and warned the family against provocations. Stepping out into the corridor in high spirits, Arkady runs into old Klavdia Viktorovna, who shows him a terrible video of drunken Samson on her smartphone and demands a high-tech price for her silence. We'll hear it in Russian first; don't worry about catching every word."
OPENER = "Let's go back through their conversation. Arkady steps into the dim hallway smiling to himself, and Klavdia Viktorovna stops him."
TRANSITION = "Let's listen to the whole hallway negotiation again from the beginning."
OUTRO = "So Klavdia Viktorovna has Arkady over a barrel, and he has until evening to find her a brand-new television with 3D glasses. Listen for 'mood', 'candidate', and 'television' when you watch. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('klavdia', 'Я гляжу, ты, Аркашенька, довольный такой.', "I see you're looking so pleased, Arkashenka.", [(613, 'Я гляжу, ты, Аркашенька, довольный такой')], ''),
    ('arkady', 'Настроение у меня действительно очень хорошее.', 'My mood really is very good.', [(617, 'настроения'), (618, 'у меня действительно очень')], "cue 618 'Она ... хорошая' normalised to neuter 'Настроение ... хорошее'"),
    ('klavdia', 'Я сейчас, Аркашенька, свет этот тебе потушу.', "I'm about to turn that light off for you, Arkashenka.", [(620, 'я сейчас, Аркашенька, свет этот тебе потушу')], "'Ну так' trimmed for sentence length"),
    ('arkady', 'Что вы имеете в виду, Клавдия Викторовна?', 'What do you mean, Klavdia Viktorovna?', [(615, 'Клавдия Викторовна'), (621, 'Что вы имеете в виду')], "'ягодка моя' replaced with 'Клавдия Викторовна'"),
    ('klavdia', 'Вот гляди, кандидат твой во всей красе!', 'Take a look: your candidate in all his glory!', [(622, 'Вот гляди, кандидат твой во всей красе')], ''),
    ('arkady', 'Что это за ужас такой? И когда это было?', 'What on earth is this horror? And when was this?', [(623, 'Что это за ужас такой'), (625, 'когда это было')], 'crude cue 624 omitted'),
    ('klavdia', 'О, это, Аркашенька, бывает очень часто. Песни орём!', 'Oh, that happens very often, Arkashenka. Bellowing songs!', [(626, 'О, это, Аркашенька, бывает очень часто'), (627, 'песни орём')], 'crude cue 628 omitted'),
    ('arkady', 'Это кошмар, я не спорю. Но зачем на видео снимать?', "That's a nightmare, I don't argue. But why film it on video?", [(629, 'Это кошмар, я не спорю, но зачем на видео снимать')], 'split into two short sentences'),
    ('klavdia', 'А я участковому хотела показать.', 'I wanted to show it to the local policeman.', [(630, 'А участковому хотела показать')], "'я' added"),
    ('arkady', 'Отдайте это видео мне. А мы обеспечим вам достойную старость.', 'Give this video to me. And we will ensure you a comfortable old age.', [(632, 'отдайте это видео мне, а мы'), (632, 'обеспечим вам достойную старость')], 'split into two short sentences'),
    ('klavdia', 'Лучше я это в новости отправлю. Мне пятнадцать тысяч переведут.', "No, I'd rather send this to the news. They'll transfer fifteen thousand to my card.", [(635, 'лучше я это в'), (636, 'мне'), (636, 'переведут')], "cue 635 'в Лах-Ньюс залью' -> 'в новости отправлю'; '15' written out as 'пятнадцать'; crude 634 omitted"),
    ('klavdia', 'У меня вот смартфон и приложение имеется.', 'I have a smartphone and the app right here.', [(637, 'У меня вот смартфон и приложение имеется')], ''),
    ('arkady', 'Какая вы прогрессивная бабушка! Что вы хотите за это видео?', 'What a modern grandma you are! What do you want for this video?', [(638, 'Какая вы'), (638, 'прогрессивная бабушка'), (639, 'Что вы хотите за это видео')], "'все-таки' trimmed"),
    ('klavdia', 'Телевизор! И чтобы поддерживал три-дэ и смарт-телевизор!', 'A television! And it has to support 3D and Smart TV!', [(640, 'Телевизор'), (646, 'и чтобы поддерживал')], "'3D и смарт-ТВ' written in Cyrillic as 'три-дэ и смарт-телевизор'"),
    ('klavdia', 'И очки в комплекте!', 'And glasses included!', [(647, 'И очки в комплекте')], ''),
]
WALK = [
    (0, None, "'I see you're looking so pleased, Arkashenka.' She uses an affectionate diminutive of his name, Arkasha, and the masculine adjective for 'pleased' or 'content'."),
    (1, None, "'My mood really is very good.' Literally 'the mood by me really is very good'. Notice the neuter ending '-oye' to match 'mood'. He adds that he can finally see light at the end of the tunnel, and Klavdia pounces on that image."),
    (2, None, "'I'm about to turn that light off for you, Arkashenka.' The verb at the end means 'I will extinguish' or 'put out'. Arkady is puzzled."),
    (3, None, "'What do you mean, Klavdia Viktorovna?' Literally 'what do you have in view?'. She holds up her phone and presses play."),
    (4, None, "'Take a look: your candidate in all his glory!' An informal command, 'look', followed by the idiom 'in all his beauty'. On the screen, Samson is roaring drunk. Arkady is horrified."),
    (5, 'Что это за ужас такой?', "'What on earth is this horror?' The construction 'what is this for a...' means 'what kind of... is this?'."),
    (5, 'И когда это было?', "'And when was this?' Neuter past tense of 'to be'."),
    (6, 'О, это, Аркашенька, бывает очень часто.', "'Oh, that happens very often, Arkashenka.' This verb means 'happens regularly'."),
    (6, 'Песни орём!', "'Bellowing songs!' Literally 'we yell songs': she uses 'we' sarcastically to describe her noisy neighbours."),
    (7, 'Это кошмар, я не спорю.', "'That's a nightmare, I don't argue.' Arkady centres the line on the verb for 'argue' alongside the noun for 'nightmare'."),
    (7, 'Но зачем на видео снимать?', "'But why film it on video?' Literally 'for what purpose to shoot onto video?'. Klavdia has a ready answer."),
    (8, None, "'I wanted to show it to the local policeman.' The noun is actually an adjective used as a noun: the officer in charge of the local district, here in the 'to' case. Arkady switches into politician mode."),
    (9, 'Отдайте это видео мне.', "'Give this video to me.' Polite plural command."),
    (9, 'А мы обеспечим вам достойную старость.', "'And we will ensure you a comfortable old age.' Literally 'a worthy old age', once they win the election. Klavdia was not born yesterday."),
    (10, 'Лучше я это в новости отправлю.', "'I'd rather send this to the news.' If that video goes online, Samson's campaign is over before it begins."),
    (10, 'Мне пятнадцать тысяч переведут.', "'They'll transfer fifteen thousand to me.' Impersonal plural: 'they will transfer to me'."),
    (11, None, "'I have a smartphone and the app right here.' Even at eighty, Klavdia knows how citizen-journalism apps pay for scoop videos."),
    (12, 'Какая вы прогрессивная бабушка!', "'What a modern grandma you are!' Literally 'what a progressive grandmother'."),
    (12, 'Что вы хотите за это видео?', "'What do you want for this video?' After 'for' in a trade or exchange, the noun takes the object-form. Klavdia names her price."),
    (13, 'Телевизор!', "'A television!' One word, and then the technical specifications."),
    (13, 'И чтобы поддерживал три-дэ и смарт-телевизор!', "'And it has to support 3D and Smart TV!' Literally 'and so that it would support'. She also demands a forty-inch screen. And one last detail."),
    (14, None, "'And glasses included!' Literally 'and glasses in the set', so she can watch her favourite singer Lev Leshchenko in three dimensions."),
]
