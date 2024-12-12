import streamlit as st

left, right = st.columns(2)
with left:
    st.title("Servas")

with right:
    st.title("Servas")

left,right = st.columns(2)
      
with left:
    st.subheader("Krass")

with right:
    st.subheader("Krass")

left, right = st.columns(2)

left.write("hallo")  
right.write("Hallo")



left, right = st.columns(2)

with left:
    st.image("https://www.testedich.de/quiz52/picture/pic_1515095611_1.jpg")

with right:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJJ_go-UXQcdWgwBjIFrcYJ6ACqmmhFkwOUQ&s")  

left, right = st.columns(2)     

with left:
    st.video("https://www.youtube.com/watch?v=QAk4I1B36FY")

with right:
    st.video("https://www.youtube.com/watch?v=T2W5LlHXZJ4")








st.title("Große Überschrift" , anchor=False)
st.header("Kleine Überschrift", anchor=False, divider="blue")
st.subheader("Noch Kleinere Überschrift",anchor=False, divider=True)
st.write("Webseite von Sasa")
st.image("https://rundum.dog/wp-content/uploads/2023/02/hund-schaut-lustig-komisch.jpg",width=100)
st.video("https://www.youtube.com/watch?v=6v0zzZ4DRa8")


st.title("Hallo", anchor=False)
st.header("Das ist ein text", anchor=False, divider=True)
st.subheader("Noch ein text", anchor=False, divider=True)
st.write("Hallo")
st.image("https://media.istockphoto.com/id/1212177973/de/foto/s%C3%BC%C3%9Fe-braun-mexikanische-chihuahua-hund-isoliert-auf-hellrosa-hintergrund-emp%C3%B6rt-ungl%C3%BCcklich.jpg?s=612x612&w=0&k=20&c=6uYCp0i1gh5lXo4OC5VySxi7byvvsfHMdOGixXSg8y4=", width=500)
st.video("https://www.youtube.com/watch?v=r-cpjrBYQ3g&list=PLHGitL3lNDzu2Z9BsqlGbcPYacPWnYjoV")
st.title("Wie gehts", anchor=False)
st.header("It",anchor=False,divider=True)
st.subheader("IT",anchor=False,divider=True)
st.write("mir geht es sehr gut")
st.image("https://www.honigpfote.de/wp-content/uploads/2017/03/Smile-Ball-Quietschspielzeug-Hund-600x600.png",width=300)
st.video("https://www.youtube.com/watch?v=hcIEuHkbTXQ")
st.title("Kebab", anchor=False,)
st.header("Kebab mit soße",anchor=False,divider=True)
st.subheader("Dürum",anchor=False,divider=True)
st.write("was machst du heute")
st.image("https://img.freepik.com/vektoren-kostenlos/hund-mit-gezogenem-anzug_79603-538.jpg",width=250)
st.video("https://www.youtube.com/watch?v=zG4nYRTWbYY")
st.title("Döner", anchor=False)
st.header("Dönerman",anchor=False,divider=True)
st.subheader("Keine ahnung",anchor=False,divider=True)
st.write("lass mal raus gehen")
st.image("https://www.publicdomainpictures.net/pictures/240000/nahled/funny-dog-15091160994Oj.jpg",width=450)
st.video("https://www.youtube.com/watch?v=uQZhehGSryU")