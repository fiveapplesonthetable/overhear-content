ID = "kukhnya-s01e14-scene-09"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 9
TITLE = "Французские блюда  (French Dishes)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = (
    "Cue 169. Max finishes preparing the gourmet French dishes at the kitchen pass "
    "and hands the plates to Kostya to serve the VIP guests."
)

INTRO = (
    "In the kitchen of Claude Monet, Max finishes preparing special French dishes for the VIP table. "
    "He calls Kostya to the kitchen pass to deliver the plates into the dining room immediately. "
    "Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Костя, новый заказ для гостей готов.",
     "Kostya, the new order for the guests is ready.",
     [], "new"),
    ("kostya", "Отлично, покажи мне эти красивые тарелки.",
     "Great, show me these beautiful plates.",
     [], "new"),
    ("anya", "Вот вкусный французский стейк и горячая рыба.",
     "Here is a delicious French steak and hot fish.",
     [(169, "Филиминьон по-фламански, лангусты а-ля Франце.")], "adapted"),
    ("kostya", "Это блюдо выглядит очень аппетитно и дорого.",
     "This dish looks very appetizing and expensive.",
     [], "new"),
    ("anya", "Я долго готовил этот редкий рецепт.",
     "I cooked this rare recipe for a long time.",
     [], "new"),
    ("kostya", "Наши гости в зале очень голодные.",
     "Our guests in the hall are very hungry.",
     [], "new"),
    ("anya", "Тогда неси эти тарелки прямо сейчас.",
     "Then carry these plates right now.",
     [], "new"),
    ("kostya", "Я быстро отнесу горячую еду гостям.",
     "I will quickly take the hot food to the guests.",
     [], "new"),
    ("anya", "Обязательно пожелай им приятного аппетита.",
     "Be sure to wish them bon appétit.",
     [], "new"),
    ("kostya", "Конечно, я всё сделаю очень вежливо.",
     "Of course, I will do everything very politely.",
     [], "new"),
    ("anya", "Скажи, что шеф готовил для них.",
     "Say that the chef cooked for them.",
     [], "new"),
    ("kostya", "Хорошо, я передам твои тёплые слова.",
     "Good, I will pass on your warm words.",
     [], "new"),
    ("anya", "Иди скорее, гости уже ждут заказ!",
     "Go quickly, the guests are already waiting for the order!",
     [], "new"),
]

OPENER = "Now let us examine Max and Kostya's conversation at the pass line by line."

WALK = [
    (0, None,
     "'Kostya, the new order for the guests is ready.' -- Max announces that the VIP meal is prepared and ready at the pass."),
    (1, None,
     "'Great, show me these beautiful plates.' -- Kostya arrives to inspect the finished dishes before carrying them."),
    (2, None,
     "'Here is a delicious French steak and hot fish.' -- Max points out the two main dishes cooked according to the recipe."),
    (3, None,
     "'This dish looks very appetizing and expensive.' -- Kostya admires the elegant culinary presentation of the food."),
    (4, None,
     "'I cooked this rare recipe for a long time.' -- Max highlights the careful effort he put into cooking the meal."),
    (5, None,
     "'Our guests in the hall are very hungry.' -- The waiter reminds the cook that the customers are waiting eagerly."),
    (6, None,
     "'Then carry these plates right now.' -- Max urges Kostya to bring the orders to the dining room immediately."),
    (7, None,
     "'I will quickly take the hot food to the guests.' -- Kostya promises to deliver the meals while they are still warm."),
    (8, None,
     "'Be sure to wish them bon appétit.' -- The young chef reminds his colleague to offer polite greetings to the table."),
    (9, None,
     "'Of course, I will do everything very politely.' -- Kostya reassures Max that the table will receive top service."),
    (10, None,
     "'Say that the chef cooked for them.' -- Max proudly asks the waiter to attribute the feast to the head chef."),
    (11, None,
     "'Good, I will pass on your warm words.' -- Kostya agrees to deliver the chef's personal compliments to the diners."),
    (12, None,
     "'Go quickly, the guests are already waiting for the order!' -- Max gives one final push to send Kostya on his way."),
]

TRANSITION = "Now let us listen to Max and Kostya once again."
OUTRO = (
    "With the intricate dishes plated and inspected, Kostya hurries out into the dining room "
    "to serve the VIP diners and deliver Max's greeting."
)
CLOSING = ("anya", "Иди скорее, гости уже ждут заказ!")
