"""Scene 12: Reporter Kang teases Joon-mo about cancellation rumours outside the hearing room."""
ID = "the-producers-s01e01-scene-12"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 12
TITLE = "제작진이 제일 늦게 알던데  (The Crew Always Knows Last)"
LEVEL = "A1 — beginner"
LABELS = {"reporter": "강기자", "joonmo": "라준모"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "Stepping out of the Broadcast Commission, Ra Joon-mo bumps into entertainment reporter Kang, who drops a "
    "chilling rumour that Joon-mo's variety show is getting axed. Listen for the words for 'news article' and "
    "'show cancellation'."
)

STORY = [
    ("joonmo", "강 기자님, 또 오셨어요?", "Reporter Kang, you came here again?", [(349, "강 기자님 또 오셨어요")], ""),
    ("reporter", "피디가 방송국에 있어야지, 맨날 방통위에 있어.", "A PD should be at the station, yet you're always at the Commission.", [(350, "피디가 방송국에 있어야지"), (351, "맨날 방통위에 있어")], ""),
    ("joonmo", "우리 거 까는 기사 좀 그만 써요.", "Please stop writing articles bashing our show.", [(353, "우리 거 까는 기사 좀 그만 좀 써요")], "Trims duplicate 좀"),
    ("reporter", "없어지면 까지도 못하지.", "Once it's gone, I won't even be able to bash it.", [(355, "없어지면 뭐 까지도 못하지")], "Trims spoken filler 뭐"),
    ("joonmo", "뭔 소리야?", "What are you talking about?", [(356, "뭔 소리야")], ""),
    ("reporter", "없어진다면서요.", "I heard it's getting cancelled.", [(357, "없어진다면서요")], ""),
    ("reporter", "원래 프로그램 폐지는 제작진이 제일 늦게 알던데.", "Usually the production crew is the very last to know about a cancellation.", [(363, "원래 프로그램 폐지는"), (364, "제작진이 제일 늦게 알던데")], ""),
    ("joonmo", "내 프로그램을 내가 왜 몰라?", "Why wouldn't I know about my own show?", [(367, "내 프로그램을 내가 왜 몰라?")], ""),
]

OPENER = "Let's unpack the eight lines of Joon-mo's hallway clash with Reporter Kang."

WALK = [
    (0, None, "'Reporter Kang, you came here again?' Adding an honorific suffix onto 'reporter' creates respectful workplace address. The little word meaning 'again' is paired with the polite past question meaning 'did you come?'."),
    (1, None, "'A PD should be at the station, yet you're always at the Commission.' The compound noun for a TV station joins 'broadcasting' and 'bureau', while the ending says 'that is where you ought to be!'. A lively word built from 'every single day' adds the sense of 'always'."),
    (2, None, "'Please stop writing articles bashing our show.' Here a slang verb that literally means peeling fruit is used in media talk for roasting or bashing a show in print. It modifies 'news article', while the closing phrase begs him to 'stop writing'."),
    (3, None, "'Once it's gone, I won't even be able to bash it.' Reporter Kang builds on the expression meaning 'to disappear' or get axed. Slipping 'even' before the negative ending sharpens the jab: 'won't even be able to bash it anymore'."),
    (4, None, "'What are you talking about?' Three punchy syllables every Korean drama fan hears constantly, literally meaning 'what sound is that?'. Use this casual expression only with close friends or peers when someone says something outrageous."),
    (5, None, "'I heard it's getting cancelled.' Adding a hearsay-and-confirmation ending onto 'to disappear' passes along a rumour while fishing for a reaction: 'people say it's disappearing, isn't it?'. Reporters love that ending because it sounds like confirmed news."),
    (6, None, "'Usually the production crew is the very last to know about a cancellation.' Television uses an official term for cancelling a programme, followed by the word naming the production staff. Near the end, pairing 'most' with 'late' gives you 'dead last'."),
    (7, None, "'Why wouldn't I know about my own show?' Rattled, Joon-mo shoots back with the casual possessive for 'my' and a blunt question meaning 'why wouldn't I know?', built from 'to not know'."),
]

TRANSITION = "Now let's listen to the whole exchange with Reporter Kang again."
OUTRO = "You learned the word for a TV station, the punchy phrase for 'what are you talking about?', and the expression for dead last. Next, a flashback to Joon-mo's outdoor shoot!"
CLOSING = ("reporter", "다음에 또 봐요!")
