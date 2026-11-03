"""Scene 17: Joon-mo learns he is keeping his post, must recast immediately, and compares cancelling a show to a wake."""
ID = "the-producers-s01e01-scene-17"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 17
TITLE = "나도 날아가요?  (Am I Getting Fired Too?)"
LEVEL = "A1 — beginner"
LABELS = {"joonmo": "라준모", "taeho": "김태호"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "Following Kim Tae-ho back to his office, Ra Joon-mo anxiously asks if he is losing his job along with his cast, "
    "then reflects on how lonely a cancelled show feels. Listen for the workplace slang for getting axed, "
    "and the expression for 'a funeral home'."
)

STORY = [
    ("joonmo", "나는 어떻게 돼요? 나도 날아가요?", "What happens to me? Am I getting blown away too?", [(559, "나는 어떻게 돼요?"), (561, "나도 날아가요?")], ""),
    ("taeho", "넌 안 날아가.", "You aren't getting blown away.", [(563, "넌 안 날아가")], ""),
    ("taeho", "일단 멤버만 새로 짜서 다시 들어가보란 말이야.", "Just put together a new cast first and jump back in.", [(564, "일단 멤버만 새로 짜서 다시 들어가보란 말이야")], ""),
    ("joonmo", "언제부터요?", "Starting when?", [(565, "언제부터요?")], ""),
    ("taeho", "뭘 언제부터야, 지금 당장이지!", "What do you mean starting when, right this second!", [(566, "뭘 언제부터야 지금 당장이지")], ""),
    ("taeho", "지금 제일 급한 거는 멤버들한테 빨리 알리는 거야.", "The most urgent thing right now is telling the cast members quickly.", [(574, "지금 제일 급한 거는 멤버들한테 빨리 알리는 거야")], ""),
    ("joonmo", "방송 시작할 때 보면 돌잔치 같죠?", "When a show starts, it looks like a first-birthday party, right?", [(608, "방송 시작할 때 보면 돌잔치 같죠?")], ""),
    ("joonmo", "방송 막 내릴 때 보면 상갓집 같아요.", "When the curtain comes down on a show, it feels like a funeral home.", [(611, "방송 막 내릴 때 보면"), (612, "상갓집 같아요")], ""),
]

OPENER = "Let's unpack the eight lines of Joon-mo's talk with Tae-ho."

WALK = [
    (0, None, "'What happens to me? Am I getting blown away too?' First comes the anxious question 'what becomes of me?'. Then comes an expression that literally means 'to fly away in the wind' — vivid workplace slang for losing your post!"),
    (1, None, "'You aren't getting blown away.' Tae-ho reassures him with a casual contraction meaning 'as for you', followed by the negated form. Placing that short negative word right before the action flips 'fly away' into 'you are staying put'."),
    (2, None, "'Just put together a new cast first and jump back in.' He opens with a handy word meaning 'first of all' or 'for starters', a lifesaver when breaking big tasks into step one. Korean variety shows borrow English 'member' for their regular cast, paired here with 'assemble freshly'."),
    (3, None, "'Starting when?' Combine the question word meaning 'when' with the marker for 'from' or 'starting at', and tack on the polite ending. Three words in English, one compact Korean chunk."),
    (4, None, "'What do you mean starting when, right this second!' Echoing a question with a dismissive 'what...' brushes it aside as obvious: 'what do you mean, when?!'. Then pairing 'now' with 'immediately' delivers 'right this instant!'."),
    (5, None, "'The most urgent thing right now is telling the cast members quickly.' The opening phrase means 'the most urgent thing', built from the word meaning 'urgent'. Then come 'quickly' and an expression meaning to break news officially."),
    (6, None, "'When a show starts, it looks like a first-birthday party, right?' Turning to the documentary crew, Joon-mo compares a premiere to Korea's traditional celebration for a baby's first birthday, followed by a polite tag meaning 'looks like it, right?'."),
    (7, None, "'When the curtain comes down on a show, it feels like a funeral home.' Here he uses the theatre idiom that literally means 'lowering the stage curtain'. Against that joyful first-birthday feast, he sets the compound noun for a house in mourning — and Tae-ho tells the crew not to edit it out!"),
]

TRANSITION = "Now let's listen to the whole conversation in Tae-ho's office again."
OUTRO = "You learned workplace slang for losing a post, how to ask 'starting when?', the emphatic phrase for 'right this instant', and the contrast between a first-birthday celebration and a funeral home. Let's head backstage at Music Bank!"
CLOSING = ("taeho", "또 만나요!")
