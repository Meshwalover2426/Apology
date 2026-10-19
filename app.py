import calendar
import random
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import streamlit as st

# ============================================================
# KARTUDII ❤️ MESHUDIII
# A complete, prewritten romantic apology website
# ============================================================

st.set_page_config(
    page_title="For Meshudiii 💗",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------- CONFIGURATION --------------------------

HER_NAME = "Meshudiii"
YOUR_NAME = "Kartudii"
TIMEZONE = ZoneInfo("Asia/Kolkata")

# Fixed baseline: midnight on October 19, 2026, India time.
# Reopening the app never resets this date.
REAL_ANCHOR = datetime(2026, 10, 19, 0, 0, 0, tzinfo=TIMEZONE)

# A virtual calendar lets us display the initial duration
# as 79 years, 8 months, and 20 days, then count upward.
VIRTUAL_ORIGIN = datetime(2000, 1, 1, 0, 0, 0)
INITIAL_YEARS = 79
INITIAL_MONTHS = 8
INITIAL_DAYS = 20


# -------------------- PAGE DESIGN ----------------------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

    :root {
        --pink: #ff82ac;
        --rose: #ffb5ca;
        --cream: #fff8f5;
        --purple: #b7a5ff;
        --ink: #493747;
    }

    .stApp {
        background:
            radial-gradient(ellipse at 5% 5%, #ffe1ed 0%, transparent 36%),
            radial-gradient(ellipse at 95% 25%, #e9e3ff 0%, transparent 36%),
            linear-gradient(150deg, #fff9f5, #fff0f5 55%, #f6f1ff);
        color: var(--ink);
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    #MainMenu, footer {
        visibility: hidden;
    }

    .block-container {
        max-width: 1120px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: #71445d !important;
    }

    .hero {
        padding: 38px 22px;
        border: 1px solid rgba(255,255,255,.85);
        border-radius: 30px;
        text-align: center;
        background: rgba(255,255,255,.66);
        box-shadow: 0 12px 45px rgba(169,100,139,.10);
        margin-bottom: 22px;
    }

    .eyebrow {
        text-transform: uppercase;
        letter-spacing: 3px;
        color: #b66a8b;
        font-size: 11px;
        font-weight: 700;
    }

    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: clamp(36px, 7vw, 66px);
        line-height: 1.12;
        color: #8b456b;
        margin: 14px 0;
    }

    .hero-subtitle {
        color: #886d7c;
        font-size: 16px;
        line-height: 1.8;
        max-width: 650px;
        margin: auto;
    }

    .card {
        height: 100%;
        padding: 25px;
        border: 1px solid rgba(255,255,255,.9);
        border-radius: 24px;
        background: rgba(255,255,255,.73);
        box-shadow: 0 8px 28px rgba(148,91,125,.08);
        margin-bottom: 15px;
    }

    .card h3 {
        font-size: 23px;
        margin-top: 8px;
    }

    .card p {
        color: #796775;
        line-height: 1.85;
    }

    .big-emoji {
        font-size: 38px;
    }

    .timer-card {
        padding: 28px 15px;
        border-radius: 28px;
        text-align: center;
        background: linear-gradient(135deg, #fff, #ffe8f1);
        border: 1px solid white;
        box-shadow: 0 10px 40px rgba(201,100,147,.13);
        margin: 20px 0;
    }

    .timer-label {
        color: #a55b7e;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-size: 11px;
        font-weight: 700;
    }

    .timer-number {
        font-family: 'Playfair Display', serif;
        color: #8e426b;
        font-size: clamp(30px, 5vw, 54px);
        font-weight: 700;
        line-height: 1.3;
        margin: 12px 0;
        overflow-wrap: anywhere;
    }

    .timer-caption {
        font-size: 13px;
        color: #9a788b;
        line-height: 1.8;
    }

    .memory-tag {
        display: inline-block;
        border-radius: 30px;
        padding: 6px 12px;
        background: #ffe5ef;
        color: #a45478;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1px;
    }

    .quote {
        font-family: 'Playfair Display', serif;
        font-size: 24px;
        line-height: 1.6;
        color: #8e426b;
        padding: 15px 0;
    }

    .soft-note {
        color: #947b8b;
        font-size: 13px;
        line-height: 1.8;
    }

    .footer {
        text-align: center;
        padding: 30px 10px;
        color: #a47b91;
        font-size: 13px;
        line-height: 2;
    }

    div.stButton > button {
        width: 100%;
        min-height: 48px;
        border-radius: 16px;
        border: 1px solid #ffd0e0;
        background: linear-gradient(135deg, #ffedf4, #f4efff);
        color: #87476b;
        font-weight: 700;
        transition: all .2s ease;
    }

    div.stButton > button:hover {
        border-color: #f59abc;
        color: #743653;
        transform: translateY(-2px);
    }

    div[data-testid="stTabs"] button {
        font-weight: 600;
    }

    .heart-line {
        color: #ef83ad;
        letter-spacing: 8px;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# -------------------- TIMER LOGIC ----------------------------

def add_months(dt, months):
    """Add calendar months while keeping the date valid."""
    total_months = dt.year * 12 + (dt.month - 1) + months
    year = total_months // 12
    month = total_months % 12 + 1
    day = min(dt.day, calendar.monthrange(year, month)[1])
    return dt.replace(year=year, month=month, day=day)


def add_initial_duration(origin):
    """Create the virtual starting point for the timer."""
    value = add_months(
        origin,
        INITIAL_YEARS * 12 + INITIAL_MONTHS,
    )
    return value + timedelta(days=INITIAL_DAYS)


def calendar_components(origin, target):
    """Calculate calendar years, months, days, hours, minutes, seconds."""
    total_months = (target.year - origin.year) * 12
    total_months += target.month - origin.month

    while add_months(origin, total_months) > target:
        total_months -= 1

    while add_months(origin, total_months + 1) <= target:
        total_months += 1

    years = total_months // 12
    months = total_months % 12

    current = add_months(origin, total_months)
    remaining = target - current

    days = remaining.days
    seconds_left = remaining.seconds

    hours = seconds_left // 3600
    minutes = (seconds_left % 3600) // 60
    seconds = seconds_left % 60

    return years, months, days, hours, minutes, seconds


@st.fragment(run_every="1s")
def live_forever_timer():
    """Refresh this section every second without resetting the timer."""
    now = datetime.now(TIMEZONE)

    # Do not count negative elapsed time if the configured start
    # date is ever changed to a future date.
    elapsed = max(now - REAL_ANCHOR, timedelta(0))

    virtual_start = add_initial_duration(VIRTUAL_ORIGIN)
    virtual_now = virtual_start + elapsed

    years, months, days, hours, minutes, seconds = (
        calendar_components(VIRTUAL_ORIGIN, virtual_now)
    )

    st.markdown(
        f"""
        <div class="timer-card">
            <div class="timer-label">A little forever counter 💗</div>
            <div class="timer-number">
                {years} years · {months} months · {days} days
            </div>
            <div class="timer-number"
                 style="font-size:clamp(24px,4vw,38px);">
                {hours:02d}:{minutes:02d}:{seconds:02d}
            </div>
            <div class="timer-caption">
                Years, months, days, hours, minutes and seconds<br>
                Every second adds another little tick to this story.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -------------------- SESSION STATE --------------------------

defaults = {
    "opened_surprise": False,
    "opened_letter": False,
    "opened_giggle": False,
    "opened_promise": False,
    "opened_final": False,
    "heart_count": 0,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# -------------------- HERO ------------------------------------

st.markdown(
    f"""
    <div class="hero">
        <div class="eyebrow">A tiny corner of the internet, made with love</div>
        <div class="hero-title">For {HER_NAME} 💗</div>
        <div class="heart-line">♡ ♥ ♡</div>
        <div class="hero-subtitle">
            A little apology, a few unforgettable memories,
            some questionable jokes, and a whole lot of love.<br>
            Made especially for you by <b>{YOUR_NAME}</b>.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="card">
        <div class="big-emoji">💌</div>
        <h3>A little note before you explore</h3>
        <p>
            This isn't here to force a smile, demand an answer, or rush
            anything. It's just a small space made to say I'm sorry,
            remember our silly moments, and remind you that your feelings
            matter to me.
        </p>
        <p>
            I know that reacting the wrong way can hurt. I take
            responsibility for how I reacted. You deserve patience,
            kindness, and respect, even when things get difficult.
            I'm sorry, Meshudiii.
        </p>
        <p><b>You don't owe me forgiveness just because I made this.</b></p>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------- TIMER -----------------------------------

st.subheader("⏳ Our little forever")

live_forever_timer()

st.caption(
    "Timer baseline: October 19, 2026, at 12:00 AM India time. "
    "It keeps its baseline when the app is reopened."
)

# -------------------- DASHBOARDS ------------------------------

tabs = st.tabs(
    [
        "💌 The Apology",
        "🎁 Surprise Box",
        "😂 Giggle Department",
        "📸 Memory Museum",
        "🌷 Promise Garden",
        "💗 One Last Thing",
    ]
)

# ==================== TAB 1: APOLOGY ==========================

with tabs[0]:
    st.markdown(
        """
        <div class="card">
            <div class="big-emoji">🫶</div>
            <h3>I'm sorry, Meshudiii.</h3>
            <p>
                I reacted in the wrong manner, and I don't want to
                hide behind excuses or pretend that good intentions
                erase hurtful reactions.
            </p>
            <p>
                I should have handled things with more care.
                You deserve to be heard without feeling that your
                emotions are a problem or that you have to make
                everything okay immediately.
            </p>
            <p>
                I'm sorry for my part in what happened. I want to
                learn to pause, listen properly, communicate calmly,
                and take responsibility instead of reacting badly.
            </p>
            <p>
                This page can't undo anything. What matters more is
                how I treat you after this, through consistent actions
                rather than pretty words alone.
            </p>
            <p><b>There's no deadline for your feelings. Take your time.</b></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Send a little heart 💗", key="heart_button"):
        st.session_state.heart_count += 1
        st.toast("One tiny heart, sent with love 💗")

    st.markdown(
        f"""
        <div class="card" style="text-align:center;">
            <div class="big-emoji">💗</div>
            <h3>Your heart collection</h3>
            <p>
                {st.session_state.heart_count} little heart(s) collected.
                Each one comes with a reminder that you matter.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ==================== TAB 2: SURPRISE BOX =====================

with tabs[1]:
    st.markdown(
        """
        <div class="card">
            <div class="big-emoji">🎁</div>
            <h3>A surprise, just for you</h3>
            <p>
                This box contains one scientifically unverified,
                extremely important reminder.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Open your surprise ✨", key="surprise_button"):
        st.session_state.opened_surprise = True
        st.balloons()

    if st.session_state.opened_surprise:
        st.markdown(
            """
            <div class="card">
                <div class="big-emoji">🌷💗🌷</div>
                <h3>Surprise!</h3>
                <div class="quote">
                    You don't have to be cheerful all the time
                    to be loved.
                </div>
                <p>
                    You can be quiet, annoyed, tired, emotional,
                    goofy, dramatic, or completely out of energy.
                    You are still you, and you still deserve care.
                </p>
                <p>
                    Today's bonus prize: one imaginary hug,
                    unlimited imaginary snacks, and absolutely
                    no pressure to react a certain way. 🧸
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ==================== TAB 3: GIGGLE DEPARTMENT =================

with tabs[2]:
    st.markdown(
        """
        <div class="card">
            <div class="big-emoji">🚜😂</div>
            <h3>The official Giggle Department</h3>
            <p>
                A highly prestigious institute dedicated to preserving
                your most legendary moments and questionable sound effects.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="card">
            <div class="memory-tag">CASE FILE 001</div>
            <h3>🚜 The Tractor-Start Laugh</h3>
            <div class="quote">
                “Even tractors give smoother starts than the start
                of her laugh.”
            </div>
            <p>
                First comes the mysterious hesitation. Then a tiny
                engine-cough sound. Then another attempt. And finally,
                the full laugh starts running like a tractor that
                has finally agreed to work.
            </p>
            <p>
                <b>Department verdict:</b> Unmatched character.
                Questionable ignition. Zero replacements available. 😂
            </p>
        </div>

        <div class="card">
            <div class="memory-tag">CASE FILE 002</div>
            <h3>🎤 The Doreamon Voice Incident</h3>
            <div class="quote">
                The concert was so powerful that even her voice
                needed a holiday.
            </div>
            <p>
                That day your voice was almost gone after singing
                loudly in dairo, and you started sounding like Doreamon.
                One legendary singing session, followed by a voice
                that apparently decided it had completed its shift.
            </p>
            <p>
                <b>Department verdict:</b> The performance was
                unforgettable. The aftermath was equally iconic. 😭💙
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Issue the official giggle certificate 🏆",
                 key="giggle_button"):
        st.session_state.opened_giggle = True
        st.snow()

    if st.session_state.opened_giggle:
        st.success(
            "CERTIFIED: Meshudiii — CEO of Legendary Laughs "
            "and Unforgettable Voice Incidents. 🏆"
        )

# ==================== TAB 4: MEMORY MUSEUM ====================

with tabs[3]:
    st.markdown(
        """
        <div class="card">
            <div class="big-emoji">📸</div>
            <h3>The Memory Museum</h3>
            <p>
                Some memories are polished and cinematic.
                Others involve a nearly missing voice and a laugh
                that needs an engine starter.
            </p>
            <p>
                Both kinds deserve a place in the museum.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    memories = [
        (
            "🎤",
            "The Doreamon Concert",
            "A day of loud singing in dairo, a nearly vanished voice, "
            "and a sound that became a memory of its own.",
        ),
        (
            "🚜",
            "The Legendary Laugh",
            "A laugh with its own starting procedure. "
            "No key, mechanic, or tractor manual could explain it.",
        ),
        (
            "💗",
            "The Little Things",
            "The small, silly details that might look ordinary to "
            "someone else but can make a memory feel uniquely yours.",
        ),
    ]

    for emoji, title, description in memories:
        st.markdown(
            f"""
            <div class="card">
                <div class="big-emoji">{emoji}</div>
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.caption(
        "These cards are ready-made. No uploading photos or adding "
        "memories is required."
    )

# ==================== TAB 5: PROMISE GARDEN ===================

with tabs[4]:
    st.markdown(
        """
        <div class="card">
            <div class="big-emoji">🌷</div>
            <h3>Promises that should show up in actions</h3>
            <p>
                A promise isn't magic. It matters when it becomes
                a habit, especially when a conversation gets difficult.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    promises = [
        (
            "🌱",
            "Pause before reacting",
            "I will work on giving myself a moment to calm down "
            "instead of letting an immediate reaction take over.",
        ),
        (
            "👂",
            "Listen to understand",
            "I will try to hear what you're saying without turning "
            "every disagreement into a battle.",
        ),
        (
            "🫶",
            "Respect your feelings",
            "You can need space or feel upset without having to "
            "justify every emotion to me.",
        ),
        (
            "🌻",
            "Show change consistently",
            "I want my behaviour over time to demonstrate what "
            "my apology means.",
        ),
    ]

    for emoji, title, description in promises:
        st.markdown(
            f"""
            <div class="card">
                <div class="big-emoji">{emoji}</div>
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if st.button("Plant a tiny imaginary flower 🌸",
                 key="promise_button"):
        st.session_state.opened_promise = True
        st.toast("One little flower planted with care 🌸")

    if st.session_state.opened_promise:
        st.markdown(
            """
            <div class="card" style="text-align:center;">
                <div class="big-emoji">🌱🌷🌸</div>
                <h3>Growing takes time.</h3>
                <p>
                    Just like a flower, trust needs patience,
                    consistency, and room to grow.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
