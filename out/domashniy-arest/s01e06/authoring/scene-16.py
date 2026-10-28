# domashniy-arest/s01e06/scene-16.py
ID = "domashniy-arest-s01e06-scene-16"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 6
SCENE = 16
TITLE = "Злостный должник  (A Chronic Debtor)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.06"
SOURCE_FILE = "sources/domashniy-arest/s01/e06.ru.dual.srt"
VOICES = {"narrator": "sky", "samson": "anja", "librarian": "angelina"}
LABELS = {"samson": "Самсон", "librarian": "Библиотекарь"}
INTRO = "While Klavdia Viktorovna orders Arkady to give her a pedicure, Ivan Samsonov visits the city library to borrow the next book on Arkady's reading list, Sun Tzu's 'The Art of War'. Inside, the stern librarian scolds him for an overdue children's book from 1984, and outside, Major Lavrov and Captain Ovechkin send disguised Lieutenant Lyova to intercept him. Let's listen in Russian first."
STORY = [
    ("librarian", "Самсонов, вот, пожалуйста, ваша книга. Это Сунь-цзы, как вы просили.", "Samsonov, here, please, is your book. This is Sun Tzu, as you asked.", [(574, 'Самсонов, вот, пожалуйста'), (574, 'как вы просили')], "ASR 'Суньзы' -> 'Сунь-цзы'"),
    ("librarian", "Книга новая, мы её только что получили. Пожалуйста, относитесь к ней бережно.", "The book is new, we just received it. Please treat it carefully.", [(575, 'Книга новая, только что получили, пожалуйста, относитесь бережно')], "split into two short sentences"),
    ("samson", "Да вы не волнуйтесь, всё будет отлично!", "Don't you worry, everything will be great!", [(576, 'не волнуйтесь, все будет')], "slang 'пучком' -> 'отлично'"),
    ("librarian", "Я вообще вам могу ничего не давать! Потому что вы злостный должник.", "I don't have to give you anything at all! Because you are a chronic debtor.", [(577, 'Я вообще вам могу ничего не'), (577, 'потому что вы злостный должник')], "simplified 'выдавать' -> 'давать'"),
    ("librarian", "Вы когда взяли книгу Носова? В восемьдесят четвёртом году!", "When did you borrow Nosov's book? In the year eighty-four!", [(578, 'Вы когда взяли'), (578, 'Носова?'), (580, 'году')], "'84-м' written out as words"),
    ("librarian", "Уже тридцать четыре года прошло! Вам не стыдно?", "Thirty-four years have passed already! Aren't you ashamed?", [(581, 'года прошло'), (582, 'Не стыдно?')], "'34' written out as words"),
    ("samson", "Но Макиавелли я же вернул! А где этот Незнайка, я не знаю.", "But I did return Machiavelli! And where that Neznaika is, I don't know.", [(583, 'я вернул'), (584, 'Не знаю, где этот')], "ASR 'Макеавель-то / Незнайкин' -> 'Макиавелли / Незнайка'"),
    ("librarian", "Ищите дома! И к новой книге относитесь бережно.", "Look for it at home! And treat the new book carefully.", [(585, 'Ищите'), (586, 'Относитесь бережно')], ""),
    ("samson", "Спасибо. До свидания!", "Thank you. Goodbye!", [(588, 'Спасибо. До свидания')], ""),
    ("samson", "Ну как, похож Лёва на ребёнка? Шапку на лоб больше не тяни!", "Well, does Lyova look like a child? Stop pulling the hat down onto your forehead!", [(594, 'похож на ребенка?'), (595, 'Шапку на лоб больше не тяни')], "skipped song in 589-593"),
    ("samson", "Вон Самсонов идёт! Всё, давай, лейтенант, пошёл!", "There goes Samsonov! Right, come on, lieutenant, go!", [(596, 'Вон'), (596, 'идет'), (597, 'Все, давай, лейтенант'), (598, 'пошел')], ""),
    ("samson", "Стой, ты зачем пистолет взял? Ты что, с ума сошёл? Дай сюда!", "Stop, why did you take a pistol? Are you out of your mind? Give it here!", [(599, 'Ты что с ума сошел? Дай сюда')], "slang 'Ствол на базу' in 600 retold as 'ты зачем пистолет взял?'"),
    ("samson", "Вернёшься — отдам обратно.", "When you come back, I'll give it back.", [(601, 'Вернешься, отдам')], ""),
    ("samson", "Алло, Нина! Я в библиотеке был. А что случилось? Всё, скоро буду.", "Hello, Nina! I was at the library. What happened? Right, I'll be there soon.", [(603, 'В библиотеке был'), (604, 'А что случилось?'), (606, 'Все, скоро буду')], ""),
    ("samson", "Да вот иду уже! Сейчас через сад и мост — и дома.", "I'm walking already! Right now through the park and the bridge, and I'm home.", [(607, 'Да вот иду уже'), (608, 'через сад и мост и дома')], ""),
]
OPENER = "Let's walk through what happens inside and outside the library."
WALK = [
    (0, None, "At the library desk, the stern librarian hands Samsonov his book: 'Samsonov, here, please, is your book. This is Sun Tzu, as you asked.'"),
    (1, 'Книга новая, мы её только что получили.', "'The book is new, we just received it.' The two-word phrase before the verb means 'just now'."),
    (1, 'Пожалуйста, относитесь к ней бережно.', "'Please treat it carefully.' The self-action verb form for 'treat' or 'relate to' takes the preposition 'to' plus the 'to/for' form."),
    (2, None, "Samson grins reassuringly: 'Don't you worry, everything will be great!' That casual tone sets the librarian off."),
    (3, 'Я вообще вам могу ничего не давать!', "'I don't have to give you anything at all!' The librarian uses the adverb for 'at all' right alongside the verb meaning 'can'."),
    (3, 'Потому что вы злостный должник.', "'Because you are a chronic debtor.' Literally a malicious or habitual debtor."),
    (4, 'Вы когда взяли книгу Носова?', "'When did you borrow Nosov's book?' Nikolai Nosov is the famous Soviet author of the children's stories about Neznaika, or Know-Nothing."),
    (4, 'В восемьдесят четвёртом году!', "'In the year eighty-four!' Notice the location ending '-u' on the word for 'year'."),
    (5, 'Уже тридцать четыре года прошло!', "'Thirty-four years have passed already!' The librarian pairs the verb for 'have passed' with 'years' in the 'of' form."),
    (5, 'Вам не стыдно?', "'Aren't you ashamed?' Literally 'to you is it not shameful?'."),
    (6, 'Но Макиавелли я же вернул!', "Samson defends himself: 'But I did return Machiavelli!'"),
    (6, 'А где этот Незнайка, я не знаю.', "'And where that Neznaika is, I don't know.' He borrowed it when he was ten years old!"),
    (7, None, "'Look for it at home! And treat the new book carefully.' The adjective for 'new' agrees in gender, number, and case with 'book'."),
    (8, None, "Samson takes the book politely: 'Thank you. Goodbye!' Outside the library, Major Lavrov and Captain Ovechkin inspect young Lieutenant Lyova in his oversized child's clothes."),
    (9, 'Ну как, похож Лёва на ребёнка?', "'Well, does Lyova look like a child?' The short adjective for 'similar to' or 'looks like' takes the preposition 'onto' plus the object-form."),
    (9, 'Шапку на лоб больше не тяни!', "'Stop pulling the hat down onto your forehead!' The negative particle sits directly before the verb for 'pull' to negate the action."),
    (10, None, "Spotting Samsonov coming out of the library doors, Lavrov gives the signal: 'There goes Samsonov! Right, come on, lieutenant, go!' Suddenly Lavrov notices a bulge under Lyova's jacket."),
    (11, 'Стой, ты зачем пистолет взял?', "'Stop, why did you take a pistol?' Major Lavrov pairs the verb for 'stop' with 'pistol' in the direct-object form."),
    (11, 'Ты что, с ума сошёл? Дай сюда!', "'Are you out of your mind? Give it here!' Lavrov confiscates the service pistol before sending Lyova to pick a fight."),
    (12, None, "'When you come back, I'll give it back.' Notice how two future-tense single-action form side by side mean 'when you return, I will give it back'. Meanwhile, Samson answers a call from Nina."),
    (13, None, "'Hello, Nina! I was at the library. What happened? Right, I'll be there soon.' The verb for 'was' is in the masculine past tense, marked by the '-l' ending."),
    (14, 'Да вот иду уже!', "'I'm walking already!' The key word here means 'I am walking', anchored at the close by 'already'."),
    (14, 'Сейчас через сад и мост — и дома.', "'Right now through the park and the bridge, and I'm home.' That footbridge is where Lyova is waiting for him."),
]
TRANSITION = "Now let's listen to the whole library scene again."
OUTRO = "Carrying Sun Tzu's 'The Art of War' under his arm, Samsonov heads across the park footbridge toward home—straight into Lavrov's camera trap. Listen for 'carefully', 'debtor', and 'at the library' when you watch. See you next time!"
CLOSING = ("samson", "Пока!")
