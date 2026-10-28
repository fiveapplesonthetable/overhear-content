# domashniy-arest/s01e03/scene-11.py
ID = "domashniy-arest-s01e03-scene-11"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 11
TITLE = "Государственный адвокат  (The Public Defender)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"
VOICES = {"narrator": "sky", "anya": "alisa", "golovkin": "anja", "mishkin": "angelina"}
LABELS = {"anya": "Аркадий", "golovkin": "Головкин", "mishkin": "Мишкин"}
INTRO = "Last time, Arkady caught Marina in his room with the foil packet and smugly turned her down, sure that his Moscow lawyer Mishkin had just arrived at the door. Instead, standing on the threshold in an oversized brown suit is a nervous, stuttering public defender named Danila Golovkin. We'll hear the scene in Russian first; don't worry about catching every word."
STORY = [
    ("golovkin", "Добрый день, Аркадий Борисович.", "Good afternoon, Arkady Borisovich.", [(363, 'добрый день, Аркадий Борисович')], ""),
    ("anya", "Здравствуйте. Вы кто?", "Hello. Who are you?", [(364, 'Здравствуйте, вы кто')], ""),
    ("golovkin", "Я Данила Головкин, ваш адвокат.", "I'm Danila Golovkin, your lawyer.", [(365, 'Я Данила Головкин, ваш')], "cue 365 stutters 'ваш авокадо'; normalised to 'ваш адвокат' in the story line and explained by the narrator"),
    ("anya", "В смысле? А Мишкин где?", "What do you mean? Where is Mishkin?", [(366, 'В смысле? А Мишкин где')], ""),
    ("golovkin", "Я не знаю. Я бесплатный государственный адвокат.", "I don't know. I'm the free state-appointed lawyer.", [(367, 'Я не знаю'), (367, 'бесплатный государственный адвокат')], "cues 367-368 'Вам полагается бесплатный государственный адвокат? Полагается. Так вот, этой я' simplified to A1"),
    ("anya", "Секунду. Сейчас я позвоню Мишкину.", "One second. I'll call Mishkin right now.", [(369, 'Секунду')], "cue 370 'Ну-ка, иди сюда, Мишкин' as he dials rewritten clearly"),
    ("anya", "Андрей Иосифович, Аникеев беспокоит.", "Andrei Iosifovich, it's Anikeev calling.", [(371, 'Андрей'), (371, 'беспокоит')], "cue 371 mistranscribes 'Иосифович' as 'Васильевич' and 'Аникеев' as 'Аникея'"),
    ("anya", "Послушайте, здесь ошибка. Ко мне прислали бесплатного адвоката. В чём дело?", "Listen, there's a mistake here. They sent me a free lawyer. What's going on?", [(372, 'Послушайте, здесь'), (373, 'Ко мне прислали бесплатного адвоката. В чем дело')], "cue 372 'какое-то недоразумение' -> A1 'ошибка'"),
    ("mishkin", "Работайте с ним. Я вынужден вернуться в Москву.", "Work with him. I'm forced to return to Moscow.", [(374, 'Работайте с ним, я вынужден вернуться в Москву')], ""),
    ("anya", "Что это значит — вернуться в Москву?", "What does that mean, return to Moscow?", [(375, 'Что это значит, вернуться в Москву')], ""),
    ("mishkin", "По семейным обстоятельствам. Не звоните мне больше.", "For family reasons. Don't call me any more.", [(376, 'По семейным обстоятельствам'), (378, 'Не звоните мне больше')], ""),
    ("anya", "Вот дела. Он уехал!", "What a mess. He left!", [], "Arkady hangs up in disbelief (replacing cue 379 'Хорошая городишка')"),
    ("golovkin", "А мне что, уйти?", "So should I leave?", [(380, 'А мне что, уйти')], ""),
    ("anya", "Нет, подождите. Заходите.", "No, wait. Come in.", [], "Arkady reluctantly lets Golovkin stay"),
]
OPENER = "Let's break it down. Arkady opens the door expecting sleek Moscow lawyer Mishkin, and sees a timid stranger with a battered briefcase."
WALK = [
    (0, None, "'Good afternoon, Arkady Borisovich.' Very polite, using first name and patronymic. Arkady stares at him."),
    (1, None, "'Hello. Who are you?' Literally 'you who?'. The newcomer introduces himself."),
    (2, None, "'I'm Danila Golovkin, your lawyer.' In the show, poor Golovkin has a strong stutter and accidentally says 'your avocado' instead of 'your lawyer'. Arkady is baffled."),
    (3, None, "'What do you mean? Where is Mishkin?' The first phrase literally means 'in what sense?' and is a very common way to say 'what do you mean?'. Golovkin explains why he is here."),
    (4, None, "'I don't know. I'm the free state-appointed lawyer.' That means a public defender paid by the state when a defendant has no lawyer of his own. Arkady immediately reaches for his phone."),
    (5, None, "'One second. I'll call Mishkin right now.' The key word here means 'second', anchored at the close by 'will call'."),
    (6, None, "'Andrei Iosifovich, it's Anikeev calling.' Literally 'Anikeev disturbs you' — standard polite phone Russian when you call someone on business."),
    (7, 'Послушайте, здесь ошибка.', "'Listen, there's a mistake here.' Then he explains what happened."),
    (7, 'Ко мне прислали бесплатного адвоката. В чём дело?', "'They sent me a free lawyer. What's going on?' Notice the animate object ending on 'free lawyer': for masculine living beings, the object form looks like the 'of' form. Mishkin's answer is cold."),
    (8, None, "'Work with him. I'm forced to return to Moscow.' The short form in the middle means 'forced' or 'obliged'. Arkady cannot believe his ears."),
    (9, None, "'What does that mean, return to Moscow?' The evening court hearing is only hours away."),
    (10, 'По семейным обстоятельствам.', "'For family reasons.' Literally 'by family circumstances' — the classic official excuse."),
    (10, 'Не звоните мне больше.', "'Don't call me any more.' And Mishkin hangs up."),
    (11, None, "'What a mess. He left!' Meanwhile, Golovkin is still standing awkwardly by the door."),
    (12, None, "'So should I leave?' Literally 'and to me what, to leave?'. With an action verb, the 'to'-form 'to me' asks what someone is supposed to do. Arkady has no choice left."),
    (13, None, "'No, wait. Come in.' Two polite commands, and Golovkin steps inside."),
]
TRANSITION = "Let's listen to the whole conversation again from the beginning."
OUTRO = "Right after this, a brief flashback shows why Mishkin fled: Pasha gave him a local souvenir showing monks who were brutally killed defending the monastery, calling it 'a hint', and Mishkin replied, 'I'm weak, but I'm not stupid.'. See you next time!"
CLOSING = ("golovkin", "Пока!")
