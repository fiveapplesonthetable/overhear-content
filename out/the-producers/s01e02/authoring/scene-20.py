"""Scene 20: While Seung-chan scrambles in a taxi, Tae-ho bursts into the dinner and accidentally reveals the cast cut."""
ID = "the-producers-s01e02-scene-20"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 2
SCENE = 20
TITLE = "우리 전원 하차라며  (You Said the Whole Cast Is Leaving)"
LEVEL = "A1 — beginner"
LABELS = {"seungchan": "백승찬", "taeho": "김태호", "joonmo": "라준모"}
SOURCE_NAME = "프로듀사 (The Producers) S1.02"
SOURCE_FILE = "sources/the-producers/s01/e02.ko.srt"

INTRO = (
    "Rookie producer Baek Seung-chan is still racing across Seoul in a taxi when chief producer Kim Tae-ho "
    "bursts late into the cast dinner. Trying to boast that he defended the actresses in front of the director, "
    "Tae-ho accidentally lets the secret slip before Ra Joon-mo can stop him. Listen for \"jeonwon hacha\", "
    "meaning the entire cast is stepping down, and \"majimak\" for 'the last'."
)

STORY = [
    ("seungchan", "제가 지금 너무 급해서요.", "I am in a huge rush right now.", [(860, "제가 지금 너무 급해서")], "Adds polite -요 ending."),
    ("seungchan", "여보세요? 선배님?", "Hello? Senior?", [(861, "여보세요? 선배님?")], ""),
    ("taeho", "이거 진짜 말도 안 돼.", "This really makes no sense at all.", [(871, "이거 진짜 말도 안 돼")], ""),
    ("taeho", "나 국장실 뒤집어 놓고 오느라고 늦었잖아.", "I'm late because I turned the director's office upside down before coming.", [(872, "나 국장실 뒤집어 놓고 오느라고 늦었잖아")], ""),
    ("joonmo", "왜 뒤집어 놔, 국장실을?", "Why turn the director's office upside down?", [(874, "왜 뒤집어 놔 국장실을")], ""),
    ("taeho", "우리 전원 하차라며?", "Didn't you say our whole cast is stepping down?", [(882, "우리 전원 하차라며")], ""),
    ("joonmo", "죄송합니다, 선생님.", "I am deeply sorry, Teacher.", [(887, "죄송합니다 선생님")], ""),
    ("joonmo", "저희 저번 녹화가 마지막이었고요.", "Our last recording was the final one.", [(888, "저희 저번 녹화가 마지막이었고요")], ""),
    ("joonmo", "멤버 체인지를 결정했습니다.", "We decided on a cast change.", [(890, "멤버 체인지를 결정했습니다")], ""),
    ("taeho", "근데 왜 여정 선생님 모르셔?", "Then why doesn't Ms. Yuh-jung know?", [(892, "근데 왜 여정 선생님 모르셔?")], ""),
    ("taeho", "세상에, 말씀 안 드린 거야?", "Good grief, did nobody tell her?", [(898, "세상에 말씀 안 드린 거야?")], ""),
    ("joonmo", "지금 어디라는 거야?", "Where does he say he is right now?", [(899, "지금 어디라는 거야?")], ""),
]

OPENER = "Let's break down how the secret comes out, one line at a time."

WALK = [
    (0, None, "'I am in a huge rush right now.' From the back of a taxi, Seung-chan pairs \"jigeum\", 'right now', with \"geuphaeseoyo\", 'because it is urgent'. Humble \"jega\" marks 'I' politely when asking a senior for help."),
    (1, None, "'Hello? Senior?' \"Yeoboseyo\" is how Koreans answer or check a phone call, never used face-to-face across a table. He follows it with \"seonbaenim\", the respectful workplace title for an experienced colleague."),
    (2, None, "'This really makes no sense at all.' Back at the restaurant, Tae-ho barges in declaring \"maldo an dwae\", literally 'it doesn't even become words' — the go-to Korean exclamation for 'unbelievable!' or 'no way!'."),
    (3, None, "'I'm late because I turned the director's office upside down before coming.' Bragging loudly, Tae-ho names \"gukjangsil\", the department director's office, and \"dwijibeo noko\", 'flipping it upside down', to excuse why he arrived late, \"neujeotjana\"."),
    (4, None, "'Why turn the director's office upside down?' Panicking across the room, Joon-mo shoots back \"wae dwijibeo nwa\", hoping Tae-ho will catch his eye and stop talking."),
    (5, None, "'Didn't you say our whole cast is stepping down?' Too late — Tae-ho blurts out \"jeonwon\", 'every single member', plus \"hacha\", 'getting off a vehicle' or 'leaving a show'. The ending \"-ramyeo\" checks a rumor he thought everyone at the table already knew."),
    (6, None, "'I am deeply sorry, Teacher.' With the room silent, Joon-mo bows his head and offers \"joesonghamnida\", the formal apology you reach for when casual 'sorry' is nowhere near enough."),
    (7, None, "'Our last recording was the final one.' Humble \"jeohui\" means 'our', \"jeobeon nokhwa\" refers to 'the previous studio shoot', and \"majimak\" lands the hard truth: 'the final one'."),
    (8, None, "'We decided on a cast change.' Korean television crews borrow the English loanwords \"membeo cheinji\" for a lineup overhaul, closing with formal \"gyeoljeonghaesseumnida\", 'we made the decision'."),
    (9, None, "'Then why doesn't Ms. Yuh-jung know?' Realizing his blunder, Tae-ho starts with \"geunde\", 'but wait', and adds respectful \"moreusyeo\" from \"moreuda\", 'not to know'."),
    (10, None, "'Good grief, did nobody tell her?' \"Sesange\", literally 'in the world', expresses pure shock, while \"malsseum an deurin geoya\" uses the honorific expression for speaking to an elder."),
    (11, None, "'Where does he say he is right now?' Fuming over the missing rookie messenger, Joon-mo demands \"jigeum eodiraneun geoya\", combining \"eodi\", 'where', with quoted speech to ask where Seung-chan claims to be."),
]

TRANSITION = "Now let's hear the whole restaurant reveal from beginning to end."
OUTRO = "With \"yeoboseyo\" for phone calls, \"maldo an dwae\" for disbelief, and \"majimak\" for the final turn, you are ready for high-drama moments too. See you next time!"
CLOSING = ("seungchan", "안녕히 가세요!")
