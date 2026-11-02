"""Scene 24: Alone in the variety office after Il-yong leaves, Seung-chan answers Youn Yuh-jung's warm phone call about homemade plum tea."""
ID = "the-producers-s01e02-scene-24"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 2
SCENE = 24
TITLE = "덕분에 재밌었다고 전해줘요  (Tell Him I Had Fun Thanks to Him)"
LEVEL = "A1 — beginner"
LABELS = {"ilyong": "유일용", "seungchan": "백승찬", "actress": "윤여정"}
SOURCE_NAME = "프로듀사 (The Producers) S1.02"
SOURCE_FILE = "sources/the-producers/s01/e02.ko.srt"

INTRO = (
    "Back at the quiet KBS variety office instead of attending his own welcome party, Baek Seung-chan gets a "
    "kind word from senior producer Ryu Il-yong before the desk phone rings. On the line is Youn Yuh-jung, "
    "calling about a jar of homemade plum tea she left on Ra Joon-mo's desk. Listen for \"maesilcha\", 'plum tea', "
    "and \"nongdam\", 'a joke'."
)

STORY = [
    ("ilyong", "어쨌든 나는 널 환영한다.", "Anyway, I welcome you.", [(995, "어쨌든 나는 널 환영한다")], ""),
    ("seungchan", "여보세요?", "Hello?", [(997, "여보세요?")], ""),
    ("actress", "나 윤여정인데요. 거기 라준모 피디 자리죠?", "This is Youn Yuh-jung. That is Producer Ra Joon-mo's desk, right?", [(998, "나 윤여정인데요"), (1000, "PD 자리죠?")], "Fixes caption typo 라주모 to 라준모 and spells out 피디."),
    ("seungchan", "네, 맞습니다.", "Yes, that is right.", [(1001, "네, 맞습니다")], ""),
    ("actress", "내가 라 피디 주려고 담근 매실차예요.", "It is plum tea I steeped to give Producer Ra.", [(1006, "주려고 담근 매실차예요")], "Fixes caption 나 PD to 라 피디."),
    ("actress", "덕분에 재밌었다고 전해줘요.", "Please tell him I had fun thanks to him.", [(1018, "덕분에 재밌었다고 전해줘요")], ""),
    ("seungchan", "네, 꼭 전해드리겠습니다.", "Yes, I will be sure to pass that along.", [(1020, "꼭 전해드리겠습니다")], ""),
    ("actress", "근데 전화 받는 분은 누구신가?", "By the way, who is answering the phone?", [(1022, "근데 전화 받는 분은 누구신가?")], ""),
    ("actress", "내가 너 고소하려고. 농담이야.", "I'm going to sue you. Just kidding.", [(1025, "내가 너 고소하려고"), (1027, "농담이야")], ""),
    ("actress", "너 이름이 뭐야?", "What is your name?", [(1029, "너 이름이 뭐야?")], ""),
    ("seungchan", "백승찬입니다.", "I am Baek Seung-chan.", [(1032, "백승찬입니다")], ""),
    ("actress", "그래요, 백승찬 피디. 수고했어요, 오늘.", "All right, Producer Baek Seung-chan. Good work today.", [(1033, "그래요 백승찬 피디"), (1035, "수고했어요 오늘")], ""),
]

OPENER = "Let's walk through this late-night office call turn by turn."

WALK = [
    (0, None, "'Anyway, I welcome you.' Before heading home to his kids, Il-yong cheers Seung-chan up with \"eojjaetdeun\", 'in any case', and warm plain-style \"hwanyeonghanda\", 'I welcome you'."),
    (1, None, "'Hello?' Alone among empty desks, Seung-chan picks up the ringing receiver with \"yeoboseyo\"."),
    (2, None, "'This is Youn Yuh-jung. That is Producer Ra Joon-mo's desk, right?' Koreans introduce themselves on the phone with \"na ...-indeyo\", 'it's me, so-and-so', and \"jari\" means someone's 'seat' or 'office desk'."),
    (3, None, "'Yes, that is right.' Standing straight even on the phone, Seung-chan replies \"ne, matseumnida\" — crisp, formal confirmation for 'that's correct'."),
    (4, None, "'It is plum tea I steeped to give Producer Ra.' \"Damgeun\" describes homemade preserves or syrups steeped by hand, and \"maesilcha\" is sweet green-plum tea, a beloved Korean digestive drink."),
    (5, None, "'Please tell him I had fun thanks to him.' All her anger gone, Yuh-jung chooses \"deokbune\", 'thanks to your efforts', paired with \"jaemisseotdago jeonaejwoyo\", 'please pass along that I enjoyed it'."),
    (6, None, "'Yes, I will be sure to pass that along.' Seung-chan adds \"kkok\", 'without fail', before humble \"jeonaedeurigesseumnida\", promising to deliver her message respectfully."),
    (7, None, "'By the way, who is answering the phone?' Shifting topics with \"geunde\", Yuh-jung uses \"bun\", the polite word for 'person', inside \"nugusinga\", 'who might you be?'."),
    (8, None, "'I'm going to sue you. Just kidding.' Recognizing the rookie from her van, she teases him with \"gosohada\", 'to file a lawsuit', before immediately smiling it off with \"nongdamiya\", 'it's a joke!'."),
    (9, None, "'What is your name?' Dropping to warm elder speech, she asks \"neo ireumi mwoya\", pairing \"ireum\", 'name', with \"mwoya\", 'what is it?'."),
    (10, None, "'I am Baek Seung-chan.' To introduce yourself formally in any Korean workplace, attach \"-imnida\" straight onto your full name."),
    (11, None, "'All right, Producer Baek Seung-chan. Good work today.' Calling him a full producer by title for the very first time, she signs off with \"sugohaesseoyo, oneul\" — 'you worked hard today'."),
]

TRANSITION = "Now let's hear the whole phone call again from start to finish."
OUTRO = "From \"matseumnida\" for crisp confirmation to \"nongdamiya\" for a friendly tease and \"sugohaesseoyo\" at the end of a long shift, those lines carry real warmth. Until next time!"
CLOSING = ("actress", "다음에 봐요!")
