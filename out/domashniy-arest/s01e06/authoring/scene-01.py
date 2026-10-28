# domashniy-arest/s01e06/scene-01.py
ID = "domashniy-arest-s01e06-scene-01"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 6
SCENE = 1
TITLE = "Искусство войны  (The Art of War)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.06"
SOURCE_FILE = "sources/domashniy-arest/s01/e06.ru.dual.srt"
VOICES = {"narrator": "sky", "anya": "alisa", "samson": "anja", "lyolya": "angelina"}
LABELS = {"anya": "Аркадий", "samson": "Самсон", "lyolya": "Лёля"}
INTRO = "Welcome back to House Arrest. We open inside Arkady's cramped room in the communal flat, where Arkady is having a vivid dream about his young girlfriend Lyolya until Samson barges in at dawn holding the book. Let's listen in Russian first."
STORY = [
    ("anya", "Лёлечка, ну зачем ты пришла?", "Lyolechka, why did you come?", [(4, 'Лёлечка, ну зачем ты пришла')], "cues 1-3 ('шлюх') omitted"),
    ("lyolya", "Так я соскучилась, кот!", "Because I missed you, kitty!", [(5, 'Так я соскучилась, кот')], ""),
    ("anya", "Ты думаешь, я не соскучился? Я уже на стенку лезу!", "Do you think I didn't miss you? I'm already climbing the wall!", [(6, 'Ты думаешь, я не соскучился? Я уже на стенку лезу')], ""),
    ("anya", "Но у меня много работы. Так что иди домой.", "But I have a lot of work. So go on home.", [(7, 'Но я'), (7, 'работы'), (8, 'Так что'), (8, 'домой')], "'должен выполнить большой объём работы' simplified to 'у меня много работы'; 'давай, дуй' -> 'иди'"),
    ("lyolya", "Что, я зря пришла? Я надела костюм зайки!", "What, did I come for nothing? I put on a bunny costume!", [(9, 'Что, я зря'), (10, 'костюм зайки')], "cue 10 'Надевала костюм зайки из Верополиса' simplified"),
    ("anya", "Это запрещённый приём!", "That is a forbidden move!", [(11, 'Это запрещённый приём')], ""),
    ("samson", "Аркаша, ты же сам сказал! Чтобы дикция была нормальная!", "Arkasha, you said so yourself! So that my diction would be normal!", [(29, 'ты же'), (29, 'сам сказал, чтобы дикция была нормальная')], "cue 29 garbled 'Рейх' -> 'Аркаша'"),
    ("samson", "Я прочитал Макиавелли, Государь этот.", "I read Machiavelli, that book The Prince.", [(30, 'прочитал'), (30, 'Государь этот')], "cue 30 'Маккавелли' -> 'Макиавелли'"),
    ("samson", "Ну злодеи они там все, конечно! Но книжка интересная.", "Well, they are all villains in there, of course! But the book is interesting.", [(31, 'ну'), (31, 'они там все, конечно'), (32, 'книжка'), (32, 'интересная')], "crude 'твари' in cue 31 -> 'злодеи'"),
    ("samson", "Что ещё тут прочитать?", "What else should I read here?", [(33, 'ещё тут прочитать')], "colloquial 'Чё' -> 'Что'"),
    ("anya", "Ещё секунду! Ты мне такой сон прервал!", "Just one more second! You interrupted such a dream of mine!", [(35, 'Ещё секунду, мне')], "cue 35 'бы секс приснился' cleaned up to 'ты мне такой сон прервал'"),
    ("anya", "Иди, позже заходи! Потом!", "Go on, come by later! Later!", [(36, 'Иди, иди позже заходи'), (37, 'Потом')], ""),
    ("samson", "Аркаш, ну ты сам говорил! Времени совсем нет!", "Arkasha, you said so yourself! There is no time at all!", [(38, 'Аркаш, ну ты'), (38, 'сам говорил, времени нет')], "'совсем' added"),
    ("anya", "Читай Искусство войны, Сунь-цзы!", "Read The Art of War, by Sun Tzu!", [(39, 'Искусство')], "cue 39 garbled 'Искусство военной сунь зей' -> 'Читай Искусство войны, Сунь-цзы!'"),
    ("samson", "Сунь что? Тебе что там снится?", "Sun what? What are you dreaming about in there?", [(40, 'Сунь'), (42, 'там снится')], "colloquial 'чё' -> 'что'"),
]
OPENER = "Let's go back through the scene step by step. In Arkady's dream, his young girlfriend Lyolya walks into his room in the communal flat."
WALK = [
    (0, None, "'Lyolechka, why did you come?' Arkady uses an affectionate diminutive of Lyolya's name."),
    (1, None, "'Because I missed you, kitty!' The self-action verb form for 'missed' is past feminine singular, and she calls Arkady her tomcat."),
    (2, 'Ты думаешь, я не соскучился?', "'Do you think I didn't miss you?' Arkady answers with the masculine past tense of the same verb."),
    (2, 'Я уже на стенку лезу!', "'I'm already climbing the wall!' Climbing onto the wall is the classic Russian idiom for going crazy from boredom or impatience."),
    (3, None, "'But I have a lot of work. So go on home.' Notice that 'home' as a direction is a special adverb."),
    (4, 'Что, я зря пришла?', "'What, did I come for nothing?' The short adverb means 'in vain' or 'for nothing'."),
    (4, 'Я надела костюм зайки!', "'I put on a bunny costume!' Literally 'costume of a little hare', with 'bunny' in the 'of' form."),
    (5, None, "'That is a forbidden move!' It is a sports term for an illegal hold or foul play. In his dream, neighbour Marina suddenly bursts in dressed as a strict police inspector while Pasha's assistant sings on stage, until someone shakes Arkady's shoulder in real life."),
    (6, None, "'Arkasha, you said so yourself! So that my diction would be normal!' Samson is standing over Arkady's bed at dawn, wide awake."),
    (7, None, "'I read Machiavelli, that book The Prince.' Arkady had given him the classic book on political power to practise reading aloud."),
    (8, 'Ну злодеи они там все, конечно!', "'Well, they are all villains in there, of course!' Samson is shocked by how ruthless politicians are."),
    (8, 'Но книжка интересная.', "'But the book is interesting.' He uses the friendly diminutive word for a book."),
    (9, None, "'What else should I read here?' An action verb question asking what he ought to read next."),
    (10, None, "'Just one more second! You interrupted such a dream of mine!' Literally 'to me you interrupted such a dream'."),
    (11, None, "'Go on, come by later! Later!' Arkady pulls the blanket over his head, but Samson won't budge."),
    (12, None, "'Arkasha, you said so yourself! There is no time at all!' With 'there is no', the noun 'time' takes the 'of'-form singular."),
    (13, None, "'Read The Art of War, by Sun Tzu!' Literally 'Art of war', with 'war' in the 'of' form singular. Samson blinks at the unfamiliar Chinese name."),
    (14, None, "'Sun what? What are you dreaming about in there?' Literally 'what dreams itself to you there?'"),
]
TRANSITION = "Now let's hear the whole opening scene again from the start."
OUTRO = "So Samson is now devouring books on political strategy at dawn. See you next time!"
CLOSING = ("anya", "Пока!")
