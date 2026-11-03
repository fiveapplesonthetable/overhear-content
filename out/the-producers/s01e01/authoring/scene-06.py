"""Scene 06: Tak Ye-jin admits she dinged an imported sedan, triggering the Jindo Dog Level Three office alert."""
ID = "the-producers-s01e01-scene-06"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 6
TITLE = "진돗개 삼 호 발령  (Jindo Dog Level Three Alert)"
LEVEL = "A1 — beginner"
LABELS = {"yejin": "탁예진", "ilyong": "유일용", "seungchan": "백승찬"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "In the Music Bank production office, main producer Tak Ye-jin confesses to junior producer Ryu Il-yong "
    "that she scratched a parked car on her way in, prompting an office-wide mood alert. Listen for the Korean "
    "expression for a car-door ding, and their secret code word for an emergency."
)

STORY = [
    ("yejin", "출근하다가 사고까지 나가지고.", "I even got into an accident on my way to work.", [(175, "출근하다가 사고까지 나가지고")], ""),
    ("ilyong", "무슨 사고? 어디 안 다쳤고?", "What accident? You didn't get hurt anywhere?", [(176, "무슨 사고? 어디 안 다쳤고?")], ""),
    ("yejin", "그런 사고 아니고, 문 콕.", "Not that kind of accident, a door ding.", [(177, "그런 사고 아니고 그 문 콕")], "Trims filler 그"),
    ("yejin", "당한 게 아니고 했어.", "It didn't happen to me, I did it.", [(180, "당한 게 아니고 했어")], ""),
    ("yejin", "그거 얼마나 나올까요? 외제차.", "How much will that cost? An imported car.", [(185, "그거 얼마나 나올까요? 외제차")], ""),
    ("seungchan", "진돗개 삼 호가 뭡니까?", "What is Jindo Dog Level Three?", [(209, "진돗개 사모가 뭡니까?")], "Restores spoken 삼 호 from caption homophone 사모"),
    ("ilyong", "진돗개는 비상상황을 나타내는 은어야.", "Jindo Dog is slang for an emergency situation.", [(211, "진돗개는 비상상황을 나타내는 우리끼리 은어야")], "Slightly trims 우리끼리 for clean pacing"),
    ("seungchan", "일 호는요?", "What about Level One?", [(215, "1호는요?")], "Spells 1호 in Hangul 일 호"),
]

OPENER = "Let's unpack the eight lines of this parking-lot crisis."

WALK = [
    (0, None, "'I even got into an accident on my way to work.' The opening phrase captures 'while commuting to work', built from the expression for going in to the office. Adding the marker meaning 'even' onto 'accident' stresses 'even an accident on top of everything else'."),
    (1, None, "'What accident? You didn't get hurt anywhere?' Worried right away, Il-yong pairs the question word meaning 'what kind of' with 'accident'. Then the closing phrase comes from 'to get injured', checking whether she is physically fine."),
    (2, None, "'Not that kind of accident, a door ding.' The first phrase waves off his wrong guess with a quick 'not that, rather...'. Korean drivers call nicking the next car with your door a two-part expression combining 'door' with a crisp sound word that mimics a sharp poke!"),
    (3, None, "'It didn't happen to me, I did it.' Korean draws a sharp contrast between the word for being on the receiving end of trouble and the past form meaning 'I did it myself'. Il-yong assumed someone hit her car, so she sets him straight."),
    (4, None, "'How much will that cost? An imported car.' Notice how Korean literally asks 'how much will come out?' when wondering what a repair bill or restaurant tab will total. The final compound word means a foreign-made car, famous in Seoul for pricey bodywork."),
    (5, None, "'What is Jindo Dog Level Three?' After Il-yong texts a warning down the hallway, Seung-chan uses the formal question form meaning 'what is it?'. Named after Korea's loyal Jindo hound, the real military alert system counts down from three to one."),
    (6, None, "'Jindo Dog is slang for an emergency situation.' Il-yong explains that this alert names an emergency situation, while the final word means insider slang shared within a group. Around this office, it tracks Ye-jin's temper!"),
    (7, None, "'What about Level One?' Adding the polite topic-question ending onto any word — here 'one' plus the counter for 'level' or 'number' — is the fastest way in Korean to bounce back 'and what about...?'."),
]

TRANSITION = "Now let's listen to the whole alert scene again without stopping."
OUTRO = "From the morning commute to a door ding in the lot and a quick follow-up question in the hall, you have practical Korean for small mishaps. Stay clear of Level One!"
CLOSING = ("ilyong", "다음에 만나요!")
