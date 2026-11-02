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
    (0, None, "The word for 'I think this outfit is so pretty, oh I'm genuinely upset.' Alone with Cindy, Ye-jin pivots 180 degrees: she praises the outfit as 'so pretty', then swears she is genuinely upset over the stuffy network rules! Notice the word for."),
    (1, None, "The word for 'You know if you go on air wearing this outfit, I have to go to the Commission.' Here, the friendly term of address means 'you, darling', often used warmly among women. The ending pairs the word 'to go' with 'must' — 'I'll get hauled to the Commission!' It comes from this."),
    (2, None, "The word for 'How about wearing something like a jacket over it for me?' Instead, of ordering a change, she suggests a jacket using a word form that literally means 'if you wear it as a favour for me', softened by a closing question meaning 'how would that be?' It is a handy word."),
    (3, None, "The word for 'Do we have a jacket?' Flattered that she isn't losing face, Cindy relents with a cool question — musing aloud to herself, 'wonder if there's a jacket around?' This short for that."),
    (4, None, "The word for 'Thank you!' Beaming in victory, Ye-jin switches to the warm, polite, friendly everyday 'thank you' you will hear constantly alongside the more formal expression This literally means that."),
    (5, None, "The word for 'Hey, polka dots! What's your name?' Back in the hall, the sweet smile vanishes! She uses the casual way to ask 'what's your name?', reserved for kids or brand-new juniors — with peers or strangers, you would use a polite or honorific phrasing instead The word doubles the."),
    (6, None, "The word for 'I am very sorry!' Scolded for calling Cindy's outfit pretty earlier, Seung-chan blurts out a formal apology by reflex — forgetting rule number two from this morning! Swap in this word."),
    (7, None, "The word for 'Yet I'm not allowed to say I'm sorry — it's a vicious cycle.' In his deadpan interview, he explains that he cannot say it: scolded if he speaks, scolded if he stays quiet — a true vicious cycle! We built from this."),
]

TRANSITION = "Now let's listen to the whole jacket negotiation and hallway scolding again."
OUTRO = "You picked up how to say something upsets you, a warm 'thank you', and the word for a no-win loop. Time for the live broadcast!"
CLOSING = ("yejin", "또 만나요!")
