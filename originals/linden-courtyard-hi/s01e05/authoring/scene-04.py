# Authoring module for linden-courtyard-hi-s01e05-scene-04.
ID = 'linden-courtyard-hi-s01e05-scene-04'
SHOW = 'linden-courtyard-hi'
SEASON = 1
EPISODE = 5
SCENE = 4
TITLE = 'Two Chairs Under the Tree  (पेड़ के नीचे दो कुर्सियाँ)'
LEVEL = 'A1 — शुरुआती स्तर'
PAIR = 'en-hi'
LABELS = {'tessa': 'Tessa', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'आँगन के लिंडन पेड़ के नीचे हैना, टेसा और ग्राहम एक शांत कोने में छोटी लकड़ी की मेज़, दो कुर्सियाँ और नीले प्याले सजा रहे हैं, जबकि ऊपर अटारी में घबराया केलेब बार-बार कमीज़ बदल रहा है! पहले पूरा दृश्य सुनिए।'
OPENER = 'आइए अब इस आत्मीय तैयारी के हर वाक्य को समझते हैं।'
TRANSITION = 'चलिए पूरा दृश्य एक बार फिर सामान्य प्रवाह में सुनते हैं।'
OUTRO = 'केक जाली पर ठंडा हो रहा है, कागज़ की कंदीलें चमक उठी हैं और अब हैना घबराए केलेब की मदद करने जा रही है। अगले दृश्य में मिलते हैं!'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('hannah', 'Let us put the small wooden table right here under the tree, away from the door.', 'चलो लकड़ी की छोटी मेज़ ठीक यहाँ पेड़ के नीचे रखते हैं, दरवाज़े से हटकर।'),
    ('graham', 'Good spot. Two solid chairs, facing the garden herbs instead of the lobby window.', 'अच्छी जगह है। दो मज़बूत कुर्सियाँ, लॉबी की खिड़की के बजाय बगीचे के पौधों की तरफ़ मुख किए हुए।'),
    ('tessa', 'Here is a clean white cloth and two blue teacups.', 'यह रहा एक साफ़ सफ़ेद मेज़पोश और दो नीले चाय के प्याले।'),
    ('hannah', 'Graham, are you polishing those hanging paper lanterns for noon?', 'ग्राहम, क्या तुम दोपहर बारह बजे की तैयारी में उन लटकती कागज़ की लालटेनों को चमका रहे हो?'),
    ('graham', 'The wire needed straightening anyway. Nothing sentimental about good maintenance.', 'तार को वैसे भी सीधा करने की ज़रूरत थी। अच्छी देखभाल में भावुकता जैसी कोई बात नहीं है।'),
    ('tessa', 'Oh, listen to Mister Maintenance! Yesterday you fixed the boiler, today you fix two brothers!', 'ओहो, मिस्टर मेंटेनेंस की सुनो! कल तुमने बॉयलर जोड़ा, आज दो भाइयों को जोड़ रहे हो!'),
    ('graham', 'I fix pipes and chairs. People have to fix their own words.', 'मैं पाइप और कुर्सियाँ ठीक करता हूँ। इंसानों को अपने शब्द खुद ठीक करने पड़ते हैं।'),
    ('hannah', 'What time does your watch say now, Graham?', 'ग्राहम, अभी तुम्हारी घड़ी में कितना बजा है?'),
    ('graham', 'Eleven twenty. Cake ready, Tessa?', 'ग्यारह बीस। केक तैयार है, टेसा?'),
    ('tessa', 'Cooling on the rack right now, golden crust and sweet lemon sugar!', 'अभी जाली पर ठंडा हो रहा है, सुनहरी परत और मीठी नींबू चीनी के साथ!'),
    ('hannah', 'Look upstairs at the attic window: Caleb has changed his shirt three times!', 'ऊपर अटारी की खिड़की पर देखो: केलेब तीन बार अपनी कमीज़ बदल चुका है!'),
    ('tessa', 'Go talk to him, Hannah, before he wears out the wooden floor!', 'जाओ उससे बात करो, हैना, इससे पहले कि वह चल-चलकर लकड़ी का फ़र्श घिस डाले!'),
]
WALK = [
    (0, None, ["'चलो लकड़ी की छोटी मेज़ ठीक यहाँ पेड़ के नीचे रखते हैं, दरवाज़े से हटकर।' भीड़ या आवाजाही से अलग कोना चुनने में", (None, 'away from the door'), 'दूरी और एकांत दोनों स्पष्ट कर देता है।']),
    (1, None, ["'अच्छी जगह है। दो मज़बूत कुर्सियाँ, लॉबी की खिड़की के बजाय बगीचे के पौधों की तरफ़ मुख किए हुए।' बैठने की दिशा समझाने वाला कृदंत शब्द", (None, 'facing the garden herbs'), 'बिना लंबा वाक्य बनाए सटीक कोण दिखाता है।']),
    (2, None, ["'यह रहा एक साफ़ सफ़ेद मेज़पोश और दो नीले चाय के प्याले।' मेज़ सजाते समय चीज़ें सामने रखते हुए", (None, 'Here is a clean white cloth'), 'पहली एकवचन संज्ञा के अनुसार इज़ चुनता है।']),
    (3, None, ["'ग्राहम, क्या तुम दोपहर बारह बजे की तैयारी में उन लटकती कागज़ की लालटेनों को चमका रहे हो?' ऊपर टँगी सजावट की पहचान कराता है", (None, 'those hanging paper lanterns'), 'जिसमें हैंगिंग विशेषण का काम कर रहा है।']),
    (4, None, ["'तार को वैसे भी सीधा करने की ज़रूरत थी। अच्छी देखभाल में भावुकता जैसी कोई बात नहीं है।' काम की ज़रूरत को निर्वैयक्तिक ढंग से कहने में", (None, 'The wire needed straightening'), 'नीड के बाद आई-एन-जी रूप का सुंदर उदाहरण है।']),
    (5, None, ["'ओहो, मिस्टर मेंटेनेंस की सुनो! कल तुमने बॉयलर जोड़ा, आज दो भाइयों को जोड़ रहे हो!' स्नेह भरी छेड़छाड़ में गढ़ा गया उपनाम", (None, 'listen to Mister Maintenance'), 'ग्राहम के नरम दिल पर मीठी मुस्कान ला देता है।']),
    (6, None, ["'मैं पाइप और कुर्सियाँ ठीक करता हूँ। इंसानों को अपने शब्द खुद ठीक करने पड़ते हैं।' जीवन की गहरी ज़िम्मेदारी बताने में अनिवार्यता सूचक", (None, 'have to fix their own words'), 'सादगी में बड़ा दर्शन पिरो देता है।']),
    (7, None, ["'ग्राहम, अभी तुम्हारी घड़ी में कितना बजा है?' किसी की घड़ी का समय पूछने का प्रामाणिक मुहावरा", (None, 'What time does your watch say'), 'घड़ी को बोलने वाले कर्ता जैसा मान लेता है।']),
    (8, None, ["'ग्यारह बीस। केक तैयार है, टेसा?' काम के बीच संक्षिप्त पूछताछ में सहायक क्रिया इज़ छोड़कर बोला गया", (None, 'Cake ready'), 'रसोई और कामकाजी संवाद की असली रफ़्तार पकड़ता है।']),
    (9, None, ["'अभी जाली पर ठंडा हो रहा है, सुनहरी परत और मीठी नींबू चीनी के साथ!' ओवन से निकले केक की प्रक्रिया को", (None, 'Cooling on the rack right now'), 'ताज़गी और खुशबू के साथ जीवंत कर देता है।']),
    (10, None, ["'ऊपर अटारी की खिड़की पर देखो: केलेब तीन बार अपनी कमीज़ बदल चुका है!' अब तक दोहराए जा चुके काम का नतीजा दिखाने में", (None, 'has changed his shirt three times'), 'पूर्ण वर्तमान काल का सटीक प्रयोग है।']),
    (11, None, ["'जाओ उससे बात करो, हैना, इससे पहले कि वह चल-चलकर लकड़ी का फ़र्श घिस डाले!' बेचैनी में टहलने पर विनोदी अतिशयोक्ति", (None, 'before he wears out the wooden floor'), 'हँसी के साथ फ़िक्र भी जताती है।']),
]
