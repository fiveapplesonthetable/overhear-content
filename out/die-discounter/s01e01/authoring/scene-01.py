# Original-German source and honest shortened beginner adaptation, not English backtranslation.
ID = 'die-discounter-s01e01-scene-01'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 1
TITLE = 'Mein erster Tag  (First-Day Taster)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'titus': 'Titus'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende, Titus introduction excerpt'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = 'Native German automatic captions, retained intact. Original audio independently checked with unprompted cached-small CPU ASR; colloquial endings expanded and one first-day sentence recast below. This is a short adaptation, not an exact source transcript.'
INTRO = ('The Discounters is a German comedy set in a supermarket in Hamburg. On his first day at work, Titus tells the camera why he has come. This short taster simplifies his introduction for beginners. Listen to the German first; you do not need to catch every word.')
OPENER = "Let's unpack his introduction, his first day, and his reason for taking the job."
TRANSITION = 'Now listen to the entire short introduction once more.'
OUTRO = ('Titus is starting a job, with earning money firmly in mind. You have practised introducing yourself, describing a first day, saying that you do not know people yet, and explaining a purpose. See you next time!')
CLOSING = ('titus', 'Tschüss!')
STORY = [
 ('titus', 'Ja, ich bin Titus.', "Yes, I'm Titus.", [(73, 'Ja, ich bin Titus')], ''),
 ('titus', 'Heute ist mein erster Tag hier.', 'Today is my first day here.', [(73, 'Tag hier')], 'Original: Ich hab heute meinen ersten Tag hier. Recast as Today is my first day here; first-day meaning unchanged, nominative mein erster replaces accusative meinen ersten.'),
 ('titus', 'Die anderen kenne ich noch nicht so gut.', "I don't know the others very well yet.", [(75, 'kenne ich'), (77, 'noch nicht so gut')], 'Expand original colloquial kenn to kenne. Automatic caption incorrectly says Die ander; original-audio ASR independently recognizes Die anderen.'),
 ('titus', 'Aber ich bin nicht hier, um Freunde zu finden.', "But I'm not here to make friends.", [(79, 'aber ich bin'), (79, 'nicht hier, um'), (81, 'Freunde zu finden')], 'Omit the optional time word jetzt. The reason-for-being-here contrast remains.'),
 ('titus', 'Ich bin hier, um Geld zu verdienen.', "I'm here to earn money.", [(81, 'um Geld zu verdienen')], 'Omit ja, eigentlich and eher, the original conversational hedges. Retain the speaker and his actual earning-money purpose.')
]
# Complete replayed sentences, English teacher; German is always replayed by Titus's native voice.
WALK = [
 (0, None, "'Yes, I'm Titus.' This is a direct self-introduction. The two words before his name identify who he is. Keep that opening and replace the name with your own when introducing yourself. The first little word simply adds an affirmative yes; it is not part of his name."),
 (1, None, "'Today is my first day here.' German can put the time expression first. The verb still takes the second position, before the subject phrase. Notice the ending on the word for first: it belongs with the masculine noun for day. The possessive tells us whose first day this is."),
 (2, None, "'I don't know the others very well yet.' The opening points to the other employees. Knowing people means being familiar with them; knowing a fact would call for a different German word. The two words expressing not yet leave room for that familiarity to grow. His final two words soften the description: he does not know them all that well."),
 (3, None, "'But I'm not here to make friends.' The opening marks a contrast with what we might expect from someone starting a new job. After the comma, he names a purpose and immediately rejects it. Literally he says finding friends; natural English usually says making friends. The plural refers to friends in general, rather than one particular friend."),
 (4, None, "'I'm here to earn money.' Listen for the purpose construction again. Its opening word introduces his goal; the little marker just before the final action word completes it. The money comes between those two markers. Both parts concern the same person: Titus is here, and Titus intends to earn the money. This sentence gives the practical reason for his new job.")
]
