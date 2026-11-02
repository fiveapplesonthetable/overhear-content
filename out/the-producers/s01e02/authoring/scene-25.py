"""Scene 25: Caught in sudden rain at the KBS entrance, Cindy borrows a lobby umbrella from Seung-chan."""
ID = "the-producers-s01e02-scene-25"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 2
SCENE = 25
TITLE = "이 우산 제 거 아니고요  (This Umbrella Isn't Mine)"
LEVEL = "A1 — beginner"
LABELS = {"cindy": "신디", "manager": "매니저", "seungchan": "백승찬"}
SOURCE_NAME = "프로듀사 (The Producers) S1.02"
SOURCE_FILE = "sources/the-producers/s01/e02.ko.srt"

INTRO = (
    "At the main doors of KBS, sudden night rain traps pop star Cindy when her manager realizes he forgot an "
    "umbrella. Baek Seung-chan steps up with a borrowed lobby umbrella, only to horrify the glamorous idol by "
    "earnestly asking for her phone number to protect his paycheck. Listen for \"usan\", 'umbrella', and "
    "\"bannap\", 'returning a borrowed item'."
)

STORY = [
    ("cindy", "무슨 매니저가 우산도 안 갖고 다녀?", "What kind of manager doesn't even carry an umbrella?", [(1036, "무슨 매니저가 우산도 안 갖고 다녀")], ""),
    ("manager", "비 올 줄 몰랐지. 차 가지고 올까?", "I had no idea it would rain. Should I bring the car around?", [(1037, "비 올 줄 몰랐지"), (1038, "차 가지고 올까?")], ""),
    ("cindy", "빨리 갔다 와.", "Hurry and go get it.", [(1044, "빨리 갔다 와")], ""),
    ("seungchan", "이거 쓰세요.", "Please use this.", [(1047, "이거 쓰세요")], ""),
    ("cindy", "고마워요.", "Thank you.", [(1048, "고마워요")], ""),
    ("seungchan", "아, 근데 이 우산 제 거 아니고요.", "Ah, by the way, this umbrella isn't mine.", [(1049, "아 근데"), (1050, "이 우산"), (1051, "제 거 아니고요")], ""),
    ("seungchan", "방금 로비 데스크에서 빌린 거거든요.", "I just borrowed it from the lobby desk.", [(1052, "방금 로비 데스크에서 빌린 거거든요")], ""),
    ("seungchan", "반납 안 하면 제 월급에서 우산값을 공제합니다.", "If you don't return it, they deduct the umbrella cost from my salary.", [(1054, "반납 안 하면 제 월급에서 우산값을")], "Fixes caption typo 공지합니다 to 공제합니다."),
    ("cindy", "네, 갖다 드릴게요.", "Okay, I will bring it back.", [(1056, "네 갖다 드릴게요")], ""),
    ("seungchan", "전화번호를 좀 주실 수 있을까요?", "Could you please give me your phone number?", [(1060, "전화번호를 좀 주실 수 있을까요?")], ""),
    ("cindy", "저 누군지 아시잖아요.", "You know who I am, don't you?", [(1063, "저 누군지 아시잖아요")], ""),
    ("seungchan", "근데 번호는 모르니까요.", "Yes, but I don't know your number.", [(1064, "근데 번호는 모르니까요")], ""),
    ("cindy", "알았어요. 그쪽 번호 찍어요.", "Fine. Punch in your number.", [(1077, "알았어요 그쪽 번호 찍어요")], ""),
    ("seungchan", "꼭 삼 일 안에 반납 부탁드리겠습니다.", "Please be sure to return it within three days.", [(1084, "반납 부탁드리겠습니다")], "Spells out 삼 일 for caption 3일."),
]

OPENER = "Let's step into the rain and unpack each exchange."

WALK = [
    (0, None, "'What kind of manager doesn't even carry an umbrella?' Irritated at the doorway, Cindy uses \"usan\" for 'umbrella' and \"gatgo danyeon\" from \"gatgo danida\", 'to carry around with you'."),
    (1, None, "'I had no idea it would rain. Should I bring the car around?' Her manager excuses himself with \"bi ol jul mollatji\", 'I didn't know rain would come', then offers \"cha gajigo olkka\", 'shall I go fetch the van?'."),
    (2, None, "'Hurry and go get it.' \"Ppalli\", 'quickly', combines with \"gatda wa\", literally 'go and come back' — the everyday Korean command for running a quick errand."),
    (3, None, "'Please use this.' Holding out a large black umbrella, Seung-chan says \"igeo sseuseyo\"; in Korean, \"sseuda\" covers putting on hats, glasses, and holding open an umbrella."),
    (4, None, "'Thank you.' Surprised by the kind gesture, Cindy replies \"gomawoyo\", a warm, natural polite 'thanks'."),
    (5, None, "'Ah, by the way, this umbrella isn't mine.' Instead, of walking away coolly, Seung-chan adds \"je geo anigoyo\", using humble \"je geo\" for 'mine'."),
    (6, None, "'I just borrowed it from the lobby desk.' \"Banggeum\" means 'just a moment ago', and \"billin\" comes from \"billida\", 'to borrow'."),
    (7, None, "'If you don't return it, they deduct the umbrella cost from my salary.' Dead serious, he pairs \"bannap\", 'returning a loaner item', with \"wolgeup\", 'monthly paycheck', and \"gongjehamnida\", 'they deduct it'."),
    (8, None, "'Okay, I will bring it back.' Trying to end the awkward lecture, Cindy promises \"gatda deurilkkeyo\", humbly offering to return it."),
    (9, None, "'Could you please give me your phone number?' Still worried, Seung-chan asks for \"jeonhwabeonho\", 'phone number', softening the request with \"jom\" and \"jusil su isseulkkayo\", 'could you possibly give me?'."),
    (10, None, "'You know who I am, don't you?' Expecting every man to be flirting with her, Cindy reminds him \"nugunji asijanayo\" — 'surely you know who I am!'."),
    (11, None, "'Yes, but I don't know your number.' Completely immune to her fame, Seung-chan points out the practical gap: \"beonhoneun moreunikkayo\", 'because I don't know the number'."),
    (12, None, "'Fine. Punch in your number.' Defeated after trying a fake number first, Cindy sighs \"arasseoyo\", uses \"geujjok\" as a cool polite 'you', and tells him \"jjigeoyo\", 'type it into my phone'."),
    (13, None, "'Please be sure to return it within three days.' He finishes with \"sam il ane\", 'within three days', and ultra-polite \"butakdeurigesseumnida\", 'I kindly ask this favor of you'."),
]

TRANSITION = "Now let's hear the whole rainy-night umbrella scene again without stopping."
OUTRO = "Now you know \"igeo sseuseyo\" for offering an umbrella, \"billida\" and \"bannap\" for borrowing and returning, and \"gatda wa\" for quick errands. See you next time!"
CLOSING = ("cindy", "안녕히 계세요!")
