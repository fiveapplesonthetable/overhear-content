ID = "dix-pour-cent-s04e04-scene-24"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 24
TITLE = "La musique dans la tête  (Music in the head)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"

VOICES = {
    "narrator": "sky",
    "lea": "lucie"
}

INTRO = (
    "The episode ends with a beautiful song playing over a montage. "
    "We hear a woman singing about not knowing where she is going. "
    "We'll hear it in French first, don't worry about catching every word."
)
OPENER = "Let's go back through it. A song begins."
TRANSITION = "Let's listen to the whole scene again."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around music in the head, and for the words meaning 'step' and 'city'. You'll catch them now. See you next time."

STORY = [
    ("lea", "Je marche dans la ville.", "I walk in the city.", [], ""),
    ("lea", "Il fait très nuit.", "It is very dark.", [], ""),
    ("lea", "Je suis un peu fatiguée.", "I am a little tired.", [], ""),
    ("lea", "Je regarde les étoiles.", "I look at the stars.", [], ""),
    ("lea", "Je ne sais pas où je vais.", "I don't know where I'm going.", [(1211, "Je ne sais pas où je vais")], ""),
    ("lea", "Je marche encore un peu.", "I walk a little more.", [], ""),
    ("lea", "J'écoute une mélodie.", "I listen to a melody.", [], ""),
    ("lea", "De la musique dans la tête.", "Music in my head.", [(1212, "De la musique dans la tête")], ""),
    ("lea", "La lune brille fort.", "The moon shines bright.", [], ""),
    ("lea", "Comme un diamant dans la nuit.", "Like a diamond in the night.", [(1212, "Comme un diamant dans la nuit")], ""),
    ("lea", "Le temps file très vite.", "Time flies very fast.", [], ""),
    ("lea", "Pendant que les jours passent.", "While the days come and go.", [(1213, "Pendant que les jours passent")], ""),
    ("lea", "La vie continue toujours.", "Life always goes on.", [], "")
]

WALK = [
    (0, None, "'I walk in the city.' She starts by singing about walking. The key noun here means 'step', anchored by its matching French article."),
    (1, None, "'It is very dark.' She describes the atmosphere of the evening. The key noun here means 'reality', anchored by its matching French article."),
    (2, None, "'I am a little tired.' She admits her exhaustion after a long day. The adjective meaning 'tired' takes its feminine form here to match the noun it describes."),
    (3, None, "'I look at the stars.' She gazes up at the sky above. Notice how 'to look' leads directly into the noun meaning 'star'."),
    (4, None, "'I don't know where I'm going.' She sings about feeling lost in life. The two-part French negation brackets the verb for 'to know' on both sides."),
    (5, None, "'I walk a little more.' She continues her journey through the streets. The key noun here means 'step', anchored by its matching French article."),
    (6, None, "'I listen to a melody.' A soft tune plays in the background. Notice how the short vowel drops before a vowel sound around 'listening ear', making the phrase flow smoothly as one unit."),
    (7, None, "'Music in my head.' She sings about the persistent melody. The key noun here means 'music', anchored by its matching French article."),
    (8, None, "'The moon shines bright.' She notices the bright light in the sky. Notice how 'to shine' leads directly into the noun meaning 'moon'."),
    (9, None, "'Like a diamond in the night.' She compares the light to a jewel. The key noun here means 'diamond', anchored by its matching French article."),
    (10, None, "'Time flies very fast.' She thinks about how quickly life moves. The verb meaning 'to hand over' pairs naturally with the noun for 'time' in everyday conversation."),
    (11, None, "'While the days come and go.' She watches the passing of time. Notice how 'to pass' leads directly into the noun meaning 'day'."),
    (12, None, "'Life always goes on.' She concludes with a hopeful thought. This conversational past tense combines a helper verb with the past participle for 'to continue'.")
]

LABELS = {
    "lea": "Chanteuse"
}

CLOSING = ("lea", "À la prochaine.")
