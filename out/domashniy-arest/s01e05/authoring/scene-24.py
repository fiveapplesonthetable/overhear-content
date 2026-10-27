ID = "domashniy-arest-s01e05-scene-24"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 5
SCENE = 24
TITLE = "Наградные часы  (The Commendation Watch)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "lavrov": "anja", "zavarzin": "angelina"}
LABELS = {"anya": "Марина", "lavrov": "Лавров", "zavarzin": "Заварзин"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.05"
SOURCE_FILE = "sources/domashniy-arest/s01/e05.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 930-953. Garbled subtitle forms 'часа Никеева' (943), 'Селда Алексеевича' (945), and 'Селд, стунил?' (951) "
    "are restored to 'часы Аникеева', 'Всеволода Алексеевича', and 'Сева, ты с ума сошёл?'. 'Произошла небольшая "
    "накладка' (935) is simplified to 'была маленькая ошибка' and 'провели с этими людьми разъяснительную беседу' "
    "(937) to 'поговорили с этими людьми'."
)

INTRO = (
    "In the university corridor. Last time, at the Society of the Blind, Ilona secretly scattered her own packet of "
    "illegal herbs onto five kilograms of burned sage and called the police with a sniffer dog. Now, after teaching "
    "the two debt collectors a painful lesson at the microloan office, Major Lavrov and Captain Zavarzin come to "
    "reassure Marina Sergeyevna. We'll hear it in Russian first; don't worry about catching every word."
)

STORY = [
 ("lavrov", "Марина Сергеевна, мы приехали сразу, как смогли.",
  "Marina Sergeyevna, we came as soon as we could.",
  [(930, "Марина Сергеевна"), (931, "мы"), (931, "сразу, как смогли")], "'отреагировали' -> 'приехали' (A1)"),
 ("lavrov", "Вы под нашей защитой. Вам не о чем волноваться.",
  "You are under our protection. You have nothing to worry about.",
  [(932, "Вы"), (932, "под нашей защитой"), (933, "вам не о чем")],
  "'находитесь' dropped; 'беспокоиться' -> 'волноваться' (A1)"),
 ("anya", "Я вам звоню, а вы не отвечаете!",
  "I call you, and you don't answer!",
  [(934, "Я вам звоню, а вы")], "'меня сбрасываете' -> 'не отвечаете' (A1)"),
 ("lavrov", "Поймите, была маленькая ошибка. Вы уж нас извините.",
  "Understand, there was a small mistake. Please forgive us.",
  [(935, "Поймите"), (936, "Вы уж нас извините")], "'произошла небольшая накладка' -> 'была маленькая ошибка' (A1)"),
 ("lavrov", "Мы поговорили с этими людьми. Они к вам больше не придут.",
  "We talked with those people. They won't come to you anymore.",
  [(937, "Мы"), (937, "с этими людьми"), (938, "они"), (938, "больше не")],
  "'провели ... разъяснительную беседу' -> 'поговорили'; 'потревожат' -> 'придут' (A1)"),
 ("lavrov", "Марина Сергеевна, не надо никуда ехать. Вы успокоились?",
  "Marina Sergeyevna, there is no need to go anywhere. Have you calmed down?",
  [(939, "Марина Сергеевна, не надо никуда ехать"), (941, "вы успокоились")], ""),
 ("anya", "Да. Подождите, что это на вашей руке?",
  "Yes. Wait, what is that on your arm?",
  [(942, "Да"), (943, "Что это")], "'Подождите ... на вашей руке' added as bridge to cue 943"),
 ("anya", "Это же часы Аникеева!",
  "That is Anikeev's watch!",
  [(943, "Это же")], "garbled 'часа Никеева' -> 'часы Аникеева'"),
 ("lavrov", "Нет. Это часы Всеволода Алексеевича.",
  "No. This is Vsevolod Alexeyevich's watch.",
  [(944, "Нет"), (945, "Это часы"), (945, "Алексеевича")], "garbled 'Селда' -> 'Всеволода'"),
 ("zavarzin", "Да, мои наградные! Из ремонта только что забрал.",
  "Yes, my commendation watch! I just picked it up from repair.",
  [(946, "Да. Мои наградные"), (947, "Из ремонта только что забрал")], ""),
 ("zavarzin", "Давайте я вам помогу с сумкой.",
  "Let me help you with your bag.",
  [(948, "Давайте я вам помогу")], "'с сумкой' added for clarity"),
 ("anya", "Не надо, я сама. До свидания.",
  "No need, I'll do it myself. Goodbye.",
  [(949, "Не надо. Сама")], "'я ... До свидания' added"),
 ("lavrov", "Сева, ты с ума сошёл?",
  "Seva, have you lost your mind?",
  [(951, "Селд")], "garbled 'Селд, стунил?' -> 'Сева, ты с ума сошёл?'"),
 ("zavarzin", "Извини, не успел убрать.",
  "Sorry, I didn't have time to put it away.",
  [(952, "Извини, не успел убрать")], ""),
]

