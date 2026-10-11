import random
import streamlit as st

st.set_page_config(
    page_title="For Meshudiii 💗",
    page_icon="💌",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------- Styling --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.stApp {
  background:
    radial-gradient(circle at 8% 3%, rgba(255,190,215,.35), transparent 27%),
    radial-gradient(circle at 92% 12%, rgba(255,224,175,.36), transparent 25%),
    linear-gradient(135deg, #fff8fb, #fffaf2 55%, #fff4f7);
}
h1, h2, h3 { font-family: 'Playfair Display', serif !important; color: #57263e; }
.hero {
  padding: 2.2rem; border-radius: 28px;
  background: linear-gradient(120deg, #ffdce8, #fff0d6 58%, #f2dcff);
  border: 1px solid rgba(128,50,80,.12);
  box-shadow: 0 14px 40px rgba(120,55,80,.08);
}
.eyebrow { text-transform: uppercase; letter-spacing: .17em; font-size: .72rem; color: #a14b6a; font-weight: 700; }
.hero h1 { font-size: clamp(2.2rem, 5vw, 4.1rem); line-height: 1.04; margin: .45rem 0; }
.hero p { color: #684052; font-size: 1.08rem; max-width: 820px; }
.soft-card {
  padding: 1.2rem; border-radius: 22px; background: rgba(255,255,255,.82);
  border: 1px solid #f1d9e4; box-shadow: 0 8px 25px rgba(110,45,70,.05);
}
.big { font-size: 2rem; font-weight: 700; color: #a13d68; }
.small { color: #8b6374; font-size: .88rem; }
.quote { font-family: 'Playfair Display', serif; font-size: 1.35rem; color: #713450; }
.stButton > button {
  border-radius: 999px; border: 1px solid #efc5d5;
  background: linear-gradient(100deg, #f8c7d8, #ffe4bd);
  color: #54253b; font-weight: 700; padding: .55rem 1rem;
}
.stButton > button:hover { border-color: #d983a4; color: #54253b; }
div[data-testid="stSidebar"] { background: #fff1f6; }
div[data-testid="stTabs"] button { font-weight: 700; }
</style>
""", unsafe_allow_html=True)

# -------------------- Session state --------------------
defaults = {
    "joke_index": 0,
    "joke_runs": 0,
    "museum": [],
    "letter_ready": False,
    "promise_done": [],
    "surprise_open": False,
    "quiz_feedback": "",
    "date_idea": "",
    "her_choice": "",
}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# -------------------- Sidebar --------------------
with st.sidebar:
    st.markdown("## 💌 Little settings")
    st.caption("Made especially for Meshudiii.")
    your_name = st.text_input("Your name / signature", value="Your favourite idiot 💗")
    st.markdown("---")
    st.markdown("### Tiny reminder")
    st.write("This page can be cute, but your apology should be real. Don't use it to pressure her into forgiving you.")
    if st.button("🎊 Confetti break"):
        st.balloons()

# -------------------- Header --------------------
st.markdown("""
<div class="hero">
  <div class="eyebrow">A small internet corner with a big heart</div>
  <h1>Meshudiii's Smile Universe 💗</h1>
  <p>One human who reacted the wrong way, a heart that wants to make things right,
  and a collection of silly little surprises made just for you.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="soft-card"><div class="big">💌</div><b>Honest words</b><div class="small">No excuses. No blame-shifting.</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="soft-card"><div class="big">🧸</div><b>Soft chaos</b><div class="small">Silly jokes and tiny surprises.</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="soft-card"><div class="big">🌱</div><b>Real effort</b><div class="small">Actions matter more than a website.</div></div>', unsafe_allow_html=True)

st.write("")
tabs = st.tabs([
    "💌 The real apology",
    "🎁 Surprise box",
    "😂 Giggle department",
    "🖼️ Our memory museum",
    "🌷 Promise garden",
    "🫶 Your choice",
])

# -------------------- 1. Apology --------------------
with tabs[0]:
    st.subheader("For you, Meshudiii 🥺")
    st.write("This is the serious corner. Make it sound like you, and only include promises you genuinely mean.")
    st.markdown('<div class="quote">“I can be wrong and still choose to do better.”</div>', unsafe_allow_html=True)
    what_happened = st.text_area(
        "What did you do or say that you want to own?",
        placeholder="I reacted by…",
        height=90,
        key="what_happened",
    )
    impact = st.text_area(
        "What do you understand about how it may have made her feel?",
        placeholder="I can understand that my reaction may have made you feel…",
        height=90,
        key="impact",
    )
    next_time = st.text_area(
        "What will you try to do differently next time?",
        placeholder="Next time I feel upset, I will pause, listen, and…",
        height=90,
        key="next_time",
    )
    if st.button("Write my honest apology 💗", key="write_apology"):
        if all(x.strip() for x in (what_happened, impact, next_time)):
            st.session_state.letter_ready = True
        else:
            st.warning("Fill in all three parts first. Specific honesty is better than a perfect-sounding paragraph.")
    if st.session_state.letter_ready:
        st.markdown("---")
        st.markdown('<div class="quote">My Meshudiii,</div>', unsafe_allow_html=True)
        st.write(f"I'm sorry for the way I reacted: {what_happened.strip().rstrip('.')} .")
        st.write(f"I understand that it may have left you feeling {impact.strip().rstrip('.')} . I don't want to minimise your feelings or act like my reaction was okay.")
        st.write(f"Next time, I want to do this differently: {next_time.strip().rstrip('.')} . I know saying it is the easy part; showing it consistently is what matters.")
        st.write("You don't have to forgive me right now, pretend you're okay, or smile because I made a website. You deserve time and space for whatever you're feeling.")
        st.write("I care about you, Meshudiii. I'm sorry, and I want to learn from this instead of repeating it.")
        st.write(f"With love and a very sincere heart,  \n**{your_name}** 💌")
        st.success("Before sharing: read it out loud, edit anything that doesn't sound like you, and follow through.")

# -------------------- 2. Surprise box --------------------
with tabs[1]:
    st.subheader("A tiny surprise, just for Meshudiii 🎁")
    st.write("Choose a little envelope. No surprise can replace an apology, but a tiny smile is welcome.")
    surprise = st.selectbox(
        "Pick an envelope",
        ["💌 Open when you need a little love",
         "🧸 Open when your day is being rude",
         "✨ Open for a random compliment",
         "🍓 Open for a tiny date idea",
         "🐣 Open for a silly emergency"],
    )
    if st.button("Open my envelope ✨"):
        st.session_state.surprise_open = True
        st.session_state.opened_envelope = surprise
    if st.session_state.surprise_open:
        chosen = st.session_state.get("opened_envelope", surprise)
        messages = {
            "💌 Open when you need a little love": (
                "A reminder: you deserve kindness on the ordinary days, not just the special ones. "
                "You don't need to be cheerful or perfect to be cared about. 💗"
            ),
            "🧸 Open when your day is being rude": (
                "Dear Day: Meshudiii did not order this nonsense. Please cancel the subscription immediately. "
                "She deserves a snack, a deep breath, and at least one thing that goes right. 😤"
            ),
            "✨ Open for a random compliment": (
                "Your existence has main-character energy. Even your tiny habits can become someone's favourite detail. "
                "Yes, this compliment has passed absolutely no scientific peer review. 🌷"
            ),
            "🍓 Open for a tiny date idea": (
                "Tiny quest: pick a favourite snack, take a little walk, and trade one good thing from the day. "
                "Only if you feel like it—low pressure, maximum cozy. 🍓"
            ),
            "🐣 Open for a silly emergency": (
                "EMERGENCY ALERT 🚨 A tiny duck in a very small hat has been dispatched to remind you that you are loved. "
                "Estimated arrival: emotionally immediate. Quack responsibly. 🦆"
            ),
        }
        st.markdown(f'<div class="soft-card"><div class="eyebrow">Envelope opened</div><h3>{chosen}</h3><p>{messages[chosen]}</p></div>', unsafe_allow_html=True)
        if st.button("One more surprise, please 🎲"):
            st.session_state.surprise_open = False
            st.rerun()

# -------------------- 3. Giggles --------------------
with tabs[2]:
    st.subheader("The Meshudiii Giggle Department 😂")
    st.write("This department has no budget, no qualifications, and unreasonable confidence.")
    jokes = [
        ("Why did my brain ask for a meeting?", "To discuss why it becomes a potato whenever I need to explain myself properly."),
        ("I tried to be smooth today.", "The floor disagreed. We are no longer on speaking terms."),
        ("My apology website has one bug.", "It cannot give me emotional maturity automatically. Developers are investigating."),
        ("If overthinking were an Olympic sport…", "I'd win gold, question whether the judges were biased, then replay the ceremony at 2 a.m."),
        ("Breaking news:", "Local idiot realises that listening calmly is more useful than trying to win every argument."),
        ("I asked a calculator how much you matter.", "It displayed ERROR: number too large for this tiny machine."),
        ("My brain has 37 tabs open.", "One is playing music, one is worrying, and one is just a picture of you being adorable.")
    ]
    if st.button("Deploy another terrible joke 🚀"):
        st.session_state.joke_index = (st.session_state.joke_index + 1) % len(jokes)
        st.session_state.joke_runs += 1
    title, punchline = jokes[st.session_state.joke_index]
    st.markdown(f'<div class="soft-card"><div class="eyebrow">Comedy attempt #{st.session_state.joke_runs + 1}</div><h3>{title}</h3><p style="font-size:1.12rem;color:#684052">{punchline}</p></div>', unsafe_allow_html=True)
    st.write("")
    reaction = st.radio("Meshudiii's official review:", [
        "😐 Please refund my time",
        "🙂 A tiny smile escaped",
        "😂 I hate that I laughed",
        "🥹 Fine, that was cute",
    ], horizontal=True, key="joke_reaction")
    if st.button("Submit highly official review"):
        if reaction.startswith(("😂", "🥹")):
            st.balloons()
            st.success("THE COMMITTEE IS SCREAMING. A tiny smile has been detected. 💗")
        elif reaction.startswith("🙂"):
            st.success("A small smile counts. The comedy department is doing a tiny dance.")
        else:
            st.info("Review accepted. The joke has been sent for additional training.")

# -------------------- 4. Memory museum --------------------
with tabs[3]:
    st.subheader("The Little Things Museum 🖼️")
    st.write("Add real memories here—tiny, ordinary moments are often the most precious.")
    memory_name = st.text_input("Exhibit name", placeholder="The day we laughed at absolutely nothing")
    memory_story = st.text_area("Tell the story", placeholder="What happened? What made it special?", height=100)
    memory_detail = st.text_input("One detail you still remember", placeholder="A song, snack, expression, silly phrase…")
    if st.button("Add this memory to the museum"):
        if memory_name.strip() and memory_story.strip():
            st.session_state.museum.append({
                "name": memory_name.strip(),
                "story": memory_story.strip(),
                "detail": memory_detail.strip(),
            })
            st.success("Exhibit added. Please admire responsibly. 🖼️")
        else:
            st.warning("Give your exhibit a name and a story first.")
    st.markdown("---")
    if st.session_state.museum:
        for number, item in enumerate(reversed(st.session_state.museum), start=1):
            with st.expander(f"🖼️ Exhibit {len(st.session_state.museum) - number + 1}: {item['name']}"):
                st.write(item["story"])
                if item["detail"]:
                    st.caption(f"Preserved tiny detail: {item['detail']}")
    else:
        st.info("The museum is empty for now. Add a real memory whenever you're ready.")
    st.caption("Only add memories you both feel comfortable sharing. This is a little scrapbook, not a scoreboard.")

# -------------------- 5. Promise garden --------------------
with tabs[4]:
    st.subheader("The Promise Garden 🌷")
    st.write("Pick the commitments you honestly want to practise. Don't promise everything just to make the moment feel better.")
    promise_options = [
        "I'll pause before replying when I'm angry or overwhelmed.",
        "I'll listen to understand, not just to prepare my defence.",
        "I'll take responsibility without adding a 'but you…'",
        "I'll ask what you need instead of assuming.",
        "I'll respect your space and your timing.",
        "I'll show change through consistent actions, not grand gestures.",
    ]
    chosen_promises = []
    for i, promise in enumerate(promise_options):
        if st.checkbox(promise, key=f"garden_{i}"):
            chosen_promises.append(promise)
    if chosen_promises:
        st.markdown(f'<div class="soft-card"><div class="eyebrow">{len(chosen_promises)} promise(s) planted</div><h3>Little actions grow into trust 🌱</h3><p>Pick one small action you can start today. Make it specific, realistic, and yours to follow through on.</p></div>', unsafe_allow_html=True)
        first_action = st.text_input("My first real-life step", placeholder="Example: take a breath before replying when I'm upset")
        if st.button("Plant my first step 🌱"):
            if first_action.strip():
                st.success(f"Planted: {first_action.strip()} — now let your actions water it.")
            else:
                st.warning("Write one concrete step first.")
    else:
        st.caption("Choose a promise to plant your first flower. Small and sincere is enough.")

# -------------------- 6. Her choice --------------------
with tabs[5]:
    st.subheader("Meshudiii gets to choose 🫶")
    st.write("This is not a reward for forgiving me. It's a gentle menu, and saying 'not right now' is completely okay.")
    her_choice = st.radio("If you feel like it, what would you prefer?", [
        "💬 A calm conversation where I listen",
        "🍓 A snack date or little treat",
        "🎧 A playlist or handwritten note",
        "🌿 Some space and a check-in later",
        "🫶 Just the apology—no big gesture",
        "🕊️ Not ready yet. Please give me time.",
    ], key="choice_radio")
    optional_note = st.text_area("Anything else you'd like me to understand? (optional)", placeholder="Your feelings, boundaries, or what would help…")
    if st.button("Save this choice"):
        st.session_state.her_choice = her_choice
        st.session_state.her_note = optional_note
        st.success("Choice noted on this page. The kindest next step is to respect it.")
    if st.session_state.her_choice:
        st.markdown(f'<div class="soft-card"><div class="eyebrow">A gentle reminder</div><h3>{st.session_state.her_choice}</h3><p>{st.session_state.get("her_note", "")}</p></div>', unsafe_allow_html=True)

# -------------------- Footer --------------------
st.write("")
st.markdown("---")
st.markdown(
    f'<p style="text-align:center;color:#94677a">Made with care by {your_name} · especially for Meshudiii 💗</p>',
    unsafe_allow_html=True,
)
st.caption("Privacy note: this demo keeps interactions in the current Streamlit session. It does not send messages, collect analytics, or save entries to a database. If you deploy it publicly, don't enter private or sensitive details.")
