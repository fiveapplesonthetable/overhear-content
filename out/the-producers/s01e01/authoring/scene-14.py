"""Scene 14: Writer Son Ji-yeon pitches Jeju Island while the head writer crosses Mapo Bridge."""
ID = "the-producers-s01e01-scene-14"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 14
TITLE = "제주도 한번 가시죠  (Let's Go to Jeju Island)"
LEVEL = "A1 — beginner"
LABELS = {"joonmo": "라준모", "writer": "손지연"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "Back in the meeting room for his weekend travel show, writer Son Ji-yeon makes excuses for the late head writer, "
    "suggests filming on Jeju Island, and asks whether Joon-mo can book girl group Miss A. Listen for the expressions for "
    "'right away' and 'if I make one phone call'."
)

STORY = [
    ("writer", "방금 통화했는데요, 지금 마포대교 건너고 계신대요.", "I just spoke with her on the phone, she says she's crossing Mapo Bridge now.", [(409, "아 방금 통화했는데요"), (410, "지금 마포대교 건너고 계신데")], "Completes indirect report ending 계신대요"),
    ("writer", "금방 오신대요.", "She says she'll be right here.", [(411, "금방 오신대요")], ""),
    ("joonmo", "다음 주 아이템은 나왔어?", "Did next week's episode topic come out?", [(416, "다음 주 아이템은 나왔어?")], ""),
    ("writer", "제주도 한번 가시죠.", "Let's take a trip to Jeju Island.", [(417, "제주도 한번 가시죠")], ""),
    ("joonmo", "지난 시즌 마지막 촬영지가 어디였지?", "Where was last season's final filming location?", [(418, "지난 시즌 마지막 촬영지가 어디였지?")], ""),
    ("writer", "제주도요.", "Jeju Island.", [(419, "제주도요")], ""),
    ("writer", "이번 녹화 게스트 미쓰에이 어떻게 됐어요?", "How did things turn out with Miss A as guests for this shoot?", [(430, "이번 녹화 게스트 미세이"), (431, "어떻게 됐어요?")], "Restores group spelling 미쓰에이 from ASR 미세이"),
    ("joonmo", "전화하면 바로 돼.", "One phone call and it's done right away.", [(435, "전화하면 바로 돼")], ""),
]

OPENER = "Let's go through the eight lines of this brainstorm in the writers' room."

WALK = [
    (0, None, "'I just spoke with her on the phone, she says she's crossing Mapo Bridge now.' The opening phrase comes from the word meaning 'to talk on the phone'. Mapo Bridge leads straight into Yeouido, and the second half reports politely that she is crossing it right now — Korea's classic 'almost there!' excuse."),
    (1, None, "'She says she'll be right here.' Opening with a handy word meaning 'very soon' or 'in a moment', the final ending layers two nuances: an honorific syllable respecting the senior head writer, and a reported-speech ending passing along her message."),
    (2, None, "'Did next week's episode topic come out?' The opening phrase pairs 'next' and 'week' to mean 'next week'. TV teams also borrow the English word 'item' to refer to an episode concept or segment idea."),
    (3, None, "'Let's take a trip to Jeju Island.' Slipping the little word meaning 'once' or 'for a try' before the polite 'let's go' form turns a suggestion into an inviting 'why don't we go together?'. Jeju is Korea's beloved volcanic holiday island."),
    (4, None, "'Where was last season's final filming location?' Suspicious of the pitch, Joon-mo combines the words for 'final' and 'filming site', then finishes with a casual question ending that muses aloud 'where was it again?'."),
    (5, None, "'Jeju Island.' Adding just the polite ending onto a place name turns a single word into a complete, courteous answer. Joon-mo's point lands fast: every cancelled show filmed its finale on Jeju!"),
    (6, None, "'How did things turn out with Miss A as guests for this shoot?' Here the noun for 'shoot' refers to a television taping or recording, and the closing phrase is the go-to workplace question for checking status: 'how did that turn out?'."),
    (7, None, "'One phone call and it's done right away.' Confident his friend Ye-jin will help him out, Joon-mo pairs 'if I phone' with the casual expression meaning 'it works immediately'. Let's see how well that boast ages!"),
]

TRANSITION = "Now let's hear the whole writers' room meeting again."
OUTRO = "You learned how to talk about phoning someone, say 'right away', and ask how a plan turned out. Next up: that fateful phone call!"
CLOSING = ("writer", "안녕히 계세요!")
