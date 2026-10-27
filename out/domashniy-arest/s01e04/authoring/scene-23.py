ID = "domashniy-arest-s01e04-scene-23"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 4
SCENE = 23
TITLE = "Место на кладбище  (The Cemetery Plot)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "klavdia": "anja", "ilona": "angelina"}
LABELS = {"anya": "Аркадий", "klavdia": "Клавдия Викторовна", "ilona": "Илона"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.04"
SOURCE_FILE = "sources/domashniy-arest/s01/e04.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 906-969. Because of the three-role limit (Arkady, Klavdia Viktorovna, Ilona), Golovkin's single-word reply "
    "in cue 918 ('Хотел') is narrated. Ilona's church decree from Bishop Yafan in cues 928-934 is simplified to A1 "
    "('Вот документ. Место в главном соборе города!'), 'билась' (915) to 'просила', and 'быть похоронены' (927) to "
    "'лежать'; 'Мой ЛК же' (948, garbled 'Мой Гриша') is restored to 'Мой Гриша'."
)

INTRO = (
    "Back in Klavdia Viktorovna's room in the communal flat. Last time, Samson was given an exclusive evening test "
    "drive of a luxury car from the dealership and took Nina for a fast ride around the city. Meanwhile, Arkady and "
    "his lawyer Golovkin have returned to Klavdia's room with the official cemetery certificate she wanted in exchange "
    "for her phone. We'll hear it in Russian first; don't worry about catching every word."
)

STORY = [
 ("anya", "Клавдия Викторовна, а вот и ваш документ.",
  "Klavdia Viktorovna, and here is your document.",
  [(906, "Клавдия Викторовна"), (907, "а вот и"), (907, "ваш документ")], "'он' dropped"),
 ("anya", "Это место на кладбище. Рядом с Григорием Сопрыкиным!",
  "It is a plot at the cemetery. Next to Grigory Soprykin!",
  [(909, "Место на кладбище"), (910, "рядом с Григорием"), (911, "Сопрыкиным")],
  "'сертификат' simplified to 'место на кладбище'"),
 ("anya", "Вот печать и подпись, как обещал.",
  "Here are the seal and signature, as I promised.",
  [(911, "Вот"), (912, "печать"), (913, "подпись, как обещал")], "'Водяные знаки' dropped for A1"),
 ("klavdia", "Ну, надо же! А я десять лет просила!",
  "Well, I never! And I asked for ten years!",
  [(914, "Ну, надо же"), (915, "А я десять лет")], "'билась' -> 'просила' (A1)"),
 ("anya", "Клавдия Викторовна, давайте ваш телефон.",
  "Klavdia Viktorovna, give me your phone.",
  [(922, "Клавдия Викторовна, давайте ваш телефон")], ""),
 ("ilona", "Всем стоять! В чём дело?",
  "Nobody move! What's going on?",
  [(923, "Всем стоять"), (924, "В чем дело")], "cue 924 folded into Ilona's entrance"),
 ("ilona", "Город высоко ценит вас и вашего мужа.",
  "The city values you and your husband highly.",
  [(925, "город высоко ценит"), (925, "вас и вашего")], "'заслуги ... покойного супруга' -> 'вас и вашего мужа'"),
 ("ilona", "Такие люди должны лежать в особенном месте!",
  "Such people should lie in a special place!",
  [(927, "Такие люди"), (927, "должны"), (927, "в особенном месте")], "'быть похоронены' -> 'лежать' (A1)"),
 ("ilona", "Вот документ. Место в главном соборе города!",
  "Here is the document. A place in the main cathedral of the city!",
  [(930, "собора")], "cues 928-934 (church decree for the Alexander Nevsky Cathedral crypt) simplified to A1"),
 ("klavdia", "Господи! Этого не может быть!",
  "Good Lord! This cannot be!",
  [(935, "Господи"), (936, "Этого не может быть")], ""),
 ("klavdia", "Мой Гриша мечтать об этом не мог! Спасибо, дочка!",
  "My Grisha could not even dream of this! Thank you, dear!",
  [(948, "Мой"), (948, "мечтать об этом не мог"), (949, "спасибо")],
  "garbled 'ЛК же' -> 'Гриша'; 'доча' -> 'дочка'"),
 ("ilona", "Я так рада! А теперь можно ваш телефон?",
  "I'm so glad! And now may I have your phone?",
  [(950, "я так рада"), (953, "а теперь"), (953, "можно")], "'телефончик все-таки' -> 'ваш телефон'"),
 ("anya", "Стойте, Клавдия Викторовна! Одну секунду!",
  "Wait, Klavdia Viktorovna! One second!",
  [(956, "Стойте, Клавдия Викторовна"), (957, "Одну секунду")], ""),
 ("anya", "Не давайте ей телефон! Сейчас я вернусь!",
  "Don't give her the phone! I'll be right back!",
  [(958, "Не давайте ей телефон"), (963, "Сейчас я вернусь")], ""),
]

