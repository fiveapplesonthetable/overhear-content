# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 16
ID = 'die-discounter-s01e01-scene-16'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 16
TITLE = 'Wo kommt das Geld her  (Where Does the Money Come From)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'thorsten': 'Thorsten', 'beyza': 'Beyza', 'pina': 'Pina'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = 'Captures Thorsten rehearsing his dinner invite aloud before Pina walks in with Moin!, plus the 15,000-euro Kernobst excuse (vulgarity in cue 523 softened).'

INTRO = (
    "Alone for a moment, Thorsten practises asking Beyza out to dinner — playing both sides of the conversation himself — right before Pina walks into the office with a breezy Hamburg greeting. "
    "Pina immediately spots a mysterious fifteen-thousand-euro surplus from last month, and Thorsten wildly claims it all came from selling summer apples and pears. "
    "Listen to the German scene first."
)
OPENER = "Let's unpack Thorsten's rehearsed dinner invite, Hamburg's favourite greeting, and the mystery of the extra fifteen thousand euros."
TRANSITION = "Now let's hear the whole three-way office scene again."
OUTRO = (
    "Now we know why those fifteen thousand euros never went into working cameras — Thorsten used the camera budget to plug last month's losses and blamed 'pome fruit in June'! "
    "You have heard how to invite someone out to eat, greet people in Hamburg, say someone knows what's going on, and ask where something comes from. "
    "See you next time!"
)
CLOSING = ('pina', 'Bis später!')

STORY = [
    ('thorsten', 'Sag mal, hast du Lust, heute mit mir essen zu gehen?', 'Tell me, do you feel like going out to eat with me today?', [(489, 'Hast du Lust mit mir essen zu gehen')], ''),
    ('thorsten', 'Deswegen frage ich dich ja heute! Und natürlich sagst du ja.', "That's why I'm asking you today! And of course you say yes.", [(495, 'deswegen frage ich dich ja heute'), (499, 'natürlich')], 'Thorsten rehearsing Beyza\'s imagined answer to himself.'),
    ('pina', 'Moin! Wie kann ich euch helfen? Was gibt es?', "Morning! How can I help you two? What's up?", [(501, 'moin'), (507, 'wie kann ich euch helfen'), (509, 'Was gibt')], 'Expand Was gibt\'s to Was gibt es for clean tokenization.'),
    ('beyza', 'Die Zahlen sehen nicht gut aus, und er weiß nicht Bescheid.', "The numbers don't look good, and he doesn't know the details.", [(511, 'Die Zahlen sehen nicht'), (511, 'gut aus'), (513, 'er weiß nicht Bescheid')], ''),
    ('thorsten', 'Quatsch, das stimmt nicht, ich weiß doch Bescheid!', "Nonsense, that's not true, of course I know what's going on!", [(515, 'Quatsch'), (517, 'Das stimmt'), (519, 'ich weiß Bescheid')], ''),
    ('pina', 'Diese fünfzehntausend Euro Plus vom letzten Monat, wo kommen die her?', 'That fifteen-thousand-euro surplus from last month — where did that come from?', [(521, 'vom letzten Monat, wo kommen die her')], 'Spell out 15 000 € as fünfzehntausend Euro.'),
    ('pina', 'Das Geld hat dich gerettet! Ohne das Geld wäre schon alles aus.', 'That money saved you! Without that money it would all be over already.', [(523, 'gerettet'), (525, 'Ohne'), (525, 'wäre schon'), (525, 'alles aus')], 'Soften dir den Arsch gerettet to hat dich gerettet.'),
    ('thorsten', 'Ja, wegen dem Kernobst! Im Sommer läuft Kernobst super, gerade im Juni.', "Yes, because of the pome fruit! In summer pome fruit sells great, especially in June.", [(527, 'Ja, wegen'), (527, 'Kernobst. Im Sommer'), (529, 'Kernobst gerade Juni')], 'Colloquial spoken wegen + dative dem Kernobst retained authentically.')
]

WALK = [
    (0, None, "'Tell me, do you feel like going out to eat with me today?' Literally, asking 'do you have desire...?' is the friendly, reusable way to invite someone to dinner, coffee, or a film."),
    (2, None, "'Morning! How can I help you two? What's up?' That famous one-syllable word is the signature greeting of Hamburg and Northern Germany — you'll hear locals say it morning, afternoon, and night!"),
    (3, None, "'The numbers don't look good, and he doesn't know the details.' Literally, 'knowing notice' or 'knowing information' is a super handy two-word idiom meaning 'to be in the loop' or 'know the score'."),
    (4, None, "'Nonsense, that's not true, of course I know what's going on!' That lively word for 'nonsense' or 'rubbish' is classic casual pushback among coworkers, followed by a handy phrase meaning 'that isn't right'."),
    (5, None, "'That fifteen-thousand-euro surplus from last month — where did that come from?' Watch how German splits 'where from?' across the question: 'where' opens the clause while the little word for 'from' lands right at the end."),
    (6, None, "'That money saved you! Without that money it would all be over already.' At the close, 'all out' — like a light switched off — is a vivid everyday expression meaning 'all over' or 'finished'."),
    (7, None, "'Yes, because of the pome fruit! In summer pome fruit sells great, especially in June.' Notice how spoken German constantly pairs 'because of' with 'the' in its everyday spoken form, and uses the verb for 'runs' to mean 'sells briskly'.")
]
