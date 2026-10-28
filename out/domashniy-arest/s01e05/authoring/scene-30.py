# Authoring module for domashniy-arest-s01e05-scene-30.
ID = 'domashniy-arest-s01e05-scene-30'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 5
SCENE = 30
TITLE = "Благодарность Марины  (Marina's Gratitude)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'marina': 'Марина'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.05'
SOURCE_FILE = 'sources/domashniy-arest/s01/e05.ru.dual.srt'
INTRO = "In Arkady's tiny room behind the wardrobe late at night. Last time, Governor Viktor Stepanovich phoned Pasha from his steam bath to berate him for losing the Blind Society scandal, asking if Pasha was worse than a monkey. Meanwhile, back at the communal flat, there is a quiet knock on Arkady's door: it is Marina Sergeyevna. Let's listen in Russian first."
OPENER = "Let's take the scene line by line. Arkady opens his door and sees Marina standing there."
TRANSITION = "Now let's hear the whole scene once more, start to finish."
OUTRO = "And that brings Episode Five to a close! Even when Arkady does something genuinely generous, he manages to ruin it in five seconds flat and earn a slap across the face. The next morning at the university, though, his good deed has a hilarious sequel: escorted by Arkady's giant former bodyguards, bruised debt collectors Uncle Grisha and Kostik have been forced to enrol as polite students in Marina's history lectures! See you in Episode Six. See you next time!"
CLOSING = ('marina', 'Пока!')
STORY = [
    ('arkady', 'О, жертва коллекторов! Вы что-то хотели?', "Oh, the collectors' victim! Did you want something?", [(1146, 'Жертва коллекторов'), (1147, 'Что-то хотели')], ''),
    ('marina', 'Да. Я пришла сказать спасибо и попросить прощения.', 'Yes. I came to say thank you and ask forgiveness.', [(1148, 'Да, сказать спасибо и попросить прощения')], "'Я пришла' added"),
    ('arkady', 'За что?', 'What for?', [(1149, 'За что')], ''),
    ('marina', 'Я вас обидела. Я была неправа.', 'I offended you. I was wrong.', [(1150, 'Я вас обидела'), (1151, 'Была неправа')], ''),
    ('arkady', 'Вот такая вы нехорошая.', "That's how naughty you are.", [(1152, 'Вот такая вы нехорошая')], ''),
    ('marina', 'Правда, спасибо вам.', 'Really, thank you.', [(1153, 'Правда, спасибо')], ''),
    ('marina', 'Но я просто не знаю, как вас поблагодарить.', "But I just don't know how to thank you.", [(1154, 'Но я просто не знаю, как вас')], "'отблагодарить' -> 'поблагодарить'"),
    ('arkady', 'Ладно, всякое бывает. Ну что вы?', 'Alright, all sorts of things happen. Oh, come on.', [(1155, 'Ладно, всякое бывает'), (1156, 'Ну что вы')], ''),
    ('arkady', 'Успокойтесь. Всё уже позади.', 'Calm down. Everything is behind us now.', [(1157, 'успокойтесь'), (1158, 'Все уже позади')], "'Дай Бог' dropped"),
    ('arkady', 'Присядьте. Всё уже хорошо, всё закончилось.', "Have a seat. Everything is fine now, it's all over.", [(1159, 'присядьте'), (1160, 'Все уже хорошо'), (1161, 'Все закончилось')], "'Господи' dropped"),
    ('arkady', 'Вот и чудесно. Это нормально.', "There, that's wonderful. That's normal.", [(1162, 'Вот и чудесно'), (1164, 'Это нормально')], 'garbled cue 1163 omitted'),
    ('arkady', 'Мужчина должен помогать женщине, верно?', 'A man must help a woman, right?', [(1165, 'Мужчина должен помогать женщине'), (1166, 'Верно')], ''),
    ('arkady', 'А женщина должна помогать мужчине.', 'And a woman must help a man.', [(1167, 'А женщина должна помогать мужчине')], ''),
    ('marina', 'Вы чего?!', "What do you think you're doing?!", [(1168, 'Вы чего')], ''),
    ('arkady', 'Вы же сами сказали, что хотите помочь!', 'But you said yourself that you want to help!', [(1169, 'Вы же сами сказали, что хотите помочь')], ''),
    ('arkady', 'Но вы не знаете как! А я знаю!', "But you don't know how! And I know!", [(1169, 'но не знаете как'), (1170, 'А я')], ''),
    ('marina', 'Вот вы с ума сошли!', 'You have lost your mind!', [(1173, 'Вот вы')], "cue 1171 'мразь' omitted; 'сдурели' (1173) -> 'с ума сошли'"),
    ('arkady', 'Подождите, вы же сами только что сказали!', 'Wait, you just said so yourself!', [(1172, 'Подождите, вы же сами сказали, только что'), (1174, 'вы сами сказали')], ''),
]
WALK = [
    (0, None, "'Oh, the collectors' Victim! Did you want something?' The word 'collectors' is in the plural 'of' form: 'victim of collectors'. Marina looks at him earnestly."),
    (1, 'Я пришла сказать спасибо и попросить прощения.', "'Yes. I came to say thank you and ask forgiveness.' Earlier today at the university, she saw Arkady's gold watch on Captain Zavarzin's wrist and realised it was really Arkady who paid her debt."),
    (2, None, "'What for?' Arkady plays innocent."),
    (3, None, "'I offended you. I was wrong.' Notice the feminine endings on both 'offended' and 'wrong'. Earlier she accused him of staging the whole thing as a cheap trick. Arkady smiles."),
    (4, None, "'That's how naughty you are.' Literally, 'such a not-good one you are', said in a gentle, teasing tone. Marina's eyes fill with tears."),
    (5, None, "'Really, thank you.' And she adds what is weighing on her heart."),
    (6, None, "'But I just don't know how to thank you.' In the show she says 'how to repay you', and bursts into tears on Arkady's shoulder. Arkady awkwardly pats her back."),
    (7, None, "'Alright, all sorts of things happen. Oh, come on.' The neuter word 'every kind of thing' with the action word 'happens' is the everyday Russian way to say 'these things happen'."),
    (8, None, "'Calm down. Everything is behind us now.' The word at the end literally means 'behind'."),
    (9, None, "'Have a seat. Everything is fine now, it's all over.' He sits her down on his narrow iron bed and dries her tears."),
    (10, None, "'There, that's wonderful. That's normal.' For a moment, Arkady actually looks like a decent human being."),
    (11, None, "'A man must help a woman, right?' After 'help', the word 'woman' takes the 'to/for' ending. Marina nods gratefully — and then Arkady ruins everything."),
    (12, None, "'And a woman must help a man.' Notice how 'must' changes to the feminine form to match 'woman', and 'man' takes the 'to/for' ending. And with that, Arkady leans in and tries to kiss her! Marina shoves him back and slaps his face."),
    (13, None, "'What do you think you're doing?!' Literally, 'you what?!'. Arkady holds his cheek in disbelief."),
    (14, None, "'But you said yourself that you want to help!' He completely misread her tears of gratitude."),
    (15, None, "'But you don't know how! And I know!' At this point, Marina glares at him in fury."),
    (16, None, "'You have lost your mind!' Literally, 'you went down from your mind'. She storms out and slams the door, leaving Arkady calling after her."),
    (17, None, "'Wait, you just said so yourself!' The two-word phrase before the action word means 'just now'."),
]
