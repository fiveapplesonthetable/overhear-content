# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 19
ID = 'die-discounter-s01e01-scene-19'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 19
TITLE = "Nicht vor achtzehn Uhr  (Not Before Six O'Clock)"
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'pina': 'Pina', 'kunde': 'Der Kunde'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = '18 Uhr spelled out as achtzehn Uhr; includes Pina\'s organic-egg limit remark and raw cue 631 open-checkout moment.'

INTRO = (
    "Pina tells the camera where she draws the line on Thorsten's shady cost-cutting tricks before opening another checkout lane. "
    "Her first shopper there is the friendly scooter rider, who rounds up his bill and quietly slips Pina his phone number — with one mysterious condition. "
    "Listen to the German conversation first."
)
OPENER = "Let's walk through Pina's limit, the classic German phrase for 'keep the change', and the twenty-four-hour clock."
TRANSITION = "Now let's listen to the whole checkout scene once more."
OUTRO = (
    "A phone number and 'not before six in the evening' — Pina's day just got a lot more interesting than Thorsten's! "
    "You now know how to say 'that's where I draw the line', tell a cashier or waiter to keep the change, invite someone to call, and tell time with the twenty-four-hour clock. "
    "Until next time!"
)
CLOSING = ('pina', 'Schönen Tag noch!')

STORY = [
    ('pina', 'Die Bioeier einfach austauschen, da ist auch bei mir Schluss!', "Just swapping out the organic eggs — that's where I draw the line too!", [(620, 'die Bioeier'), (625, 'also da ist auch bei mir'), (625, 'Schluss')], 'Simplify Bodenhaltungseiern compound while preserving the Bioeier joke.'),
    ('kunde', 'Hallo noch mal! Ist diese Kasse hier jetzt offen?', 'Hello again! Is this checkout here open now?', [], 'Restored from raw rolling cue 631 (ist drüben eine Kasse offen).'),
    ('pina', 'Ja, komm gerne rüber! Ich mache gerade auf.', "Yes, come on over! I'm just opening up.", [], 'Natural checkout welcome bridging cue 631.'),
    ('pina', 'Das macht dann neun Euro fünfzig, bitte.', 'That comes to nine euros fifty then, please.', [], 'Standard checkout total leading into cue 629/checkout tip.'),
    ('kunde', 'Hier sind zehn Euro. Stimmt so!', 'Here is ten euros. Keep the change!', [(629, 'Stimmt. So')], ''),
    ('pina', 'Oh, danke! Und was steht hier auf dem Zettel?', 'Oh, thanks! And what is written on this slip of paper?', [], 'Bridges the visual gag of the customer sliding his number across the belt.'),
    ('kunde', 'Das ist meine Nummer. Du kannst mich gerne mal anrufen.', 'That is my number. Feel free to give me a call sometime.', [(634, 'anrufen')], ''),
    ('kunde', 'Aber ruf bitte nicht vor achtzehn Uhr an!', "Only please don't call before six o'clock in the evening!", [(635, 'Nicht vor'), (635, 'Uhr')], 'Spell out 18 as achtzehn and frame with ruf ... an.')
]

WALK = [
    (0, None, "'Just swapping out the organic eggs — that's where I draw the line too!' Notice the prefix 'bio-' glued onto 'eggs' — that's the everyday word for 'organic' on German food labels. At the close, 'there is with me end!' is a vivid idiom for 'that's where it stops for me!'."),
    (2, None, "'Yes, come on over! I'm just opening up.' The short directional word meaning 'across here' or 'over here' is what you'll hear whenever a cashier waves shoppers over to a newly opened lane."),
    (3, None, "'That comes to nine euros fifty then, please.' At a till or cafe, German literally says 'that makes nine euros fifty' — using the everyday word for 'makes' just like in English when someone says 'that makes ten pounds'."),
    (4, None, "'Here is ten euros. Keep the change!' Those two crisp words — literally 'is-correct so!' — are the magic phrase across Germany whenever you hand over cash and want the cashier or server to keep the change."),
    (5, None, "'Oh, thanks! And what is written on this slip of paper?' Where English asks 'what is written on the note?', German asks 'what stands here on the slip?' — text on paper, signs, and screens always 'stands' there."),
    (6, None, "'That is my number. Feel free to give me a call sometime.' Pairing 'can' with 'gladly once' gives a handy phrase that turns 'you can call me' into a warm, low-pressure invitation."),
    (7, None, "'Only please don't call before six o'clock in the evening!' Unlike English, everyday spoken German uses the twenty-four-hour clock for appointments: eighteen 'clock' is six p.m., leaving zero doubt between morning and evening.")
]
