import streamlit as st

import random

import time

from streamlit_autorefresh import st_autorefresh

def generate_problem():
    max_number = st.session_state.level * 10

    st.session_state.num1 = random.randint(1, max_number)
    st.session_state.num2 = random.randint(1, max_number)


    st.session_state.start_time = time.time()

    st.session_state.time_limit = get_time_limit()

    st.session_state.operation = st.session_state.mode

def get_time_limit():
    if st.session_state.level <= 2:
        return 4 
    
    elif st.session_state.level <= 5:
        return 5
    
    else:

        return 6
    


if "score" not in st.session_state:
    st.session_state.score = 0

if "level" not in st.session_state:
    st.session_state.level = 1

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

if "time_used" not in st.session_state:
    st.session_state.time_used = 0

if "wrong_time" not in st.session_state:
    st.session_state.wrong_time = 0

if "timeout_time" not in st.session_state:
    st.session_state.timeout_time = 0

if "time_limit" not in st.session_state:
    st.session_state.time_limit = 4

if "time_left" not in st.session_state:
    st.session_state.time_left = 0

if "mode" not in st.session_state:
   st.session_state.mode = "home"

if "operation" not in st.session_state:
   st.session_state.operation = "Addition"

st.sidebar.title("Player Stats")

st.sidebar.write(f"Points: {st.session_state.score}")

st.sidebar.write(f"Level: {st.session_state.level}")

st.title("Math Speed Trainer")

if st.session_state.mode == "home":

    if st.button("Addition Practice"):
        st.session_state.mode = "Addition"
        
    if st.button("Subtraction Practice"):
        st.session_state.mode = "Subtraction"



def check_answer():
     

    if st.session_state.operation == "Addition":
        correct_answer = st.session_state.num1 + st.session_state.num2

    else:
        correct_answer = st.session_state.num1 - st.session_state.num2


    if st.session_state.answer:
        user_answer = int(st.session_state.answer)

        st.session_state.time_used = time.time() - st.session_state.start_time


        if user_answer == correct_answer:
         st.session_state.score += 1
         st.session_state.level += 1
         generate_problem()
         st.session_state.answer = ""
            
        else:

         st.session_state.level = 1
         generate_problem()

         st.session_state.wrong_time = time.time()

         st.session_state.answer = ""






if st.session_state.mode == "Addition":

    if st.button("Back to Home"):
        st.session_state.mode = "home"

    st_autorefresh(interval=1000)


    if "num1" not in st.session_state:
     generate_problem()

    st.session_state.time_left = (
        st.session_state.time_limit
        - (time.time() - st.session_state.start_time)
    )


    if st.session_state.time_left <= 0:
     st.session_state.level = 1
     generate_problem()
     st.session_state.timeout_time = time.time()
     st.session_state.answer = ""

    st.write(f"Time Left: {max(0, st.session_state.time_left):.1f} seconds")

    if st.session_state.operation == "Addition":
       st.write(f"{st.session_state.num1} + {st.session_state.num2} =")

    else:
       st.write(f"{st.session_state.num1} - {st.session_state.num2} =")

    if st.session_state.operation == "Addition":
       correct_answer = st.session_state.num1 + st.session_state.num2

    else:
       correct_answer = st.session_state.num1 - st.session_state.num2


    answer = st.text_input("Your Answer", key="answer", on_change=check_answer)

    # Show message for 1 second

    if time.time() - st.session_state.wrong_time < 1:
     st.write("Wrong!")

    # Show Timeout message for 1 second

    if time.time() - st.session_state.timeout_time < 1:
     st.write("Timeout!")

    submit = st.button("Submit Answer")

    if submit:
        check_answer()



if st.session_state.mode == "Subtraction":
   
   if st.button("Back to Home"):
      st.session_state.mode = "home"


   st_autorefresh(interval=1000)

   if "num1" not in st.session_state:
      generate_problem()

   st.session_state.time_left = (
       st.session_state.time_limit
       - (time.time() - st.session_state.start_time)
    )
   
   if st.session_state.time_left <= 0:
       st.session_state.level = 1
       generate_problem()
       st.session_state.timeout_time = time.time()
       st.session_state.answer =""

   st.write(f"Time Left: {max(0, st.session_state.time_left):.1f} seconds")
   
   st.write(f"{st.session_state.num1} - {st.session_state.num2} =")
    
   correct_answer = st.session_state.num1 - st.session_state.num2

   answer = st.text_input("Your Answer", key="answer", on_change=check_answer)

   if time.time() - st.session_state.wrong_time < 1:
      st.write("Wrong!")

   if time.time() - st.session_state.timeout_time < 1:
      st.write("Timeout!")

   if st.button("Submit Answer"):
      check_answer()
