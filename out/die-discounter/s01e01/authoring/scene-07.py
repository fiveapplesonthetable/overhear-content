# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 07
ID = 'die-discounter-s01e01-scene-07'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 7
TITLE = 'Geh heute in den Park  (Go to the Park Today)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'thorsten': 'Thorsten', 'camper': 'Der Mann'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = 'Crude dog/swearing remarks softened to clean workplace German; 40 € spelled out as vierzig Euro.'

INTRO = (
    "Remembering that he has been letting a man and his little dog Puffi camp in a back room of the supermarket, Thorsten rushes over before Sabine can spot them. "
    "He presses forty euros into the camper's hand and begs him to spend the day in the park instead. "
    "Listen to the German conversation first."
)
OPENER = "Let's unpack Thorsten's urgent favours and the everyday phrases for packing up and heading to the park."
TRANSITION = "Now let's hear the whole back-room exchange once more."
OUTRO = (
    "Puffi and his owner reluctantly pack their bags for the park while Thorsten tells the camera his conscience is completely clear. "
    "You now know how to ask for a favour, warn about big trouble, talk about packing things up, and say someone has just settled in. "
    "See you next time!"
)
CLOSING = ('camper', 'Bis später!')

STORY = [
    ('thorsten', 'Pass mal auf, komm bitte kurz mit.', 'Listen up, come with me for a second.', [(199, 'Pass mal auf'), (201, 'Komm mit')], ''),
    ('thorsten', 'Das geht so nicht! Der Hund kann hier nicht bleiben.', "This won't work like this! The dog cannot stay here.", [(203, 'Das geht so nicht. Der Hund kann'), (203, 'nicht')], 'Soften crude dog line into clean A1 German.'),
    ('thorsten', 'Sabine kommt gleich! Wie stehe ich denn dann da?', 'Sabine is coming any minute! How is that going to make me look?', [(207, 'kommt gleich. Wie stehe ich denn dann da')], 'Restore Sabine from auto-caption Der Bine.'),
    ('thorsten', 'Tu mir einen Gefallen und pack deine Sachen mal zusammen.', 'Do me a favour and pack your things up.', [(207, 'gefallen'), (209, 'Pack'), (211, 'mal zusammen')], 'Replace colloquial Krams with everyday Sachen.'),
    ('thorsten', 'Geh heute mal in den Park! Sonst gibt es großen Ärger.', 'Go to the park today! Otherwise there will be big trouble.', [(211, 'und geh'), (213, 'in Park heute. Es gibt'), (213, 'Ärger')], 'Restore standard in den Park and großen Ärger.'),
    ('thorsten', 'Hier sind vierzig Euro, mach das mal bitte im Park.', 'Here is forty euros — please do that in the park.', [(215, 'Mach das mal bitte im Park')], 'Spell out 40 € from cue 213 as vierzig Euro.'),
    ('camper', 'Komm her, Puffi! Wir packen alles ein.', 'Come here, Puffi! We are packing everything up.', [(217, 'Puffi'), (217, 'Pack ein')], 'Omit swear word from cue 217.'),
    ('camper', 'Ich habe mich hier gerade erst eingerichtet.', 'I only just got myself settled in here.', [(221, 'ich habe mich'), (221, 'gerade eingerichtet')], ''),
    ('thorsten', 'Ich habe da kein schlechtes Gewissen. Ist ja gut!', "I don't have a guilty conscience about it. Alright, alright!", [(223, 'Gewissen'), (229, 'ist ja gut')], 'Restore schlechtes from auto-caption truncation sches.')
]

WALK = [
    (0, None, "'Listen up, come with me for a second.' Both halves rely on split-apart action words: 'watch out' becomes 'listen up' when calling for attention, and 'come with' needs no extra 'me' at the end in German, unlike English."),
    (1, None, "'This won't work like this! The dog cannot stay here.' Literally the first sentence says 'that goes so not' — a short, punchy phrase you'll hear whenever someone puts a stop to a situation that isn't acceptable."),
    (2, None, "'Sabine is coming any minute! How is that going to make me look?' Word for word, Thorsten asks 'how do I stand there then?', an expressive idiom for how you come across in front of other people."),
    (3, None, "'Do me a favour and pack your things up.' Asking 'do to me a favour' works almost word for word like English. Then 'pack' teams up with 'together' at the end of the clause to mean gathering scattered belongings."),
    (4, None, "'Go to the park today! Otherwise there will be big trouble.' Notice 'in the park' uses the movement form for 'into' here, whereas the next line uses the contracted location form for 'inside the park'. At the close, German literally says 'it gives big trouble' where English says 'there will be big trouble'."),
    (7, None, "'I only just got myself settled in here.' The long word at the end is built from 'in' and 'arrange' or 'furnish': used with 'myself', it means setting up camp or making a space feel like home."),
    (8, None, "'I don't have a guilty conscience about it. Alright, alright!' Where English speaks of a guilty conscience, German literally says a 'bad conscience'. His closing three words — 'is indeed good!' — brush off complaints when a speaker wants the matter dropped.")
]
