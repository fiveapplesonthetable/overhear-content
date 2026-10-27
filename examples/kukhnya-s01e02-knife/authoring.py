ID = "06-knife"
TITLE = "Эпизод 6: Где мой нож?  (Where's My Knife?)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.02"
SOURCE_FILE = "sources/kukhnya/s01/e02.ru.dual.srt"

INTRO = ("This one is set in the kitchen from the show, and it's built from the second episode. "
         "The chef has lost his favourite knife, and nearly every line is one you'll hear when you watch. "
         "As always, the whole story in Russian first, then I'll take you back through it in English. "
         "Don't worry about catching every word.")

STORY = [
 ("chef", "Где мой нож? Кто взял мой нож?", "Where is my knife? Who took my knife?",
  [(76, "где мой нож"), (80, "Кто взял мой нож")], ""),
 ("anya", "Шеф, я не брала.", "Chef, I didn't take it.",
  [(233, "Я не брал")], "брал -> брала (the speaker is a woman)"),
 ("chef", "Повторяю. Кто взял мой нож?", "I repeat: who took my knife?",
  [(81, "Повторяю"), (80, "Кто взял мой нож")], ""),
 ("anya", "Я не знаю.", "I don't know.", [(192, "Я не знаю")], ""),
 ("chef", "Так, все ищем нож. Живо!", "Right, everyone, we're looking for the knife. Quick!",
  [(90, "Так, все ищем нож"), (91, "Живо")], ""),
 ("anya", "Хорошо, шеф.", "All right, chef.", [(117, "Хорошо")], "'шеф' added as address"),
 ("chef", "Нож нашли?", "Have you found the knife?", [(228, "Нож нашли")], ""),
 ("anya", "Ещё нет, шеф.", "Not yet, chef.", [(238, "Ещё нет, шеф")], ""),
 ("chef", "Везде смотрели?", "Did you look everywhere?", [(238, "Везде смотрели")], ""),
 ("anya", "Да, везде. Нигде нет.", "Yes, everywhere. It isn't anywhere.",
  [(249, "везде искали, нигде нет")], "смотрели/искали unified: 'везде' + 'нигде нет' kept"),
 ("chef", "Ищите везде!", "Look everywhere!", [(243, "Ищите везде")], ""),
 ("anya", "Шеф, вот он! Нож в рыбе.", "Chef, here it is! The knife is in the fish.",
  [(241, "в рыбе"), (253, "рыбий нож нашли")], "'Шеф, вот он!' new"),
 ("chef", "В рыбе?", "In the fish?", [(242, "В рыбе")], ""),
 ("anya", "Да, шеф. Вот.", "Yes, chef. Here.", [(244, "Да, шеф")], "'Вот.' new"),
 ("chef", "Спасибо. Ты молодец.", "Thank you. Well done.", [(277, "Спасибо")], "'Ты молодец.' new (the chef's praise)"),
 ("anya", "Пожалуйста, шеф!", "You're welcome, chef!", [], ""),
]

OPENER = "Right, let's go through it slowly. The chef's knife has gone, and he is not happy."

WALK = [
 (0, "Где мой нож?",
  "'Where is my knife?' The first word means 'where', and 'my' sits in front of the knife, as in English. Next, he wants to know who is responsible."),
 (0, "Кто взял мой нож?",
  "'Who took my knife?' The word for 'who' comes first, and 'took' is in the past tense. Anya answers straight away."),
 (1, None,
  "'Chef, I didn't take it.' Literally, 'I not took.' The 'a' on the end of the last word tells you the speaker is a woman. A man would leave it off. The chef doesn't believe her, so he asks again, starting with one word."),
 (2, "Повторяю.",
  "'I repeat.' You'll hear it whenever someone is losing patience. Anya has no better answer."),
 (3, None,
  "'I don't know.' One of the most useful sentences in the language. So the chef gives an order to everybody."),
 (4, "Так, все ищем нож.",
  "'Right, everyone, we're looking for the knife.' The chef says 'we', so he joins the search himself. Then one word, shouted."),
 (4, "Живо!",
  "'Quick!' It comes from the word for 'alive', so 'look lively', get a move on. A little later he checks on the others."),
 (6, None,
  "'Have you found the knife?' There's no 'you' in it at all. The verb is in the past tense, and that's enough. Anya has to say no."),
 (7, None,
  "'Not yet, chef.' Literally, 'still no'. But the chef wants to be sure."),
 (8, None,
  "'Did you look everywhere?' The first word is 'everywhere'. Anya says yes, and uses two words that are opposites."),
 (9, None,
  "'Yes, everywhere. It's nowhere.' One word for 'everywhere', and its mirror image, 'nowhere'. The chef sends everybody off again."),
 (10, None,
  "'Look everywhere!' That's the command form for talking to a group of people. And then Anya spots something."),
 (11, None,
  "'Chef, here it is! The knife is in the fish.' The little word after 'Chef' points at things, like 'here it is', and 'it' is masculine to match the knife. The chef can hardly believe it."),
 (12, None,
  "'In the fish?' He just repeats the words, with a question mark in his voice. Anya confirms."),
 (13, None,
  "'Yes, chef. Here.' And at last the chef says what a boss almost never says."),
 (14, None,
  "'Thank you. Well done.' Notice he uses the casual 'you' with Anya, as bosses do in a kitchen. Anya answers politely."),
 (15, None,
  "'You're welcome, chef!' The word for 'please' is also how Russians say 'you're welcome'."),
]

TRANSITION = "Alright, let's hear the whole thing once more."

OUTRO = ("And that's it for today. When you watch the second episode, listen for the chef asking where his knife is, "
         "and for the one word he shouts when he's in a hurry. You'll catch them now. See you next time.")
CLOSING = ("anya", "Пока!")
