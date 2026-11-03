"""Scene 08: Demonstrating the studio crane camera, Ye-jin spots Joon-mo and Hye-joo sitting together."""
ID = "the-producers-s01e01-scene-08"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 8
TITLE = "누구야, 사람 있네  (Who's That? Someone's There)"
LEVEL = "A1 — beginner"
LABELS = {"yejin": "탁예진", "ilyong": "유일용", "seungchan": "백승찬"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "Inside the empty Music Bank studio, Tak Ye-jin shows the rookies how overhead crane cameras work — "
    "until the monitor zooms in on Ra Joon-mo chatting cozily with assistant producer Shin Hye-joo. "
    "Listen for the casual question for 'who is it?' and the word for 'rumour'."
)

STORY = [
    ("yejin", "콜을 정확히 하는 게 중요해요.", "Calling camera cues accurately is important.", [(244, "코를 정확히 하는 게 중요해요")], "Restores broadcast term 콜을 ('call') from ASR homophone 코를"),
    ("yejin", "그 카메라가 지미집이야.", "That camera is a Jimmy Jib.", [(250, "그 카메라가 지미집이야, 지미집")], "Keeps one clean statement without the trailing echo"),
    ("yejin", "누구야? 사람 있네.", "Who is that? Somebody's there.", [(253, "누구야? 사람 있네")], ""),
    ("seungchan", "자는 거 아닌데?", "They aren't sleeping, though?", [(255, "자는 거 아닌데?")], ""),
    ("yejin", "옆에 누구야? 라준모네!", "Who is beside her? It's Ra Joon-mo!", [(258, "옆에 누구야?"), (259, "라준보네")], "Restores character name 라준모네 from ASR typo 라준보네"),
    ("yejin", "오늘 방통위 간다 그랬는데?", "Didn't he say he was going to the Broadcast Commission today?", [(261, "오늘 방통위 간다 그랬는데?")], ""),
    ("ilyong", "둘이 사귄다는 소문이 있던데.", "There was a rumour that the two of them are dating.", [(262, "둘이 사귄다는 소문이 있던데 사실이구먼")], "Keeps the crisp rumour clause"),
    ("ilyong", "내가 그걸 어떻게 압니까?", "How would I know that?", [(267, "아이고 내가 그거 어떻게 압니까")], "Trims interjection 아이고 and restores standard object contraction 그걸"),
]

OPENER = "Let's zoom in on each of the eight lines from the studio floor."

WALK = [
    (0, None, "'Calling camera cues accurately is important.' In a control booth, a director's shot cue uses the loanword for 'call', paired with a word meaning 'accurately' or 'with precision'. Ending with that polite phrase highlights that something 'is important'."),
    (1, None, "'That camera is a Jimmy Jib.' The pointing word before 'camera' means 'that' when referring to something you both just noticed. Korean crews call a giant sweeping crane camera by a name adapted straight from the crane's brand name."),
    (2, None, "'Who is that? Somebody's there.' Spotting figures on the monitor, Ye-jin asks a casual 'who is it?' built from the question word meaning 'who'. Then she pairs 'a person' with the lively ending Koreans use when noticing a surprise right before their eyes."),
    (3, None, "'They aren't sleeping, though?' Earlier Ye-jin guessed tired assistants were napping, so Seung-chan counters using 'to sleep' inside a negative phrasing. That trailing question ending gently contradicts a senior without sounding blunt."),
    (4, None, "'Who is beside her? It's Ra Joon-mo!' Opening with the location word meaning 'next to' or 'beside' is handy whenever you describe where people sit. Recognizing her longtime friend on screen, she tacks that same surprise ending directly onto Joon-mo's name!"),
    (5, None, "'Didn't he say he was going to the Broadcast Commission today?' Ye-jin uses every TV worker's three-syllable shorthand for the Broadcast Standards Commission, followed by a reported-speech ending that recalls what someone said earlier: 'didn't he say he was going?'."),
    (6, None, "'There was a rumour that the two of them are dating.' The opening word means 'the two of them together', paired with the everyday expression for dating romantically. Attach the phrase meaning 'a rumour that...' whenever you pass along office gossip."),
    (7, None, "'How would I know that?' Pressed about their age gap, Il-yong throws up his hands with a formal rhetorical question meaning 'how am I supposed to know?'. Notice how 'to know' drops its final consonant sound right before the formal question ending."),
]

TRANSITION = "Now let's hear the whole studio crane scene again."
OUTRO = "You spotted the casual question for 'who is it?', the word for 'beside', the word for dating, and the rhetorical question for 'how would I know?'. Let's see what happens when Seung-chan runs into Hye-joo in the hall!"
CLOSING = ("yejin", "또 봐요!")
