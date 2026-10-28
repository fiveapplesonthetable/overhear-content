# Authoring module for dix-pour-cent-s04e04-scene-24.
ID = 'dix-pour-cent-s04e04-scene-24'
SHOW = 'dix-pour-cent'
SEASON = 4
EPISODE = 4
SCENE = 24
TITLE = 'La musique dans la tête  (Music in the head)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'chanteuse': 'Chanteuse'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S04E04'
SOURCE_FILE = 'sources/dix-pour-cent/s04/e04.fr.dual.srt'
INTRO = "The episode ends with a beautiful song playing over a montage. We hear a woman singing about not knowing where she is going. We'll hear it in French first, don't worry about catching every word."
OPENER = "Let's go back through it. A song begins."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around music in the head, and for the words meaning 'step' and 'city'. You'll catch them now. See you next time!"
CLOSING = ('chanteuse', 'À la prochaine.')
STORY = [
    ('chanteuse', 'Je marche dans la ville.', 'I walk in the city.', [], ''),
    ('chanteuse', 'Il fait très nuit.', 'It is very dark.', [], ''),
    ('chanteuse', 'Je suis un peu fatiguée.', 'I am a little tired.', [], ''),
    ('chanteuse', 'Je regarde les étoiles.', 'I look at the stars.', [], ''),
    ('chanteuse', 'Je ne sais pas où je vais.', "I don't know where I'm going.", [(1211, 'Je ne sais pas où je vais')], ''),
    ('chanteuse', 'Je marche encore un peu.', 'I walk a little more.', [], ''),
    ('chanteuse', "J'écoute une mélodie.", 'I listen to a melody.', [], ''),
    ('chanteuse', 'De la musique dans la tête.', 'Music in my head.', [(1212, 'De la musique dans la tête')], ''),
    ('chanteuse', 'La lune brille fort.', 'The moon shines bright.', [], ''),
    ('chanteuse', 'Comme un diamant dans la nuit.', 'Like a diamond in the night.', [(1212, 'Comme un diamant dans la nuit')], ''),
    ('chanteuse', 'Le temps file très vite.', 'Time flies very fast.', [], ''),
    ('chanteuse', 'Pendant que les jours passent.', 'While the days come and go.', [(1213, 'Pendant que les jours passent')], ''),
    ('chanteuse', 'La vie continue toujours.', 'Life always goes on.', [], ''),
]
WALK = [
    (0, None, "'I walk in the city.' She starts by singing about walking."),
    (1, None, "'It is very dark.' She describes the atmosphere of the evening."),
    (2, None, "'I am a little tired.' She admits her exhaustion after a long day."),
    (3, None, "'I look at the stars.' She gazes up at the sky above."),
    (4, None, "'I don't know where I'm going.' She sings about feeling lost in life."),
    (5, None, "'I walk a little more.' She continues her journey through the streets."),
    (6, None, "'I listen to a melody.' A soft tune plays in the background."),
    (7, None, "'Music in my head.' She sings about the persistent melody."),
    (8, None, "'The moon shines bright.' She notices the bright light in the sky."),
    (9, None, "'Like a diamond in the night.' She compares the light to a jewel."),
    (10, None, "'Time flies very fast.' She thinks about how quickly life moves."),
    (11, None, "'While the days come and go.' She watches the passing of time."),
    (12, None, "'Life always goes on.' She concludes with a hopeful thought. Let's listen to the whole scene again."),
]
