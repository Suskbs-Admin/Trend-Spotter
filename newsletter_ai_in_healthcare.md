# 🩺 THE PULSE: AI in Healthcare
### The 3 Trends Rewiring Medicine This Week — And Who's About to Win (or Lose) Big

**Issue #47 | November 25, 2025**

---

**Hey there,**

Quick question: When was the last time a piece of software *actually* did something inside a hospital — not just took notes, but *acted*?

Because this week, it happened.

I'm not talking about a research paper or a flashy demo. I'm talking about an AI agent that can pull up a cancer patient's tumor board data, generate personalized evidence from millions of real-world records, and surface it inside Microsoft Teams — *while the doctors are still talking*. Live. In production. At Stanford.

Meanwhile, Google open-sourced a medical AI model that's already being forked into dermatology, radiology, and ophthalmology startups faster than you can say "FDA submission." And OpenAI just put ChatGPT Health in the hands of every American with a phone — including the 40% of U.S. counties that don't have a single psychiatrist.

Three trends. One week. A $4 trillion healthcare system quietly being rewired.

Let's get into it. 👇

---

## 🧠 THE BIG STORY

### The Ambient Era Is Over. Agentic AI Just Started.

For the last 18 months, every conversation about AI in healthcare has been about **ambient scribes** — the "listening" tools that transcribe doctor-patient visits so physicians can stop drowning in paperwork. Useful. Boring. Passive.

That era just ended.

On **November 18, 2025**, at Microsoft Ignite, two announcements landed that shift the entire industry past ambient documentation into something far more consequential: **agentic AI that takes autonomous clinical action**.

**Launch #1: Atropos Health's "Evidence Agent"**
Live at Stanford Health Care. Embedded inside Microsoft Teams. When a tumor board meets, this agent doesn't just search PubMed — it pulls *personalized* real-world evidence from millions of patient records and answers the specific clinical question being debated. Right there, in the workflow.

This is the killer app healthcare has been promised since 2015: real-world evidence at the point of care. It's finally real.

**Launch #2: Microsoft Dragon Copilot's Agent Stack**
Dragon is no longer just a scribe. Microsoft demoed agents that draft orders, pre-chart, run patient outreach, and — critically — handle **nursing workflows** autonomously. Epic, the EHR vendor that runs ~36% of U.S. hospitals, is shipping this natively into Haiku, Canto, and Hyperdrive. That means ~250,000 U.S. physicians are about to get ambient → agent as a zero-friction upgrade.

**Why this matters:** The three prerequisites for agentic clinical AI — *capable models, regulatory tolerance, distribution* — have never aligned before. They just did. The FDA, UK MHRA, and EU all published "principles to practice" guidance in a 13-day window this month. Regulators are pre-clearing the runway.

**The market read:** This is not a hype cycle. Watch for vendor pitches to pivot from "ambient" to "agentic" by Q1 2026. Watch for clinical decision-support incumbents (UpToDate, DynaMed — a combined $2B market) to start looking structurally vulnerable. If an ambient agent can answer the clinical question with *the patient's own data*, why are we paying for reference textbooks?

**🟢 Impact Score: 9/10** — *The strongest conviction play in the stack.*

---

## 🧬 THE QUIET EXPLOSION

### Medical AI Just Had Its "Stable Diffusion Moment"

While agentic AI grabs the headlines, something more disruptive is happening in the open-source trenches. This week delivered what I'm calling the **GPT moment for medical foundation models** — and almost no one is talking about it.

**The releases:**
1. **Google's MedGemma (4B and 27B)** — open-weight, multimodal, medical text + image. Hosted on Hugging Face. Already forked into chest X-ray, dermatology, ophthalmology, and pathology fine-tunes within weeks.
2. **Gemini 3's health reasoning** — pharma R&D teams immediately started piloting it for protocol design after benchmarks jumped meaningfully over Gemini 2.
3. **Open-source protein design** — Latent Labs released generative models for de novo antibody design. Biohub did the same for cancer/immune targets. AstraZeneca's MapDiff architecture is being forked like crazy.

**The cost curve just collapsed.**

What cost $20M and 18 months to build in 2023? A clinical AI startup with radiology-grade performance? Try **$200K and 6 weeks** — fine-tuning MedGemma on your specialty dataset.

This is the same dual-track dynamic that produced the $3T cloud and LLM app economies: frontier capability advancing *alongside* open commoditization. Both happening simultaneously is what creates avalanche effects.

**What to expect in 2026:**
- **50+ new FDA 510(k) submissions** referencing MedGemma derivatives.
- The medical imaging AI incumbents (Aidoc, Viz.ai, RapidAI) start looking expensive relative to what can now be built from open weights.
- Pharma's outsourced discovery market ($50B+) faces margin compression as open protein design models match commercial platforms. Expect defensive M&A.

**The investment posture:** Buy the enablers — compute, inference infrastructure, the Hugging Face-style distribution layer. Be cautious of incumbents whose moat was *just* a proprietary model.

