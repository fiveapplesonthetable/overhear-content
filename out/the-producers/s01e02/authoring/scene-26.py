"""Scene 26: At the rookie welcome pub, Tae-ho cheers Seung-chan up while Ye-jin counts his remaining probation strikes."""
ID = "the-producers-s01e02-scene-26"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 2
SCENE = 26
TITLE = "두 번 남았네? 조심해  (Two Strikes Left — Watch Out)"
LEVEL = "A1 — beginner"
LABELS = {"taeho": "김태호", "yejin": "탁예진", "seungchan": "백승찬"}
SOURCE_NAME = "프로듀사 (The Producers) S1.02"
SOURCE_FILE = "sources/the-producers/s01/e02.ko.srt"

INTRO = (
    "At a lively beer pub near KBS, the variety department gathers to welcome its newest producers. Chief "
    "producer Kim Tae-ho waves Baek Seung-chan over to laugh off his rough day, right before Tak Ye-jin sits "
    "down to ask whether Seung-chan's father lowered her car-repair bill. Listen for \"sago\", 'an accident or "
    "blunder', and \"josimhae\", 'be careful'."
)

STORY = [
    ("taeho", "우리 신입 피디들 환영한다!", "Welcome to all our rookie producers!", [(1088, "우리 신입 피디들 환영한다")], ""),
    ("seungchan", "잘 부탁드리겠습니다.", "I look forward to working with you.", [(1090, "잘 부탁드리겠습니다")], ""),
    ("taeho", "야, 너 왜 이렇게 늦게 왔어? 앉아.", "Hey, why did you get here so late? Sit down.", [(1104, "야 너 왜 이렇게 늦게 왔어 앉아")], ""),
    ("taeho", "너 오늘 사고 쳤다며? 괜찮아.", "I heard you caused a blunder today? It's fine.", [(1105, "너 오늘 사고 쳤다며?"), (1106, "괜찮아")], ""),
    ("taeho", "나중에 네 프로 잘하면 다 괜찮아지는 거야.", "Later on, if your own show does well, everything turns out fine.", [(1107, "나중에"), (1107, "프로 잘하면 그냥 다 괜찮아지는 거야")], "Uses standard 네 for caption 니."),
    ("yejin", "아버지한테 연락은 왔니?", "Did you hear back from your father?", [(1108, "아버지한테 연락은")], "Uses natural 왔니 for ASR 받니."),
    ("seungchan", "네, 꼭 필요한 수리비만 받으신 거라고 하셨습니다.", "Yes, he said he charged only the strictly necessary repair cost.", [(1109, "네"), (1112, "꼭 필요한 수리비만 받으신 거라")], "Completes polite reported clause."),
    ("yejin", "아, 그래? 너 지금 수습이지?", "Oh, really? You are on probation right now, aren't you?", [(1115, "아, 그래? 너 지금 수습이지?")], ""),
    ("seungchan", "예, 삼 개월 동안입니다.", "Yes, for three months.", [(1116, "예"), (1116, "개월 동안")], "Spells out 삼 개월 and adds 입니다."),
    ("yejin", "수습 때 사고 치면 잘릴 수도 있어.", "If you mess up during probation, you can get fired.", [(1117, "수습 때 사고 치면 잘릴 수도")], "Shortens rhetorical ending to direct warning."),
    ("yejin", "너 벌써 한 번 사고 쳤지?", "You already messed up once, right?", [(1120, "너 벌써 한 번 사고 쳤지?")], ""),
    ("yejin", "두 번 남았네? 조심해.", "You have two times left, huh? Watch out.", [(1121, "두 번 남았네?"), (1122, "조심해")], ""),
]

OPENER = "Let's go around the pub table and unpack these twelve lines."

WALK = [
    (0, None, "'Welcome to all our rookie producers!' Raising a glass, Tae-ho pairs warm inclusive \"uri\", 'our', with \"sinip\", 'newcomer', and plain cheering \"hwanyeonghanda\", 'we welcome you!'."),
    (1, None, "'I look forward to working with you.' Every new hire in Korea learns \"jal butakdeurigesseumnida\" on day one — a humble bow in words asking seniors for their guidance and goodwill."),
    (2, None, "'Hey, why did you get here so late? Sit down.' Spotting Seung-chan by the door, Tae-ho calls out \"wae ireoke neutge wasseo\", using \"neutge\" for 'late', then pats a chair with casual \"anja\", 'have a seat'."),
    (3, None, "'I heard you caused a blunder today? It's fine.' In Korean workplaces, \"sago chida\" means 'to cause an accident' or 'make a big blunder'. Tae-ho brushes it right off with \"gwaenchana\", 'it's okay'."),
    (4, None, "'Later on, if your own show does well, everything turns out fine.' \"Najunge\" looks ahead to 'later on', while \"gwaenchanajineun geoya\" turns 'okay' into 'it becomes okay over time'."),
    (5, None, "'Did you hear back from your father?' Sliding in beside him, Ye-jin asks about \"abeoji\", 'father', hoping for a discount on the bumper scratch from Episode 1."),
    (6, None, "'Yes, he said he charged only the strictly necessary repair cost.' Honest to a fault, Seung-chan relays \"suribi\", 'repair fee', restricted with \"-man\", 'only', leaving zero wiggle room for a bargain."),
    (7, None, "'Oh, really? You are on probation right now, aren't you?' Her smile vanishes on \"a, geurae\", 'oh, is that so?', as she brings up \"suseup\", a new employee's probationary period."),
    (8, None, "'Yes, for three months.' \"Sam gaewol\" counts 'three months', followed by \"dongan\", 'for the duration of'."),
    (9, None, "'If you mess up during probation, you can get fired.' Dropping the hammer, Ye-jin uses \"jallida\" — literally 'to get cut', the blunt everyday word for getting fired."),
    (10, None, "'You already messed up once, right?' \"Beolsseo\" means 'already', and \"han beon\" counts 'one time' against the company's three-strike rule."),
    (11, None, "'You have two times left, huh? Watch out.' Counting down with \"du beon namanne\", 'two times remain', she leaves him with \"josimhae\" — 'watch your step!'."),
]

TRANSITION = "Now let's hear the whole welcome-party scene straight through."
OUTRO = "With \"jal butakdeurigesseumnida\" for day-one introductions, \"gwaenchana\" to reassure someone, and \"josimhae\" as a sharp warning, you can handle any office gathering. Until next time!"
CLOSING = ("taeho", "또 봐요!")
