"""Scene 22: Cindy throws off the jacket live on air and bolts; the cameraman asks how Seung-chan's first day went."""
ID = "the-producers-s01e01-scene-22"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 22
TITLE = "오늘 하루 어떠셨어요?  (How Was Your Day Today?)"
LEVEL = "A1 — beginner"
LABELS = {"yejin": "탁예진", "seungchan": "백승찬", "camera_pd": "촬영자"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "In the Music Bank control booth, Tak Ye-jin calls the live broadcast — until Cindy flings off the promised jacket "
    "on stage and vanishes from the building, leaving Seung-chan to take the heat on his very first day. "
    "Listen for the surprised expression for 'already?', and the warm word for 'today's whole day'."
)

STORY = [
    ("yejin", "자, 첫 커트는 카메라 포로 갈게요.", "Alright, for the opening shot we'll go with Camera Four.", [(860, "자 첫 커트는 카메라 4로 갈게요")], "Spells 4로 in Hangul 포로"),
    ("yejin", "수고하셨습니다! 신디 매니저 당장 튀어오라고 해!", "Good work, everyone! Tell Cindy's manager to get up here right now!", [(872, "수고하셨습니다"), (873, "신디 매니저 당장 튀어라고 해")], "Restores 튀어오라고 해 from rapid-speech caption 튀어라고 해"),
    ("yejin", "벌써? 이것들이 나 무서워서 내뺐네.", "Already? They were scared of me and bolted.", [(875, "벌써?"), (876, "이것들이 나 무서워서 내뺐네")], ""),
    ("yejin", "방통위는 네가 가면 되겠네.", "You can be the one who goes to the Broadcast Commission.", [(889, "방통위는 네가 가면 되겠네")], ""),
    ("yejin", "아까 신디 옷 예쁘다며, 가서 그렇게 얘기해라.", "Earlier you said Cindy's outfit was pretty, so go tell them that.", [(890, "아까 신디옷 이쁘다며"), (891, "가서 그렇게 얘기해라")], "Standardizes 신디 옷 예쁘다며"),
    ("seungchan", "첫 출근이었는데.", "It was my very first day at work.", [(893, "첫 출근이었는데")], ""),
    ("camera_pd", "오늘 하루 어떠셨어요?", "How was your day today?", [(894, "오늘 하루 어떠셨어요?")], ""),
    ("seungchan", "어떠실 것 같으세요?", "How do you think it was?", [(895, "어떠실 것 같으세요?")], ""),
]

OPENER = "Let's unpack the eight lines of this chaotic live broadcast finale."

WALK = [
    (0, None, "'Alright, for the opening shot we'll go with Camera Four.' The opening interjection claps everyone to attention — 'alright, here we go!'. After the word for 'first' opening cut, the closing word ('we will go with') announces the director's choice smoothly to the crew This literally means that."),
    (1, None, "'Good work, everyone! Tell Cindy's manager to get up here right now!' Right as the song ends, Ye-jin calls out Korea's essential workplace thank-you for hard effort — then explodes in the very next breath, ordering someone to tell him to bounce up here this instant! It is a handy word."),
    (2, None, "'Already? They were scared of me and bolted.' Hearing Cindy's van already left, she gasps in disbelief — 'already?!'. She follows up with the word for 'scary' and vivid slang for making a getaway It comes from this."),
    (3, None, "'You can be the one who goes to the Broadcast Commission.' Looking around for someone to blame, she lands on poor Seung-chan with a pointed suggestion meaning 'it'll work nicely if you go instead of me!' It comes from this."),
    (4, None, "'Earlier you said Cindy's outfit was pretty, so go tell them that.' The opening word points back to 'earlier today'. attaching a hearsay ending to the word for 'pretty' throws his own words back at him: 'didn't you say it was pretty earlier?' This means that."),
    (5, None, "'It was my very first day at work.' Slumped in his chair afterward, Seung-chan pairs the word for 'first' with 'going to work' and trails off with a wistful past-word ending — letting the sigh finish the sentence This literally means that."),
    (6, None, "'How was your day today?' Pairing the word for 'today' with 'one full day' gives you a warm evening check-in, using the respectful past word of the word for 'how is it?' Notice the word for."),
    (7, None, "'How do you think it was?' Even exhausted, Seung-chan stays ultra-polite, bouncing the exact same word right back in a respectful 'how do you think it would be?' phrasing — the politest deadpan comeback in Korean television! This means that."),
]

TRANSITION = "Now let's listen to the whole control-booth meltdown again."
OUTRO = "You learned the workplace thank-you after a job well done, the surprised gasp for 'already?', the word for earlier today, and the warm evening check-in asking how the day went. Let's check in on Cindy and Joon-mo next!"
CLOSING = ("camera_pd", "안녕히 계세요!")
