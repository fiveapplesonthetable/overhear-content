# Authoring module for linden-courtyard-de-s01e06-scene-08.
ID = 'linden-courtyard-de-s01e06-scene-08'
SHOW = 'linden-courtyard-de'
SEASON = 1
EPISODE = 6
SCENE = 8
TITLE = 'Room Nine  (Zimmer neun)'
LEVEL = 'A1 — Anfänger'
PAIR = 'en-de'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah', 'arthur': 'Arthur'}
INTRO = 'Spät am Freitagabend liegt der Innenhof still da, während Hannah und Arthur den Empfang abschließen und Graham mit Klappstühlen und einer verstaubten Holztruhe aus dem hinteren Keller heraufsteigt. Hören Sie zuerst die ganze Szene.'
OPENER = 'Schauen wir uns dieses geheimnisvolle Staffelfinale nun Satz für Satz genau an.'
TRANSITION = 'Hören wir uns die allerletzte Szene der ersten Staffel jetzt noch einmal im Zusammenhang an.'
OUTRO = 'Ein neunter Messingschlüssel, eine Zedernholztruhe mit der Aufschrift Zimmer neun und ein Bauplan mit einer verborgenen Tür auf genau dieser Etage! Herzlichen Glückwunsch zum Abschluss der ersten Staffel im Gasthof Lindenhof — wir freuen uns auf Sie in Staffel zwei!'
CLOSING = ('graham', 'Until tomorrow!')
STORY = [('hannah',
  'Did you find the three folding chairs behind the boiler room, Graham?',
  'Hast du hinter dem Heizungsraum die drei Klappstühle gefunden, Graham?'),
 ('graham',
  'Found the chairs, and behind an old brick wall, I found this.',
  'Die Stühle habe ich gefunden, und hinter einer alten Ziegelmauer fand ich das hier.'),
 ('arthur',
  'A small cedar chest? I have never seen that box in fifteen years!',
  'Eine kleine Zedernholztruhe? Diesen Kasten habe ich in fünfzehn Jahren noch nie gesehen!'),
 ('hannah',
  'Brush the dust off the brass plate on top... wait, read that number!',
  'Wisch mal den Staub vom Messingschild oben drauf... Moment, lies diese Zahl!'),
 ('arthur',
  "Let me pull my glasses down from my forehead... 'Room Nine'?!",
  'Lass mich kurz meine Brille von der Stirn herunterziehen... "Zimmer neun"?!'),
 ('hannah',
  'Graham, look at the wooden key board behind us: one, two, three, four, five, six, seven, eight!',
  'Graham, schau aufs hölzerne Schlüsselbrett hinter uns: eins, zwei, drei, vier, fünf, sechs, sieben, acht!'),
 ('arthur',
  'This guesthouse has only ever had eight rooms! Where on earth is Room Nine?!',
  'Dieses Gästehaus hatte schon immer nur acht Zimmer! Wo um alles in der Welt ist Zimmer neun?!'),
 ('graham',
  'Listen when I tilt the box. Something metal just slid inside.',
  'Hört mal hin, wenn ich die Truhe kippe. Drinnen ist gerade etwas Metallisches verrutscht.'),
 ('hannah',
  'There is a tiny keyhole on the front latch, and look taped underneath: an old brass key!',
  'Vorn am Riegel sitzt ein winziges Schlüsselloch, und schaut mal unten angeklebt: ein alter Messingschlüssel!'),
 ('arthur',
  'A ninth brass key?! Do we open it tonight or wait until morning?!',
  'Ein neunter Messingschlüssel?! Machen wir sie noch heute Abend auf oder warten wir bis morgen früh?!'),
 ('graham',
  'Look at the folded blueprint sticking out of the hinge. There is a hidden door drawn on this floor!',
  'Schaut auf den gefalteten Bauplan, der aus dem Scharnier ragt. Auf dieser Etage ist eine verborgene Tür eingezeichnet!'),
 ('hannah',
  'Grab the flashlight, both of you. My second week starts right now!',
  'Schnappt euch die Taschenlampe, ihr beiden. Meine zweite Woche fängt genau jetzt an!')]
