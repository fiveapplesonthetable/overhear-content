"""Scene 05: At the KBS cafeteria, Tae-ho praises four-thousand-won meal tickets and pretends to know pop stars."""
ID = "the-producers-s01e01-scene-05"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 5
TITLE = "여기 밥 맛있어  (The Food Here Is Delicious)"
LEVEL = "A1 — beginner"
LABELS = {"taeho": "김태호", "seungchan": "백승찬"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "At noon in the KBS staff cafeteria, Kim Tae-ho hands out lunch coupons and boasts that passing pop stars "
    "all know him well. Listen for the expressions for 'the food is delicious' and 'I had no idea'."
)

STORY = [
    ("taeho", "이게 하나에 사천 원씩인데.", "These are four thousand won apiece.", [(143, "이게 하나에 4천 원씩인데")], "Spells 4천 in Hangul 사천"),
    ("taeho", "여기 밥 맛있어.", "The food here is delicious.", [(146, "여기 밥 맛있어")], ""),
    ("seungchan", "두 개씩 먹어도 돼요?", "May I eat two of these?", [(155, "두 개씩 먹어도 돼요?")], ""),
    ("taeho", "먹어!", "Go ahead and eat!", [(156, "먹어")], ""),
    ("taeho", "사람 모이면 귀찮으니까 조용히 밥이나 먹자.", "It's a hassle if a crowd gathers, so let's just eat quietly.", [(165, "사람 모이고 그러면 귀찮으니까 조용히 밥이나 먹자")], "Tightens 모이고 그러면 to 모이면"),
    ("seungchan", "친하십니까?", "Are you close with them?", [(166, "친해집니까?")], "Restores spoken honorific 친하십니까 from caption typo 친해집니까"),
    ("taeho", "아, 친하다뿐이냐!", "Oh, close doesn't even cover it!", [(167, "아 친하다뿐이냐")], ""),
    ("seungchan", "전혀 몰랐어요.", "They didn't know him at all.", [(170, "몰랐어요 전혀")], "Places 전혀 in standard order before 몰랐어요; spoken by the passing singer in the cutaway, reported in clean polite Korean"),
]

OPENER = "Let's savour each line of this cafeteria lunch."

WALK = [
    (0, None, "'These are four thousand won apiece.' Holding up a paper meal ticket, Tae-ho states the price per ticket: 'for one', followed by 'four thousand', with a handy suffix tacked onto the price to add the sense of 'each' or 'apiece'."),
    (1, None, "'The food here is delicious.' Three short words you can use at any good lunch spot: 'here', the word meaning cooked rice — and by extension a whole meal — and 'tastes great'. Add a polite ending to say it to restaurant staff."),
    (2, None, "'May I eat two of these?' Reaching for side dishes, Seung-chan counts 'two items' plus that same suffix meaning 'each'. Following an action with this permission-asking ending is the classic Korean way to ask 'may I?' or 'is it okay if I?'."),
    (3, None, "'Go ahead and eat!' Tae-ho grants permission with one casual form of 'to eat'. Between friends or from a senior to a junior, that bare spoken form works as both 'eat!' and 'sure, help yourself!'."),
    (4, None, "'It's a hassle if a crowd gathers, so let's just eat quietly.' Spotting famous singers across the room, Tae-ho pretends fans will mob him, combining an expression meaning 'because it is bothersome' with 'quietly' and a casual suggestion meaning 'let's just eat our meal'."),
    (5, None, "'Are you close with them?' Impressed, Seung-chan builds his question on the word meaning 'close friends'. Inserting an honorific syllable honours his boss, while the formal question ending keeps the rookie's tone respectful."),
    (6, None, "'Oh, close doesn't even cover it!' Tae-ho brags by literally asking 'is it merely being close?' — a lively idiom meaning 'way more than just close!'. You will hear that emphatic ending whenever someone exaggerates how obvious something is."),
    (7, None, "'They didn't know him at all.' Here comes the punchline: an emphatic word meaning 'not at all' teams up with the past form of 'to not know'. Pair that intensifier with a negative expression whenever you want to say 'zero clue'."),
]

TRANSITION = "Now let's listen to the whole cafeteria scene from top to bottom."
OUTRO = "With phrases for praising the food, asking permission to eat, and saying someone had no idea at all, you are ready for lunch and office tall tales alike. See you after lunch!"
CLOSING = ("taeho", "안녕히 계세요!")
