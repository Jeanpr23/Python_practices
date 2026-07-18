from core.note_analyzer import extract_keywords

def generate_flashcards(text):

    keywords = extract_keywords(text)

    flashcards = []

    sentences = text.split(".")

    for keyword in keywords:

        definition = "Found in your study notes"

        for sentence in sentences:

            if keyword.lower() in sentence.lower():

                definition = sentence.strip()

                break

        flashcards.append({
            "front": keyword,
            "back": definition
        })

    return flashcards