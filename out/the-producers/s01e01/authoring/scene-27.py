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
    ("baek_mom", "얘가 왜 사 자야?", "How does his job end in the syllable 'sa'?", [(1102, "얘가 왜 사자야?")], "Writes 사 자 ('the syllable 사') spaced clearly for the wordplay"),
    ("baek_dad", "프로듀... 사! 아니야?", "Produ-sa! Isn't it?", [(1103, "프로듀"), (1104, "사"), (1105, "아니야?")], ""),
]

OPENER = "Let's savour the eight lines of Episode One's family finale — including the show's title pun!"

WALK = [
    (0, None, "'Let's pray!' With candles flickering on the cake, Seung-chan's dad Bo-sun announces that it's time to pray, attaching the casual 'let's!' ending onto the word 'to pray' This means that."),
    (1, None, "'It's a public broadcaster, Father.' His dad Bo-sun keeps calling KBS state-run television, so Seung-chan gently corrects him with the term for 'public broadcasting' and a polite ending It is a handy word."),
    (2, None, "'Goodness, hurry up and pray, the candles are burning all the way down.' Jum-soon nudges her husband along to hurry up, pointing out that the candles are burning down using the words for 'candle' and 'to burn' This means that."),
    (3, None, "'It is a joyous occasion for our family.' In his grand prayer voice, Bo-sun declares it a joyous family occasion, combining the word for the whole household or clan with a term for a proud, celebratory milestone It comes from this."),
    (4, None, "'Your father feels truly wonderful.' Once the candles are blown out, he expresses warm contentment, pairing the word for 'mood' or 'feeling' with an expression meaning 'truly good' The word doubles the."),
    (5, None, "'Our son-in-law is a doctor, and now even you, Seung-chan!' Korean families prize professions ending in that prestigious scholarly title suffix, starting with 'doctor', which their son-in-law already holds This literally means that."),
    (6, None, "'How does his job end in the syllable 'sa'?' Jum-soon spots the flaw right away and asks how it qualifies: doctors, judges, and prosecutors all share that prestigious final syllable, whereas the Korean loanword for 'producer' normally ends in a different syllable! Swap in this word."),
    (7, None, "'Produ-sa! Isn't it?' Here is the joke behind the entire drama's Korean title! Bo-sun twists the pronunciation of 'producer' so his youngest son joins that prestigious club too, sealing it with a beaming 'isn't it?!' This literally means that."),
]

TRANSITION = "Now let's listen to the whole family celebration scene from start to finish."
OUTRO = "Now you even get the Korean pun inside The Producers! Congratulations on completing Episode One from first sprint to final candle. Until next time!"
CLOSING = ("seungchan", "안녕히 계세요!")
