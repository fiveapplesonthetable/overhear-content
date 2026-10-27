ID = "kukhnya-s01e04-scene-05"
TITLE = "Обед для персонала  (Staff Lunch)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Макс", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.04"
SOURCE_FILE = "sources/kukhnya/s01/e04.ru.dual.srt"

INTRO = ("In this scene, Chef Viktor Barinov gives Max his very first cooking assignment: making lunch for the restaurant staff. "
         "However, the chef warns him that if the food tastes bad, the hungry cooks will eat Max instead. "
         "Listen to their lively exchange in Russian first, and then we will break it down together.")

STORY = [
 ("chef", "Здесь не ночлежка, а работа!", "This is not a shelter, but work!",
  [(37, "Здесь не ночлежка, работа")], ""),
 ("anya", "Шеф, вы всё равно не даёте мне готовить.", "Chef, you still won't let me cook.",
  [(38, "вы все равно мне готовить не даете")], ""),
 ("anya", "Я уже отклеил все этикетки от бананов.", "I already peeled all labels from the bananas.",
  [(39, "этикетки от бананов я уже")], "на месяц вперёд omitted"),
 ("chef", "Хорошо, хочешь готовить — будешь готовить!", "Fine, you want to cook — you will cook!",
  [(40, "Хочешь готовить, будешь готовить")], ""),
 ("chef", "Внимание, повара ресторана!", "Attention, cooks of the restaurant!",
  [(41, "Внимание")], "extended for clarity"),
 ("chef", "Сегодня обед для персонала готовит наш огузок.", "Today our runt is cooking lunch for the staff.",
  [(42, "Сегодня обед для персонала готовит")], "огузок used"),
 ("chef", "Это очень ответственное задание.", "This is a very important assignment.",
  [(43, "Это очень ответственное задание")], ""),
 ("chef", "Если им не понравится, они съедят тебя.", "If they don't like it, they will eat you.",
  [(44, "Если им не понравится"), (44, "съесть тебя")], "simplified"),
 ("chef", "Ты меня понял?", "Did you understand me?",
  [(45, "Понял")], ""),
 ("anya", "Да, шеф, я всё понял.", "Yes, Chef, I understood everything.",
  [(45, "Понял")], ""),
 ("anya", "Я так мечтал готовить на кухне.", "I dreamed so much of cooking in the kitchen.",
  [(47, "Я так мечтал")], "simplified"),
 ("chef", "Ну что, ты доволен?", "Well, are you pleased?",
  [(49, "Ну, ты доволен")], ""),
 ("anya", "Я очень рад, шеф, только выпью кофе.", "I am very glad, Chef, just let me drink coffee.",
  [(49, "Я очень рад, шеф, только")], ""),
 ("chef", "Быстро переодевайся, работаем!", "Quickly change clothes, let's get to work!",
  [(50, "Переодевайся"), (51, "Работаем")], ""),
]

OPENER = "Let's break down this high-stakes kitchen assignment step by step."

WALK = [
 (0, None,
  "'This is not a shelter, but work!' Viktor Barinov reminds Max where he is."),
 (1, None,
  "'Chef, you still won't let me cook.' Max protests his boring kitchen duties."),
 (2, None,
  "'I already peeled all labels from the bananas.' Boasting about finishing his menial chores."),
 (3, None,
  "'Fine, you want to cook — you will cook!' The chef unexpectedly takes him up on the challenge."),
 (4, None,
  "'Attention, cooks of the restaurant!' Barinov addresses the entire kitchen team."),
 (5, None,
  "'Today our runt is cooking lunch for the staff.' Announcing Max's first big test."),
 (6, None,
  "'This is a very important assignment.' Highlighting the serious stakes of feeding the crew."),
 (7, None,
  "'If they don't like it, they will eat you.' Issuing a hilarious culinary threat."),
 (8, None,
  "'Did you understand me?' Making sure the message was received loud and clear."),
 (9, None,
  "'Yes, Chef, I understood everything.' Max nervously acknowledges the condition."),
 (10, None,
  "'I dreamed so much of cooking in the kitchen.' Expressing his long-awaited aspiration."),
 (11, None,
  "'Well, are you pleased?' Checking if Max appreciates the opportunity."),
 (12, None,
  "'I am very glad, Chef, just let me drink coffee.' Asking for a quick caffeine boost first."),
 (13, None,
  "'Quickly change clothes, let's get to work!' Shutting down any delay and ordering him to start."),
]

TRANSITION = "Now let's listen to the whole exchange once again."

OUTRO = ("That concludes our fifth scene. In Kukhnya, cooking staff lunch is the ultimate rite of passage "
         "for every newcomer. See you next time!")

CLOSING = ("anya", "До встречи!")
