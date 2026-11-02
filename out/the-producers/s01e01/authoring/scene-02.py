"""Scene 02: After the induction ceremony, Seung-chan explains his first paycheque and why he joined variety."""
ID = "the-producers-s01e01-scene-02"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 2
TITLE = "실감이 나요  (It Finally Feels Real)"
LEVEL = "A1 — beginner"
LABELS = {"seungchan": "백승찬", "camera_pd": "촬영자"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "Right after the KBS induction ceremony, Baek Seung-chan talks to the documentary cameraman about his first salary "
    "and his secret motive for joining the variety department. Listen for the feeling that something is finally real, "
    "and what a younger man calls an older female friend."
)

STORY = [
    ("seungchan", "오늘 이거 받으니까 실감이 나요.", "Getting this today makes it feel real.", [(30, "오늘 이거 하고"), (31, "이거 받으니까"), (32, "실감이 나요")], "Tightens the two-part gesture into one clear A1 sentence"),
    ("seungchan", "현금으로 찾아서 어머니한테 다 드렸습니다.", "I withdrew it in cash and gave it all to my mother.", [(35, "현금으로 찾아서 어머니한테 다 드렸습니다")], "Drops redundant slang prefix 싹 다 for clean beginner listening"),
    ("seungchan", "받고 우시더라고요.", "She cried when she got it.", [(36, "받고 우시더라고요")], ""),
    ("camera_pd", "말 못할 이유라도 있으신 거예요?", "Do you have a reason you can't say?", [(38, "말 못할 이유라도 있으신 거예요?")], ""),
    ("seungchan", "아, 아니요.", "Ah, no.", [(39, "아, 아니요")], ""),
    ("seungchan", "제가 좋아하는 분이 예능국에 계셔서요.", "Someone I like is in the variety department.", [(42, "제가 좋아하는 분이"), (43, "예능국에 근무하고 계셔서")], "Uses everyday 계셔서요 in place of stiffer 근무하고 계셔서"),
    ("seungchan", "그냥 가까이 있고 싶어서요.", "I just wanted to be close by.", [(45, "그냥"), (46, "가까이 있고 싶은")], "Completes the trailed-off spoken reason with 싶어서요"),
    ("camera_pd", "누나가 기자가 됐으면 기자 시험을 보셨겠네요.", "If she had become a reporter, you would have taken the reporter exam.", [(47, "누나가 기자가 됐으면"), (48, "기자시험을 보셨겠네요")], "Standard spacing between 기자 and 시험"),
]

OPENER = "Let's walk through the eight lines of Seung-chan's confession."

WALK = [
    (0, None, "'Getting this today makes it feel real.' Pointing at his new employee badge, Seung-chan pairs a real-life sense with a word meaning 'comes up'. Before that, a connector links 'since I received this' directly to the feeling Notice the word for."),
    (1, None, "'I withdrew it in cash and gave it all to my mother.' In Korean, the word for withdrawing cash literally means 'finding' money at the bank — the everyday way to say taking out cash. Rather than plain giving, he chooses the respectful gift word reserved for elders like one's mother We built from this."),
    (2, None, "'She cried when she got it.' No 'she' is needed in Korean when everyone knows who is meant. The first word chains 'received and then' to the crying word, whose ending recalls a touching moment the speaker witnessed firsthand It is a handy word."),
    (3, None, "'Do you have a reason you can't say?' The cameraman gently probes why Seung-chan chose variety. Placing the negation marker for 'cannot' before the word 'to do' turns 'to speak' into 'unable to say aloud' It comes from this."),
    (4, None, "'Ah, no.' Just as Korean has a standard polite word for 'yes', this is your polite, all-purpose 'no'. Keep the polite ending at the end whenever you answer someone older or on the job It is a handy word."),
    (5, None, "'Someone I like is in the variety department.' Instead of the plain word for person, Seung-chan chooses an honorific word to refer to someone respectfully, saying 'a person I like', followed by the name for the television variety department It is a handy word."),
    (6, None, "'I just wanted to be close by.' Starting with 'just' or 'simply' downplays a big admission so it sounds shy rather than dramatic, followed by 'close by' and the word ending that explains 'because I wanted to' It is a handy word."),
    (7, None, "'If she had become a reporter, you would have taken the reporter exam.' Earlier Seung-chan mentioned she was an older female friend or senior from college. The cameraman teases him about the journalist entrance exam, and Korean says 'see an exam' where English says 'take an exam' It is a handy word."),
]

TRANSITION = "Now let's listen to the whole interview from start to finish."
OUTRO = "You heard how to express a milestone feeling real, a polite 'no', and a man's term for an older female senior. Catch you in the variety lobby!"
CLOSING = ("camera_pd", "다음에 또 만나요!")
