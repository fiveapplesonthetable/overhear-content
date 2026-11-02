"""Scene 27: Seung-chan silently delivers Youn Yuh-jung's plum tea to Joon-mo, and a flashback reveals Joon-mo stamping his thumbprint on Ye-jin's roommate pledge."""
ID = "the-producers-s01e02-scene-27"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 2
SCENE = 27
TITLE = "도장 한 번 더 찍어줄게  (I'll Stamp It Once More for Sure)"
LEVEL = "A1 — beginner"
LABELS = {"joonmo": "라준모", "seungchan": "백승찬", "yejin": "탁예진"}
SOURCE_NAME = "프로듀사 (The Producers) S1.02"
SOURCE_FILE = "sources/the-producers/s01/e02.ko.srt"

INTRO = (
    "In the final scene of Episode 2, Baek Seung-chan obeys Ra Joon-mo's ban on speaking by silently setting "
    "Youn Yuh-jung's plum tea on the editing desk. Then a warm flashback shows how Ye-jin came to live at "
    "Joon-mo's flat: worried she might stay in a cramped motel, Joon-mo stamps his own thumbprint onto her "
    "roommate pledge. Listen for \"mal geolda\", 'to start talking to someone', and \"dojang\", 'a personal seal'."
)

STORY = [
    ("joonmo", "야, 이거 뭐야? 안 들려?", "Hey, what is this? Can't you hear me?", [(1129, "야 이거 뭐야 안 들려?")], ""),
    ("joonmo", "이게 뭔지 말해야 될 거 아니야!", "You have to tell me what this is!", [(1131, "이게 뭔지 말해야 될 거 아니야")], ""),
    ("seungchan", "윤여정 선생님이 선배님께 전해드리라고 하셨습니다.", "Ms. Youn Yuh-jung asked me to pass this to you.", [(1132, "윤여정 선생님이 선배님께 전해드리라고")], "Completes polite verb 하셨습니다."),
    ("seungchan", "그동안 재밌었다는 말도 같이 전해달라고 하셨습니다.", "She also asked me to tell you she had fun all this time.", [(1133, "그동안 재밌었다는 말도 같이")], "Completes polite clause."),
    ("joonmo", "너 그걸 이제 말하면 어떡해?", "How can you tell me that only now?", [(1134, "너 그걸 이제 말하면")], "Uses standard 어떡해 for caption 어떻게."),
    ("seungchan", "말 걸지 말라고 하셔서요.", "Because you told me not to speak to you.", [(1135, "말 걸지 말라고 하셔서")], "Adds polite -요 ending."),
    ("joonmo", "아, 이건 말을 했었어야지!", "Ah, you still should have told me about this!", [(1136, "아 이건 말을 했었어야지")], ""),
    ("yejin", "모텔 같은 데 장기투숙이나 해야지 뭐.", "I suppose I'll just stay long-term at a motel or somewhere.", [(1153, "모텔 같은데"), (1153, "장기투숙이나 해야지 뭐")], "Uses standard spacing 같은 데."),
    ("yejin", "너 나중에 딴소리 하기 없기다.", "No going back on your word later.", [(1155, "너 나중에 딴소리 하기 없기다")], ""),
    ("joonmo", "진짜 딴소리 안 해.", "I really won't go back on my word.", [(1156, "진짜 딴소리 안 해")], ""),
    ("joonmo", "내가 도장 한 번 더 찍어줄게.", "I will stamp my seal one more time for good measure.", [(1164, "내가 도장 한 번"), (1164, "더 찍어줄게")], ""),
    ("yejin", "감사합니다.", "Thank you very much.", [(1165, "감사합니다.")], ""),
]

OPENER = "Let's unpack the Episode 2 finale and its flashback line by line."

WALK = [
    (0, None, "'Hey, what is this? Can't you hear me?' Staring at the mystery shopping bag on his desk, Joon-mo snaps \"igeo mwoya\", 'what is this?', followed by \"an deullyeo\", 'can't you hear?'."),
    (1, None, "'You have to tell me what this is!' Exasperated by Seung-chan's stony silence, Joon-mo insists \"malhaeya doel geo aniya\" — 'obviously you need to speak up!'."),
    (2, None, "'Ms. Youn Yuh-jung asked me to pass this to you.' Freed to talk, Seung-chan uses honorific \"seonbaenimkke\", 'to you, senior', with \"jeonaedeurirago\", 'told me to hand this over'."),
    (3, None, "'She also asked me to tell you she had fun all this time.' \"Geudongan\" spans their whole season working together, and \"gachi\", 'together' or 'along with it', attaches her warm farewell note."),
    (4, None, "'How can you tell me that only now?' Touched and flustered at once, Joon-mo blurts out \"ije malhamyeon eotteokhae\", using \"ije\" for 'only now'."),
    (5, None, "'Because you told me not to speak to you.' Deadpan as ever, Seung-chan cites Joon-mo's own command: \"mal geolda\" means 'to strike up speech with someone', negated in \"mal geolji mallago\"."),
    (6, None, "'Ah, you still should have told me about this!' Groaning at how literally the rookie obeys orders, Joon-mo mutters \"mareul haesseosseoyaji\" — 'you obviously should have said so!'."),
    (7, None, "'I suppose I'll just stay long-term at a motel or somewhere.' Flashing back four months earlier over drinks, homeless Ye-jin sighs about \"janggitusuk\", 'a long-term stay', at a cheap \"motel\"."),
    (8, None, "'No going back on your word later.' Once Joon-mo caves and offers his spare room, Ye-jin pulls out a written contract and warns \"ttansori hagi eopgida\" — literally 'no talking differently later!', a classic Korean pinky-swear rule."),
    (9, None, "'I really won't go back on my word.' Joon-mo reassures his longtime friend with \"jinjja ttansori an hae\", 'I truly won't change my tune', worrying about her safety in rough lodgings."),
    (10, None, "'I will stamp my seal one more time for good measure.' Pressing his red ink thumbprint onto her paper again, he says \"dojang\", 'personal stamp', and \"jjigeojulkke\", 'I'll stamp it for you'."),
    (11, None, "'Thank you very much.' Dropping her usual bickering tone, Ye-jin beams with formal \"gamsahamnida\" — bringing Episode 2 of The Producers to a warm close."),
]

TRANSITION = "Now let's listen to the entire final scene of Episode 2 from beginning to end."
OUTRO = "That wraps up Episode 2! You now know \"mal geolda\" for starting a conversation, \"ttansori\" for changing your story, and \"dojang\" for sealing a promise. Until Episode 3!"
CLOSING = ("yejin", "다음에 만나요!")
