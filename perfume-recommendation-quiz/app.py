import streamlit as st
st.set_page_config(page_title="Find Your Fragrance",page_icon="✨")
st.title("Find Your Fragrance")
st.caption("A simple preference-matching demo. Recommendations are illustrative, not measured fragrance descriptions.")
occasion=st.selectbox("Where will you wear it?",["Everyday","Office","Evening","Special occasion"])
vibe=st.radio("Which scent family do you prefer?",["Fresh","Sweet","Woody","Intense"])
weather=st.select_slider("Typical weather",options=["Cool","Mild","Hot"],value="Hot")
intensity=st.slider("Desired intensity",1,5,3)
profiles={
 "Fresh Start":{"family":"Fresh","occasion":"Everyday","weather":"Hot","intensity":2,"notes":"Clean, fresh direction"},
 "Soft Glow":{"family":"Sweet","occasion":"Special occasion","weather":"Mild","intensity":3,"notes":"Soft, sweet direction"},
 "Wood Trail":{"family":"Woody","occasion":"Office","weather":"Cool","intensity":3,"notes":"Smooth, woody direction"},
 "Nightfall":{"family":"Intense","occasion":"Evening","weather":"Cool","intensity":5,"notes":"Bold, deep direction"},
}
if st.button("Get recommendations",type="primary"):
 scores=[]
 for name,p in profiles.items():
  score=4*(p["family"]==vibe)+2*(p["occasion"]==occasion)+1*(p["weather"]==weather)+(5-abs(p["intensity"]-intensity))
  scores.append((score,name,p))
 for rank,(_,name,p) in enumerate(sorted(scores,reverse=True)[:3],1):
  st.subheader(f"{rank}. {name}")
  st.write(f"{p['notes']} | {p['family']} | Suggested intensity {p['intensity']}/5")
 st.caption("Replace demo profiles with verified product note pyramids and wear-test results before using with real customers.")