OPENER = (
    "Let's go through the scene line by line. Arkady walks in waving the paper that Golovkin just got from the "
    "cemetery office."
)

WALK = [
 (0, None,
  "'Klavdia Viktorovna, and here is your document.' The little phrase 'and here is' is how you proudly present "
  "something people have been waiting for."),
 (1, "Это место на кладбище.",
  "'It is a plot at the cemetery.' The word for 'place' or 'plot' is neuter, and 'at the cemetery' uses the "
  "preposition 'on' with the prepositional case."),
 (1, "Рядом с Григорием Сопрыкиным!",
  "'Next to Grigory Soprykin!' After 'next to, beside', the preposition 'with' puts both her late husband's first "
  "name and surname into the instrumental case."),
 (2, None,
  "'Here are the seal and signature, as I promised.' The verb 'promised' has the masculine past ending because Arkady "
  "is speaking. Klavdia Viktorovna looks at the paper in amazement."),
 (3, None,
  "'Well, I never! And I asked for ten years!' Her verb ends in '-la', the feminine past tense, and after 'ten' the "
  "word for years becomes the genitive plural 'of summers'. After Golovkin shyly confirms he wanted to help, Arkady "
  "reaches out his hand."),
 (4, None,
  "'Klavdia Viktorovna, give me your phone.' Just as Klavdia is about to hand it over, the door flies open and Ilona "
  "bursts in."),
 (5, None,
  "'Nobody move! What's going on?' Literally, 'to everyone, to stand!', using the dative plural and an infinitive as a "
  "sharp command. Then she turns on her warmest campaign smile."),
 (6, None,
  "'The city values you and your husband highly.' Because 'husband' is an animate masculine noun, its accusative form "
  "matches the genitive."),
 (7, None,
  "'Such people should lie in a special place!' The plural word for 'must, should' is followed by the infinitive 'to "
  "lie', and 'in a special place' takes the prepositional case. Ilona unrolls an ornate church scroll from the local "
  "bishop."),
 (8, None,
  "'Here is the document. A place in the main cathedral of the city!' She has arranged for both Grigory and Klavdia "
  "to rest inside the crypt of the Alexander Nevsky Cathedral itself. Klavdia gasps."),
 (9, None,
  "'Good Lord! This cannot be!' With negative 'cannot be', the pronoun 'this' stands in the genitive singular."),
 (10, None,
  "'My Grisha could not even dream of this! Thank you, dear!' The verb 'to dream' is followed by the preposition "
  "'about' with the prepositional case, and she calls Ilona 'little daughter', a warm way for an older woman to "
  "address a young woman."),
 (11, None,
  "'I'm so glad! And now may I have your phone?' Ilona uses the feminine short adjective 'glad', and asks 'is it "
  "possible your phone?' Arkady panics."),
 (12, None,
  "'Wait, Klavdia Viktorovna! One second!' He uses the polite plural command 'stand, wait', and 'one second' is in "
  "the accusative case for a span of time."),
 (13, None,
  "'Don't give her the phone! I'll be right back!' The reflexive future verb at the end means 'I will return', and "
  "Arkady dashes out of the room to play his final card."),
]

TRANSITION = "Now let's hear the whole scene again, from start to finish."

OUTRO = (
    "So Ilona topped Arkady's cemetery certificate with a place in the city cathedral, and Arkady has one last "
    "chance to win Klavdia's heart before she hands over the phone. See you in the next scene."
)
CLOSING = ("anya", "Сейчас я вернусь!")
