"""Scene 27 (incorporating merged Scene 26): Seung-chan's family prays over a cake and celebrates prestigious '-sa' titles."""
ID = "the-producers-s01e01-scene-27"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 27
TITLE = "공영방송이에요, 아버지  (It's Public Broadcasting, Father)"
LEVEL = "A1 — beginner"
LABELS = {"baek_dad": "백보선", "baek_mom": "김점순", "seungchan": "백승찬"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "At the end of an exhausting first day, Baek Seung-chan comes home to a round celebration cake, where his proud "
    "father Bo-sun leads a rambling prayer and counts prestigious professional titles in the family. Listen for "
    "the phrase for 'public broadcasting' and the title joke behind the drama's name."
)

STORY = [
    ("baek_dad", "기도하자!", "Let's pray!", [(1052, "기도하자")], ""),
    ("seungchan", "공영방송이에요, 아버지.", "It's a public broadcaster, Father.", [(1056, "공영방송이에요 아버지")], ""),
    ("baek_mom", "아이고, 얼른 기도하세요, 초 다 타네.", "Goodness, hurry up and pray, the candles are burning all the way down.", [(1067, "아이고 얼른 기도하세요 초 다 타네")], ""),
    ("baek_dad", "집안의 경사입니다.", "It is a joyous occasion for our family.", [(1072, "집안의 경사입니다")], ""),
    ("baek_dad", "이 아버지는 기분이 참 좋다.", "Your father feels truly wonderful.", [(1096, "이 아버지는 기분이 참 좋다")], ""),
    ("baek_dad", "우리 사위는 의사고, 이제 승찬이 너까지!", "Our son-in-law is a doctor, and now even you, Seung-chan!", [(1097, "우리 사위는 의사고"), (1100, "이제 승찬이 너까지")], ""),
    ("baek_mom", "얘가 왜 사 자야?", "How does his job have that scholar ending?", [(1102, "얘가 왜 사자야?")], "Writes 사 자 ('the syllable 사') spaced clearly for the wordplay"),
    ("baek_dad", "프로듀... 사! 아니야?", "Producer! Isn't it?", [(1103, "프로듀"), (1104, "사"), (1105, "아니야?")], ""),
]

OPENER = "Let's savour the eight lines of Episode One's family finale — including the show's title pun!"

WALK = [
    (0, None, "'Let's pray!' With candles flickering on the cake, Seung-chan's dad Bo-sun announces that it is time to pray, attaching the casual 'let's!' ending onto the verb 'to pray'."),
    (1, None, "'It's a public broadcaster, Father.' Seung-chan gently corrects his dad with the compound term for 'public broadcasting' and a polite ending, since Bo-sun keeps calling KBS state-run television."),
    (2, None, "'Goodness, hurry up and pray, the candles are burning all the way down.' Jum-soon nudges her husband along with an everyday word meaning 'quickly' or 'right away', pointing out that the candles are burning down using 'candle' and 'to burn'."),
    (3, None, "'It is a joyous occasion for our family.' In his grand prayer voice, Bo-sun declares it a proud milestone, combining the word for the whole household with the traditional term for a joyful family celebration."),
    (4, None, "'Your father feels truly wonderful.' Once the candles are blown out, he expresses warm contentment, pairing the noun meaning 'mood' or 'feeling' with 'truly good'."),
    (5, None, "'Our son-in-law is a doctor, and now even you, Seung-chan!' Korean parents prize classic professions ending in a traditional scholar-title suffix — starting with the word for 'doctor', which their son-in-law already holds."),
    (6, None, "'How does his job have that scholar ending?' Jum-soon spots the flaw right away: in Korean, prestigious professions like doctor, judge, and prosecutor all share the same esteemed final syllable, whereas the loanword for 'producer' normally ends differently!"),
    (7, None, "'Producer! Isn't it?' Here is the wordplay behind the entire drama's Korean title, The Producers! Bo-sun stretches the final syllable of 'producer' to match that prestigious scholar ending so his youngest son joins the club too, sealing it with a beaming 'isn't it?'."),
]

TRANSITION = "Now let's listen to the whole family celebration scene from start to finish."
OUTRO = "Now you even get the Korean pun inside The Producers! Congratulations on completing Episode One from first sprint to final candle. Until next time!"
CLOSING = ("seungchan", "안녕히 계세요!")
