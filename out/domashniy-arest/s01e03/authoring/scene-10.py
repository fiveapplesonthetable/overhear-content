# domashniy-arest/s01e03/scene-10.py
ID = "domashniy-arest-s01e03-scene-10"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 10
TITLE = "В комнате Аркадия  (Caught in Arkady's Room)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"
VOICES = {"narrator": "sky", "anya": "alisa", "marina": "angelina"}
LABELS = {"anya": "Аркадий", "marina": "Марина"}
INTRO = "Back in the communal flat, while Arkady hogs the bathroom for twenty minutes, Marina slips into his room to stick the listening bug in place — still hidden inside the small foil packet the agents gave her — when Arkady suddenly walks in. Let's hear the conversation in Russian first."
STORY = [
    ("anya", "Что вы здесь делаете, Марина Сергеевна?", "What are you doing in here, Marina Sergeyevna?", [(329, 'Что вы здесь делаете')], "cue 329 'женщина' replaced with her name and patronymic"),
    ("marina", "А я извиниться зашла.", "I dropped in to apologise.", [(330, 'А я извиниться зашла')], ""),
    ("anya", "За что это?", "For what, exactly?", [(331, 'За что это')], ""),
    ("marina", "Вчера я наговорила вам лишнего.", "Yesterday I said too much to you.", [(332, 'вчера наговорила вам лишнего')], ""),
    ("anya", "А, да. Вам должно быть стыдно.", "Ah, yes. You ought to be ashamed.", [(333, 'А, да. Вам должно быть стыдно')], ""),
    ("marina", "Мне не стыдно. Я пойду.", "I'm not ashamed. I'll go.", [(334, 'Не стыдно. Я пойду')], "'Мне' added for clarity"),
    ("anya", "Стойте! Что вы делаете в моей комнате? Что-то моё взяли?", "Stop! What are you doing in my room? Did you take something of mine?", [(335, 'Стойте'), (337, 'Что вы делаете в моей комнате'), (338, 'Что-то мое взяли')], ""),
    ("anya", "Ну, покажите руки. Что у вас за спиной?", "Well, show me your hands. What is behind your back?", [(339, 'Ну, покажите руки'), (341, 'Что у вас за спиной')], ""),
    ("marina", "Я ничего не брала.", "I didn't take anything.", [(342, 'Ничего не брала')], "'Я' added"),
    ("anya", "Покажите правую руку! Ну?", "Show me your right hand! Well?", [(343, 'Покажите'), (345, 'Правую руку'), (347, 'Ну')], ""),
    ("anya", "Ага! Вот оно в чём дело.", "Aha! So that's what this is about.", [(348, 'Вот оно в чем дело')], "'Ага!' added as he sees the small foil packet in her hand"),
    ("marina", "Да нет, это не то, что вы подумали!", "No, it isn't what you thought!", [(349, 'Да нет, это не то, что вы подумали')], ""),
    ("anya", "А что тут думать? Всё понятно.", "What is there to think about? Everything is clear.", [(350, 'А что тут думать'), (351, 'Все понятно')], ""),
    ("anya", "Я рад вам помочь. Но вы, к сожалению, не в моём вкусе.", "I would be glad to help you. But unfortunately you are not my type.", [(354, 'рад вам помочь'), (355, 'К сожалению, вы не в моем вкусе')], "crude lines 352 and 356-357 dropped; second half of 354 replaced by 355"),
    ("anya", "К сожалению, я занят. Ко мне Мишкин пришёл. Дела!", "Unfortunately, I'm busy. Mishkin has come to see me. Business!", [(355, 'К сожалению'), (359, 'ко мне Мишкин пришел'), (361, 'Дела')], "clean pompous refusal closing the scene"),
]
OPENER = "Let's go back through the scene line by line. Arkady opens the door of his tiny room and finds Marina standing there."
WALK = [
    (0, None, "'What are you doing in here, Marina Sergeyevna?' They always use the polite 'you' with each other. Marina quickly invents an excuse."),
    (1, None, "'I dropped in to apologise.' The verb at the end is feminine past, meaning 'stepped in briefly on the way'. Arkady raises an eyebrow."),
    (2, None, "'For what, exactly?' Literally 'for what is this?'. Marina thinks of their quarrel in the courtyard the day before."),
    (3, None, "'Yesterday I said too much to you.' The prefix on the verb means piling up a lot of words, and the last word means 'extra' or 'things I shouldn't have said'. Arkady enjoys this."),
    (4, None, "'Ah, yes. You ought to be ashamed.' Literally 'to you it must be shameful'. That is too much for Marina's pride."),
    (5, None, "'I'm not ashamed. I'll go.' Literally 'to me not shameful'. She edges toward the door, still hiding the bug behind her back, and Arkady gets suspicious."),
    (6, 'Стойте! Что вы делаете в моей комнате?', "'Stop! What are you doing in my room?' Then he guesses she might be stealing."),
    (6, 'Что-то моё взяли?', "'Did you take something of mine?' He uses the plural past form because he addresses her with the polite 'you'."),
    (7, None, "'Well, show me your hands. What is behind your back?' After the preposition 'behind', 'back' takes the 'with/as' ending."),
    (8, None, "'I didn't take anything.' Remember that Russian uses double negation: 'nothing not took', with the feminine past ending in 'a'."),
    (9, None, "'Show me your right hand! Well?' Reluctantly, Marina holds out her hand with the small foil packet the agents used to disguise the bug. Arkady's face lights up with smug delight."),
    (10, None, "'Aha! So that's what this is about.' An everyday idiom: literally 'here it is in what the matter is'. He completely misunderstands why she has that packet."),
    (11, None, "'No, it isn't what you thought!' Notice how 'yes no' together just means an emphatic 'no, not at all!'. Marina cannot explain the bug without giving herself away."),
    (12, None, "'What is there to think about? Everything is clear.' In the show Arkady launches into a pompous speech, convinced that Marina is in love with him and came to seduce him."),
    (13, 'Я рад вам помочь.', "'I am glad to help you.' The little particle after 'I' means 'would', and 'glad' is masculine because Arkady is a man."),
    (13, 'Но вы, к сожалению, не в моём вкусе.', "'But unfortunately you are not my type.' Word for word: 'not in my taste'. Then the doorbell rings."),
    (14, 'К сожалению, я занят.', "'Unfortunately, I'm busy.' Again, a masculine short form."),
    (14, 'Ко мне Мишкин пришёл. Дела!', "'Mishkin has come to see me. Business!' He thinks his expensive Moscow lawyer has arrived for the evening hearing, and waves Marina out of the room."),
]
TRANSITION = "Let's listen to the whole encounter in Arkady's room again."
OUTRO = "So Marina fails to plant the bug, and Arkady smugly believes she came to flirt with him. Now he goes to the front door expecting his Moscow lawyer Mishkin — and gets a surprise instead. See you next time!"
CLOSING = ("anya", "Пока!")
