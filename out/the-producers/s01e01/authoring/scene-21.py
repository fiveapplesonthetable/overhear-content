"""Scene 21: Ye-jin flatters Cindy into wearing a jacket, then traps Seung-chan in an apology loop."""
ID = "the-producers-s01e01-scene-21"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 21
TITLE = "자켓 같은 걸 좀 입어주면  (What If You Wear a Jacket?)"
LEVEL = "A1 — beginner"
LABELS = {"yejin": "탁예진", "cindy": "신디", "seungchan": "백승찬"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "Once everyone leaves the room, Tak Ye-jin switches tactics from scolding to flattery to get a jacket over Cindy's "
    "sheer outfit — then steps into the hall to scold Seung-chan all over again. Listen for the words for 'upset' "
    "and 'a vicious cycle'."
)

STORY = [
    ("yejin", "나는 이 옷이 너무 예쁜데, 아 나 진심 속상해.", "I think this outfit is so pretty, oh I'm genuinely upset.", [(781, "나는 이 옷이 너무 예쁜데"), (783, "아 나 진심 속상해")], ""),
    ("yejin", "자기가 이 옷 입고 방송 나가잖아? 나 방통위 가야 돼.", "You know if you go on air wearing this outfit, I have to go to the Commission.", [(787, "지금 자기가 이 옷 입고 방송 나가잖아?"), (788, "나 방통위 가야 돼")], ""),
    ("yejin", "자켓 같은 걸 좀 입어주면 어떨까?", "How about wearing something like a jacket over it for me?", [(793, "이렇게 자켓 같은 걸 좀 입어주면 어떨까?")], ""),
    ("cindy", "자켓이 있나?", "Do we have a jacket?", [(802, "자켓이 있나?")], ""),
    ("yejin", "고마워요!", "Thank you!", [(807, "고마워요")], ""),
    ("yejin", "야, 땡땡이! 너 이름이 뭐니?", "Hey, polka dots! What's your name?", [(812, "야 땡땡이"), (814, "너 이름이 뭐니?")], ""),
    ("seungchan", "죄송합니다!", "I am very sorry!", [(819, "죄송합니다")], ""),
    ("seungchan", "죄송하단 말은 할 수가 없고, 악순환이네요.", "Yet I'm not allowed to say I'm sorry — it's a vicious cycle.", [(833, "그렇지만 죄송하단 말은 할 수가 없고"), (834, "악순환이네요")], ""),
]

OPENER = "Let's unpack the eight lines of Ye-jin's sweet talk and Seung-chan's catch-twenty-two."

WALK = [
    (0, None, "'I think this outfit is so pretty, oh I'm genuinely upset.' Alone with Cindy, Ye-jin does a complete turnaround: she praises the outfit as 'so pretty', then pairs a word meaning 'genuinely' with an everyday expression meaning 'upset' or 'heartbroken' over the stuffy rules!"),
    (1, None, "'You know if you go on air wearing this outfit, I have to go to the Commission.' Notice her warm, affectionate word for 'you' — often used fondly among women like 'darling'. The closing pattern pairs 'go' with 'must' to warn: 'I'll have to go to the Commission!'."),
    (2, None, "'How about wearing something like a jacket over it for me?' Instead of ordering a change, she suggests a jacket using a polite form that literally means 'if you wear it as a favour for me', softened by a closing question meaning 'how would that be?'."),
    (3, None, "'Do we have a jacket?' Flattered that she isn't losing face, Cindy relents with a soft self-directed question ending — musing aloud to her stylist, 'I wonder if there is a jacket around?'."),
    (4, None, "'Thank you!' Beaming in victory, Ye-jin switches to the warm, friendly polite version of 'thank you' that you will hear constantly alongside the stiffer formal expression."),
    (5, None, "'Hey, polka dots! What's your name?' Back in the hall, her sweet smile vanishes! She uses the casual question form for 'what is your name?', reserved for kids or brand-new juniors rather than peers or strangers."),
    (6, None, "'I am very sorry!' Scolded for calling Cindy's outfit pretty earlier, Seung-chan blurts out that formal workplace expression for 'I am sorry' by reflex — forgetting rule number two from this morning!"),
    (7, None, "'Yet I'm not allowed to say I'm sorry — it's a vicious cycle.' In his deadpan interview, he uses the pattern meaning 'cannot say', then sums up his trap with the compound word for 'vicious cycle' — scolded if he speaks, scolded if he stays quiet!"),
]

TRANSITION = "Now let's listen to the whole jacket negotiation and hallway scolding again."
OUTRO = "You picked up how to say something upsets you, a warm 'thank you', and the word for a no-win loop. Time for the live broadcast!"
CLOSING = ("yejin", "또 만나요!")
