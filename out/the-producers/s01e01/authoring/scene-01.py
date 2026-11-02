"""Scene 01: Outside KBS, a documentary cameraman stops rookie PD Baek Seung-chan on his first morning."""
ID = "the-producers-s01e01-scene-01"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = "왜 뛰세요?  (Why Are You Running?)"
LEVEL = "A1 — beginner"
LABELS = {"camera_pd": "촬영자", "seungchan": "백승찬", "yejin": "탁예진"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "Outside the KBS broadcasting centre in Seoul, a documentary cameraman stops rookie producer Baek Seung-chan "
    "as he sprints up the front steps on his first morning. Listen for the question word for 'why', "
    "and the word for the induction ceremony he is afraid of missing."
)

STORY = [
    ("camera_pd", "KBS 신입사원이시죠?", "You're a new KBS employee, right?", [(1, "신입사원이시죠?")], "Restores the KBS network prefix spoken on screen before the caption cue"),
    ("seungchan", "아, 네.", "Ah, yes.", [(2, "아, 네")], ""),
    ("camera_pd", "왜 뛰세요?", "Why are you running?", [(3, "왜 뛰세요?")], ""),
    ("seungchan", "아, 저 입사식 하는데요.", "Ah, I have an induction ceremony.", [(4, "아, 저 입사식 하는데요")], ""),
    ("seungchan", "늦은 거 같아가지고.", "Because I think I'm late.", [(5, "늦은 것 같아가지고")], "Uses natural spoken 거 for 것"),
    ("seungchan", "TS1이 어디입니까?", "Where is TS1?", [(7, "TS1이 어디입니까?")], ""),
    ("camera_pd", "저 따라오세요.", "Follow me.", [(8, "저 따라오세요")], ""),
    ("yejin", "혹시 방금 이것도 찍었어요?", "Did you happen to film this just now too?", [(18, "혹시 방금 이것도 찍었어요?")], ""),
]

OPENER = "Let's unpack those eight lines one turn at a time."

WALK = [
    (0, None, "It literally means this. 'You're a new KBS employee, right?' The cameraman checks Seung-chan's badge using the word for a new employee, built from newly entering and company staff. A polite ending invites the listener to confirm This literally means that."),
    (1, None, "It literally means this. 'Ah, yes.' Out of breath, Seung-chan answers with the everyday polite 'yes' you will use constantly with strangers and colleagues. That soft exclamation at the front buys him half a second to catch his breath This means that."),
    (2, None, "It literally means this. 'Why are you running?' Here the question word for 'why' comes right at the start of the question. Adding a polite ending to the word 'to run' shows respect to someone you have just met It comes from this."),
    (3, None, "It literally means this. 'Ah, I have an induction ceremony.' Notice the humble version of 'I' that Korean speakers choose in polite settings. The word for 'induction ceremony' joins entering a company with a formal ceremony, and the word ending sets up the background reason Swap in this word."),
    (4, None, "It literally means this. 'Because I think I'm late.' Instead of stating flatly that he is late, Seung-chan softens 'late' inside the expression for 'it seems I am late'. Tacking a colloquial connector onto the end turns that impression into a spoken 'because' This means that."),
    (5, None, "It literally means this. 'Where is TS1?' The word meaning 'where' sits right before the formal question ending. Swap any studio, station, or room name in front of that 'where is' pattern when you need directions fast It comes from this."),
    (6, None, "It literally means this. 'Follow me.' The cameraman offers help with a polite command pairing 'follow' and 'come' in one welcoming invitation. Here the humble word means 'me', spoken without an extra marker as often happens in quick conversation Notice the word for."),
    (7, None, "It literally means this. 'Did you happen to film this just now too?' Nearby in the parking lot, senior producer Tak Ye-jin spots the camera after dinging a car door and starts with an word meaning 'by any chance' to cushion an awkward question. Another word pinpoints 'just a moment ago', while the past-word at the end asks whether he caught it on video The word doubles the."),
]

TRANSITION = "Now let's hear the whole morning encounter again from start to finish."
OUTRO = "From asking why someone is running on the steps to saying 'follow me' on the way inside, you now have polite questions and quick workplace answers for day one. Until next time!"
CLOSING = ("seungchan", "안녕히 계세요!")
