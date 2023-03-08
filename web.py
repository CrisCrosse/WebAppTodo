import streamlit as st
import functions

def add_todo():
    #print("Function executed")
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This lists all the todos I need to complete")
st.write("This app is designed to enhance productivity")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        #print("checkbox ticked")
        todos.pop(index)
        functions.write_todos(todos)
        #remove checked item from local list and write to file
        del st.session_state[todo]
        st._rerun()


st.text_input(label="Input:", placeholder="Add a new todo here...",
              on_change=add_todo, key="new_todo")

#st.session_state

#print("script executed")