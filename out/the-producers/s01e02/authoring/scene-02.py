"""Scene 02: Ye-jin vents about her housing crisis at a pub."""
ID = "the-producers-s01e02-scene-02"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 2
SCENE = 2
TITLE = "길바닥에 나올 게 생겼다니까  (I Am About To End Up on the Streets)"
LEVEL = "A1 — beginner"
LABELS = {"joonmo": "라준모", "yejin": "탁예진"}
SOURCE_NAME = "프로듀사 (The Producers) S1.02"
SOURCE_FILE = "sources/the-producers/s01/e02.ko.srt"

INTRO = (
    "At the start of the episode, senior producer Tak Ye-jin vents to her longtime friend Ra Joon-mo "
    "over drinks in a neighbourhood pub about a sudden housing crisis. Listen for \"jeonse\", the unique "
    "Korean lease system where tenants give the landlord a large returnable deposit instead of paying monthly rent."
)

STORY = [
    ("yejin", "전세 만기가 2월 말.", "My jeonse lease expires at the end of February.", [(51, "전세 만기가 2월 말")], ""),
    ("yejin", "그리고 내 동탄 새 아파트 입주가 6월 말.", "And I move into my new apartment in Dongtan at the end of the sixth month.", [(52, "그리고 내 동탄 새 아파트 입주가 6월 말")], ""),
    ("yejin", "이렇게 딱 넉 달이 비는데,", "So there is exactly a four-month gap,", [(53, "이렇게 딱 넉 달이")], "The STT incorrectly transcribed 비는데 as 빚는데, so it is excluded from the alignment."),
    ("yejin", "그 넉 달만 그냥 연장해 주면 얼마나 좋냐고.", "how great would it be if they just extended it for those four months?", [(54, "그 넉 달만 그냥 연장해 주면 얼마나 좋냐고")], ""),
    ("yejin", "근데 그 집주인이 안 된다는 거야.", "But the landlord says no.", [(55, "근데 그 집주인이 안 된다는 거야")], ""),
    ("yejin", "그냥 전세 연장을 하든 아니면 이사를 나가든지 하래요.", "He told me to either extend the lease or move out.", [(56, "그냥 전세 연장을 하든 아니면 이사를 나가든지 하래요")], ""),
    ("yejin", "나 지금 길바닥에 나올 게 생겼다니까.", "I am about to end up on the streets right now.", [(57, "나 지금 길바닥에 나올 게 생겼다니까")], ""),
    ("joonmo", "전세 연장해.", "Extend the lease.", [(58, "전세 연장해")], ""),
    ("yejin", "2억을 더 달라는데?", "They are asking for two hundred million won more?", [(59, "2억을 더 달라는데?")], ""),
    ("joonmo", "2억?", "Two hundred million?", [(60, "2억?")], ""),
    ("joonmo", "월세 같은 거 없나? 단기 월세.", "Isn't there something like monthly rent? Short-term monthly rent.", [(64, "월세 같은 거 없나? 단기 월세")], ""),
    ("yejin", "넉 달 때우려고?", "To fill in four months?", [(65, "넉 달 때우려고?")], ""),
    ("yejin", "이사 비용에 복비 더블로 내야 되지.", "I would have to pay moving costs and realtor fees double.", [(66, "이사 비용에 복비 더블로 내야 되지")], ""),
]

OPENER = "Let's unpack those thirteen lines one turn at a time."

WALK = [
    (0, None, "'My jeonse lease expires at the end of February.' Ye-jin starts her rant using \"jeonse\", the deposit-based lease system. She specifies the timing with \"mangi\", meaning 'expiration', followed by \"i-wol\", 'February', and \"mal\", 'end'."),
    (1, None, "'And I move into my new apartment in Dongtan at the end of the sixth month.' Ye-jin connects her thoughts with \"geurigo\", 'and', pointing out her destination with \"sae\", 'new', and \"apateu\", 'apartment'. The move itself is \"ipju\", meaning 'moving in', scheduled for \"yu-wol mal\", the end of the sixth month, in a suburb south of Seoul."),
    (2, None, "'So there is exactly a four-month gap,' Ye-jin explains her dilemma starting with \"ireoke\", 'like this'. She highlights the exact timeframe using \"ttak\", 'exactly', and \"neok dal\", 'four months'. The verb \"bineunde\" describes the time as being empty or vacant."),
    (3, None, "'how great would it be if they just extended it for those four months?' Ye-jin refers back to the timeframe with \"geu\", 'that', and emphasizes 'only' with the particle \"-man\". The phrase \"yeonjanghae jumeon\" means 'if they extend it for me', expressing her wish."),
    (4, None, "'But the landlord says no.' Ye-jin shifts the tone with \"geunde\", a casual 'but'. She points her frustration at \"geu jipjuin\", 'that landlord', who is firmly saying \"an doendaneun geoya\", meaning it is not possible."),
    (5, None, "'He told me to either extend the lease or move out.' Ye-jin quotes the ultimatum using \"isareul nagadeunji\", 'or move out'. The ending \"haraeyo\" passes along the command she was given."),
    (6, None, "'I am about to end up on the streets right now.' Ye-jin dramatizes her situation starting with \"na\", 'I', and \"jigeum\", 'now'. She uses \"gilbadak\", 'street', and \"saenggyeotdanikka\", 'I am telling you it ended up like this', to show her panic."),
    (7, None, "'Extend the lease.' Joon-mo offers a simple solution. He drops all formalities and just says \"yeonjanghae\", the casual command to 'extend' the contract."),
    (8, None, "'They are asking for two hundred million won more?' Ye-jin shoots back the ridiculous condition. She names the price with \"i-eok\", 'two hundred million', adding \"deo\", 'more', right before \"dallaneunde\", 'they are asking for'."),
    (9, None, "'Two hundred million?' Joon-mo repeats the massive sum in disbelief, simply echoing \"i-eok\"."),
    (10, None, "'Isn't there something like monthly rent? Short-term monthly rent.' Joon-mo suggests an alternative using \"wolse\", 'monthly rent', and \"gatteun geo\", 'something like'. He clarifies his idea by adding \"dangi\", meaning 'short-term'."),
    (11, None, "'To fill in four months?' Ye-jin questions the practicality of that plan. She repeats \"neok dal\", 'four months', and asks his intention with \"ttaeullyeogo\", meaning 'to fill in' or 'make do'."),
    (12, None, "'I would have to pay moving costs and realtor fees double.' Ye-jin lists the financial burdens starting with \"isabiyong\", 'moving costs', and \"bokbi\", 'realtor fees'. She emphasizes the waste by saying she would have to pay them \"deobeullo\", 'double'."),
]

CLOSING = ("yejin", "다음에 만나요.")

TRANSITION = "Now let's hear the whole conversation about the lease from start to finish."
OUTRO = "From \"mangi\" for expiration to \"wolse\" for monthly rent, you now have some essential vocabulary for navigating the Korean housing market. Catch you later!"
