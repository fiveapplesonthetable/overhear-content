# Authoring module for kukhnya-s01e03-scene-18.
ID = 'kukhnya-s01e03-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 18
TITLE = 'Праздничный гусь  (The Festive Goose)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = "The golden goose arrives at the guest of honour's table, and the chef presents it as though it were a triumph. Max chips in to help, and the guest is thrilled. Here is the Russian first."
OPENER = "Let's go through the presentation."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'The goose is a hit, which no one in the kitchen quite believes. Keep the wish before a meal in mind.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('guest', 'Скажите, пожалуйста, это мой праздничный гусь?', 'Tell me please, is that my festive goose?', [(319, 'Это мой гусь?')], ''),
    ('barinov', 'Да, это ваш главный заказ сегодня!', 'Yes, this is your main order today!', [], ''),
    ('barinov', 'Мы готовили его по старинному рецепту.', 'We prepared it according to an ancient recipe.', [], ''),
    ('max', 'Наш шеф лично проверял каждую деталь.', 'Our chef personally checked every detail.', [], ''),
    ('guest', 'Гусь выглядит и пахнет просто великолепно!', 'The goose looks and smells simply magnificent!', [], ''),
    ('barinov', 'Мясо получилось очень нежным и сочным.', 'The meat turned out very tender and juicy.', [], ''),
    ('max', 'Мы подали его с яблоками и травами.', 'We served it with apples and herbs.', [], ''),
    ('guest', 'Мои гости будут в полном восторге!', 'My guests will be in total delight!', [], ''),
    ('barinov', 'Наш ресторан держит только высший уровень.', 'Our restaurant maintains only the highest standard.', [], ''),
    ('guest', 'Спасибо вам за прекрасную работу, повара!', 'Thank you for the wonderful work, chefs!', [], ''),
    ('barinov', 'Приятного аппетита вам и вашим гостям!', 'Bon appetit to you and your guests!', [], ''),
    ('max', 'Надеемся увидеть вас снова в ресторане.', 'We hope to see you again at the restaurant.', [], ''),
    ('barinov', 'Макс, живо возвращайся обратно на кухню!', 'Max, quickly get back to the kitchen!', [], ''),
]
WALK = [
    (0, None, [
        "'Tell me please, is that my festive goose?' For this line, ",
        ('guest', 'Скажите, пожалуйста,'),
        " explicitly translates to 'say, please', a polite way to open a question. ",
        ('guest', 'это мой праздничный гусь?'),
        " is literally 'this my festive goose?'."
    ]),
    (1, None, [
        "'Yes, this is your main order today!' Barinov says ",
        ('barinov', 'ваш'),
        ", the polite word for 'your'. ",
        ('barinov', 'главный заказ'),
        " translates to 'main order'."
    ]),
    (2, None, [
        "'We prepared it according to an ancient recipe.' Here we see ",
        ('barinov', 'по'),
        " here means 'according to', and it changes the shapes of the words that follow it: ",
        ('barinov', 'по старинному рецепту.'),
        " The word for 'ancient' is ",
        ('barinov', 'старинному'),
        ", which is built from an old root meaning 'old times'."
    ]),
    (3, None, [
        "'Our chef personally checked every detail.' In Russian, ",
        ('max', 'проверял'),
        ", meaning 'checked', is an action word meant for checking over and over. ",
        ('max', 'каждую деталь.'),
        " translates to 'every detail'."
    ]),
    (4, None, [
        "'The goose looks and smells simply magnificent!' As you hear, ",
        ('guest', 'выглядит и пахнет'),
        " literally means 'looks and smells'. The word for 'magnificent', ",
        ('guest', 'великолепно!'),
        ", is built from the word for 'great' and an old term for 'beautiful'."
    ]),
    (5, None, [
        "'The meat turned out very tender and juicy.' Listen carefully, ",
        ('barinov', 'получилось'),
        " has a neutral shape to match the word for 'meat', ",
        ('barinov', 'Мясо'),
        ". The phrase ",
        ('barinov', 'нежным и сочным.'),
        " translates to 'tender and juicy' and takes a special shape after 'turned out'."
    ]),
    (6, None, [
        "'We served it with apples and herbs.' In this sentence, ",
        ('max', 'подали'),
        " translates to 'we served'. In the phrase ",
        ('max', 'с яблоками и травами.'),
        ", both words get a shape for more than one thing when they follow ",
        ('max', 'с'),
        " which literally means 'with'."
    ]),
    (7, None, [
        "'My guests will be in total delight!' What happens here, ",
        ('guest', 'в полном восторге!'),
        " translates to 'in full delight', with the word for 'full', ",
        ('guest', 'полном'),
        ", matching the shape. ",
        ('guest', 'будут'),
        " is 'will be', in a shape for more than one to match the guests."
    ]),
    (8, None, [
        "'Our restaurant maintains only the highest standard.' In Russian, ",
        ('barinov', 'держит'),
        ", literally 'holds', here translates to 'keeps up'. ",
        ('barinov', 'высший уровень.'),
        " is the phrase for 'highest level'."
    ]),
    (9, None, [
        "'Thank you for the wonderful work, chefs!' Looking closely, ",
        ('guest', 'Спасибо вам за'),
        " literally translates to 'thanks to you for', and the words for 'wonderful work', ",
        ('guest', 'прекрасную работу,'),
        " take a special shape. The word for 'chefs', ",
        ('guest', 'повара!'),
        ", is a shape for more than one."
    ]),
    (10, None, [
        "'Bon appetit to you and your guests!' Let us check ",
        ('barinov', 'Приятного аппетита'),
        " translates to 'pleasant appetite' and is the standard wish before a meal. ",
        ('barinov', 'вам и вашим гостям!'),
        " means 'to you and to your guests', built from special shapes."
    ]),
    (11, None, [
        "'We hope to see you again at the restaurant.' What happens here, ",
        ('max', 'Надеемся'),
        " is the word for 'we hope'. ",
        ('max', 'увидеть вас снова'),
        " translates to 'to see you again'."
    ]),
    (12, None, [
        "'Max, quickly get back to the kitchen!' The word ",
        ('barinov', 'живо'),
        " is built from the word for 'alive', and here it literally means 'look lively'. ",
        ('barinov', 'возвращайся обратно'),
        " translates to 'come back back', doubling up for emphasis."
    ]),
]
