"""s01e10 scene 20: Шокирующая новость (Shocking News)."""

ID = "kukhnya-s01e10-scene-20"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 20
TITLE = "Шокирующая новость  (Shocking News)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja"}
LABELS = {"anya": "Саша", "max": "Макс"}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"
SOURCE_NOTE = "Cues 156-161. In the service corridor, Sasha stops Max for an urgent private chat and reveals she is pregnant."

INTRO = (
    "In the quiet service corridor of Claude Monet, waitress Sasha stops Max as he hurries past. "
    "After an awkward exchange of casual pleasantries, Sasha drops all pretense and delivers a stunning personal revelation that catches Max completely off guard. "
    "Let's listen to their dramatic corridor encounter in Russian."
)

STORY = [
    ("max", "Привет, Саша. Как твои дела?", "Hi, Sasha. How are you doing?",
     [(156, "Привет"), (156, "Как дела?")], ""),
    ("anya", "Привет. Всё нормально, а у тебя?", "Hi. Everything is fine, and with you?",
     [(156, "Привет"), (157, "у тебя")], ""),
    ("max", "У меня тоже всё хорошо, бегу.", "Everything is fine with me too, running.",
     [(157, "у меня")], ""),
    ("anya", "Стой, подожди хотя бы одну секунду.", "Wait, wait at least one second.",
     [(158, "Стой")], ""),
    ("max", "Что такое? Шеф ждёт на кухне.", "What is it? The chef is waiting in the kitchen.",
     [], ""),
    ("anya", "Мне срочно нужно поговорить с тобой.", "I urgently need to talk to you.",
     [(159, "Мне нужно поговорить с тобой")], ""),
    ("anya", "Есть одна очень важная личная вещь.", "There is one very important personal thing.",
     [(160, "Есть одна вещь")], ""),
    ("max", "Ты пугаешь меня таким серьёзным видом.", "You scare me with such a serious look.",
     [], ""),
    ("anya", "Я не могу больше скрывать правду.", "I can no longer hide the truth.",
     [(160, "скрывать от тебя")], ""),
    ("anya", "Я знаю, что я нравлюсь тебе.", "I know that you like me.",
     [(161, "тебе нравлюсь")], ""),
    ("anya", "Я беременна от тебя, Макс.", "I am pregnant with your child, Max.",
     [(161, "Я беременна от тебя")], ""),
    ("max", "Что ты только что сейчас сказала?", "What did you just say right now?",
     [], ""),
    ("anya", "Ты слышал меня отлично с первого раза.", "You heard me perfectly the first time.",
     [], ""),
]

OPENER = "Let's explore how Sasha halts Max in the corridor and delivers an unexpected life-changing announcement."

WALK = [
    (3, None,
     "'Wait, wait at least one second.' Two urgent imperative verbs used together to immediately stop someone in their tracks."),
    (5, None,
     "'I urgently need to talk to you.' An impersonal construction with an adverb expressing pressing necessity for a private conversation."),
    (9, None,
     "'I know that you like me.' A subordinate clause introduced by a conjunction to acknowledge mutual romantic feelings between colleagues."),
    (10, None,
     "'I am pregnant with your child, Max.' A direct revelation using a short adjective construction that abruptly changes the entire situation."),
]

TRANSITION = "Now, let's listen to Sasha break the stunning news to Max once more."

OUTRO = (
    "Now you know how to initiate serious conversations, share urgent personal news, and express disbelief in Russian. "
    "Listen for these impactful interpersonal phrases as the story continues."
)

CLOSING = ("max", "Я просто не верю своим ушам.")
