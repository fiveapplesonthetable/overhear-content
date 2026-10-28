ID = "kukhnya-s04e18-scene-11"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 18
SCENE = 11
TITLE = "Горячий нож и укроп  (The Hot Knife and the Dill)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "german": "anja", "fedya": "angelina"}
LABELS = {"anya": "Шеф", "german": "Герман", "fedya": "Федя"}
SOURCE_NAME = "Кухня (Kukhnya) S4.18"
SOURCE_FILE = "sources/kukhnya/s04/e18.ru.srt"
SOURCE_NOTE = "While Senya distracts German in the kitchen with a heated knife handle, Barinov and Fedya sneak into the office to inspect German's pills and nearly get caught."

INTRO = "To distract German while Barinov and Fedya search his office, Senya heats up the handle of German's favorite knife. When German burns his hand and storms back toward his office, he catches Fedya holding something behind his back. Let's listen to this tense moment in Russian."

STORY = [
    ("german", "Где мой нож, никто не видел?", "Where is my knife, has nobody seen it?", [(112, 'Где'), (113, 'мой нож, а? Никто не видел')], "adapted"),
    ("german", "Кому тут сегодня так весело?", "Who is having so much fun in here today?", [(115, 'Кому-то весело')], "adapted"),
    ("german", "Я ещё раз спрашиваю, где мой нож?", "I am asking once again, where is my knife?", [(116, 'Я ещё раз спрашиваю, где мой нож')], ""),
    ("anya", "А вот это разве не ваш нож?", "Isn't this one right here your knife?", [(117, 'А вот это не ваш нож')], "adapted"),
    ("german", "Почему мой нож такой горячий?", "Why is my knife so hot?", [(118, 'Почему нож горячий')], "adapted"),
    ("anya", "Извините, он лежал около плиты.", "Excuse me, it was lying near the stove.", [(119, 'Извините')], "adapted"),
    ("german", "Так, стой, что ты там прячешь?", "All right, stop, what are you hiding there?", [(120, 'Так стой')], "adapted"),
    ("german", "Что это сейчас у тебя в руке?", "What is that in your hand right now?", [(121, 'Что это у тебя')], "adapted"),
    ("fedya", "Это просто свежий зелёный укроп.", "It is just fresh green dill.", [], "new"),
    ("german", "Укроп? Зачем он тебе тут нужен?", "Dill? Why do you need it in here?", [], "new"),
    ("fedya", "Хотите немного? Это очень полезно.", "Do you want some? It is very healthy.", [(123, 'Хотите? Очень полезно')], "adapted"),
    ("anya", "Пошли быстрее отсюда на кухню.", "Let's get out of here to the kitchen faster.", [], "new"),
]

OPENER = "Now let's trace the distraction with the hot knife and the close call line by line."

WALK = [
    (0, None, "'Where is my knife, has nobody seen it?' Double negation with the negative subject pronoun meaning nobody is standard in Russian questions."),
    (1, None, "'Who is having so much fun in here today?' An impersonal dative question asks who is feeling amused in the kitchen."),
    (2, None, "'I am asking once again, where is my knife?' German repeats his demand using an adverbial phrase meaning one more time."),
    (3, None, "'Isn't this one right here your knife?' A pointing particle and a question word introduce a polite plural possessive pronoun."),
    (4, None, "'Why is my knife so hot?' After grabbing the heated handle, German uses a masculine singular adjective meaning hot."),
    (5, None, "'Excuse me, it was lying near the stove.' A polite plural apology precedes a past-tense verb of position and a genitive preposition."),
    (6, None, "'All right, stop, what are you hiding there?' German spots Fedya near the office and uses a singular imperative meaning stop or stand still."),
    (7, None, "'What is that in your hand right now?' A possessive phrase combines with the prepositional singular of the noun for hand."),
    (8, None, "'It is just fresh green dill.' Having swallowed the pill, Fedya holds up a bunch of dill and names it in the nominative case."),
    (9, None, "'Dill? Why do you need it in here?' A masculine short adjective of need agrees with the pronoun referring to the dill."),
    (10, None, "'Do you want some? It is very healthy.' Fedya offers the herbs to the baffled head chef using a neuter short predicate adverbial."),
    (11, None, "'Let's get out of here to the kitchen faster.' Barinov hustles Fedya away using a plural past verb functioning as a brisk imperative."),
]

TRANSITION = "Let's hear the entire kitchen scene again from beginning to end."
OUTRO = "To keep German from discovering the stolen pill bottle, Fedya secretly swallows one of German's mysterious pills on the spot. Listen for the adjectives meaning hot and useful in their exchange. See you in the next scene."
CLOSING = ("german", "Почему мой нож такой горячий?")
CLOSING_TRANS = "Why is my knife so hot?"
