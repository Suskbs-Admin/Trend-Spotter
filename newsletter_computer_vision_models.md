# 👁️ VISION CURRENTS — Issue #47
**Late November 2025 | The Computer Vision Intelligence Brief**

*Hey reader,*

Something shifted this week in computer vision. Not a single breakthrough — but a pattern. Foundation models aren't just getting bigger; they're **absorbing entire pipelines**. Segmentation, detection, tracking used to be three different problems. This week, Meta shipped one model that does all three. Robotics used to be five modules. Now it's one neural network. Image gen used to require an IP-Adapter sandwich. Now it's one forward pass.

That's the through-line. Everything else is detail.

Let's get into it.

---

## 🔥 THE THREE TRENDS EVERY CV ENGINEER IS TALKING ABOUT

### **#1 — SAM 3: "Has Anyone Else Felt Like Segmentation Is... Solved?"**

Meta dropped SAM 3 on **November 19**. Seven days later, the field is still arguing about it.

The innovation has a name — **Promptable Concept Segmentation (PCS)** — and it's more important than it sounds. Until now, segmentation meant clicking on one object. SAM 3 lets you type *"the one red car"* (or paste an example image) and get **persistent, tracked masks for every matching instance across an entire video**.

Detection + segmentation + tracking — three problems that used to require three models — collapsed into one prompt.

**Why this matters more than the benchmarks:**

The killer app isn't prettier masks. It's **labelling economics**. Every CV team on Earth burns 60–80% of project time on annotation. The r/computervision "Auto-labelling datasets with SAM 3" thread isn't excitement — it's relief. Roboflow, Ultralytics, and Voxel51 all shipped same-week integrations. When tooling vendors integrate on day one, you're looking at infrastructure — not a model.

**The contrarian take:** SAM 3 isn't a *better* model. It's a **new API for the segmentation layer**. And APIs are sticky in a way benchmarks aren't. Nobody asks "which cuDNN should I use?" — they just use cuDNN. SAM is heading the same direction.

**One number that landed:** 900+ citations within days of release. Citation velocity ≠ correctness, but it does tell you which papers the field is going to spend the next year arguing about.

🔗 Meta Research · arXiv 2511.16719 · GitHub: `facebookresearch/sam3`

---

### **#2 — FLUX.2 [dev]: The 32B Model That Everyone's Mad About**

Black Forest Labs released FLUX.2 on **November 25**. It's a 32-billion-parameter flow-matching transformer that does generation, single-reference editing, and **multi-reference composition** (up to 10 input images blended coherently) in one architecture.

The community reaction split sharply within 48 hours:

- **The fans:** *"Finally, gen + edit in one model without the ControlNet hack-stack."*
- **The critics:** *"32B parameters feels deliberately too big to run locally. The open release is open in name only."*

Both are correct.

**The real unlock isn't the parameter count.** It's that **multi-reference composition works**. Previously, blending three reference images into one coherent output required IP-Adapter + multiple ControlNets + manual compositing. Now it's one prompt. That's a UX collapse, not a benchmark bump.

**The strategic catch:** The non-commercial license is a tell. BFL is monetizing the Pro API and using open weights for mindshare. The "open" in "open weights" is a marketing surface. Meanwhile, Z-Image Turbo and Chroma are pushing the *efficient* frontier — meaning the headline 32B model will be SOTA for maybe 2–3 months before the next 32B competitor lands.

**My read:** Real technical achievement. Genuine architectural step. But image generation is **commoditizing at a brutal pace**. SAM has held the segmentation SOTA for 2+ years between major releases; FLUX will not have that runway.

🔗 BFL Blog · Hugging Face · r/StableDiffusion Debate Thread

---

### **#3 — VLA Models: The Most Asymmetric Bet in AI Right Now**

**Vision-Language-Action models** — single neural networks that map camera pixels + natural language → robot joint torques — went from "interesting research" to "structural shift" this quarter.

The freshest contribution: **EvoVLA** (Nov 19), which cuts stage-hallucination on long-horizon manipulation tasks from **38.5% → 14.8%**. That sounds incremental. It's not — it's evidence that long-horizon robot reasoning is becoming tractable.

**Why this is the trend I'd bet a fund on:**

