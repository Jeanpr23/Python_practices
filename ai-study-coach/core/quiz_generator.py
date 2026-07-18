from core.note_analyzer import extract_keywords
from core.note_analyzer import filter_keywords

def generate_questions(text, difficulty):

    keywords = extract_keywords(text)

    keywords = filter_keywords(keywords)

    questions = []

    sentences = text.split(".")

    for keyword in keywords:

        answer = "Found in your stufy notes"

        for sentence in sentences:

            if keyword.lower() in sentence.lower():

                answer = sentence.strip()

                break




        if difficulty == "Easy":

            question = f"What is {keyword}?"

        elif difficulty == "Medium":

            question = f"Explain {keyword}."

        else:

            question = f"How does {keyword} relate to the topic?"



        questions.append({
            "question": question,
            "answer": answer
        })
            
    return questions