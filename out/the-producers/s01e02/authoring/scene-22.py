"""Scene 22: Outside the noisy restaurant at night, Joon-mo tells Hye-joo plainly that they should stop meeting privately."""
ID = "the-producers-s01e02-scene-22"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 2
SCENE = 22
TITLE = "따로 만나는 거 그만하자  (Let's Stop Meeting Privately)"
LEVEL = "A1 — beginner"
LABELS = {"hyejoo": "신혜주", "joonmo": "라준모"}
SOURCE_NAME = "프로듀사 (The Producers) S1.02"
SOURCE_FILE = "sources/the-producers/s01/e02.ko.srt"

INTRO = (
    "Stepping onto the night sidewalk outside the noisy restaurant, Ra Joon-mo runs into assistant director "
    "Shin Hye-joo, whom he has been casually seeing without real commitment. Stung by Youn Yuh-jung's scolding "
    "about honesty, Joon-mo decides to end things clearly and politely instead of vanishing. Listen for "
    "\"ibyeol\", 'a breakup', and \"geumanhaja\", 'let's stop'."
)

STORY = [
    ("hyejoo", "안 그래도 전화하려고 나왔는데.", "I actually just stepped out to call you.", [(969, "안 그래도 전화하려고 나왔는데")], ""),
    ("hyejoo", "안에 시장통이야. 우리 따로 나가요.", "Inside is chaotic like a marketplace. Let's slip out separately.", [(970, "안에 시장통이야 우리 따로 나가요")], ""),
    ("joonmo", "혜주야, 나 너한테 할 말 있다.", "Hye-joo, I have something to say to you.", [(971, "혜주야 나 너한테 할 말 있다")], ""),
    ("hyejoo", "네? 무슨 말이요?", "Yes? What is it?", [(972, "네? 무슨")], "Completes natural polite question 말이요."),
    ("joonmo", "아니다 싶으면 확실하게 얘기해야지.", "When something doesn't feel right, a person should say so clearly.", [(973, "아니다 싶으면 확실하게 얘기해서")], "Adapts Ye-jin's advice into a standalone statement."),
    ("joonmo", "이별에도 예의라는 게 있는 법이야.", "Even in a breakup, there is such a thing as courtesy.", [(974, "이별에도 예의라는 게 있는 법이에요")], "Uses casual 이야 matching Joon-mo's voice."),
    ("joonmo", "네가 좋고 이쁘긴 한데.", "You're nice and pretty, though.", [(975, "네가 좋고 이쁘긴 한데")], ""),
    ("joonmo", "우리는 네가 원하는 관계가 될 순 없을 것 같아.", "I don't think we can become the kind of relationship you want.", [(976, "네가 원하는"), (976, "관계가 될 순 없을 것 같아")], ""),
    ("hyejoo", "네?", "Pardon?", [(977, "네?")], ""),
    ("joonmo", "따로 만나는 거 그만하자.", "Let's stop meeting on our own.", [(978, "따로 만나는 거 그만하자")], ""),
    ("joonmo", "미안하다.", "I'm sorry.", [(979, "미안하다")], ""),
    ("hyejoo", "알겠어요, 선배.", "I understand, senior.", [], "Adds calm closing acknowledgment for round-off."),
]

OPENER = "Let's go through Joon-mo's quiet talk outside the restaurant step by step."

WALK = [
    (0, None, "'I actually just stepped out to call you.' Hye-joo opens with \"an geuraedo\", a handy conversational bridge meaning 'as a matter of fact' or 'just as you showed up', before \"jeonhwaharyeogo\", 'intending to phone'."),
    (1, None, "'Inside is chaotic like a marketplace. Let's slip out separately.' Calling a loud room \"sijangtong\", 'a bustling street market', is vivid everyday Korean. \"Ttaro\" means 'apart from the crowd' or 'just the two of us'."),
    (2, None, "'Hye-joo, I have something to say to you.' Adding \"-ya\" to a name ending in a vowel is friendly casual address, while \"hal mal itda\" signals serious news: 'I have something I need to tell you'."),
    (3, None, "'Yes? What is it?' Sensing the shift in mood, Hye-joo switches to polite \"ne\" and asks \"museun mariyo\", using \"museun\" for 'what kind of'."),
    (4, None, "'When something doesn't feel right, a person should say so clearly.' Remembering how badly hints went inside, Joon-mo chooses \"hwaksilhage\", 'unmistakably' or 'clearly', alongside \"yaegihaeyaji\", 'one ought to speak up'."),
    (5, None, "'Even in a breakup, there is such a thing as courtesy.' Here \"ibyeol\" means 'parting ways', and \"yeui\" is 'good manners' or 'decency' — echoing the exact lesson he heard earlier in the day."),
    (6, None, "'You're nice and pretty, though.' He softens the blow with \"joko\", 'kind and likable', and spoken \"ippeugin hande\", 'you certainly are pretty, but...', leaving the contrast hanging gently."),
    (7, None, "'I don't think we can become the kind of relationship you want.' \"Wonhaneun\" means 'wishing for', modifying \"gwangye\", 'relationship', while \"eopsseul geot gata\" softens 'cannot become' into 'it seems we cannot'."),
    (8, None, "'Pardon?' Caught off guard, Hye-joo lets out a quiet, rising \"ne?\" — the polite way to ask 'what did you just say?'."),
    (9, None, "'Let's stop meeting on our own.' Rather than ghosting her, Joon-mo states it plainly: \"ttaro mannaneun geo\", 'seeing each other privately', plus \"geumanhaja\", 'let's call it off'."),
    (10, None, "'I'm sorry.' With a younger colleague he knows well, Joon-mo uses plain \"mianhada\", sincere and unadorned."),
    (11, None, "'I understand, senior.' Taking a quiet breath, Hye-joo answers \"algesseoyo\", a calm 'got it, I understand', addressing him simply as \"seonbae\"."),
]

TRANSITION = "Now let's hear the entire sidewalk conversation again from top to bottom."
OUTRO = "You just picked up \"an geuraedo\" for natural transitions, \"hwaksilhage\" for speaking clearly, and \"geumanhaja\" when it is time to wrap something up. Until next time!"
CLOSING = ("hyejoo", "안녕히 가세요!")
