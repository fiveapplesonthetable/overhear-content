"""s01e09 scene 21: Допрос мэра (restaurant / date)."""

ID = "domashniy-arest-s01e09-scene-21"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 9
SCENE = 21
TITLE = "Допрос мэра  (Interrogating the Mayor)"
LEVEL = "beginner"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "arkady": "anja"}
LABELS = {"anya": "Марина", "arkady": "Аркадий"}
SOURCE_NAME = "Домашний арест, Сезон 1, Эпизод 9"
SOURCE_FILE = "sources/domashniy-arest/s01/e09.ru.dual.srt"
SOURCE_NOTE = "Cues 666-692 (00:35:59-00:37:08). Marina questions Arkady about the demolished monastery and the hidden bribe money."

INTRO = (
    "Previously, Nina angrily rejected young Danya outside the communal apartment. "
    "Meanwhile, in a restaurant room, Marina conducts an FSB-monitored interrogation disguised as a private date, "
    "questioning former mayor Arkady about his past corrupt schemes."
)

STORY = [
    ("anya", "Как можно сносить старый монастырь?",
     "How is it possible to demolish an old monastery?",
     [(667, "Как можно было отдать приказ сосносить")], "shortened cue 667"),
    ("arkady", "Я хотел построить там торговый центр.",
     "I wanted to build a shopping center there.",
     [(669, "Хотел построить там торговую зону")], "adapted cue 669"),
    ("arkady", "Там будет современный красивый комплекс.",
     "There will be a modern, beautiful complex there.",
     [(671, "новый современный торговый комплекс")], "adapted cue 671"),
    ("anya", "А в другом месте построить нельзя?",
     "And was it impossible to build it elsewhere?",
     [(674, "А в другом месте это построить нельзя?")], "shortened cue 674"),
    ("anya", "Монастырь — это наша древняя история!",
     "The monastery is our ancient history!",
     [(679, "А здесь наша история")], "expanded cue 679"),
    ("anya", "Надо было дать денег на восстановление.",
     "You should have given money for its restoration.",
     [(681, "дать денег"), (682, "чтобы восстановить этот монастырь")], "adapted cues 681-682"),
    ("arkady", "Вы очень красивая, когда сердитесь.",
     "You are very beautiful when you are angry.",
     [(683, "Такая красивая, когда сердитесь")], "added Вы очень"),
    ("arkady", "И когда улыбаетесь, тоже очень красивая.",
     "And when you smile, you are also very beautiful.",
     [(684, "И когда не сердитесь, тоже красивая")], "adapted cue 684"),
    ("anya", "Прекратите, мы сейчас говорим о деле!",
     "Stop it, we are talking about business now!",
     [], "stern reaction"),
    ("arkady", "Я ответил на все ваши вопросы.",
     "I have answered all your questions.",
     [(687, "Я ответил на все ваши вопросы")], ""),
    ("arkady", "Какой результат у моего экзамена?",
     "What is the result of my exam?",
     [(688, "узнать результаты экзамена")], "adapted cue 688"),
    ("anya", "Сядьте обратно на своё место.",
     "Sit back down in your seat.",
     [(689, "Нет, не на все. Сядьте")], "adapted cue 689"),
    ("arkady", "Хорошо, я внимательно вас слушаю.",
     "Alright, I am listening to you attentively.",
     [(691, "Я вас слушаю")], "added Хорошо, я внимательно"),
    ("anya", "Где те деньги, которые ищет Осипенко?",
     "Where is that money Osipenko is hunting for?",
     [(692, "А у вас есть те деньги, за которыми охотится Асипенко?")], "adapted cue 692"),
]

OPENER = "Let's see how Marina questions Arkady about his controversial decisions as mayor."

WALK = [
    (0, None,
     "'How is it possible to demolish an old monastery?' Marina challenges Arkady's corrupt municipal past."),
    (1, None,
     "'I wanted to build a shopping center there.' The past tense verb explains his commercial ambitions."),
    (2, None,
     "'There will be a modern, beautiful complex there.' The future tense promises a luxurious venue."),
    (3, None,
     "'And was it impossible to build it elsewhere?' The impersonal construction conveys her strong skepticism."),
    (4, None,
     "'The monastery is our ancient history!' Marina defends the sacred cultural heritage of the town."),
    (5, None,
     "'You should have given money for its restoration.' The verbal noun indicates rebuilding the shrine."),
    (6, None,
     "'You are very beautiful when you are angry.' Arkady shamelessly tries to charm his way out."),
    (7, None,
     "'And when you smile, you are also very beautiful.' He continues showering her with smooth compliments."),
    (8, None,
     "'Stop it, we are talking about business now!' Marina sharply redirects the conversation back to serious matters."),
    (9, None,
     "'I have answered all your questions.' The prepositional phrase marks the completion of the interrogation."),
    (10, None,
     "'What is the result of my exam?' Arkady playfully treats her questioning like a school test."),
    (11, None,
     "'Sit back down in your seat.' The polite imperative commands him to remain seated and orderly."),
    (12, None,
     "'Alright, I am listening to you attentively.' The adverb of manner indicates his focused attention."),
    (13, None,
     "'Where is that money Osipenko is hunting for?' Marina suddenly drops the biggest question of all."),
]

TRANSITION = "Now listen to the interrogation between Marina and Arkady once more."
OUTRO = "Marina keeps her composure and asks the critical question about the missing bribe funds."
CLOSING = ("anya", "Где те деньги, которые ищет Осипенко?")
