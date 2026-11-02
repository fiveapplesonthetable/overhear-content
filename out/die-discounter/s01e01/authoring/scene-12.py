# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 12
ID = 'die-discounter-s01e01-scene-12'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 12
TITLE = 'Der Schlüssel im Wagen  (The Key in the Trolley)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'kunde': 'Der Kunde', 'pina': 'Pina'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = 'Colloquial omissions supplied (Er kennt sich..., was ich da machen soll) while preserving the warm, slightly flirty aisle exchange.'

INTRO = (
    "Out in the supermarket aisles, a friendly shopper flags Pina down with an everyday German shopping mishap: he used his house key to unlock a trolley, and now the key refuses to come back out. "
    "Pina points him toward veteran colleague Wilhelm and offers to grab a proper plastic token. "
    "Listen to the German conversation first."
)
OPENER = "Let's walk through how the customer explains his stuck key and how Pina points him to the right person."
TRANSITION = "Now let's hear the whole aisle conversation again."
OUTRO = (
    "Armed with Pina's tip to find Wilhelm, the grateful customer heads off to rescue his house key. "
    "You now have natural phrases for explaining a problem with something, saying an item won't come out, saying someone knows their stuff, and thanking someone warmly. "
    "See you next time!"
)
CLOSING = ('pina', 'Bis später!')

STORY = [
    ('kunde', 'Hallo! Ich habe hier ein Problem mit dem Wagen.', 'Hello! I have a problem with the trolley here.', [(370, 'Hallo'), (375, 'ich habe hier ein Problem mit dem Wagen')], ''),
    ('kunde', 'Mein Schlüssel geht da leider nicht mehr raus.', 'Unfortunately my key will not come out of there anymore.', [(375, 'Mein Schlüssel geht da nicht mehr raus')], ''),
    ('pina', 'Frag mal nach Wilhelm, ich glaube, das kommt öfter vor.', 'Ask for Wilhelm — I think that happens pretty often.', [(379, 'Frag mal nach'), (379, 'Wilhelm. Ich glaube, das kommt öfter vor')], ''),
    ('pina', 'Er kennt sich damit gut aus.', 'He really knows his way around that.', [(381, 'kennt sich damit'), (381, 'aus')], 'Supply dropped subject pronoun Er.'),
    ('pina', 'Ich weiß jetzt nicht, was ich da machen soll.', "I don't really know right now what I should do with it.", [(381, 'ich'), (383, 'jetzt nicht, was ich da')], 'Replace subjunctive wüsste and supply machen soll for clean A1 structure.'),
    ('pina', 'Es wäre ja schade wegen des Schlüssels.', 'It would be a shame about the key, after all.', [(383, 'wäre schade wegen des Schlüssels')], ''),
    ('kunde', 'Danke, das ist sehr lieb von dir!', 'Thanks, that is very sweet of you!', [(387, 'Danke. Lieb von dir')], ''),
    ('pina', 'Gerne! Ich hole dir noch schnell einen Chip.', "Gladly! I'll quickly grab a trolley token for you too.", [(389, 'Gerne')], 'Sets up Pina returning with the token in Scene 14.'),
    ('kunde', 'Danke schön!', 'Thank you very much!', [(391, 'Danke schön')], '')
]

WALK = [
    (0, None, "'Hello! I have a problem with the trolley here.' Saying 'I have a problem with...' works almost word for word like English. Notice that the everyday word for 'car' or 'wagon' is also what shoppers call a supermarket trolley."),
    (1, None, "'Unfortunately my key will not come out of there anymore.' Where English says a key 'won't come out', German literally says it 'goes not more out', pairing 'not anymore' right before the directional word 'out'."),
    (2, None, "'Ask for Wilhelm — I think that happens pretty often.' Asking for a person uses the preposition for 'after' — literally 'ask once after Wilhelm'. Then 'comes more often forward' is the natural German idiom for something happening fairly often."),
    (3, None, "'He really knows his way around that.' This handy expression builds on 'know' plus 'oneself' and 'out' at the end: whenever someone knows a topic, machine, or neighbourhood inside out, this is the phrase to reach for."),
    (4, None, "'I don't really know right now what I should do with it.' Notice Pina uses the word for knowing a fact rather than the word for knowing people that Titus used earlier, because she's talking about knowing what step to take."),
    (6, None, "'Thanks, that is very sweet of you!' Calling something 'sweet' or 'dear of you' sounds warm and appreciative among younger speakers, especially since the two of them immediately use the informal 'you'."),
    (7, None, "'Gladly! I'll quickly grab a trolley token for you too.' That single word for 'gladly' is the friendliest everyday answer to 'thank you' in Germany — light, upbeat, and reusable in every shop or cafe.")
]
