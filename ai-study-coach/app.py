import streamlit as st

from core.quiz_generator import generate_questions

from core.flashcard_generator import generate_flashcards

from data.study_data import study_session

from core.note_analyzer import extract_keywords

from core.note_analyzer import extract_nouns

from core.note_analyzer import extract_phrases



st.title("AI Study Coach")

st.write("Paste your study notes below and we will turn them into quizzes and flashcards.")


if st.button("Reset Quiz"):

    st.session_state.score = 0 

    st.session_state.answered_questions = []

    st.session_state.total_questions = 0

    study_session.clear()

    st.success("Quiz reset!")

# input box

user_notes = st.text_area("Your Notes", height=250)

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered_questions" not in st.session_state:
    st.session_state.answered_questions = []

if "total_questions" not in st.session_state:
    st.session_state.total_questions = 0



difficulty = st.selectbox(
    "Quiz Difficulty", 
    ["Easy", "Medium", "Hard"]
)


if st.button("Generate Quiz"):
    st.subheader("Quiz Time!")

    if user_notes:
        quiz_questions = generate_questions(

            user_notes,
            difficulty
        )

        study_session["notes"] = user_notes
        study_session["quizzes"] = quiz_questions

        st.session_state.total_questions = len(quiz_questions)


        for i, q in enumerate(quiz_questions):

            st.write(f"Q{i+1}: {q['question']}")

            user_answer = st.text_input(
                f"Your Answer for Question {i+1}",
                key=f"answer_{i}"
            )


            if st.button(
                f"Check Answer {i+1}",
                key=f"check_{i}"
            ):
                
                if i not in st.session_state.answered_questions:

                
                    if user_answer.strip().lower() in q["answer"].lower():

                        st.success("Correct!")

                        st.session_state.score += 1

                    else:

                        st.error("Not quite. Try again.")

                    st.session_state.answered_questions.append(i)

                else:


                    st.info("You already answered this question.")





            if st.button(
                f"Show Answer {i+1}",
                key=f"show_{i}"
            ):

                st.write("Correct Answer:")

                st.write(q["answer"])


            st.subheader("Quiz Progress")

            completed = len(st.session_state.answered_questions)

            st.write(
                f"Completed: {completed}/{st.session_state.total_questions}"
            )

            st.write(
                f"Score: {st.session_state.score}/{st.session_state.total_questions}"
            )




if st.button("Generate Flashcards"):

    if user_notes:

        flashcards = generate_flashcards(user_notes)

        study_session["notes"] = user_notes
        study_session["flashcards"] = flashcards



        st.subheader("Flashcards")

        for i, card in enumerate(flashcards):

            st.write(f"Card {i+1}")

            st.write("Front:", card["front"])

            st.write("Back:", card["back"])

            st.write("---")
    else:
        st.write("Please enter some notes first.")


st.subheader("Debug Data")

st.write(study_session)


if user_notes:
    st.subheader("Detected Nouns")

    nouns = extract_nouns(user_notes)

    st.write(nouns)


    st.subheader("Important Keywords")

    keywords = extract_keywords(user_notes)

    study_session["keywords"] = keywords

    st.write(keywords)

    st.subheader("Detected Phrases")

    phrases = extract_phrases(user_notes)

    study_session["phrases"] = phrases

    st.write(phrases)

    st.subheader("Study Statistics")

    word_count = len(user_notes.split())

    keyword_count = len(keywords)

    phrase_count = len(phrases)

    st.write("Words:", word_count)

    st.write("Keywords:", keyword_count)

    st.write("Phrases: ", phrase_count)