1. **The hardware finally shipped.** Figure, 1X, Apptronik, Unitree, Tesla Optimus — humanoids are in commercial pilots *this year*, not 2030.
2. **The data flywheel closed.** NVIDIA Cosmos + world foundation models mean robotics teams can now train manipulation policies on **mostly synthetic visual data**. Iteration costs just collapsed.
3. **Capital has converged.** Physical Intelligence ($400M+), Figure ($700M+), Skild AI, DeepMind robotics — more money is behind embodied AI in 2025 than ever before in the field's history. When this much capital aligns on one paradigm, the paradigm persists.

**The honest caveats:** No VLA has yet demonstrated reliable 8-hour warehouse deployment. Every demo is a curated video. The TAM is real but back-loaded to 2030+. And if Tesla/Figure each ship proprietary VLA stacks, the open generalist thesis (OpenVLA, EvoVLA) may lose the ecosystem to closed platforms.

But the asymmetry is what matters. Downside: "we waited 3 years." Upside: a decade of platform rents.

🔗 EvoVLA Paper · VLA Survey · NVIDIA Cosmos

---

## 📊 THE BIGGER PICTURE

Here's what unifies these three releases — and what it means for your roadmap:

| Old World | New World |
|---|---|
| Detection → Segmentation → Tracking (3 models) | One concept prompt (SAM 3) |
| Generation + Edit + Composition (hack-stack) | One forward pass (FLUX.2) |
| Perception → Planning → Control (5 modules) | One neural network (VLA) |

**Foundation models are eating vertical pipelines.** The competitive question is no longer "how do I build a better detector / generator / motion planner?" It's **"which foundation-model primitive do I build on top of, and what vertical value do I capture?"**

The companies that win 2026–2030 will be the ones that treat SAM, FLUX, and VLAs as **commodity infrastructure** — and build differentiated value on top via vertical data, deployment tooling, hardware integration, and trust guarantees.

The companies that lose will be the ones still competing on the foundation models themselves.

---

## 👀 WHAT TO WATCH NEXT WEEK

These almost cracked the top 3 — keep them on your radar:

- **YOLO26** — Ultralytics' NMS-free edge detector. 43% faster on CPU than YOLO11. Community is loud but divided on real-world gains.
- **Qwen3-VL** — Alibaba's open multimodal LLM. Quietly dominant for OCR, GUI agents, and manga translation. The "daily driver" VLM for many local workflows.
- **Feed-Forward 3D Gaussian Splatting** — NeurIPS/ICLR pipelines (LocoMoco, FCGS, GIFSplat) making 3DGS work in sparse-view, real-time settings. AV and avatar applications heating up.

---

## 🎯 THE CALL TO ACTION

Three things, depending on what you do:

**If you're a CV practitioner:**
→ **Run SAM 3 on your hardest labelling pipeline today.** Don't read another paper about it. The auto-labelling demo is the strongest ROI you'll see this quarter. Clone `facebookresearch/sam3`, point it at your worst dataset, and measure hours saved.

**If you're building tooling or infrastructure:**
→ **Pick one of these three primitives and build the workflow layer on top.** The foundation models will be free within 12 months. The workflows around them (eval harnesses, deployment SDKs, dataset curation tools, robotics middleware) will not.

**If you're allocating capital or hiring:**
→ **Bet on the VLA ecosystem.** Not on the foundation models themselves — on the vertical-specific applications (warehouse manipulation, surgical robotics, agricultural robotics) where domain data is the defensible moat. The generalist VLA will commoditize by 2027. The vertical specialist won't.

---

## 📚 DEEP DIVES (If You Want to Go Further)

- **SAM 3 deep dive:** arXiv 2511.16719 · Meta blog · Ultralytics docs
- **FLUX.2 analysis:** BFL official · Greg Robison technical breakdown · WaveSpeed deployment guide
- **VLA state of play:** EvoVLA project page · OpenVLA paper · VLA Survey 2025

---

*That's the week. Foundation models are eating the stack. Pick yours.*

**— The Vision Currents Team**
*Reply to this email. We read everything. Tell us what you're building.*

---

*You're receiving this because you signed up for Vision Currents, the weekly intelligence brief on computer vision models, trends, and infrastructure. [Forward to a colleague] · [Manage preferences] · [Unsubscribe]*