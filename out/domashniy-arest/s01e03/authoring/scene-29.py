# Authoring module for domashniy-arest-s01e03-scene-29.
ID = 'domashniy-arest-s01e03-scene-29'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 3
SCENE = 29
TITLE = "Решение суда  (The Court's Ruling)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'judge': 'Илья Олегович', 'prosecutor': 'Прокурор'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.03'
SOURCE_FILE = 'sources/domashniy-arest/s01/e03.ru.dual.srt'
INTRO = "In the courtroom a little later. Last time, glamorous Lyolya charmed Slavik's classmates at Dimon's party by pretending to be Slavik's obedient girlfriend. Meanwhile at the city court, Judge Berg has kept his end of the bargain to save his dog and is reading out the ruling on Arkady's appeal. We'll hear it in Russian first; don't worry about catching every word."
OPENER = "Let's go through the courtroom scene line by line. Judge Berg stands behind the bench reading his decision."
TRANSITION = "Let's hear the whole scene once more, start to finish."
OUTRO = 'Just when Arkady thought he was walking out of court on a travel ban, his own public defender has turned up as a witness for the prosecution. You followed all that courtroom Russian; well done. See you next time!'
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('judge', 'Суд учёл новые обстоятельства дела.', 'The court has considered the new circumstances of the case.', [(1001, 'Суд учел новые обстоятельства дела')], ''),
    ('judge', 'Конфликты с соседями угрожают здоровью подсудимого.', "Conflicts with the neighbours threaten the defendant's health.", [(1004, 'конфликты с соседями'), (1005, 'угрожают здоровью'), (1005, 'подсудимого')], 'simplified from cues 1004-1005'),
    ('judge', 'Суд постановил жалобу Аникеева удовлетворить.', "The court has ruled to grant Anikeev's appeal.", [(1008, 'суд постановил'), (1008, 'жалобу Аникеева'), (1009, 'удовлетворить')], 'simplified from cues 1008-1009'),
    ('judge', 'Заменить домашний арест на подписку о невыезде.', 'To replace house arrest with a travel ban.', [(1011, 'на подписку о невыезде')], 'simplified from cues 1010-1011'),
    ('arkady', 'Да! Наконец-то! Я свободен!', "Yes! At last! I'm free!", [], "Arkady celebrates in court, prompting Judge Berg's call for order in cue 1013"),
    ('judge', 'Требую тишины! Уважайте суд!', 'I demand silence! Respect the court!', [(1013, 'Требую тишины. Уважайте суд')], ''),
    ('prosecutor', 'Ваша честь, у нас есть важное заявление.', 'Your Honour, we have an important statement.', [(1016, 'Ваша честь')], 'lead-in to cue 1016'),
    ('prosecutor', 'Обвинение просит приобщить новый материал.', 'The prosecution asks to add new material to the case.', [(1016, 'обвинение')], "'обращается с ходатайством о приобщении к делу нового материала' (1016-1017) -> 'просит приобщить новый материал'"),
    ('arkady', 'Какого ещё материала? Что такое?', 'What new material? What is this?', [(1018, 'Какого еще материала'), (1019, 'что такое')], ''),
    ('judge', 'Хорошо. Пригласите вашего свидетеля.', 'Very well. Call your witness.', [], 'Judge Berg allows the witness before cue 1021'),
    ('prosecutor', 'Прошу в зал суда.', 'Please enter the courtroom.', [], 'prosecutor invites the witness in'),
    ('arkady', 'Кто это? Вы?!', 'Who is that? You?!', [(1021, 'Вы')], "'Кто это?' added"),
]
WALK = [
    (0, None, "'The court has considered the new circumstances of the case.' The verb literally means 'took into account'. And what are those new circumstances?"),
    (1, None, "'Conflicts with the neighbours threaten the defendant's health.' After the verb 'threaten', 'health' takes the 'to/for' form: literally, 'threaten to the health'. That is how Berg justifies letting Arkady leave the communal flat."),
    (2, None, "'The court has ruled to grant Anikeev's appeal.' In Russian legal style, the basic verb form 'to satisfy' comes right at the end of the sentence."),
    (3, None, "'To replace house arrest with a travel ban.' With the verb 'replace', the new thing is introduced by 'onto': replace house arrest onto a travel ban. Arkady can't contain his joy."),
    (4, None, "'Yes! At last! I'm free!' He uses the short masculine form for 'free'. Judge Berg bangs his gavel."),
    (5, None, "'I demand silence! Respect the court!' After 'I demand', 'silence' takes the 'of'-form ending. Just as Arkady prepares to walk out a free man, the prosecutor rises."),
    (6, None, "'Your Honour, we have an important statement.' In a Russian courtroom, the judge is addressed as 'Your Honour'. Then comes the bombshell."),
    (7, None, "'The prosecution asks to add new material to the case.' Literally, 'to attach new material'. Arkady's smile vanishes."),
    (8, None, "'What new material? What is this?' He echoes the prosecutor's word in the 'of' form: 'of what material besides?' Judge Berg has no choice in open court."),
    (9, None, "'Very well. Call your witness.' Literally, that means 'invite your witness into the room'."),
    (10, None, "'Please enter the courtroom.' Literally, 'I ask into the hall of the court'. The door opens, and Arkady stares at the man who walks in."),
    (11, None, "'Who is that? You?!' It is his own stuttering public defender, Danila Golovkin, whom Arkady casually bragged to about handing out flats through connections."),
]
