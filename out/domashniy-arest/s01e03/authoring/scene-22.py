# domashniy-arest/s01e03/scene-22.py
ID = "domashniy-arest-s01e03-scene-22"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 22
TITLE = "Аванс  (The Advance)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"
VOICES = {"narrator": "sky", "chief": "anja", "marina": "angelina"}
LABELS = {"chief": "Михаил Михайлович", "marina": "Марина"}
INTRO = "Meanwhile, at security headquarters, Marina is meeting the local chief, Mikhail Mikhailovich. Here at headquarters, the chief has good news for Marina about her mission to plant the listening bug, plus an envelope she does not expect. Let's listen in Russian first."
STORY = [
    ("chief", "Марина Сергеевна, присядьте. Попробуйте чай с сушками, очень вкусные.", "Marina Sergeyevna, have a seat. Try the tea with bread rings, they're very tasty.", [(732, 'Присядьте'), (729, 'попробуйте с сушками. Очень вкусные')], "'Марина Сергеевна' and 'чай' added"),
    ("marina", "Да, спасибо, Михаил Михайлович.", "Yes, thank you, Mikhail Mikhailovich.", [(733, 'Да, спасибо, Михаил Михайлович')], ""),
    ("chief", "Ну вот, само всё разрешилось. Аникеев сегодня едет в суд.", "Well, everything worked itself out. Anikeev is going to court today.", [(735, 'Ну вот, само все разрешилось'), (736, 'едет в суд')], "cue 736 'А Никеев' is a transcription slip for 'Аникеев'; 'сегодня' added"),
    ("chief", "Его не будет часа два. Вы спокойно всё сделаете.", "He'll be gone for about two hours. You'll do everything calmly.", [(736, 'его не будет часа два'), (737, 'Вы спокойно все сделаете')], ""),
    ("marina", "А дальше? Я очень волнуюсь, я к этому не приспособлена.", "And then what? I'm very nervous, I'm not cut out for this.", [(738, 'А дальше'), (739, 'я к этому не приспособлена')], "cue 739 garbled 'Я у него тахария' (tachycardia) -> 'Я очень волнуюсь'"),
    ("chief", "Да, кстати, чуть не забыл.", "Oh, by the way, I almost forgot.", [(740, 'Да, кстати, чуть не забыл')], ""),
    ("marina", "Что это?", "What's this?", [(741, 'Что это')], ""),
    ("chief", "Это ваш аванс. Вот в ведомости расписаться надо.", "This is your advance. Here, you need to sign the payment sheet.", [(742, 'Это ваш аванс'), (743, 'ведомости расписаться надо')], "cue 743 'Вот и' -> 'Вот в'"),
    ("marina", "Вы что, меня покупаете, что ли?", "What, are you buying me or something?", [(744, 'Вы что, меня покупаете, что ли')], ""),
    ("chief", "Да никто никого не покупает. Это заложено в бюджет операции.", "Nobody is buying anybody. It's built into the operation budget.", [(745, 'Да никто никого не покупает'), (746, 'Это заложено в бюджет операции')], ""),
    ("chief", "Прошу.", "Please, go ahead.", [(747, 'Прошу')], ""),
    ("marina", "Хорошо. Значит, вот куда идут деньги налогоплательщиков.", "Fine. So this is where taxpayers' money goes.", [(748, 'Хорошо. Значит, вот куда идут'), (749, 'Деньги')], "cue 749 'налог, платильщиков' is a transcription slip for 'налогоплательщиков'"),
    ("marina", "Всё, я пошла. До свидания.", "Right, I'm off. Goodbye.", [(730, 'Все, я пошла')], "moved to Marina's exit; 'До свидания' added"),
    ("chief", "Надо было бабушку брать.", "We should have taken the old lady.", [(753, 'Надо было'), (753, 'брать')], "'бабку' -> 'бабушку'"),
]
OPENER = "Let's go through it step by step. Mikhail Mikhailovich welcomes Marina into his office and offers her tea and dry bread rings."
WALK = [
    (0, 'Марина Сергеевна, присядьте.', "'Marina Sergeyevna, have a seat.' He uses her first name and father's name, with a polite plural command that literally means 'sit down for a moment'. Then he points to the table."),
    (0, 'Попробуйте чай с сушками, очень вкусные.', "'Try the tea with bread rings, they're very tasty.' Bread rings are small, crunchy ring-shaped rolls that Russians love with tea. After 'with', the noun takes the 'with'-form plural ending. Marina replies politely."),
    (1, None, "'Yes, thank you, Mikhail Mikhailovich.' Both of them stay on formal terms. Now the chief gets to the news."),
    (2, 'Ну вот, само всё разрешилось.', "'Well, everything worked itself out.' Literally 'everything resolved itself on its own'. Remember, earlier Marina couldn't plant the bug because Arkady came back to his room too soon."),
    (2, 'Аникеев сегодня едет в суд.', "'Anikeev is going to court today.' The verb for 'is going' specifically means going by vehicle, not on foot. And that gives Marina plenty of time."),
    (3, 'Его не будет часа два.', "'He'll be gone for about two hours.' Literally 'of him there will not be hours two'. In Russian, putting the noun 'hours' before the number 'two' turns it into an estimate: 'about two hours'."),
    (3, 'Вы спокойно всё сделаете.', "'You'll do everything calmly.' A future-tense form: one clean job, finished while Arkady is away. Marina is still uneasy."),
    (4, 'А дальше?', "'And then what?' Literally 'and further?'. She isn't a secret agent, and this whole business scares her."),
    (4, 'Я очень волнуюсь, я к этому не приспособлена.', "'I'm very nervous, I'm not cut out for this.' The last word has the feminine short ending because Marina is a woman: literally 'not adapted to this'. Then the chief reaches into his desk."),
    (5, None, "'Oh, by the way, I almost forgot.' The little word before 'not' means 'nearly' or 'almost', so 'almost didn't forget' is the Russian idiom for 'almost forgot'. He puts an envelope on the table."),
    (6, None, "'What's this?' Two tiny words. The chief explains."),
    (7, 'Это ваш аванс.', "'This is your advance.' Cash up front for helping the security service. And like any Russian office, there is paperwork."),
    (7, 'Вот в ведомости расписаться надо.', "'Here, you need to sign the payment sheet.' Literally 'in the register to sign it is necessary'. Marina looks at the money with indignation."),
    (8, None, "'What, are you buying me or something?' The two little words at the end add an indignant 'or what?'. Remember, she only agreed to help because of her son and her job. The chief doesn't blink."),
    (9, 'Да никто никого не покупает.', "'Nobody is buying anybody.' Mikhail Mikhailovich uses the single-action form form for 'is buying' to point to a single, definite result."),
    (9, 'Это заложено в бюджет операции.', "'It's built into the operation budget.' To the chief, it's just normal bookkeeping. He hands her the pen."),
    (10, None, "'Please, go ahead.' Literally 'I ask', a formal one-word way to invite someone to sign or step through a door. Marina signs the sheet and takes the envelope, but she can't resist a parting shot."),
    (11, 'Хорошо.', "'Fine.' She gives in, then looks at the cash."),
    (11, 'Значит, вот куда идут деньги налогоплательщиков.', "'So this is where taxpayers' money goes.' That long last word is 'of taxpayers', built from the words for 'tax' and 'payer'. Then she gets up to leave."),
    (12, None, "'Right, I'm off. Goodbye.' She uses the feminine past form, 'I set off', which is how Russians say 'I'm heading out'. In the show, she even tries to walk out through the archive door by mistake. Once she is gone, the chief sighs."),
    (13, None, "'We should have taken the old lady.' Literally 'it was necessary to take the grandmother'—meaning old Klavdia Viktorovna, whom he wanted to recruit in the first place."),
]
TRANSITION = "Now let's hear the whole conversation at headquarters again."
OUTRO = "So Marina has her advance in her pocket and believes Arkady is off to court for two hours—though as we know, Arkady is still tied to a chair in the communal flat. See you next time!"
CLOSING = ("chief", "Пока!")