OPENER = (
    "Let's go through the scene line by line. Major Lavrov and Captain Zavarzin meet Marina in the corridor to stop "
    "her from packing up and leaving the flat."
)

WALK = [
 (0, None,
  "'Marina Sergeyevna, we came as soon as we could.' Both verbs are in the plural past tense ending in '-li'."),
 (1, None,
  "'You are under our protection. You have nothing to worry about.' The preposition 'under' takes the instrumental "
  "case, and 'nothing to worry about' literally says 'to you there is not about what to worry'."),
 (2, None,
  "'I call you, and you don't answer!' Marina is still upset that Zavarzin kept hanging up when the collectors broke "
  "into her room."),
 (3, None,
  "'Understand, there was a small mistake. Please forgive us.' Lavrov uses two polite plural imperatives to smooth "
  "things over."),
 (4, None,
  "'We talked with those people. They won't come to you anymore.' He doesn't mention that he and Zavarzin posed as her "
  "relatives from Armavir and beat both collectors up."),
 (5, None,
  "'Marina Sergeyevna, there is no need to go anywhere. Have you calmed down?' He needs Marina to stay in the communal "
  "flat so she can keep watching Arkady for them."),
 (6, None,
  "'Yes. Wait, what is that on your arm?' As Zavarzin steps closer, Marina catches sight of a gleaming gold watch on "
  "his wrist."),
 (7, None,
  "'That is Anikeev's watch!' In Russian, the word for 'watch' or 'clock' is always plural, literally 'hours', and she "
  "recognises the mayor's ten-thousand-dollar Swiss watch that Arkady gave the collectors."),
 (8, None,
  "'No. This is Vsevolod Alexeyevich's watch.' Without blinking, Lavrov uses Zavarzin's formal first name and "
  "patronymic to sound official."),
 (9, None,
  "'Yes, my commendation watch! I just picked it up from repair.' A commendation watch is an engraved watch awarded "
  "to officers for service, and 'just now' goes before the past-tense verb."),
 (10, None,
  "'Let me help you with your bag.' Zavarzin reaches for her heavy bag, using the preposition 'with' and the "
  "instrumental case."),
 (11, None,
  "'No need, I'll do it myself. Goodbye.' The feminine pronoun 'myself' ends in '-a', and Marina walks off down the "
  "corridor, leaving the two officers alone."),
 (12, None,
  "'Seva, have you lost your mind?' The idiom 'went off one's mind' is how Russian says 'went crazy', and Lavrov "
  "glares at his partner for wearing stolen evidence in front of their witness."),
 (13, None,
  "'Sorry, I didn't have time to put it away.' The verb for 'succeeded in time' is followed by the infinitive 'to put "
  "away'."),
]

TRANSITION = "Now let's hear the whole scene again, from start to finish."

OUTRO = (
    "So Lavrov and Zavarzin calmed Marina down so she will stay in the communal flat, though Zavarzin nearly gave "
    "the game away by wearing Arkady's gold watch on his wrist. See you in the next scene."
)
CLOSING = ("zavarzin", "Извини, не успел убрать.")
