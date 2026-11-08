# Authoring module for linden-courtyard-hi-s01e05-scene-01.
ID = 'linden-courtyard-hi-s01e05-scene-01'
SHOW = 'linden-courtyard-hi'
SEASON = 1
EPISODE = 5
SCENE = 1
TITLE = 'Truth in the Courtyard  (आँगन में पूरा सच)'
LEVEL = 'A1 — शुरुआती स्तर'
PAIR = 'en-hi'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah', 'evelyn': 'Evelyn'}
INTRO = 'आँगन की सुबह की धूप में मिस एवेलिन और हैना के सामने खड़ा केलेब बताता है कि सोमवार की ट्रेन में सूटकेस कैसे बदल गया था और शाम को अपने बड़े भाई ओवेन को इसी गली में देखकर वह क्यों घबरा गया था। पहले पूरा दृश्य सुनिए।'
OPENER = 'अब आइए इस खुलासे के एक-एक वाक्य को आराम से समझते हैं।'
TRANSITION = 'आइए पूरा दृश्य एक बार फिर सामान्य गति से सुनते हैं।'
OUTRO = 'तो सफ़ेद काग़ज़ के पैकेट में रखी हर चीज़ केलेब के बड़े भाई ओवेन की है! अगले दृश्य में स्वागत डेस्क पर चलते हैं और सुनते हैं तीन साल की खामोशी की कहानी।'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('evelyn', 'Let me look at you properly, Caleb! You grew taller than the piano!', 'मुझे तुम्हें ढंग से देखने दो, केलेब! तुम तो पियानो से भी ज़्यादा लंबे हो गए हो!'),
    ('caleb', 'I cannot believe you are staying in the exact same guesthouse, Miss Evelyn.', 'मुझे यकीन नहीं हो रहा कि आप बिल्कुल इसी गेस्टहाउस में ठहरी हैं, मिस एवेलिन।'),
    ('hannah', 'Wait, so we rode the same train on Monday, and you took her suitcase?', 'रुकिए, तो सोमवार को हमने एक ही ट्रेन में सफ़र किया, और आप इनका सूटकेस ले गए?'),
    ('caleb', "By complete accident! At my cousin's apartment I opened it and saw sheet music and a red ribbon.", 'पूरी तरह अनजाने में! अपने चचेरे भाई के अपार्टमेंट पर जब मैंने इसे खोला तो संगीत के पन्ने और लाल रिबन दिखे।'),
    ('evelyn', 'Why did you leave my bag on the step at night and run away?', 'तुम रात को मेरा बैग चौखट पर छोड़कर भाग क्यों गए थे?'),
    ('caleb', 'Because when I walked here on Monday evening, I saw my older brother walking down this street!', 'क्योंकि जब मैं सोमवार शाम यहाँ पैदल आया, तो मैंने अपने बड़े भाई को इसी गली में जाते देखा!'),
    ('hannah', 'Your older brother lives here in Portland?', 'आपके बड़े भाई यहाँ पोर्टलैंड में रहते हैं?'),
    ('caleb', 'Yes. I panicked, rang your bell, and slipped the Friday note onto the handle.', 'हाँ। मैं घबरा गया, आपकी घंटी बजाई, और शुक्रवार वाली पर्ची हैंडल पर सरका दी।'),
    ('evelyn', 'Wait, and Wednesday night you checked in here under your real name?', 'ठहरो, और बुधवार रात तुमने अपने असली नाम से यहाँ चेक-इन किया?'),
    ('caleb', 'I needed a quiet place nearby before Friday, and honestly forgot you still had my bag!', 'मुझे शुक्रवार से पहले पास में एक शांत जगह चाहिए थी, और सच में भूल गया था कि मेरा बैग अब भी आपके पास है!'),
    ('hannah', 'Until you called us on Tuesday asking us not to open the white package!', 'जब तक आपने मंगलवार को हमें फ़ोन करके सफ़ेद पैकेट न खोलने की गुज़ारिश नहीं की!'),
    ('caleb', 'Everything in that white paper belongs to my brother Owen, not me.', 'उस सफ़ेद काग़ज़ के भीतर रखी हर चीज़ मेरे भाई ओवेन की है, मेरी नहीं।'),
]
WALK = [
    (0, None, ["'मुझे तुम्हें ढंग से देखने दो, केलेब! तुम तो पियानो से भी ज़्यादा लंबे हो गए हो!' स्नेह से भरकर किसी बड़े हो चुके बच्चे को निहारने में", (None, 'look at you properly'), 'और तुलना वाला', (None, 'grew taller than'), 'खूब आत्मीयता जगाते हैं।']),
    (1, None, ["'मुझे यकीन नहीं हो रहा कि आप बिल्कुल इसी गेस्टहाउस में ठहरी हैं, मिस एवेलिन।' अद्भुत संयोग पर सुखद अविश्वास प्रकट करता है", (None, 'I cannot believe'), 'और हूबहू समानता पर बल देता है', (None, 'the exact same guesthouse'), 'का ज़ोरदार मेल।']),
    (2, None, ["'रुकिए, तो सोमवार को हमने एक ही ट्रेन में सफ़र किया, और आप इनका सूटकेस ले गए?' घटनाओं की कड़ी जोड़कर पुष्टि माँगते समय", (None, 'we rode the same train on Monday'), 'दिन से पहले ऑन का नियम निभाता है।']),
    (3, None, ["'पूरी तरह अनजाने में! अपने चचेरे भाई के अपार्टमेंट पर जब मैंने इसे खोला तो संगीत के पन्ने और लाल रिबन दिखे।' कोई भूल बिना इरादे के हुई हो तो", (None, 'By complete accident'), 'पूरी सफ़ाई तीन शब्दों में दे देता है।']),
    (4, None, ["'तुम रात को मेरा बैग चौखट पर छोड़कर भाग क्यों गए थे?' एक ही भूतकाल सहायक क्रिया डिड से जुड़े दो काम", (None, 'leave my bag'), 'और उसके बाद आया', (None, 'run away'), 'दोनों मूल रूप में रहते हैं।']),
    (5, None, ["'क्योंकि जब मैं सोमवार शाम यहाँ पैदल आया, तो मैंने अपने बड़े भाई को इसी गली में जाते देखा!' किसी को चलते हुए देखने का जीवंत दृश्य", (None, 'saw my older brother walking'), 'में सी के बाद आई-एन-जी रूप से उभरता है।']),
    (6, None, ["'आपके बड़े भाई यहाँ पोर्टलैंड में रहते हैं?' बिना डज़ आगे लाए केवल प्रश्नवाचक लहजे से बना", (None, 'Your older brother lives here'), 'बातचीत में अचानक उठी हैरानी दिखाता है।']),
    (7, None, ["'हाँ। मैं घबरा गया, आपकी घंटी बजाई, और शुक्रवार वाली पर्ची हैंडल पर सरका दी।' तीन तेज़ क्रियाओं की शृंखला में अंतिम कड़ी", (None, 'slipped the Friday note onto the handle'), 'चुपके से पर्ची फँसाने की गति दिखाती है।']),
    (8, None, ["'ठहरो, और बुधवार रात तुमने अपने असली नाम से यहाँ चेक-इन किया?' रजिस्टर में दर्ज नाम बताने में पूर्वसर्ग अंडर से बना", (None, 'under your real name'), 'होटल और कानूनी काग़ज़ात का मानक रूप है।']),
    (9, None, ["'मुझे शुक्रवार से पहले पास में एक शांत जगह चाहिए थी, और सच में भूल गया था कि मेरा बैग अब भी आपके पास है!' ईमानदारी से अपनी भूल मानने में", (None, 'honestly forgot'), 'बिना किसी बनावट के सीधी बात कहता है।']),
    (10, None, ["'जब तक आपने मंगलवार को हमें फ़ोन करके सफ़ेद पैकेट न खोलने की गुज़ारिश नहीं की!' किसी काम से मना करने का विनम्र निवेदन", (None, 'asking us not to open'), 'में नॉट को टू से ठीक पहले रखता है।']),
    (11, None, ["'उस सफ़ेद काग़ज़ के भीतर रखी हर चीज़ मेरे भाई ओवेन की है, मेरी नहीं।' मालिकाना हक स्पष्ट करने वाली क्रिया", (None, 'belongs to my brother Owen'), 'हमेशा टू पूर्वसर्ग के साथ ही जुड़ती है।']),
]
