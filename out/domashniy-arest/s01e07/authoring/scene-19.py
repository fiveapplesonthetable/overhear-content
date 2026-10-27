# -*- coding: utf-8 -*-
"""Scene 19 of domashniy-arest s01e07: Romantic Breakfast."""

ID = "domashniy-arest-s01e07-scene-19"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 19
TITLE = "Романтический завтрак  (Romantic Breakfast)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.07"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "dean": "anja",
    "marina": "angelina",
}

LABELS = {
    "anya": "Аркадий",
    "dean": "Эдуард Владимирович",
    "marina": "Марина",
}

INTRO = (
    "Last time in the communal kitchen, Samson grew jealous over Danya's cheese fondue "
    "and invited everyone on a winter shashlik trip to the forest. The next morning in "
    "Marina's room, her former dean Eduard Vladimirovich has brought coffee, fresh berries, "
    "and croissants for a quiet breakfast, when Arkady barges through the door with both "
    "arms in plaster casts. Listen to the Russian conversation first, and do not worry "
    "about catching every word."
)

OPENER = "Let's go through this awkward breakfast interruption line by line."

STORY = [
    ("dean", "Всё по-новому. Нам сейчас никто не будет мешать.",
     "Everything is new now. No one is going to bother us right now.",
     [(734, "Все по-новому"), (734, "нам сейчас никто не будет мешать")], ""),
    ("marina", "Ой! Что такое?",
     "Oh! What is the matter?",
     [(737, "Что такое")], "Arkady accidentally bangs the door open with his plaster cast"),
    ("anya", "Извините, ради бога! Я хотел постучаться и не рассчитал.",
     "Forgive me, for goodness' sake! I wanted to knock and misjudged it.",
     [(738, "Извините, ради бога"), (738, "Я хотел постучаться и не рассчитал")], ""),
    ("anya", "Я хочу извиниться за вчерашнее. Просто отошёл наркоз, и были дикие боли.",
     "I want to apologise for yesterday. The anaesthesia just wore off, and I had wild pain.",
     [(740, "Я хочу извиниться за вчерашнее"), (741, "Просто отошел наркоз и были дикие боли")], ""),
    ("marina", "Ничего страшного, Аркадий Борисович.",
     "It is alright, Arkady Borisovich.",
     [(743, "Ничего страшного")], ""),
    ("dean", "Ну, хорошо, вы извинились. Пожалуйста, уже можно закрыть дверь.",
     "Well, fine, you have apologised. Now please, you can close the door.",
     [(744, "Ну, хорошо. Извинились"), (744, "пожалуйста, уже можно закрыть дверь")], ""),
    ("anya", "Свежие ягоды, кофе! У вас тут романтический завтрак.",
     "Fresh berries, coffee! You are having a romantic breakfast here.",
     [(745, "Свежие ягоды"), (746, "Кофе"), (747, "У вас романтический завтрак")], ""),
    ("anya", "Я тоже очень хочу завтракать. Но ничего, будем худеть.",
     "I really want to have breakfast too. But that is alright, we will lose weight.",
     [(749, "Я тоже очень хочу завтракать"), (751, "Но ничего"), (752, "Будем худеть")], ""),
    ("dean", "Пожалуйста, худейте там, за дверью. Закройте дверь, пожалуйста!",
     "Please, lose weight out there, behind the door. Close the door, please!",
     [(755, "Пожалуйста, худейте"), (759, "Закройте дверь, пожалуйста")], ""),
    ("marina", "Эдик, а давай угостим Аркадия круассанами.",
     "Edik, let's offer Arkady some croissants.",
     [(764, "Эдик"), (766, "А давай угостим Аркадия круассанами")], ""),
    ("dean", "Почему мы должны угощать кого-то нашими круассанами?",
     "Why should we treat anyone to our croissants?",
     [(767, "Почему мы должны угощать кого-то нашими круассанами")], ""),
    ("anya", "Вы ничего не должны, это правда. Он абсолютно прав.",
     "You do not owe anything, that is true. He is absolutely right.",
     [(769, "Вы ничего не должны, это правда, он абсолютно прав")], ""),
    ("dean", "Хорошо, вот, возьмите круассан! И, пожалуйста, только уходите.",
     "Fine, here, take a croissant! And please, just leave.",
     [(771, "Хорошо, вот, возьмите"), (772, "пожалуйста, только уходите")], ""),
    ("anya", "Больно мне! Зачем вы мне руку прищемили?",
     "That hurts me! Why did you pinch my arm in the door?",
     [(779, "больно мне"), (780, "Зачем вы мне руку прищемили")], "Eduard tries to shut the door on Arkady's plaster cast"),
    ("dean", "Я не прищемил! Вы её здесь оставили специально.",
     "I did not pinch it! You left it right here on purpose.",
     [(781, "Я не прищемил, вы ее здесь оставили специально")], ""),
    ("anya", "Извините, вы очень щедрый, а я неловкий. Я пойду попробую приготовить себе кашу.",
     "Forgive me, you are very generous, and I am clumsy. I will go try to cook myself some porridge.",
     [(782, "вы очень щедрый, а я"), (782, "неловкий"), (783, "Я пойду попробую приготовить себе кашу")], ""),
]

