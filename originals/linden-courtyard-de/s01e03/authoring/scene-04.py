# Authoring module for linden-courtyard-de-s01e03-scene-04.
ID = 'linden-courtyard-de-s01e03-scene-04'
SHOW = 'linden-courtyard-de'
SEASON = 1
EPISODE = 3
SCENE = 4
TITLE = 'In from the Rain  (Herein aus dem Regen)'
LEVEL = 'A1 — Anfänger'
PAIR = 'en-de'
LABELS = {'hannah': 'Hannah', 'caleb': 'Caleb', 'tessa': 'Tessa'}
INTRO = 'Unten in der Empfangshalle tritt Caleb, ein ruhiger Reisender Anfang dreißig, herein und schüttelt seinen nassen Regenschirm ab. Hannah empfängt ihn freundlich am Tresen, während Tessa schon mit einem trockenen Handtuch bereitsteht. Hören Sie zunächst die ganze Szene.'
OPENER = 'Sehen wir uns diese erste Begegnung mit Caleb nun Satz für Satz genauer an.'
TRANSITION = 'Hören wir uns das Gespräch an der Rezeption jetzt noch einmal flüssig von vorn bis hinten an.'
OUTRO = 'Ehrlichkeit, ein trockenes Handtuch und eine heiße Tasse Suppe haben die Lage wunderbar entspannt. In der nächsten Szene steigt Caleb mit nach oben und prüft das Dachstudio selbst. Bis gleich!'
CLOSING = ('caleb', 'See you soon!')
STORY = [('hannah', 'Good evening! Come inside out of the rain, sir.', 'Guten Abend! Kommen Sie herein aus dem Regen.'),
 ('caleb',
  'Good evening. Sorry for dripping water on your clean floor.',
  'Guten Abend. Entschuldigen Sie, dass ich Wasser auf Ihren sauberen Boden tropfe.'),
 ('hannah', 'Do not worry at all! You must be Caleb.', 'Machen Sie sich überhaupt keine Sorgen! Sie müssen Caleb sein.'),
 ('caleb', 'Yes, Caleb. I booked room seven by phone yesterday.', 'Ja, Caleb. Ich habe gestern telefonisch Zimmer sieben gebucht.'),
 ('tessa',
  'Here is a dry towel for your coat and a cup of hot soup, sir.',
  'Hier ist ein trockenes Handtuch für Ihren Mantel und eine Tasse heiße Suppe.'),
 ('caleb',
  'Hot soup? After that cold walk in the rain, that sounds wonderful.',
  'Heiße Suppe? Nach diesem kalten Bahnsteig klingt das wunderbar.'),
 ('hannah',
  'Sir, before we go upstairs, I owe you an honest apology.',
  'Bevor wir nach oben gehen, schulde ich Ihnen eine ehrliche Entschuldigung.'),
 ('caleb', 'Oh? Is there a problem with my booking?', 'Ach? Gibt es ein Problem mit meiner Buchung?'),
 ('hannah', 'We accidentally booked two guests into room seven tonight.', 'Wir haben für heute Nacht versehentlich zwei Gäste auf Zimmer sieben gebucht.'),
 ('caleb',
  'Ah... in this rain? Every hotel near the station looked full.',
  'Oje... bei diesem Regen? Jedes Hotel in Bahnhofsnähe sah ausgebucht aus.'),
 ('hannah',
  'Please do not worry! We prepared our quiet third floor attic study just for you.',
  'Bitte machen Sie sich keine Sorgen! Wir haben unser ruhiges Dachstudio im zweiten Stock extra für Sie hergerichtet.'),
 ('caleb', 'An attic study? May I see it first?', 'Ein Dachstudio? Darf ich es mir zuerst anschauen?')]
WALK = [(0,
  None,
  ["'Guten Abend! Kommen Sie herein aus dem Regen.' Zwei Richtungen ergänzen einander in",
   (None, 'inside out of the rain'),
   'nämlich ins Warme hinein und aus dem Schauer heraus.']),
 (1,
  None,
  ["'Guten Abend. Entschuldigen Sie, dass ich Wasser auf Ihren sauberen Boden tropfe.' Statt eines langen Nebensatzes knüpft",
   (None, 'Sorry for dripping'),
   'den Grund der Bitte um Verzeihung direkt mit der Verlaufsform an.']),
 (2,
  None,
  ["'Machen Sie sich überhaupt keine Sorgen! Sie müssen Caleb sein.' Ganz ans Ende einer Verneinung gehängt, verstärkt",
   (None, 'at all'),
   'die Beruhigung zu überhaupt nicht.']),
 (3,
  None,
  ["'Ja, Caleb. Ich habe gestern telefonisch Zimmer sieben gebucht.' Kommunikationswege wie Telefon oder Post stehen in festen Wendungen "
   'wie',
   (None, 'by phone'),
   'immer ohne Artikel.']),
 (4,
  None,
  ["'Hier ist ein trockenes Handtuch für Ihren Mantel und eine Tasse heiße Suppe.' Auch wenn zwei Dinge überreicht werden, richtet sich",
   (None, 'Here is a dry towel'),
   'natürlich nach dem zuerst genannten Handtuch.']),
 (5,
  None,
  ["'Heiße Suppe? Nach diesem kalten Bahnsteig klingt das wunderbar.' Positive Reaktionen auf einen Vorschlag drückt man im Alltag sehr "
   'oft mit',
   (None, 'that sounds wonderful'),
   'aus.']),
 (6,
  None,
  ["'Bevor wir nach oben gehen, schulde ich Ihnen eine ehrliche Entschuldigung.' Sowohl für Geldbeträge als auch im übertragenen Sinn "
   'bedeutet',
   (None, 'I owe you'),
   'ich schulde Ihnen.']),
 (7,
  None,
  ["'Ach? Gibt es ein Problem mit meiner Buchung?' Höflich und sachlich erkundigt sich ein Reisender mit der Frageformel",
   (None, 'Is there a problem'),
   'nach einer möglichen Schwierigkeit.']),
 (8,
  None,
  ["'Wir haben für heute Nacht versehentlich zwei Buchungen auf Zimmer sieben eingetragen.' Das Umstandswort",
   (None, 'accidentally'),
   'mildert das Missgeschick ab, und',
   (None, 'booked'),
  'bedeutet gebucht.']),
 (9,
  None,
  ["'Oje... bei diesem Regen? Jedes Hotel in Bahnhofsnähe sah ausgebucht aus.' Obwohl",
   (None, 'Every hotel'),
   'inhaltlich alle Häuser meint, steht das Hauptwort dahinter stets in der Einzahl.']),
 (10,
  None,
  ["'Bitte machen Sie sich keine Sorgen! Wir haben unser ruhiges Dachstudio im zweiten Stock extra für Sie hergerichtet.' Herzliche "
   'Wertschätzung vermittelt der Zusatz',
   (None, 'just for you'),
   'im Sinne von eigens für Sie.']),
 (11,
  None,
  ["'Ein Dachstudio? Darf ich es mir zuerst anschauen?' Besonders höfliche Bitten unter Erwachsenen leitet das Modalverb in",
   (None, 'May I see it'),
   'deutlich feiner ein als bloßes können.'])]
