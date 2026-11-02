"""Scene 05: Seung-chan runs into Hye-joo outside his home."""
ID = "the-producers-s01e02-scene-05"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 2
SCENE = 5
TITLE = "포기는 빠른 편이라  (I Tend to Give Up Quickly)"
LEVEL = "A1 — beginner"
LABELS = {"seungchan": "백승찬", "hyejoo": "신혜주"}
SOURCE_NAME = "프로듀사 (The Producers) S1.02"
SOURCE_FILE = "sources/the-producers/s01/e02.ko.srt"

INTRO = (
    "Outside his home, rookie producer Baek Seung-chan runs into Shin Hye-joo, the senior he has a crush on. "
    "She casually mentions her boyfriend, breaking his heart. Listen for \"namchin\", slang for boyfriend, "
    "and \"pogi\", meaning 'giving up'."
)

STORY = [
    ("hyejoo", "집이 여기?", "Your house is here?", [(160, "집이 여기?")], ""),
    ("seungchan", "누나도 여기 사세요?", "Do you live here too, noona?", [(162, "누나도 여기 사세요?")], ""),
    ("hyejoo", "아니, 나 말고 내 남친.", "No, not me, my boyfriend.", [(163, "아니 나 말고 내 남친")], ""),
    ("hyejoo", "지금 1박 2일 하거든.", "He is doing 2 Days and 1 Night right now.", [(164, "지금 1박 2일 하거든")], ""),
    ("hyejoo", "참, 너 배정 어디로 났어?", "By the way, where did you get assigned?", [(165, "참 너 배정 어디로")], "Omits the STT typo 놨어."),
    ("seungchan", "아직 안 났습니다.", "It hasn't come out yet.", [(166, "아직 안")], "Omits the STT typo 놨습니다."),
    ("hyejoo", "그래? 와. 나 거기 있잖아.", "Really? Come on over. I am there.", [(167, "그래?"), (167, "와 나 거기 있잖아")], "Drops the specific show name to keep the vocabulary focused."),
    ("seungchan", "제가 아니다 싶으면 포기는 빠른 편이라.", "I tend to give up quickly if I think it's not meant to be.", [(172, "제가 아니다 싶으면 포기는 빠른 편이라")], ""),
    ("seungchan", "솔직히 아까 오후에 봤을 때는 놀랐죠.", "Honestly, I was surprised when I saw you this afternoon.", [(173, "솔직히 아까 오후에 봤을 때는 놀랐죠")], ""),
    ("seungchan", "저도 사람이니까.", "Because I am human too.", [(174, "저도 사람이니까")], ""),
    ("seungchan", "근데 지금은 정말 아무렇지도 않고,", "But now I am really totally fine,", [(175, "근데 지금은 정말 아무렇지도 않고")], ""),
    ("seungchan", "두 분 예쁜 사랑하셨으면 좋겠어요.", "I hope the two of you have a beautiful love.", [(176, "두 분 예쁜 사랑하셨으면 좋겠어요")], ""),
]

OPENER = "Let's unpack those twelve lines one turn at a time."

WALK = [
    (0, None, "'Your house is here?' Hye-joo recognizes him and asks a quick question using \"jibi\", 'house', and \"yeogi\", 'here'."),
    (1, None, "'Do you live here too, noona?' Seung-chan answers with his own polite question. He calls her \"nuna\", a respectful term for an older female friend, and asks \"saseyo\", 'do you live'."),
    (2, None, "'No, not me, my boyfriend.' Hye-joo casually drops a bomb. She says \"na malgo\", 'not me', and introduces \"nae namchin\", short for 'my boyfriend'."),
    (3, None, "'He is doing 2 Days and 1 Night right now.' She mentions his show using \"jigeum\", 'right now'. The ending \"hageodeun\" explains what he does in a friendly tone."),
    (4, None, "'By the way, where did you get assigned?' Hye-joo changes the subject with \"cham\", 'by the way'. She asks about his \"baejeong\", 'assignment', with \"eodiro\", 'to where'."),
    (5, None, "'It hasn't come out yet.' Seung-chan formally replies using \"ajik\", 'yet', and the negative adverb \"an\". He finishes with \"natseumnida\", the polite form of 'came out'."),
    (6, None, "'Really? Come on over. I am there.' Hye-joo invites him using \"geurae\", 'really', and the command \"wa\", 'come'. She adds \"na geogi itjana\", 'you know I am there'."),
    (7, None, "'I tend to give up quickly if I think it's not meant to be.' Seung-chan tries to save face. He uses \"pogi\", 'giving up', and \"ppareun pyeonira\", meaning 'tend to be fast'. He prefaces this with \"anida sipeumyeon\", 'if I think it is not'."),
    (8, None, "'Honestly, I was surprised when I saw you this afternoon.' Seung-chan admits his feelings using \"soljiki\", 'honestly', and \"ohue\", 'in the afternoon'. He confesses he was \"nollatjyo\", 'surprised'."),
    (9, None, "'Because I am human too.' He justifies his reaction using \"jeodo\", 'me too', and \"saraminikka\", 'because I am a person'."),
    (10, None, "'But now I am really totally fine,' Seung-chan lies bravely. He uses \"geunde jigeumeun\", 'but now', and \"jeongmal\", 'really'. The phrase \"amureochido anko\" means 'not bothered at all'."),
    (11, None, "'I hope the two of you have a beautiful love.' Seung-chan delivers a painful blessing. He uses \"du bun\", 'you two', and \"yeppeun saranghasyeosseumyeon\", 'wish you have a beautiful love', ending with \"jokesseoyo\", 'I hope'."),
]

TRANSITION = "Now let's listen to the whole awkward encounter again."
OUTRO = "From \"namchin\" for boyfriend to \"baejeong\" for assignment, you now have the vocabulary for workplace gossip and romance. Keep practicing!"
CLOSING = ("seungchan", "안녕히 가세요.")
