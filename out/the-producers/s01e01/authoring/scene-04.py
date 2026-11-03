"""Scene 04: Tae-ho explains the morning ratings sheet and how to refuse Gag Concert ticket requests."""
ID = "the-producers-s01e01-scene-04"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = "매일 아침 보게 될 시청률표  (The Morning Ratings Sheet)"
LEVEL = "A1 — beginner"
LABELS = {"taeho": "김태호", "seungchan": "백승찬"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "Walking the rookies through the open variety floor, Kim Tae-ho shows them the daily ratings printout "
    "and demonstrates how to fend off friends asking for Gag Concert studio tickets. Listen for the phrases "
    "for 'ratings chart' and 'there aren't any'."
)

STORY = [
    ("taeho", "이게 매일 아침 보게 될 시청률표야.", "This is the ratings chart you'll see every morning.", [(98, "이제 이게 여러분들이"), (99, "매일 아침 보게 될 시청률표")], "Adds casual copula -야 to complete the spoken word phrase"),
    ("taeho", "이게 우리한테는 성적표 같은 거지.", "For us, this is like a report card.", [(100, "이게 우리한테는 성적표 같은 거지")], ""),
    ("taeho", "요새 칠 나오기 쉽지가 않아요.", "Getting a seven isn't easy these days.", [(103, "요새 7 나오기 쉽지가 않아요")], "Spells 7 in Hangul 칠"),
    ("seungchan", "되게 기대를 많이 하고 왔단 말이에요.", "I came here with really high expectations.", [(115, "그래서 되게 기대를 많이 하고 왔단 말이에요")], ""),
    ("seungchan", "가끔 혼란이 오더라고요.", "Sometimes I get confused.", [(117, "가끔 혼란이 오더라고요")], ""),
    ("taeho", "다들 내가 하는 거 잘 봐.", "Everyone, watch closely what I do.", [(119, "다들 내가 하는 거 잘 봐")], ""),
    ("taeho", "이번 주 개콘표? 없어요.", "This week's Gag Concert tickets? We don't have any.", [(120, "이번 주 개콘표"), (121, "없어요")], "Combines the phone prompt and his instant refusal"),
    ("taeho", "처음부터 안 된다고 선을 그어놓는 게 좋아.", "It's good to draw the line from the start and say no.", [(130, "안 된다고 처음부터 확실하게 선을 그어놓는 게 좋아")], "Slightly trims 확실하게 for pacing"),
]

OPENER = "Let's break down those eight lines from the variety office tour."

WALK = [
    (0, None, "'This is the ratings chart you'll see every morning.' The phrase meaning 'every morning' pairs 'every day' with 'morning', a handy time chunk you can drop into any daily routine. The compound term for 'ratings chart' tacks 'chart' or 'table' onto television viewership ratings."),
    (1, None, "'For us, this is like a report card.' Adding 'to' plus a topic marker onto 'us' means 'as far as we are concerned'. He compares the numbers to a school report card, followed by a casual expression meaning 'it is something like that'."),
    (2, None, "'Getting a seven isn't easy these days.' He opens with the breezy spoken cousin of the standard word meaning 'these days'. Seven percent is read in the number system borrowed from Chinese, and the closing pattern flips 'easy' into 'not easy at all'."),
    (3, None, "'I came here with really high expectations.' Cutting to his interview, Seung-chan pairs a casual intensifier meaning 'really' or 'super' with the expression meaning 'to have big expectations'. The final ending adds an earnest 'I mean, honestly!' tone."),
    (4, None, "'Sometimes I get confused.' Korean says confusion comes to you, literally phrasing it as 'confusion came'. The opening word means 'sometimes' or 'every now and then'."),
    (5, None, "'Everyone, watch closely what I do.' Back at his desk, Tae-ho gathers the rookies with the everyday word meaning 'everyone'. His command pairs 'closely' with the casual form meaning 'look!'."),
    (6, None, "'This week's Gag Concert tickets? We don't have any.' Notice how the exact same syllable that meant 'chart' earlier means an admission 'ticket' for Gag Concert here! His one-word answer meaning 'there are none' works in shops, offices, and cafés alike."),
    (7, None, "'It's good to draw the line from the start and say no.' The opening phrase means 'from the very beginning', followed by a quoted 'no way'. Remarkably like English, Korean uses an idiom that literally means 'draw a line' for setting firm boundaries."),
]

TRANSITION = "Now let's listen to the whole office tour scene again."
OUTRO = "You picked up the phrase for every morning, two meanings of the word for chart and ticket, and a crisp way to say 'there are none'. Next stop: lunch!"
CLOSING = ("seungchan", "또 만나요!")
