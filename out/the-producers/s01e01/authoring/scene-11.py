"""Scene 11 (incorporating merged transition Scene 10): Joon-mo faces the Broadcast Standards Commission."""
ID = "the-producers-s01e01-scene-11"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 11
TITLE = "식사 시간에 코딱지  (Boogers at Dinnertime)"
LEVEL = "A1 — beginner"
LABELS = {"joonmo": "라준모", "commissioner": "심의위원"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "Pushing his afternoon meeting back, Ra Joon-mo heads to the Broadcast Standards Commission, where a stern "
    "commissioner questions him for airing a crude word fifteen times during Sunday dinner. Listen for the word for "
    "'meeting', and the phrase for 'I reflect on my mistake'."
)

STORY = [
    ("joonmo", "회의 네 시에 하자니까, 방통위 간다고.", "Let's hold the meeting at four, I told you I'm going to the Commission.", [(302, "회의 4시 하자니까"), (304, "방통위 간다고")], "Folds in merged Scene 10 transition cue and spells 4시 in Hangul 네 시"),
    ("joonmo", "거기서 부르면 싫죠.", "Nobody likes being called in by them.", [(316, "근데 일단 뭐 거기서 부르면 싫죠")], "Trims spoken fillers 근데 일단 뭐"),
    ("commissioner", "오늘은 방송 중 비속어를 사용했네요.", "Today, vulgar language was used during the broadcast.", [(330, "아 오늘은"), (331, "방송 중 비속어를 사용했네요")], ""),
    ("commissioner", "어떤 단어였죠?", "Which word was it?", [(332, "어떤 단어였죠?")], ""),
    ("joonmo", "코딱지였습니다.", "It was 'booger'.", [(333, "코딱지였습니다")], ""),
    ("commissioner", "다른 품위 있는 말로 대체 가능하지 않았어요?", "Couldn't you have replaced it with a more dignified word?", [(339, "다른 품위 있는 말로 대처 가능하지 않았어요?")], "Restores standard 대체 ('replacement') from ASR near-homophone 대처"),
    ("commissioner", "시청자들이 식사하면서 보는데 밥맛이 좋겠어요?", "Viewers watch while eating a meal — would they have an appetite?", [(344, "시청자들이 식사하면서 보는데 밥맛이 좋겠어요?")], ""),
    ("joonmo", "반성합니다, 죄송합니다.", "I reflect deeply on it, I'm sorry.", [(342, "반성합니다"), (345, "죄송합니다.")], "Pairs Joon-mo's two rapid-fire hearing apologies"),
]

OPENER = "Let's step through the eight lines of Joon-mo's hearing."

WALK = [
    (0, None, "'Let's hold the meeting at four, I told you I'm going to the Commission.' Hurrying out of the office, Joon-mo pairs the word meaning 'meeting' with 'at four o'clock'. His emphatic ending reminds his team impatiently: 'I already told you let's do it then!'."),
    (1, None, "'Nobody likes being called in by them.' In his interview, 'to call' or 'summon' is paired with a polite tag meaning 'you dislike it, naturally'. Even veteran producers dread getting summoned here."),
    (2, None, "'Today, vulgar language was used during the broadcast.' Across the table, the commissioner uses the formal Korean term for crude slang alongside 'you used'. Placing the short word meaning 'during' right after 'broadcast' means 'in the middle of the broadcast'."),
    (3, None, "'Which word was it?' The question opens with a word asking 'which' or 'what kind of', right before 'was the word?'. Notice how that closing question ending asks Joon-mo to state for the record something they both already see in the file."),
    (4, None, "'It was \"booger\".' Forced to say a silly childhood word with a deadpan face, Joon-mo answers with the word for 'booger' — built from the word for 'nose' — plus the stiffest formal past ending. The contrast between baby talk and courtroom formality is pure comedy."),
    (5, None, "'Couldn't you have replaced it with a more dignified word?' The commissioner pairs the noun meaning 'dignity' or 'class' with 'speech' to mean 'dignified phrasing', then uses 'substitution' to ask why his editors left the joke untouched."),
    (6, None, "'Viewers watch while eating a meal — would they have an appetite?' The polite word for dining is used in a form meaning 'while having a meal'. Then the expression for 'appetite' literally joins 'cooked rice' and 'taste'!"),
    (7, None, "'I reflect deeply on it, I'm sorry.' Seasoned by too many hearings, Joon-mo folds instantly with the classic Korean public-apology expression meaning 'I reflect on my fault', before sealing it with a formal 'I am sorry'."),
]

TRANSITION = "Now let's hear the whole Commission hearing again from start to finish."
OUTRO = "From scheduling a meeting at four to saving someone's appetite at dinner and apologizing for your mistake, you survived the hearing room. Until next time!"
CLOSING = ("commissioner", "안녕히 가세요!")
