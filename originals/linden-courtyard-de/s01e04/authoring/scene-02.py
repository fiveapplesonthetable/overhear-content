# Authoring module for linden-courtyard-de-s01e04-scene-02.
ID = 'linden-courtyard-de-s01e04-scene-02'
SHOW = 'linden-courtyard-de'
SEASON = 1
EPISODE = 4
SCENE = 2
TITLE = 'The Blue Door  (Die blaue Tür)'
LEVEL = 'A1 — Anfänger'
PAIR = 'en-de'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'Zehn Minuten später hat Hannah die Flussbrücke in Portland bereits hinter sich gelassen, doch hinter der Apotheke zweigen zwei kleine Straßen ab. Vom Steinbrunnen aus ruft sie Graham an. Hören wir zuerst in die Szene hinein.'
OPENER = 'Schauen wir uns dieses eilige Telefonat unterwegs nun Zeile für Zeile an.'
TRANSITION = 'Lassen Sie uns Hannahs Einkauf an der blauen Tür jetzt noch einmal ohne Unterbrechung hören.'
OUTRO = 'Zwei neue Messingventile in der Tasche, während im Gasthof schon die ersten Schritte auf der Treppe knarren! Gleich in der nächsten Szene müssen Tessa und Arthur beim Frühstück Zeit schinden.'
CLOSING = ('graham', 'Bye for now!')
STORY = [('hannah',
  'Graham, can you hear me? I just passed the green pharmacy!',
  'Graham, hörst du mich? Ich bin gerade an der grünen Apotheke vorbei!'),
 ('graham', 'Loud and clear. Are you standing by the little stone fountain?', 'Laut und deutlich. Stehst du am kleinen Steinbrunnen?'),
 ('hannah',
  'Yes! There are two small streets on the left. Which one do I take?',
  'Ja! Links gehen zwei kleine Gassen ab. Welche nehme ich?'),
 ('graham',
  'Take the second street, beside the flower stand, not the narrow alley.',
  'Nimm die zweite Straße neben dem Blumenstand, nicht die schmale Gasse.'),
 ('hannah',
  'Walking now... oh, I see the golden key sign and the blue door!',
  'Ich gehe schon weiter... ach, ich sehe das Schild mit dem goldenen Schlüssel und die blaue Tür!'),
 ('graham', 'Good! Is the shutter open?', 'Gut! Ist der Rollladen schon oben?'),
 ('hannah', 'The clerk is unlocking it right now! Stay on the phone one second.', 'Der Rezeptionist schließt ihn genau in diesem Moment auf! Bleib kurz am Apparat.'),
 ('graham',
  'Make sure the brass ring inside is twenty millimeters wide.',
  'Achte darauf, dass der Messingring innen zwanzig Millimeter breit ist.'),
 ('hannah',
  'He matched it against the old one. He has two left on the shelf!',
  'Er hat es direkt an das alte gehalten. Er hat noch zwei Stück im Regal!'),
 ('graham', 'Buy both! A spare valve saves next winter too.', 'Kauf beide! Ein Ersatzventil rettet uns auch den nächsten Winter.'),
 ('hannah',
  'Paid in cash! Keep your toolbox open, I am running back across the bridge!',
  'Bar bezahlt! Lass deinen Werkzeugkasten offen, ich renne schon zurück über die Brücke!'),
 ('graham',
  'Hurry, I just heard footsteps on the second floor stairs!',
  'Beeil dich, ich habe gerade Schritte auf der Treppe im ersten Stock gehört!')]
WALK = [(0,
  None,
  ["'Graham, hörst du mich? Ich bin gerade an der grünen Apotheke vorbei!' Bei Sinneswahrnehmungen am Telefon setzt das Englische gern das "
   'Modalverb in',
   (None, 'can you hear me'),
   'vor das Verb hören.']),
 (1,
  None,
  ["'Laut und deutlich. Stehst du am kleinen Steinbrunnen?' Beste Verbindungsqualität bestätigt die schwungvolle Zwillingsformel",
   (None, 'Loud and clear'),
   'Wort für Wort wie im Deutschen.']),
 (2,
  None,
  ["'Ja! Links gehen zwei kleine Gassen ab. Welche nehme ich?' Damit das Hauptwort Straße nicht wiederholt werden muss, springt in",
   (None, 'Which one'),
   'das kleine Ersatzwort ein.']),
 (3,
  None,
  ["'Nimm die zweite Straße neben dem Blumenstand, nicht die schmale Gasse.' Verkaufsstände unter freiem Himmel heißen im Amerikanischen",
   (None, 'flower stand'),
   'mit dem Wort für Stand am Ende.']),
 (4,
  None,
  ["'Ich gehe schon weiter... ach, ich sehe das Schild mit dem goldenen Schlüssel und die blaue Tür!' Sobald etwas ins Blickfeld rückt, "
   'meldet die einfache Form',
   (None, 'I see'),
   'den Treffer ohne Verlaufsform.']),
 (5,
  None,
  ["'Gut! Ist der Rollladen schon oben?' Sowohl Fensterläden aus Holz als auch metallene Ladenrollos nennt man",
   (None, 'shutter'),
   'vor dem Schaufenster.']),
 (6,
  None,
  ["'Er schließt ihn genau in diesem Moment auf! Bleib kurz am Apparat.' Wenn der Gesprächspartner nicht auflegen soll, bittet man am "
   'Handy mit',
   (None, 'Stay on the phone'),
   'um einen kurzen Moment Geduld.']),
 (7,
  None,
  ["'Achte darauf, dass der Messingring innen zwanzig Millimeter breit ist.' Maßangaben stellen im Englischen wie in",
   (None, 'twenty millimeters wide'),
   'erst Zahl und Einheit vor das Eigenschaftswort.']),
 (8,
  None,
  ["'Er hat es direkt an das alte gehalten. Er hat noch zwei Stück im Regal!' Übrig gebliebene Bestände im Geschäft drückt das "
   'nachgestellte Wort in',
   (None, 'two left'),
   'äußerst knapp aus.']),
 (9,
  None,
  ["'Kauf beide! Ein Ersatzventil rettet uns auch den nächsten Winter.' Sind genau zwei Exemplare gemeint, greift der Einkäufer mit",
   (None, 'Buy both'),
   'ohne Artikel nach beiden zugleich.']),
 (10,
  None,
  ["'Bar bezahlt! Lass deinen Werkzeugkasten offen, ich renne schon zurück über die Brücke!' Barzahlung an der Ladenkasse kennzeichnet "
   'immer die feste Präposition in',
   (None, 'in cash'),
   'anstelle von mit.']),
 (11,
  None,
  ["'Beeil dich, ich habe gerade Schritte auf der Treppe im ersten Stock gehört!' Ohne jedes rückbezügliche Fürwort treibt der einzelne "
   'Zuruf',
   (None, 'Hurry'),
   'zur höchsten Eile an.'])]
