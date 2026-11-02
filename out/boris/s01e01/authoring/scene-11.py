# Authoring module for boris-s01e01-scene-11.
ID = 'boris-s01e01-scene-11'
SHOW = 'boris'
SEASON = 1
EPISODE = 1
SCENE = 11
TITLE = 'Scambiato per il giornalista  (Mistaken for the Journalist)'
LEVEL = 'A1 — beginner'
PAIR = 'it-en'
LABELS = {'corinna': 'Corinna', 'alessandro': 'Alessandro', 'arianna': 'Arianna'}
SOURCE_NAME = 'Boris S01E01'
SOURCE_FILE = 'sources/boris/s01/e01.it.srt'
INTRO = (
    'Hoping for glowing press coverage, Corinna walks up to Alessandro with notebook in hand and mistakes the intern for Repubblica journalist Antonio Di Pollina. '
    'Before Alessandro can explain, she dictates her berry-scented shower routine and invites him to a beach calendar shoot — right as Rene secretly orders Arianna to throw the intern out. '
    'Listen to the Italian scene first without trying to catch every word.'
)
OPENER = (
    "Let's walk through Corinna's accidental interview and Alessandro's sudden ejection."
)
TRANSITION = 'Now hear the whole mistaken-identity interview again from start to finish.'
OUTRO = (
    'You have heard "di solito" for "usually", "diamoci del tu" for switching to first-name terms, '
    'and Arianna\'s blunt "fuori!" when throwing Alessandro off the set. See you next time.'
)
CLOSING = ('corinna', 'A domani!')
STORY = [
    ('corinna', 'Ciao. Scusami per prima, non so che mi è successo.', 'Hi. Forgive me for earlier, I do not know what came over me.', [(351, 'Ciao'), (353, 'Scusami per prima'), (353, 'so che mi è successo')], ''),
    ('corinna', 'Io di solito sono una ragazza normalissima.', 'Usually I am a completely normal girl.', [(354, 'Io di solito sono una ragazza normalissima')], ''),
    ('corinna', 'Sei Di Pollina?', 'Are you Di Pollina?', [(355, 'Sei di Pollina')], 'Capitalised surname "Di Pollina".'),
    ('alessandro', 'Se vuoi.', 'If you like.', [(356, 'Se vuoi')], ''),
    ('corinna', 'Allora diamoci del tu.', 'Then let us use the informal you.', [(357, 'Allora diamoci del')], 'Whisper heard "del tuo"; restored to Italian idiom "del tu".'),
    ('corinna', 'Quando torno dal lavoro mi faccio sempre la doccia.', 'When I come back from work I always take a shower.', [(359, 'quando torno dal lavoro mi faccio'), (359, 'sempre la doccia')], ''),
    ('corinna', 'Con una spugna viola e un bagnoschiuma profumato.', 'With a purple sponge and a scented bubble bath.', [(360, 'con una spugna'), (360, 'viola, e un bagnoschiuma profumato')], ''),
    ('corinna', 'Che fai, non lo scrivi?', 'What are you doing, are you not writing it down?', [(362, 'Che fai, non lo scrivi')], ''),
    ('corinna', 'Lampone, fragola, mirtillo, mandarino.', 'Raspberry, strawberry, blueberry, tangerine.', [(364, 'Lampone, fragola, mirtillo, mandarino')], ''),
    ('alessandro', 'Ah, lo devo scrivere?', 'Oh, do I have to write it down?', [(365, 'Ah, lo devo scrivere')], ''),
    ('corinna', 'Domenica faccio un calendario. Se ti va, vieni. Ti regalo una foto.', 'On Sunday I am shooting a calendar. If you fancy it, come along. I will give you a photo.', [(372, 'domenica faccio un calendario'), (376, 'se ti va vieni'), (379, 'ti regalo una foto')], ''),
    ('alessandro', 'Sì, sto scrivendo.', 'Yes, I am writing.', [(395, 'sto scrivendo')], ''),
    ('arianna', 'Scusa Corinna, siamo pronti a girare.', 'Excuse me Corinna, we are ready to shoot.', [(397, 'Scusa Corinna, siamo pronti a girare')], ''),
    ('arianna', 'Che hai combinato? Fuori!', 'What mischief did you pull? Out!', [(402, 'hai combinato'), (404, 'Fuori')], ''),
    ('arianna', 'Ciliegia e mandarino?', 'Cherry and tangerine?', [(408, 'Ciliegia e mandarino')], ''),
]
WALK = [
    (0, None, [
        '\'Hi. Forgive me for earlier, I do not know what came over me.\' "Che mi e successo" literally asks "what happened to me", a smooth way to brush off a tantrum.'
    ]),
    (1, None, [
        '\'Usually I am a completely normal girl.\' "Di solito" is the everyday chunk for "usually", and "normalissima" piles on "-issima" again for "super normal".'
    ]),
    (2, None, [
        "'Are you Di Pollina?' Thinking Alessandro is the feared newspaper reporter, Corinna turns on maximum charm."
    ]),
    (3, None, [
        '\'If you like.\' Fresh from being renamed Seppia by Stanis, Alessandro shrugs with "se vuoi" — "if you want" — assuming it is another studio nickname.'
    ]),
    (4, None, [
        '\'Then let us use the informal you.\' "Diamoci del tu" is the classic social bridge when two adults agree to drop formal "lei" and speak as equals.'
    ]),
    (5, None, [
        '\'When I come back from work I always take a shower.\' Where English "takes" a shower, Italian "makes" one for yourself: "farsi la doccia".'
    ]),
    (6, None, [
        '\'With a purple sponge and a scented bubble bath.\' Notice "bagnoschiuma" glues "bagno", bath, and "schiuma", foam, into one compound word, while colour "viola" never changes its ending.'
    ]),
    (7, None, [
        '\'What are you doing, are you not writing it down?\' Opening with "che fai" — literally "what are you doing?" — nudges someone when they miss their cue.'
    ]),
    (8, None, [
        "'Raspberry, strawberry, blueberry, tangerine.' Four fruit flavours in a row, dictated solemnly as if they were breaking front-page news."
    ]),
    (9, None, [
        "'Oh, do I have to write it down?' Still thinking this is an odd assistant duty, Alessandro dutifully opens his pad."
    ]),
    (10, None, [
        '\'On Sunday I am shooting a calendar. If you fancy it, come along. I will give you a photo.\' "Regalare" means giving something as a gift, warmer and more generous than plain "dare".'
    ]),
    (11, None, [
        '\'Yes, I am writing.\' Just like "stiamo risolvendo" in the previous scene, "sto scrivendo" captures the pen moving right now.'
    ]),
    (12, None, [
        '\'Excuse me Corinna, we are ready to shoot.\' "Siamo pronti a" means "we are ready to", with "pronti" in the plural to cover the whole crew.'
    ]),
    (13, None, [
        '\'What mischief did you pull? Out!\' "Combinare" literally means combining things, and in everyday speech "che hai combinato?" asks "what mess have you gotten into now?"'
    ]),
    (14, None, [
        '\'Cherry and tangerine?\' Looking down at the notepad Alessandro left behind, Arianna reads his fruit-salad notes — where he even misremembered "lampone" as "ciliegia", cherry.'
    ]),
]