WALK = [
    (0, "Всё по-новому.",
     "'Everything is in a new way.' Eduard Vladimirovich is enjoying a quiet morning with Marina."),
    (0, "Нам сейчас никто не будет мешать.",
     "'No one will bother us now.' The dative pronoun means 'to us'."),
    (1, None,
     "'Oh! What is the matter?' Suddenly Arkady's heavy plaster cast bangs the door open."),
    (2, "Извините, ради бога!",
     "'Forgive me, for goodness' sake!' Literally 'for the sake of God'."),
    (2, "Я хотел постучаться и не рассчитал.",
     "'I wanted to knock and miscalculated.' With both arms in plaster casts, he swung too hard."),
    (3, "Я хочу извиниться за вчерашнее.",
     "'I want to apologise for yesterday.' The adjective used as a noun means 'yesterday's events'."),
    (3, "Просто отошёл наркоз, и были дикие боли.",
     "'The anaesthesia simply wore off, and there were wild pains.' He blames the hospital painkillers for his rude behaviour the night before."),
    (4, None,
     "'It's nothing terrible, Arkady Borisovich.' Marina accepts his apology politely."),
    (5, "Ну, хорошо, вы извинились.",
     "'Well, fine, you have apologised.' Eduard wants him out of the room immediately."),
    (5, "Пожалуйста, уже можно закрыть дверь.",
     "'Please, one can close the door now.' He points firmly toward the hallway."),
    (6, "Свежие ягоды, кофе!",
     "'Fresh berries, coffee!' Instead of leaving, Arkady peers eagerly at the table."),
    (6, "У вас тут романтический завтрак.",
     "'You have a romantic breakfast here.' He acts delighted by their spread."),
    (7, "Я тоже очень хочу завтракать.",
     "'I really want to have breakfast too.' He puts on his most pitiful voice."),
    (7, "Но ничего, будем худеть.",
     "'But that is alright, we will lose weight.' He sighs tragically as if starving."),
    (8, "Пожалуйста, худейте там, за дверью.",
     "'Please, lose weight out there, behind the door.' Eduard is not moved at all."),
    (8, "Закройте дверь, пожалуйста!",
     "'Close the door, please!' He repeats the polite plural imperative."),
    (9, None,
     "'Edik, let's treat Arkady to some croissants.' Marina feels sorry for the helpless neighbour."),
    (10, None,
     "'Why must we treat someone to our croissants?' Notice the instrumental plural ending on 'croissants' after the verb for 'to treat'."),
    (11, "Вы ничего не должны, это правда.",
     "'You don't owe anything, that is true.' Arkady plays the humble martyr."),
    (11, "Он абсолютно прав.",
     "'He is absolutely right.' That makes Marina feel even guiltier."),
    (12, "Хорошо, вот, возьмите круассан!",
     "'Fine, here, take a croissant!' Eduard shoves a pastry onto Arkady's cast."),
    (12, "И, пожалуйста, только уходите.",
     "'And please, just leave.' He tries to push the door shut."),
    (13, "Больно мне!",
     "'It hurts me!' Literally 'it is painful to me!'."),
    (13, "Зачем вы мне руку прищемили?",
     "'Why did you pinch my arm?' Arkady's plaster cast is wedged in the doorway."),
    (14, "Я не прищемил!",
     "'I didn't pinch it!' Eduard protests."),
    (14, "Вы её здесь оставили специально.",
     "'You left it here on purpose.' The adverb means 'deliberately' or 'on purpose'."),
    (15, "Извините, вы очень щедрый, а я неловкий.",
     "'Sorry, you are very generous, and I am clumsy.' Contrast the two masculine adjectives: 'generous' and 'clumsy'."),
    (15, "Я пойду попробую приготовить себе кашу.",
     "'I will go try to cook myself porridge.' Eduard tells him to go right ahead and finally shuts the door."),
]

TRANSITION = "Now listen to the whole breakfast scene again from start to finish."

OUTRO = (
    "Clutching his croissant between his plaster casts, Arkady heads off to the communal "
    "kitchen to cook porridge on his own. Join us next time to see the mess that follows."
)

CLOSING = ("anya", "Я пойду попробую приготовить себе кашу.")
