# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 17
ID = 'die-discounter-s01e01-scene-17'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 17
TITLE = 'Laufen die Kameras  (Are the Cameras Running)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'beyza': 'Beyza', 'thorsten': 'Thorsten', 'pina': 'Pina'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = 'Auto-caption mishearings Eitona, kennen, Bisa, and förmig restored to Altona, klären, Beyza, and förmlich.'

INTRO = (
    "Unimpressed by Thorsten's apple-and-pear excuse, Beyza warns him straight out that he will be replaced if the store's security system doesn't stop the constant stock losses. "
    "Thorsten blames the lively Hamburg district of Altona, then hurriedly shoos Pina out of the room so he can ask Beyza what she is doing tonight. "
    "Listen to the German conversation first."
)
OPENER = "Let's unpack Beyza's warning, how to ask why something is happening, and how Thorsten clears the room."
TRANSITION = "Now let's listen to the whole office exchange once more."
OUTRO = (
    "Even with his job on the line, Thorsten cannot resist shooing Pina out to try his luck with Beyza. "
    "You now have natural phrases for asking 'do you realize...?', asking whether machines are running, asking what the reason is, and promising to sort something out later. "
    "Until next time!"
)
CLOSING = ('beyza', 'Auf Wiedersehen!')

STORY = [
    ('beyza', 'Ist dir klar, dass du ausgetauscht wirst, wenn das hier nicht läuft?', 'Do you realize you will be replaced if things do not work here?', [(533, 'Ist dir klar, dass du ausgetauscht wirst, wenn das hier nicht läuft')], ''),
    ('thorsten', 'Moment, wenn was genau nicht läuft?', 'Wait a second — if what exactly is not working?', [(535, 'Wenn was nicht läuft')], ''),
    ('beyza', 'Das Sicherheitssystem! Laufen die Kameras überhaupt?', 'The security system! Are the cameras even running?', [(539, 'Das Sicherheitssystem'), (541, 'laufen die Kameras')], ''),
    ('beyza', 'Woran liegt das, dass hier immer noch so viel Ware verloren geht?', 'Why is it that so much stock is still going missing here?', [(545, 'Woran liegt das, dass hier immer noch so viel Ware'), (547, 'verloren geht')], ''),
    ('thorsten', 'Jonas macht hier einen super Job! Aber das hier ist schließlich Altona.', 'Jonas does a great job here! After all, this is Altona.', [(549, 'Jonas macht hier'), (549, 'Job'), (551, 'schließlich')], 'Replace 1A with super and restore Hamburg district name Altona from Eitona.'),
    ('thorsten', 'Pina, kannst du uns bitte ganz kurz mal alleine lassen?', 'Pina, could you please leave us alone for just a quick moment?', [(567, 'Pina'), (573, 'ganz kurz noch mal alleine lassen, bitte')], ''),
    ('beyza', 'Also, ein paar Punkte hätte ich eigentlich noch.', 'Well, I actually still have a few points left.', [(577, 'Also'), (577, 'paar Punkte'), (579, 'hätte ich noch')], ''),
    ('thorsten', 'Das klären wir später! Pina, schreib das bitte auf.', "We'll sort that out later! Pina, please write that down.", [(581, 'wir dann später'), (583, 'schreib das auf bitte')], 'Restore klären from auto-caption mishearing kennen.'),
    ('thorsten', 'Sag mal Beyza, jetzt brauchen wir nicht mehr so förmlich zu sein. Was machst du heute Abend?', "Tell me, Beyza, we don't need to be so formal anymore. What are you doing tonight?", [(587, 'jetzt brauchen wir ja nicht mehr so'), (589, 'heute Abend')], 'Restore Beyza and förmlich from Bisa / förmig.')
]

WALK = [
    (0, None, "'Do you realize you will be replaced if things do not work here?' Literally Beyza opens with 'is to-you clear that...?', a sharp everyday way to ask 'do you realize...?'. At the end, 'runs' means 'works smoothly'."),
    (2, None, "'The security system! Are the cameras even running?' Look at the compound built from 'security' and 'system'. Then the same verb for 'running' asks whether the cameras are switched on, boosted by the final word meaning 'at all' or 'even'."),
    (3, None, "'Why is it that so much stock is still going missing here?' Word for word, the opening chunk asks 'where-on lies that?' — a super natural German way to ask what the underlying cause of a problem is. At the close, 'goes lost' means 'goes missing'."),
    (4, None, "'Jonas does a great job here! After all, this is Altona.' That key word for 'after all' lets a speaker justify something as obvious to anyone who knows the busy Hamburg neighbourhood of Altona."),
    (5, None, "'Pina, could you please leave us alone for just a quick moment?' Putting those three small words for 'quite briefly once' together softens a delicate request when asking a colleague to step out and 'leave us alone'."),
    (7, None, "'We'll sort that out later! Pina, please write that down.' The verb built from the word for 'clear' means 'to clear up' or 'sort out'. Then 'write' pairs with 'up' or 'on' at the end for 'write down'."),
    (8, None, "'Tell me, Beyza, we don't need to be so formal anymore. What are you doing tonight?' Notice how German expresses 'tonight' by joining 'today' and 'evening' — literally 'today evening' rather than a separate single word.")
]
