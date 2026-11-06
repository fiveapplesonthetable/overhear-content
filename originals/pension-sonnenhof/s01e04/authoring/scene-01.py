# Authoring module for pension-sonnenhof-s01e04-scene-01.
ID = 'pension-sonnenhof-s01e04-scene-01'
SHOW = 'pension-sonnenhof'
SEASON = 1
EPISODE = 4
SCENE = 1
TITLE = 'Viertel vor sieben  (Six Forty-Five)'
LEVEL = 'A1 — beginner'
PAIR = 'de-en'
LABELS = {'werner': 'Werner', 'klara': 'Klara'}
SOURCE_NAME = 'Overhear Original'
INTRO = 'It is six forty-five in the morning at the Pension Sonnenhof in Leipzig. While the guests still sleep upstairs, Werner sketches a quick street map on paper for Klara. Listen to the whole scene first.'
OPENER = "Now let's follow Werner's directions line by line."
TRANSITION = "Now let's listen to the whole conversation again."
OUTRO = 'Left at the gate, across the bridge, past the green pharmacy, and left into the square, Klara is off on her dawn mission. See you next time.'
CLOSING = ('klara', 'Bis später!')
STORY = [
    ('klara', 'Guten Morgen, Werner! Sind die Duschen oben wirklich schon kalt?', 'Good morning, Werner! Are the showers upstairs really cold already?'),
    ('werner', 'Kalt wie Flusswasser. Steck dieses kaputte Ventil in deine Manteltasche.', 'Cold as river water. Put this broken valve into your coat pocket.'),
    ('klara', 'Hab ich. Erklär mir jetzt den Weg zum Eisenladen.', 'Got it. Now explain to me the way to the hardware shop.'),
    ('werner', 'Geh vor dem Tor nach links und immer geradeaus bis zur Steinbrücke.', 'Turn left outside the gate and go straight ahead to the stone bridge.'),
    ('klara', 'Vor dem Tor links, geradeaus zur Brücke. Gehe ich über den Fluss?', 'Left outside the gate, straight to the bridge. Do I cross the river?'),
    ('werner', 'Ja, geh über die Brücke und dann rechts an der grünen Apotheke vorbei.', 'Yes, cross the bridge and then pass the green pharmacy on the right.'),
    ('klara', 'Über die Brücke, an der grünen Apotheke vorbei. Und danach?', 'Across the bridge, past the green pharmacy. And after that?'),
    ('werner', 'Bieg links auf den kleinen Platz ab. Such nach einer blauen Holztür.', 'Turn left into the small square. Look for a blue wooden door.'),
    ('klara', 'Hängt draußen ein großes Schild am Laden?', 'Is there a big sign hanging outside the shop?'),
    ('werner', 'Nur ein goldener Schlüssel über der Tür. Zeig dem Verkäufer das Ventil.', 'Only a golden key above the door. Show the clerk the valve.'),
    ('klara', 'Zwanzig Millimeter, Messing, Kesselventil, das sage ich mir unterwegs vor!', 'Twenty millimetres, brass, boiler valve, I will repeat that along the way!'),
    ('werner', 'Lauf schnell, Klara. Zimmer vier wacht um Viertel nach sieben auf!', 'Run fast, Klara. Room four wakes up at quarter past seven!'),
]
WALK = [
    (0, None, "'Good morning, Werner! Are the showers upstairs really cold already?' In German, a yes-or-no question simply moves 'are' to the very front ahead of 'the showers'."),
    (1, None, ["'Cold as river water. Put this broken valve into your coat pocket.' Two vivid everyday words here, starting with:", (None, 'kaputte'), 'Spoken German reaches for this word constantly whenever a machine or part is broken.']),
    (2, None, ["'Got it. Now explain to me the way to the hardware shop.' Listen to that brisk two-word confirmation:", (None, 'Hab ich.'), "Dropping the final vowel off 'have' and flipping 'have I' gives you a natural 'got it!'."]),
    (3, None, ["'Turn left outside the gate and go straight ahead to the stone bridge.' Essential walking direction:", (None, 'geradeaus'), "Built from 'straight' and 'out', it means 'straight ahead'."]),
    (4, None, "'Left outside the gate, straight to the bridge. Do I cross the river?' German says 'go I over the river' rather than using a separate word for 'cross'."),
    (5, None, ["'Yes, cross the bridge and then pass the green pharmacy on the right.' Notice how 'go past' wraps around the landmark:", (None, 'vorbei.'), "You name the green pharmacy in the middle and drop 'past' right at the close."]),
    (6, None, ["'Across the bridge, past the green pharmacy. And after that?' Handy one-word connector for step-by-step plans:", (None, 'danach?'), "Literally 'there-after', meaning 'after that'."]),
    (7, None, ["'Turn left into the small square. Look for a blue wooden door.' Notice how 'turn off' splits in two:", (None, 'Bieg'), "At the front sits 'bend', and 'off' waits at the end to complete 'turn off'."]),
    (8, None, "'Is there a big sign hanging outside the shop?' Again German pictures a sign specifically 'hanging' at the shop."),
    (9, None, "'Only a golden key above the door. Show the clerk the valve.' Notice 'to the clerk' comes before 'the valve', just like 'show the clerk this part' in English."),
    (10, None, ["'Twenty millimetres, brass, boiler valve, I will repeat that along the way!' Compound check:", (None, 'Kesselventil'), "Built from 'kettle' and 'valve', locking the exact spare part into one word."]),
    (11, None, ["'Run fast, Klara. Room four wakes up at quarter past seven!' Useful clock phrase beside 'half eight':", (None, 'Viertel nach sieben'), "Literally 'quarter after seven', meaning seven fifteen."]),
]
