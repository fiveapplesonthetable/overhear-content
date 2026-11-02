"""Scene 23: Joon-mo buys hot gimbap and fish-cake soup for hungry Cindy, puzzling her in the van."""
ID = "the-producers-s01e01-scene-23"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 23
TITLE = "밥은 먹여가면서 굴리라고  (At Least Feed Her While She Works)"
LEVEL = "A1 — beginner"
LABELS = {"joonmo": "라준모", "manager": "매니저", "cindy": "신디"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "Outside KBS, Ra Joon-mo spots Cindy's road manager buying a tiny convenience-store diet snack for her dinner "
    "before a late show in Suwon, and marches him over to a hot street-food tent instead. Listen for the word for "
    "'dinner', and the polite phrase for 'please wrap it to go'."
)

STORY = [
    ("joonmo", "그게 저녁이야?", "Is that her dinner?", [(907, "그게 저녁이야?")], ""),
    ("manager", "열 시까지 수원 가야 되는데 지금 시간이 없어가지고.", "We have to get to Suwon by ten o'clock and we have no time right now.", [(910, "10시까지 수원 가야 되는데 지금 시간이 없어가지고")], "Spells 10시 in Hangul 열 시"),
    ("joonmo", "여기 멸치김밥하고 소고기김밥하고 어묵탕 하나 싸주세요.", "Please pack one anchovy gimbap, one beef gimbap, and one fish-cake soup to go.", [(914, "여기 멸치김밥하고 소고기김밥하고 어묵탕 하나 싸주세요")], ""),
    ("joonmo", "애를 굴리려면 밥은 먹여가면서 굴리라고.", "Tell him if he's going to work the kid ragged, at least feed her meals along the way.", [(918, "애를 굴리려면 밥은 먹여가면서 굴리라고")], ""),
    ("cindy", "장난해? 나 지금 탄수화물 안 먹는 거 몰라?", "Are you kidding me? Don't you know I'm not eating carbs right now?", [(924, "장난해?"), (925, "나 지금 탄수화물 안 먹는 거 몰라?")], ""),
    ("manager", "피디가 사주면서 들고 가라는 걸.", "A PD bought it for you and told me to bring it along.", [(929, "피디가 사주면서 들고 가라는 거")], ""),
    ("cindy", "누구라고? 내 팬이래?", "Who did you say? Did he say he's my fan?", [(930, "누구라고?"), (932, "내 팬이래?")], ""),
    ("manager", "아닐걸, 우리 대표님이랑 철천지원수라니까.", "Probably not, he and our agency boss are sworn enemies.", [(933, "아닐걸"), (934, "우리 대표님이랑 완전 철천지 왼수지 가니까")], "Restores standard idiom 철천지원수라니까 from ASR 철천지 왼수지 가니까"),
]

OPENER = "Let's savour the eight lines of Joon-mo's gruff kindness at the snack tent."

WALK = [
    (0, None, "'Is that her dinner?' Staring at a sad little diet pouch, Joon-mo asks if that is her dinner, using a word that means both 'evening' and the 'evening meal', just like 'dinner' The word doubles the."),
    (1, None, "'We have to get to Suwon by ten o'clock and we have no time right now.' Attach the 'by' word directly after a time to say 'by ten o'clock'. Then comes every busy worker's go-to excuse: 'because there's no time' This means that."),
    (2, None, "'Please pack one anchovy gimbap, one beef gimbap, and one fish-cake soup to go.' At any Korean snack stall, chain items together using the 'and' connector: anchovy seaweed rolls, beef rolls, and hot fish-cake soup. Finish with the polite request literally meaning 'wrap it up please' to order takeout! Swap in this word."),
    (3, None, "'Tell him if he's going to work the kid ragged, at least feed her meals along the way.' Gruff outside, soft inside: Joon-mo builds on the word 'to feed someone' to insist her agency boss at least keep her fed while running her from stage to stage It comes from this."),
    (4, None, "'Are you kidding me? Don't you know I'm not eating carbs right now?' Inside the van, Cindy opens with a casual 'are you joking?!', derived from the word for a prank. Then she mentions 'carbohydrates', followed by 'don't you know I don't eat them?' This literally means that."),
    (5, None, "'A PD bought it for you and told me to bring it along.' The manager pairs the word 'buy' with 'give as a kindness', followed by a compound word meaning 'carry it with you' This means that."),
    (6, None, "'Who did you say? Did he say he's my fan?' Intrigued despite herself, Cindy asks 'who did you say?' and tacks a reported-speech question ending onto 'fan' to ask 'did he say he is my fan?' Swap in this word."),
    (7, None, "'Probably not, he and our agency boss are sworn enemies.' He opens with a handy casual guess meaning 'probably not!', then uses a dramatic four-character idiom for bitter, sworn enemies — making the warm takeout bag even more mysterious to Cindy Notice the word for."),
]

TRANSITION = "Now let's listen to the whole street-stall and van scene again."
OUTRO = "You learned the word for dinner, the takeout favorite meaning 'please wrap it to go', the casual expression for 'are you kidding?', and a handy way to guess 'probably not!'. Next, back to the dark KBS parking lot!"
CLOSING = ("cindy", "다음에 만나요!")
