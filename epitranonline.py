import epitran

from flask import Flask, jsonify, g, request, render_template

app = Flask(__name__)

langs = [('aar-Latn', 'Afar'),
    ('amh-Ethi', 'Amharic'),
    ('ara-Arab', 'Literary Arabic'),
    ('aze-Cyrl', 'Azerbaijani (Cyrillic)'),
    ('aze-Latn', 'Azerbaijani (Latin)'),
    ('ben-Beng', 'Bengali'),
    ('ben-Beng-red', 'Bengali (reduced)'),
    ('cat-Latn', 'Catalan'),
    ('ceb-Latn', 'Cebuano'),
    ('cmn-Hans', 'Mandarin (Simplified)\\*'),
    ('cmn-Hant', 'Mandarin (Traditional)\\*'),
    ('ckb-Arab', 'Sorani'),
    ('deu-Latn', 'German'),
    ('deu-Latn-np', 'German†'),
    ('deu-Latn-nar', 'German (more phonetic)'),
    ('eng-Latn', 'English‡'),
    ('fas-Arab', 'Farsi (Perso-Arabic)'),
    ('fra-Latn', 'French'),
    ('fra-Latn-np', 'French†'),
    ('hau-Latn', 'Hausa'),
    ('hin-Deva', 'Hindi'),
    ('hun-Latn', 'Hungarian'),
    ('ilo-Latn', 'Ilocano'),
    ('ind-Latn', 'Indonesian'),
    ('ita-Latn', 'Italian'),
    ('jav-Latn', 'Javanese'),
    ('kaz-Cyrl', 'Kazakh (Cyrillic)'),
    ('kaz-Latn', 'Kazakh (Latin)'),
    ('kin-Latn', 'Kinyarwanda'),
    ('kir-Arab', 'Kyrgyz (Perso-Arabic)'),
    ('kir-Cyrl', 'Kyrgyz (Cyrillic)'),
    ('kir-Latn', 'Kyrgyz (Latin)'),
    ('kmr-Latn', 'Kurmanji'),
    ('lao-Laoo', 'Lao'),
    ('mar-Deva', 'Marathi'),
    ('mlt-Latn', 'Maltese'),
    ('mya-Mymr', 'Burmese'),
    ('msa-Latn', 'Malay'),
    ('nld-Latn', 'Dutch'),
    ('nya-Latn', 'Chichewa'),
    ('orm-Latn', 'Oromo'),
    ('pan-Guru', 'Punjabi (Eastern)'),
    ('pol-Latn', 'Polish'),
    ('por-Latn', 'Portuguese'),
    ('ron-Latn', 'Romanian'),
    ('rus-Cyrl', 'Russian'),
    ('sna-Latn', 'Shona'),
    ('som-Latn', 'Somali'),
    ('spa-Latn', 'Spanish'),
    ('swa-Latn', 'Swahili'),
    ('swe-Latn', 'Swedish'),
    ('tam-Taml', 'Tamil'),
    ('tel-Telu', 'Telugu'),
    ('tgk-Cyrl', 'Tajik'),
    ('tgl-Latn', 'Tagalog'),
    ('tha-Thai', 'Thai'),
    ('tir-Ethi', 'Tigrinya'),
    ('tuk-Cyrl', 'Turkmen (Cyrillic)'),
    ('tuk-Latn', 'Turkmen (Latin)'),
    ('tur-Latn', 'Turkish (Latin)'),
    ('ukr-Cyrl', 'Ukranian'),
    ('uig-Arab', 'Uyghur (Perso-Arabic)'),
    ('uzb-Cyrl', 'Uzbek (Cyrillic)'),
    ('uzb-Latn', 'Uzbek (Latin)'),
    ('vie-Latn', 'Vietnamese'),
    ('xho-Latn', 'Xhosa'),
    ('yor-Latn', 'Yoruba'),
    ('zul-Latn', 'Zulu')]

@app.route('/')
def index():
    return render_template('index.jinja2', langs=langs)

@app.route('/gettrans')
def gettrans():
    lang = request.args.get('lang', 'eng-Latn', type=str)
    textin = request.args.get('textin', '', type=str)
    epi = epitran.Epitran(lang, cedict_file='data/cedict_1_0_ts_utf-8_mdbg.txt')
    trans = ' '.join([epi.transliterate(w) for w in textin.split(' ')])
    return trans
