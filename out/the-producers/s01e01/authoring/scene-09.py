"""Scene 09: Hye-joo forgets Seung-chan's college background, and Joon-mo grumbles in the men's restroom."""
ID = "the-producers-s01e01-scene-09"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 9
TITLE = "학교 후배입니다  (I'm Your College Junior)"
LEVEL = "A1 — beginner"
LABELS = {"seungchan": "백승찬", "hyejoo": "신혜주", "joonmo": "라준모"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "In the hallway outside the studio, Baek Seung-chan finally greets his college crush Shin Hye-joo — "
    "only to discover she barely remembers where she knows him from. Listen for the word for a junior from school or work, "
    "and the word for 'alone'."
)

STORY = [
    ("hyejoo", "너 여기 왜 있어? 뮤뱅 방청 왔니?", "Why are you here? Did you come to watch Music Bank?", [(275, "너 여기 왜 있어?"), (276, "뮤뱅 방창 왔니?")], "Restores studio-audience word 방청 from ASR vowel slip 방창"),
    ("seungchan", "아니요, 저 예능국 신입사원으로 들어왔어요.", "No, I joined the variety department as a new employee.", [(277, "아니요"), (278, "저 예능국"), (279, "신입사원으로 들어왔어요")], ""),
    ("hyejoo", "얘 백승찬이라고 내 교회 후배인데.", "This is Baek Seung-chan, my junior from church.", [(283, "얘 백승찬이라고"), (284, "내 교회 후배인데")], ""),
    ("seungchan", "학교 후배입니다.", "I'm your junior from university.", [(285, "학교 후배입니다")], ""),
    ("seungchan", "아, 저 여의도 사는데요.", "Ah, I live in Yeouido, actually.", [(288, "아 저 여의도 사는데요")], ""),
    ("hyejoo", "잘됐네, 회사랑 가깝고! 다음에 또 보자.", "That's great, close to the office! Let's meet again next time.", [(291, "잘 됐네 회사랑 가깝고"), (292, "다음에 또 보자")], ""),
    ("seungchan", "저 좀 혼자 있고 싶은데요.", "I'd like to be alone for a bit.", [(296, "저 좀 혼자 있고 싶은데요")], ""),
    ("joonmo", "다큐 삼일? 화장실에서까지 찍어?", "Documentary Three Days? You even film in the restroom?", [(299, "아 다큐 3일?"), (300, "화장실에서까지 찍어")], "Spells 3일 in Hangul 삼일"),
]

OPENER = "Let's walk through the eight lines of Seung-chan's bittersweet reunion."

WALK = [
    (0, None, "'Why are you here? Did you come to watch Music Bank?' Speaking casually to a younger acquaintance, Hye-joo uses the informal word for 'you' to ask why he is there. She also uses fan shorthand for Music Bank and the term for sitting in a live studio audience We built from this."),
    (1, None, "'No, I joined the variety department as a new employee.' Proudly correcting her with the polite word for 'no', Seung-chan attaches a word meaning 'as' or 'in the role of' to the term for a new employee. The word at the end literally means 'came inside' — the natural Korean way to say you joined a company It is a handy word."),
    (2, None, "'This is Baek Seung-chan, my junior from church.' Ouch — introducing him to a colleague, Hye-joo mistakes him for a younger member from church! In Korea, that term for a junior names anyone who entered your school, club, or workplace after you It is a handy word."),
    (3, None, "'I'm your junior from university.' Quietly heartbroken, he swaps the word for 'church' for the word for 'school' or 'university'. That stiff formal ending lets you hear the wind go right out of his sails This short for that."),
    (4, None, "'Ah, I live in Yeouido, actually.' When she misremembers his neighbourhood too, he replies using the word 'to live' with a soft explanatory ending. Adding that ending cushions a correction so you never sound combative This literally means that."),
    (5, None, "'That's great, close to the office! Let's meet again next time.' Smiling brightly, Hye-joo cheers that it worked out well, noting Yeouido is close to the company. Her breezy sign-off is the classic casual 'see you around!' Swap in this word."),
    (6, None, "'I'd like to be alone for a bit.' Hiding in the men's room while the cameraman follows him, Seung-chan pleads that he wants to be alone, pairing the word for 'alone' with 'want to be'. Slipping the word for 'a little' near the front turns it into a gentle 'please give me a moment' This means that."),
    (7, None, "'Documentary Three Days? You even film in the restroom?' Out steps Joon-mo, startled to see a lens by the sinks! He uses the word for 'restroom' and stacks the word for 'in' with the word for 'even' to capture his disbelief: 'even inside the bathroom?!' This literally means that."),
]

TRANSITION = "Now let's listen to the whole hallway and restroom scene again."
OUTRO = "You picked up the term for a school junior, gentle corrections with a soft ending, and how to say you want to be alone when you need space. Next, we follow Joon-mo across town!"
CLOSING = ("hyejoo", "다음에 봐요!")