WALK = [(0,
  None,
  ["'Hast du hinter dem Heizungsraum die drei Klappstühle gefunden, Graham?' Zusammenklappbare Stühle für zusätzliche Gäste heißen "
   'anschaulich',
   (None, 'folding chairs'),
   'mit der Verlaufsform vor dem Nomen.']),
 (1,
  None,
  ["'Die Stühle habe ich gefunden, und hinter einer alten Ziegelmauer fand ich das hier.' In knapper Handwerkersprache spart sich",
   (None, 'Found the chairs'),
   'am Anfang das eigene Fürwort.']),
 (2,
  None,
  ["'Eine kleine Zedernholztruhe? Diesen Kasten habe ich in fünfzehn Jahren noch nie gesehen!' Erfahrungen bis zum heutigen Tag fasst",
   (None, 'I have never seen'),
   'zwingend in der vollendeten Gegenwart zusammen.']),
 (3,
  None,
  ["'Wisch mal den Staub vom Messingschild oben drauf... Moment, lies diese Zahl!' Staub von einer Oberfläche herunterstreifen beschreibt "
   'die Verbindung',
   (None, 'Brush the dust off'),
   'klar und bildhaft.']),
 (4,
  None,
  ['\'Lass mich kurz meine Brille von der Stirn herunterziehen... "Zimmer neun"?!\' Bewegung nach unten und weg von der Stirn bündelt',
   (None, 'pull my glasses down from'),
   'Schritt für Schritt.']),
 (5,
  None,
  ["'Graham, schau aufs hölzerne Schlüsselbrett hinter uns: eins, zwei, drei, vier, fünf, sechs, sieben, acht!' Im Rücken der Sprechenden "
   'liegt das Brett',
   (None, 'behind us'),
   'mit dem Fürwort im Objektfall.']),
 (6,
  None,
  ["'Dieses Gästehaus hatte schon immer nur acht Zimmer! Wo um alles in der Welt ist Zimmer neun?!' Fassungsloses Staunen legt die "
   'Verstärkung',
   (None, 'Where on earth'),
   'direkt hinter das Fragewort.']),
 (7,
  None,
  ["'Hört mal hin, wenn ich die Truhe kippe. Drinnen ist gerade etwas Metallisches verrutscht.' Auch hier tritt die Beschaffenheit in",
   (None, 'Something metal'),
   'hinter das unbestimmte Wort für etwas.']),
 (8,
  None,
  ["'Vorn am Riegel sitzt ein winziges Schlüsselloch, und schaut mal unten angeklebt: ein alter Messingschlüssel!' Zusammengeschrieben "
   'entspricht',
   (None, 'keyhole'),
   'Bestandteil für Bestandteil unserem deutschen Schlüsselloch.']),
 (9,
  None,
  ["'Ein neunter Messingschlüssel?! Machen wir sie noch heute Abend auf oder warten wir bis morgen früh?!' Achten Sie auf die "
   'Rechtschreibung der Ordnungszahl',
   (None, 'ninth'),
   'bei der das stumme Schluss-e von neun wegfällt.']),
 (10,
  None,
  ["'Schaut auf den gefalteten Bauplan, der aus dem Scharnier ragt. Auf dieser Etage ist eine verborgene Tür eingezeichnet!' Dass eine "
   'Ecke hervorsteht, macht',
   (None, 'sticking out of'),
   'unmittelbar sichtbar.']),
 (11,
  None,
  ["'Schnappt euch die Taschenlampe, ihr beiden. Meine zweite Woche fängt genau jetzt an!' Unmittelbaren Aufbruch ins nächste Abenteuer "
   'verkündet',
   (None, 'starts right now'),
   'in der einfachen Gegenwart.'])]
