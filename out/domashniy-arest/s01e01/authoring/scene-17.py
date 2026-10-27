ID = "domashniy-arest-s01e01-scene-17"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 1
SCENE = 17
TITLE = "Один-один  (One-All)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "samson": "anja", "nina": "angelina"}
LABELS = {"anya": "Аркадий", "samson": "Самсон", "nina": "Нина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.01"
SOURCE_FILE = "sources/domashniy-arest/s01/e01.ru.dual.srt"
SOURCE_NOTE = ("Arkady is `anya` (label Аркадий). Samson's word 'раб' (slave, cue 681) is softened to 'слуга' "
               "(servant), which also sets up his 'servant of the people' joke.")

INTRO = ("Still in the communal flat, a few minutes later. Last time, the officers moved Arkady into his old room "
         "behind the wardrobe and fixed a tag to his ankle. Now Samson, the man he tricked with that humiliating "
         "kiss, is standing in the doorway, and Arkady tries to talk his way out; we'll hear it in Russian first, so "
         "don't worry about catching every word.")

STORY = [
 ("anya", "Самсон, послушай. Это была месть.", "Samson, listen. It was revenge.",
  [(650, "Самсон, послушай"), (651, "Это была месть")], ""),
 ("samson", "Месть?", "Revenge?",
  [], "new: Samson is silent in the source; a one-word echo"),
 ("anya", "Ты меня, я тебя. Теперь у нас один-один.", "You got me, I got you. Now it's one-all.",
  [(651, "Ты меня, я тебя"), (652, "один-один")], "'Все у нас теперь' -> 'Теперь у нас' (word order)"),
 ("samson", "Ну-ну.", "Yeah, right.",
  [], "new: Samson's sceptical reaction"),
 ("anya", "Всё по правилам, как рыцарский турнир.", "All by the rules, like a knights' tournament.",
  [(653, "Все по правилам, как"), (653, "рыцарский турнир")], "'этот' dropped"),
 ("anya", "Самсон, ну улыбнись. У нас мир.", "Samson, come on, smile. We're at peace.",
  [(656, "Самсон, ну улыбнись"), (657, "у нас мир")], ""),
 ("samson", "Мир!", "Peace!",
  [(659, "Мир")], "Samson shakes on it and squeezes"),
 ("anya", "Ай! Мой палец!", "Ow! My finger!",
  [], "new: Samson breaks Arkady's finger"),
 ("nina", "Самсон, больше ему ничего не ломай.", "Samson, don't break anything else of his.",
  [(668, "больше ему ничего не ломай")], "garbled 'Самсону' in the cue written as the address 'Самсон'"),
 ("samson", "Не волнуйся, не буду.", "Don't worry, I won't.",
  [(672, "Не волнуйся, не буду")], ""),
 ("nina", "Давай руку. Вот так.", "Give me your hand. That's it.",
  [], "new: Nina bandages the finger (cues 669-670 mention her bandages)"),
 ("anya", "Твоя жена очень мудрая женщина. Ты её слушай.", "Your wife is a very wise woman. You listen to her.",
  [(673, "Твоя жена очень мудрая женщина"), (673, "ты ее слушай")], ""),
 ("samson", "Всё, Нинок. Теперь у нас есть личный слуга.", "That's it, Ninok. Now we have our own personal servant.",
  [(677, "Все, Нинок"), (680, "Теперь у нас есть")], "'личный раб' (681) -> 'личный слуга' (servant)"),
 ("anya", "Что, простите?", "I beg your pardon?",
  [(682, "Что, простите")], ""),
 ("samson", "Ты же слуга народа. А мы — народ.", "You're a servant of the people. And we are the people.",
  [(684, "Ты же слуга народа")], "garbled 'а мы есть' (684) -> 'А мы — народ' (the English subtitle's sense)"),
 ("samson", "Так что будешь нам служить.", "So you'll serve us.",
  [(685, "Так что будешь нам служить")], ""),
]

OPENER = "Let's go through it together. Arkady speaks first, and he speaks fast."

WALK = [
 (0, "Самсон, послушай.",
  "'Samson, listen.' The casual command, because these two have known each other since they were boys. Then a "
  "short confession."),
 (0, "Это была месть.",
  "'It was revenge.' The word for 'was' ends in 'a' to match 'revenge', which is feminine. Samson isn't sure what "
  "he means."),
 (1, None,
  "'Revenge?' Just one word, and not a friendly one. Arkady explains with a neat little formula."),
 (2, "Ты меня, я тебя.",
  "'You got me, I got you.' Word for word, just 'you me, I you'; the verbs are missing, and you don't need them. "
  "Then the score."),
 (2, "Теперь у нас один-один.",
  "'Now it's one-all.' Like a football score: the toilet when they were boys, and the kiss today. Samson isn't "
  "convinced."),
 (3, None,
  "'Yeah, right.' A tiny word said twice, slowly, and it means 'I don't believe a word of it'. Arkady keeps going."),
 (4, None,
  "'All by the rules, like a knights' tournament.' He makes it sound like a fair duel between gentlemen. Then he "
  "tries charm."),
 (5, "Самсон, ну улыбнись.",
  "'Samson, come on, smile.' The little word in front of the command softens it, like 'come on'. And then the big "
  "word of the scene."),
 (5, "У нас мир.",
  "'We're at peace.' Literally, 'at us, peace'. The same word means both 'peace' and 'the world'. Samson agrees, a "
  "little too happily."),
 (6, None,
  "'Peace!' He takes Arkady's hand, shakes it, and squeezes hard."),
 (7, None,
  "'Ow! My finger!' The finger is broken. Samson's wife Nina comes in and sees what he has done."),
 (8, None,
  "'Samson, don't break anything else of his.' After 'not', the word for 'nothing' stays negative too, so Russian "
  "happily uses a double negative. Samson promises."),
 (9, None,
  "'Don't worry, I won't.' The second part is short for 'I won't break anything'. Nina is a nurse, and she gets to "
  "work with a bandage."),
 (10, None,
  "'Give me your hand. That's it.' The first word literally means 'give', and it's a very common way to start a "
  "request. Arkady takes his chance to flatter her."),
 (11, "Твоя жена очень мудрая женщина.",
  "'Your wife is a very wise woman.' The word for 'wise' has a feminine ending, to match 'woman'. Then some advice "
  "for Samson."),
 (11, "Ты её слушай.",
  "'You listen to her.' But Samson has his own plans, and he tells Nina about them."),
 (12, None,
  "'That's it, Ninok. Now we have our own personal servant.' Ninok is a pet name for Nina. To say 'we have', "
  "Russians say 'at us there is'. Arkady can't believe his ears."),
 (13, None,
  "'I beg your pardon?' Literally, 'what, forgive me?' Very polite, and here very shocked. Samson explains, using "
  "a phrase politicians love."),
 (14, None,
  "'You're a servant of the people. And we are the people.' Officials like to call themselves servants of the "
  "people, and Samson takes it literally. Then the conclusion."),
 (15, None,
  "'So you'll serve us.' The future again: 'will' plus the verb 'to serve'. The tables have turned on the mayor."),
]

TRANSITION = "Now let's listen to the whole scene again."

OUTRO = ("The peace lasted exactly one handshake, and now the former mayor has a bandaged finger and a new job as the "
         "family's servant. Look after your own fingers, and see you next time.")
CLOSING = ("samson", "Ну, за работу!")