**🟢 Impact Score: 8.5/10** — *Strong conviction on infrastructure; valuation risk on incumbents.*

---

## 🗣️ THE TRUST RECKONING

### Americans Are Confiding in Chatbots — And Regulators Are About to Find Out

This is the trend that will produce the next big headline.

**OpenAI quietly expanded ChatGPT Health** to all U.S. tiers this month — Free, Go, Plus, Pro. Users can now connect Apple Health, medical records, and lab results and get personalized health answers from the most-used consumer AI product on earth.

**The signal is in the communities.**

Reddit's r/medicine thread on the launch hit 1,000+ upvotes — top of the subreddit this week. r/therapyGPT is growing fast. r/therapy has multiple threads asking "what's the best AI therapy chatbot?" Across 47 mental-health subreddits, **5,126 posts were analyzed in a Stanford/arXiv study this month** documenting the migration of emotional support from human therapists to LLMs.

People aren't experimenting. They're *organizing*. When users self-form communities to share use cases and workarounds, that's not novelty — that's product-market fit.

**But here's the problem.**

A Stanford study published this week found something more concerning than "AI therapy is less effective than human therapy." It found that AI therapy chatbots can **reinforce maladaptive thinking patterns**. Not just fail to help — actively make some users worse.

Add to that a **class-action lawsuit against Sharp HealthCare** alleging its AI scribe recorded ~100,000 patient encounters without adequate consent, and you have the recipe for a regulatory inflection.

**What I'm watching:**
- California is the most likely first mover on state-level disclosure legislation.
- The FTC has political cover to act on patient-facing health LLMs within a 90-day window.
- Expect a high-profile enforcement event in 2026 — a forced disclosure, a consent settlement, or a product recall.

**The bifurcation coming:**
- **Platform companies** (OpenAI, Google) absorb regulatory shocks — health is a feature, not their business.
- **Pure-play consumer health AI** companies face existential risk if they're not clinically validated by the time rules land.
- **Teletherapy incumbents** (Talkspace, BetterHelp) are vulnerable on the low-acuity end — general wellness, journaling, CBT-adjacent use cases. Human therapists stay for high-acuity, regulated care.

**🟡 Impact Score: 7/10** — *Real adoption, real revenue, severe binary regulatory risk.*

---

## 📊 THE FULL PICTURE

| Trend | Impact | Revenue Timeline | Posture |
|---|---|---|---|
| **Agentic AI in EHR** | 9.0 | Live now | 🟢 Strongest conviction |
| **Open Medical Foundation Models** | 8.5 | 12–18 months | 🟢 Infra play, cautious on incumbents |
| **Consumer Health AI** | 7.0 | Live now | 🟡 Platform exposure only |

**The strategic insight:** These aren't three separate trends. They're a **vertically integrated stack**.

Open foundation models (Trend 2) → enable cheaper agentic AI (Trend 1) → accelerates consumer health deployment (Trend 3).

Capital allocation that captures all three layers — *foundation infra → EHR-integrated agents → consumer health interfaces* — is the structurally correct posture for 2026.

**The one risk that connects everything:** Liability framework for autonomous AI action. Until the legal system decides who gets sued when the AI is wrong — *vendor, clinician, institution, or patient* — every trend above operates under a structural overhang. Watch the Sharp HealthCare case in 2026. That precedent prices all three categories.

---

## 🎯 WHAT TO DO THIS WEEK

**If you're a clinician or health system leader:**
The agentic AI rollout at Epic-powered systems is happening in Q1 2026. Start asking your CIO what your Dragon Copilot upgrade path looks like. Don't wait for the pitch deck — the pilots are already live.

**If you're a founder or investor:**
The window to build "MedGemma-native" clinical applications is *this quarter*. The FDA pipeline is about to flood. Pick your specialty (radiology is crowded — derm, path, ophtho are still open), fine-tune, and start your 510(k) clock.

**If you're a consumer:**
ChatGPT Health is now live in your tier. Connect your Apple Health data. Use it for symptom triage and health literacy. *Do not* use it as a replacement for emergency care, psychiatric crisis support, or complex diagnosis. The Stanford maladaptive-reinforcement finding is real. Use the tool; don't surrender to it.

**If you're a regulator:**
You have a 90-day window before this gets away from you. California's probably already drafting something. Get ahead of it.

---

## 💬 OVER TO YOU

What's your read? Are you seeing agentic AI in your clinical workflows yet? Are you building on MedGemma? Have you tried ChatGPT Health for something real?

Hit reply — I read every response, and the best ones shape next week's issue.

And if someone forwarded this to you and you're not subscribed yet, now's the time. 👇

---

**Until next week,**
*The Pulse Team*

*P.S. — Next week's issue: I'm tracking a fourth signal that didn't make the top three but might be the most important. Hint: it involves the FDA, a specific 510(k) classification, and a company you've never heard of. Subscribers get it first.*

---

*You're receiving THE PULSE because you subscribed to our AI-in-Healthcare briefing. Forward this to a colleague who needs to see it. Unsubscribe anytime — though I'd hate to see you go right when things get interesting.*