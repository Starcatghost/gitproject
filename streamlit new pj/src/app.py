import streamlit as st
import api
import app_db


st.title('streamlit modren project')
option = st.sidebar.selectbox('enter your option: ',
('CALL MOVIE LIST BY PAGE', 'SHOW ALL MOVIES'))

if option == 'CALL MOVIE LIST BY PAGE':
    page_id = st.number_input('eneter page number: ', min_value= 1 , max_value= 25)
    result = api.get_movie1_list_by_page(page_id)
    if st.button('show movie list'):
        
        if result != 'ERROR':
            st.write(result)
        else:
             st.error('your request can not be send!!!') 

elif option == 'INSERT MOVIES FROM API':
    page_id = st.number_input('eneter page number: ', min_value= 1 , max_value= 25)
    result1 = api.get_movie1_list_by_page(page_id)
    if st.button('add movie list'):
            
            if result1 != 'ERROR':
                result2 = app_db.insert_list_of_movies(result1)
                st.success(result2)
            else:
                 st.error('your request can not be send!!!')           