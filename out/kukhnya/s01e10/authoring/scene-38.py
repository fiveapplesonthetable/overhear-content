from pathlib import Path

ID = "kukhnya-s01e10-scene-38"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 38
TITLE = "Ответ Вики  (Vika's Answer)"
LEVEL = "A1"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja"}
LABELS = {"anya": "Вика", "max": "Макс"}
SOURCE_NAME = "Кухня s01e10"
SOURCE_FILE = Path("sources/kukhnya/s01/e10.ru.dual.srt")

INTRO = (
    "Stunned by Max's audacious public proposal, Victoria pauses to assess the situation. "
    "Rather than getting flustered, she looks him in the eye and boldly calls his bluff by accepting to marry him. "
    "Let's listen to their conversation in Russian."
)

STORY = [
    ("anya", "Максим, ты думал, что я испугаюсь?",
     "Maxim, did you think that I would get scared?",
     [(275, "Я согласна")], "challenging his bluff"),
    ("max", "Я просто сделал тебе красивое предложение.",
     "I simply made you a beautiful proposal.",
     [(275, "Я согласна")], "defending proposal"),
    ("anya", "Ты хотел проверить мою смелость сейчас?",
     "You wanted to test my courage now?",
     [(275, "Я согласна")], "questioning motives"),
    ("max", "Я готов создать с тобой крепкую семью.",
     "I am ready to create a strong family with you.",
     [(275, "Я согласна")], "doubling down"),
    ("anya", "Ты уверен в своих громких словах?",
     "Are you confident in your loud words?",
     [(275, "Я согласна")], "pressing Max"),
    ("max", "Я абсолютно уверен в каждом своём слове!",
     "I am absolutely confident in every word of mine!",
     [(275, "Я согласна")], "insisting firmly"),
    ("anya", "Тогда слушай мой честный ответ при всех.",
     "Then listen to my honest answer in front of everyone.",
     [(275, "Я согласна")], "preparing answer"),
    ("anya", "Я согласна стать твоей законной женой!",
     "I agree to become your lawful wife!",
     [(275, "Я согласна")], "accepting proposal"),
    ("max", "Ты действительно сейчас говоришь чистую правду?",
     "Are you really speaking the pure truth now?",
     [(275, "Я согласна")], "staring in shock"),
    ("anya", "Да, я принимаю твоё неожиданное предложение.",
     "Yes, I accept your unexpected proposal.",
     [(275, "Я согласна")], "confirming acceptance"),
    ("max", "Теперь мы станем настоящими женихом и невестой!",
     "Now we will become real groom and bride!",
     [(275, "Я согласна")], "reacting to agreement"),
    ("anya", "Посмотрим, как ты справишься с этим, Максим!",
     "We will see how you handle this, Maxim!",
     [(275, "Я согласна")], "challenging future"),
    ("max", "Я готов ко всем трудностям нашей свадьбы!",
     "I am ready for all the difficulties of our wedding!",
     [(275, "Я согласна")], "accepting challenge"),
]

OPENER = (
    "Let's examine the dialogue sentence by sentence. "
    "Notice the declarations of intent, emotional boldness, and marriage vocabulary."
)

WALK = [
    (0, "Максим, ты думал, что я испугаюсь?",
     "'Maxim, did you think that I would get scared?' Direct address name with subject pronoun, past verb, subordinating conjunction, subject pronoun, and future reflexive verb."),
    (1, "Я просто сделал тебе красивое предложение.",
     "'I simply made you a beautiful proposal.' Subject pronoun with limiting particle, past verb, dative pronoun, and accusative adjective-noun phrase."),
    (2, "Ты хотел проверить мою смелость сейчас?",
     "'You wanted to test my courage now?' Subject pronoun with past modal verb, perfective infinitive, accusative possessive-noun phrase, and temporal adverb."),
    (3, "Я готов создать с тобой крепкую семью.",
     "'I am ready to create a strong family with you.' Subject pronoun with short adjective, infinitive, instrumental prepositional pronoun phrase, and accusative adjective-noun phrase."),
    (4, "Ты уверен в своих громких словах?",
     "'Are you confident in your loud words?' Subject pronoun with short adjective, and locative prepositional possessive-adjective-noun phrase."),
    (5, "Я абсолютно уверен в каждом своём слове!",
     "'I am absolutely confident in every word of mine!' Subject pronoun with degree adverb, short adjective, and locative prepositional determinative-possessive-noun phrase."),
    (6, "Тогда слушай мой честный ответ при всех.",
     "'Then listen to my honest answer in front of everyone.' Temporal connector with imperative verb, accusative possessive-adjective-noun phrase, and prepositional phrase."),
    (7, "Я согласна стать твоей законной женой!",
     "'I agree to become your lawful wife!' Subject pronoun with short adjective, infinitive copula, and instrumental possessive-adjective-noun predicate phrase."),
    (8, "Ты действительно сейчас говоришь чистую правду?",
     "'Are you really speaking the pure truth now?' Subject pronoun with modal adverb, temporal adverb, present verb, and accusative adjective-noun phrase."),
    (9, "Да, я принимаю твоё неожиданное предложение.",
     "'Yes, I accept your unexpected proposal.' Affirmative particle with subject pronoun, present transitive verb, and accusative possessive-adjective-noun phrase."),
    (10, "Теперь мы станем настоящими женихом и невестой!",
     "'Now we will become real groom and bride!' Temporal adverb with subject pronoun, future copular verb, instrumental plural adjective, and coordinated predicate nouns."),
    (11, "Посмотрим, как ты справишься с этим, Максим!",
     "'We will see how you handle this, Maxim!' Future verb with subordinating interrogative adverb, subject pronoun, future verb, prepositional phrase, and vocative name."),
    (12, "Я готов ко всем трудностям нашей свадьбы!",
     "'I am ready for all the difficulties of our wedding!' Subject pronoun with short adjective, dative preposition, and dative plural determinative-noun-possessive-noun phrase."),
]

TRANSITION = "Now let's listen to the entire exchange one more time at normal speed."

OUTRO = (
    "Refusing to back down in front of her sister, Victoria calls Max's bluff by accepting his marriage proposal on the spot. "
    "Great work practicing conversational Russian!"
)

CLOSING = ("anya", "Я согласна стать твоей законной женой!")
