# Authoring module for kukhnya-s01e08-scene-02.
ID = 'kukhnya-s01e08-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 2
TITLE = 'Спор в прямом эфире  (On-Air Debate)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Back in the television studio, the cooking show is on air. Barinov is cooking young lamb, and beside him sits his rival, Elena Sokolova, who runs Arcobaleno, the Italian restaurant across the road. He picks this moment to say what he thinks about women in kitchens. It's in Russian first."
OPENER = "Let's go back through it. Barinov stirs things up, and Elena answers him calmly and firmly."
TRANSITION = "Now let's hear the two of them again without stopping."
OUTRO = "Elena's lines are the ones to keep: u menya yest opyt, 'I have experience', and kukhnya, eto vsya moya zhizn, 'the kitchen is my whole life'. Swap in your own work and they're yours. See you next time."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Сегодня я приготовлю мясо молодого ягнёнка.', 'Today I will prepare meat of a young lamb.', [(20, 'Я приготовлю сегодня жигой гненка')], ''),
    ('elena', 'Какое интересное и сложное мясное блюдо!', 'What an interesting and complex meat dish!', [(22, 'Это блюдо')], ''),
    ('barinov', 'Такое блюдо лучше всего готовят мужчины.', 'Men prepare such a dish best of all.', [(22, 'лучше всего удается поварам-мужчинам')], ''),
    ('elena', 'Почему вы говорите такие странные вещи?', 'Why do you say such strange things?', [(28, 'вы действительно считаете, что')], ''),
    ('barinov', 'Женщины часто режут мясо совсем неправильно.', 'Women often cut meat completely incorrectly.', [(25, 'а женщинам что-то норовят поперек')], ''),
    ('elena', 'Вы просто не уважаете женский талант.', 'You simply do not respect female talent.', [], ''),
    ('barinov', 'Женщина не способна стать великим шефом.', 'A woman is not capable of becoming a great chef.', [(26, 'женщина априори не может быть хорошим поваром')], ''),
    ('elena', 'Я руковожу кухней известного ресторана Аркабалено!', 'I run the kitchen of the famous Arcobaleno restaurant!', [], ''),
    ('barinov', 'Настоящий шеф-повар требует сильной воли.', 'A real head chef requires strong willpower.', [(27, 'Женщина на кухне — это кухарка')], ''),
    ('elena', 'У меня есть опыт и сильная воля.', 'I have experience and strong willpower.', [], ''),
    ('barinov', 'Для вас кухня остаётся обычной работой.', 'For you the kitchen remains an ordinary job.', [], ''),
    ('elena', 'Кухня — это вся моя жизнь, Виктор!', 'The kitchen is my whole life, Viktor!', [], ''),
    ('barinov', 'Мы скоро проверим ваши смелые слова.', 'We will soon check your bold words.', [], ''),
]
WALK = [
    (0, None, "'Today I will prepare meat of a young lamb.' Like dokazhu earlier, prigotovlyu, 'I will prepare', looks present but means a finished job ahead. After myaso, 'meat', the lamb goes into the 'of' form: molodogo yagnyonka."),
    (1, None, "'What an interesting and complex meat dish!' Here kakoye, 'what a', ends in -oye to match blyudo, 'dish'. Russian says myasnoye blyudo, 'a meaty dish', turning myaso into a describing word."),
    (2, None, "'Men prepare such a dish best of all.' The phrase luchshe vsego, 'best of all', is literally 'better than everything'. Saving muzhchiny, 'men', for the end of the sentence gives it the punch."),
    (3, None, "'Why do you say such strange things?' Elena answers with vy, the polite 'you', to a man she barely knows. The plural veshchi comes from veshch, 'thing', a feminine word ending in a soft sign."),
    (4, None, "'Women often cut meat completely incorrectly.' In rezhut, 'they cut', the z of rezat turns into zh, and it stays zh in every present form. Putting ne in front of pravilno, 'correctly', gives nepravilno, written as one word."),
    (5, None, "'You simply do not respect female talent.' With vy, uvazhat, 'to respect', becomes uvazhayete. Pairs like zhenskiy, 'women's', and muzhskoy, 'men's', go with zhenshchina and muzhchina."),
    (6, None, "'A woman is not capable of becoming a great chef.' The short form sposobna, 'capable', ends in -a because he's talking about a woman. After stat, 'to become', what you become takes -im and -om: velikim shefom."),
    (7, None, "'I run the kitchen of the famous Arcobaleno restaurant!' Built from ruka, 'hand', and vodit, 'to lead', rukovozhu means 'I run, I'm in charge of'. What you run takes an -ey or -oy ending, so kukhnya becomes kukhney."),
    (8, None, "'A real head chef requires strong willpower.' With trebuyet, 'requires', the thing required takes the 'of' form, so silnaya volya turns into silnoy voli. The word volya means both 'will' and 'freedom'."),
    (9, None, "'I have experience and strong willpower.' Russian says 'I have' as u menya yest, literally 'by me there is'. She throws his own words, silnaya volya, straight back at him."),
    (10, None, "'For you the kitchen remains an ordinary job.' After ostayotsya, 'remains', the role takes -oy endings: obychnoy rabotoy. Even while needling her, Barinov keeps the polite dlya vas, 'for you'."),
    (11, None, "'The kitchen is my whole life, Viktor!' A dash plus eto is a common way to say 'X is Y': kukhnya, eto vsya moya zhizn. The words vsya and moya are feminine because zhizn, 'life', is feminine despite its soft sign."),
    (12, None, "'We will soon check your bold words.' With proverim, 'we will check', he promises a single test ahead. The word smelyye, 'bold', is related to smelost, 'courage'."),
]
