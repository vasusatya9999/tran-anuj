from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='.')

# Devanagari character mapping (rule-based transliteration)
devanagari_mapping = {
    "अ": "अ", "आ": "आ", "इ": "इ", "ई": "ई", "उ": "उ", "ऊ": "ऊ",
    "ऋ": "ऋ", "ए": "ए", "ऐ": "ऐ", "ओ": "ओ", "औ": "औ",
    "क": "क", "ख": "ख", "ग": "ग", "घ": "घ", "ङ": "ङ",
    "च": "च", "छ": "छ", "ज": "ज", "झ": "झ", "ञ": "ञ",
    "ट": "ट", "ठ": "ठ", "ड": "ड", "ढ": "ढ", "ण": "ण",
    "त": "त", "थ": "थ", "द": "द", "ध": "ध", "न": "न",
    "प": "प", "फ": "फ", "ब": "ब", "भ": "भ", "म": "म",
    "य": "य", "र": "र", "ल": "ल", "व": "व", "श": "श",
    "ष": "ष", "स": "स", "ह": "ह",
    "ा": "ा", "ि": "ि", "ी": "ी", "ु": "ु", "ू": "ू",
    "े": "े", "ै": "ै", "ो": "ो", "ौ": "ौ", "ं": "ं", "ः": "ः",
    "्": "्"
}

# Additional word-level mapping for exceptions
word_mapping = {
    "बोलत": "बोलता",
    "खावत": "खाता",
    "जावत": "जाता",
    # Add more word mappings here
}

# Transliteration function
def transliterate_chhattisgarhi_to_hindi(chhattisgarhi_word):
    # Check word-level mapping first
    if chhattisgarhi_word in word_mapping:
        return word_mapping[chhattisgarhi_word]
    
    # If no word-level mapping, proceed with character mapping
    hindi_word = ""
    for char in chhattisgarhi_word:
        hindi_word += devanagari_mapping.get(char, char)  # Default to same char if no mapping
    return hindi_word

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/transliterate", methods=["POST"])
def transliterate():
    # Get data from the POST request
    data = request.json
    chhattisgarhi_word = data.get("word", "")
    
    # Perform transliteration
    hindi_word = transliterate_chhattisgarhi_to_hindi(chhattisgarhi_word)
    
    # Return the transliterated word
    return jsonify({"hindi_word": hindi_word})

if __name__ == "__main__":
    app.run(debug=True)
