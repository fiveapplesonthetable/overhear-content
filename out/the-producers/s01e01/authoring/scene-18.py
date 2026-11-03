"""Scene 18: Tae-ho brings Director Jang's teenage daughter into K-pop star Cindy's waiting room for a photo."""
ID = "the-producers-s01e01-scene-18"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 18
TITLE = "여기서 잠깐 사진만 찍자고  (Just a Quick Photo Here)"
LEVEL = "A1 — beginner"
LABELS = {"inpyo": "장인표", "taeho": "김태호", "cindy": "신디"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "Director Jang hints that his teenage daughter is visiting KBS and adores pop star Cindy, sending Kim Tae-ho "
    "down to Cindy's waiting room minutes before the live show. Listen for the words for 'live broadcast' "
    "and 'photograph'."
)

STORY = [
    ("inpyo", "오늘 뮤직뱅크에 신디가 나오나?", "Is Cindy appearing on Music Bank today?", [(624, "오늘 뮤직뱅크에 신디가 나오나?")], ""),
    ("taeho", "예, 일 위 후보입니다.", "Yes, she's a contender for number one.", [(625, "예 1위 후보입니다")], "Spells 1위 in Hangul 일 위"),
    ("inpyo", "우리 둘째가 그 친구 팬인가 봐.", "It seems my second child is a fan of hers.", [(626, "우리 둘째가 말이야 그 친구 팬인가 봐")], "Trims spoken filler 말이야"),
    ("taeho", "우리 신디 뭐 불편한 거 없나?", "Is there anything uncomfortable for our Cindy?", [(633, "우리 씬디몬 불편한 거 없나")], "Restores 신디 뭐 from ASR 씬디몬"),
    ("cindy", "아닙니다, 진짜 괜찮습니다.", "Not at all, I'm really fine.", [(638, "아닙니다 진짜 괜찮습니다")], ""),
    ("cindy", "이제 곧 생방이라서요.", "Because the live broadcast is starting very soon.", [(639, "이제 곧 생방이라서")], "Adds polite trailing -요"),
    ("taeho", "여기서 잠깐 사진만 찍자고.", "Let's just take a quick photo right here.", [(658, "여기서 잠깐 사진만 찍자고")], ""),
    ("cindy", "네?", "Excuse me?", [(659, "네?")], ""),
]

OPENER = "Let's step through the eight lines of Tae-ho's awkward backstage favour."

WALK = [
    (0, None, "'Is Cindy appearing on Music Bank today?' On television, performers literally 'come out' on a show, using the everyday verb meaning 'to come out' for appearing on air, softened here into a casual boss's question."),
    (1, None, "'Yes, she's a contender for number one.' With his own boss, Tae-ho switches to a crisper, slightly more formal word meaning 'yes', and calls Cindy a contender by pairing 'first place' with the noun for 'candidate' or 'nominee'."),
    (2, None, "'It seems my second child is a fan of hers.' Korean parents count birth order with a dedicated word meaning 'second-born child'. Tacking an ending meaning 'it looks like' onto the loanword for 'fan' drops an unmistakable hint."),
    (3, None, "'Is there anything uncomfortable for our Cindy?' Down in the dressing room, Tae-ho fusses over the lights and chairs using a warm 'our Cindy' and a phrase built from the word meaning 'uncomfortable' or 'inconvenient'."),
    (4, None, "'Not at all, I'm really fine.' Keeping a cool professional wall up, Cindy answers in crisp formal speech, pairing a formal 'no, not at all' with an emphatic expression meaning 'really, it is fine'."),
    (5, None, "'Because the live broadcast is starting very soon.' Trying politely to usher him out, she pairs 'very soon now' with shorthand for 'live broadcast' and a polite ending meaning 'because it is...' — a textbook workplace brush-off."),
    (6, None, "'Let's just take a quick photo right here.' Tae-ho springs the trap anyway! He combines 'just for a moment' with 'only a photo' and a casual suggestion urging 'let's snap one!' — in Korean, you literally 'stamp' or 'press' a photograph."),
    (7, None, "'Excuse me?' Notice how rising intonation flips the standard polite word for 'yes' from a calm agreement into a stunned 'pardon?' or 'what did you just say?' as the teenage girls barge straight through her door!"),
]

TRANSITION = "Now let's listen to the whole waiting-room ambush again."
OUTRO = "You picked up the word for appearing on a show, a formal way to say 'I'm really fine', and the expression for taking a photo. No wonder Cindy is in a foul mood for the next scene!"
CLOSING = ("cindy", "안녕히 계세요!")
