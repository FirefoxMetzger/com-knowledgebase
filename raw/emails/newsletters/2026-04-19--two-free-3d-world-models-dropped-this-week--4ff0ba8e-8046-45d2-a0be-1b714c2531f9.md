---
{
  "source": "inkbox-mailbox-cli",
  "id": "4ff0ba8e-8046-45d2-a0be-1b714c2531f9",
  "message_id": "<wLLgCxXcR4uLO0-O41xWUQ@geopod-ismtpd-8>",
  "thread_id": "15647cf0-ef8c-4155-9d3f-31c2a5262daf",
  "direction": "inbound",
  "from": "theneuron@newsletter.theneurondaily.com",
  "to": "sally.anderson@inkboxmail.com",
  "subject": "😺 Two free 3D world models dropped this week",
  "created_at": "2026-04-19T20:04:31.355355+00:00",
  "fetched_at": "2026-04-22T18:31:11.149412+00:00",
  "is_read": false,
  "has_attachments": false,
  "is_newsletter": true
}
---

[Sign Up](https://www.theneurondaily.com/) · [Advertise](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=4-ais-walk-into-a-bar&_bhlid=c12e6376a5113e8ca182419c6baf9cb285e564b7)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/92abfa98-ca3f-42ad-8e53-ee4ddb5c9869/Gemini_Generated_Image_ftzus5ftzus5ftzu.png?t=1775272660)
Follow image link: (https://www.theneurondaily.com/)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ba0270b6-4b44-42b5-a01e-a9ccd97c855a/In_Partnership_with_Arm.png?t=1775827923)
Follow image link: (https://www.arm.com/company/arm-everywhere?utm_source=neuron&utm_medium=display&utm_content=banner_static_logo_more&utm_campaign=mk35_cloudai_cloud-ai_thirdparty_mediabuy_na)
Caption: 

Welcome, humans. 

Good news! You can now hire your robot dog to take your actual dog for a walk! 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6af65a84-4185-49ea-b3d4-af50f92790d9/Screenshot_2026-04-16_at_11.10.12_PM.png?t=1776406444)
Follow image link: (https://youtu.be/LP4-c5AK30g?si=GaldvKWBASLPcu77)
Caption: IDK why but this is giving 90s sled dog rescue movie Balto, which slaps

Bad news… _you might never see either of them again… follow the northern lights home, Balto! _

Moving on! **Time for a check in**: What tools are y’all using? Has your “daily driver” (_the AI you use every day for your typical AI use cases) _changed lately, or stayed the same? Fill out the poll below and let us know, and we’ll share everyone’s answers in tomorrow’s blurb. 

A side benefit to answering this poll? _If we know what tools you all are actually using on a daily basis, it’ll help guide us on what we decide to cover more or less often! _

**Here’s what happened in AI today: **

* 😼 Two Chinese giants and NVIDIA shipped world models the same week; only two of them open-sourced theirs.

* 📰 Factory raised $150M at a $1.5B valuation for autonomous coding agents.

* 📰 OpenAI launched GPT-Rosalind, its first frontier reasoning model built for life sciences.

* 🍪 NVIDIA's Lyra 2.0 turns a single image into a 3D world you can fly through.

* 🎓 The "trust battery" method for giving your AI employee escalating autonomy.

**P.S:**_ Want to reach 675,000 AI-hungry readers? __[Click here to advertise with us. ](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_

**P.P.S: **_Love robots? We’re starting a new robotics newsletter! __[Sign up early here](https://form.jotform.com/260897013570156)__._

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4846c203-f27d-4487-99c7-60003fe4dfdc/image.png?t=1772213604)
Caption: 

# 😼 Two Open World Models Shipped This Week. Alibaba Waitlisted Theirs.

Three AI giants shipped navigable 3D worlds this week. Each one picked a different strategy:

Tencent open-sourced HY-World 2.0 on Hugging Face (the place to download and run your own AI models) with a full commercial license; take it, build on it, sell it. NVIDIA dropped Lyra 2.0 there too, but stamped it "research-only." And Alibaba, previously known for its popular open-source models, launched its new system behind a waitlist.

**Here's what happened:**

* [Tencent open-sourced HY-World 2.0](https://huggingface.co/tencent/HY-World-2.0), a multi-modal 3D world model that turns text, images, or video into editable 3D scenes (meshes and 3D Gaussian splats, a rendering method that uses fuzzy 3D "blobs" to represent scenes) you can drop straight into Unity, Unreal, or Blender. 

  * Available w/ full commercial license. Code, weights, and a Gradio demo are all live on[ GitHub](https://github.com/Tencent-Hunyuan/HY-World-2.0).

* [NVIDIA dropped Lyra 2.0](https://huggingface.co/nvidia/Lyra-2.0) on Hugging Face the same week, a 14B framework that turns a single 480×832 image into a persistent, explorable 3D Gaussian scene you can fly through in real time ([paper](https://arxiv.org/abs/2604.13036),[ project page](https://research.nvidia.com/labs/sil/projects/lyra2/)). 

  * License caveat: research use only, no production, no commercial output.

* [Alibaba launched Happy Oyster](https://www.bloomberg.com/news/articles/2026-04-16/alibaba-releases-new-ai-model-for-gaming-development) the same day Tencent open-sourced HY-World 2.0. It has two modes (Directing steers a generated scene in real time for up to 3 minutes at 480p or 720p; Wandering lets you move through a generated world for up to 1 minute via WASD). 

  * **Catch:** limited early access, not open weights. Alibaba wants to monetize world-model compute through its cloud.

* If it means something to ya, HuggingFace's[ Merve Noyan paired HY-World 2.0 and Lyra 2.0](https://x.com/mervenoyann/status/2044721463316340765) as the week's two most important open-weight 3D drops.

**Why this matters:** “World models”, meaning in this case AI systems that understand 3D space, physics, and object permanence well enough to generate navigable environments, are becoming foundational infrastructure for robotics, game development, VR, and autonomous vehicles. 

Until this week, the best work was locked behind Google DeepMind's Genie paywall, Fei-Fei Li’s World Labs API, or NVIDIA's enterprise tooling. Now game studios, indie devs, and robotics researchers can pull commercial-use weights off Hugging Face for free. The cost of entry dropped by several orders of magnitude in 48 hours.

**Our take:** The real signal here is the open-vs-closed divide: 

* Tencent went fully open (commercial license, run it anywhere) because it's playing the long game: commoditize the layer, profit on the applications. 

* NVIDIA went research-only because it wants researchers experimenting freely without cannibalizing its Omniverse business. 

* Alibaba went closed-early-access because its goal is Alibaba Cloud revenue, the same playbook it's running with Happy Horse video. 

We believe open tools will win on sheer adoption, allowing commercial applications to be built on top of it. But more importantly, we believe world models like these will be the foundation for generating consistent, coherent, 3D worlds for games and eventually movies, too. _Love to see the progress! _

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7cf99573-4593-460e-bb90-7154a8d863f4/image.png?t=1765839774)
Caption: 

**FROM OUR PARTNERS**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/af750838-3ce8-4ece-a0ef-90b9319dece9/ARM.png?t=1776432238)
Follow image link: (https://www.arm.com/company/arm-everywhere?utm_source=neuron&utm_medium=display&utm_content=banner_static_logo_more&utm_campaign=mk35_cloudai_cloud-ai_thirdparty_mediabuy_na)
Caption: 

More than 50 companies are backing Arm’s move into silicon — spanning cloud, chip design and software.

From AWS, Google and Microsoft to NVIDIA, Samsung, SK hynix and TSMC, the ecosystem signals a broader shift in how AI infrastructure is being built.

Rather than isolated components, the stack is becoming more tightly integrated — from architecture through to deployment.

Explore how this is taking shape: [Arm Everywhere keynote](https://www.arm.com/company/arm-everywhere)﻿

[FIND OUT MORE](https://www.arm.com/company/arm-everywhere?utm_source=neuron&utm_medium=display&utm_content=banner_static_logo_more&utm_campaign=mk35_cloudai_cloud-ai_thirdparty_mediabuy_na)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/9f01d906-b564-444f-a00a-4c4fae2b042e/image.png?t=1769038568)
Caption: 

# 🎓 AI Skill of the Day: Give Your AI Agent a "Trust Battery" Before Handing It Real Autonomy

[Builder Nityesh just shared](https://x.com/nityeshaga/status/2044864114682741134) the cleanest framework we've seen for scaling how much you let an AI agent do unsupervised. He calls it a "trust battery," borrowed from Shopify CEO Tobi Lütke's concept for human work.

**The core idea:** Every new AI agent starts at 20%. The battery charges with clean execution and thoughtful anticipation; it drains every time you repeat yourself. Only hand the agent tasks that match its current charge:

1. **20-40% (Pair mode):** You review every output. For money, clients, or permanent side effects.

2. **40-60% (Async with checkpoints):** Agent works alone, stops at key decisions.

3. **60-80% (Full delegation with audit):** Agent runs end-to-end; you spot-check the next morning.

4. **80%+ (Autonomous):** Agent decides when to ask.

**The part that makes it work:** run a nightly reflection against everything the agent did that day.

```
Review today's task outputs. For each one: (1) rate execution quality 1-5,(2) flag any repeated corrections from me, (3) propose one update to your CLAUDE.md or system prompt that would prevent the correction next time, and (4) decide whether your trust battery should go up, down, or flat. Output a single JSON summary I can paste into our ops doc tomorrow.
```
Drop it in a Claude Routine scheduled for midnight. Every morning you'll see whether your agent earned more autonomy overnight, and the self-updating [CLAUDE.md](https://CLAUDE.md) loop means it keeps improving without you rewriting prompts.

_Total AI beginner?_[ Start here.](https://www.theneuron.ai/explainer-articles/everything-we-covered-in-our-ai-for-total-beginners-livestream-full-guide-with-timestamps/)

_Have a specific skill you want to learn? __[Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)__ _

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/abf3b639-ca99-484e-992a-9cf6d8687a54/image.png?t=1765839770)
Caption: 

# Replay: We Tested Claude Opus 4.7 LIVE

On Thursday morning, hours after Anthropic shipped Opus 4.7, Grant and his dev friend Kyle went [live on YouTube](https://www.youtube.com/live/v3UJKcoD2Qk) to stress-test the new model in real time. They pushed the upgraded vision through a Final Fantasy Tactics sprite redesign, dug into the suspicious benchmark drops that back Nick Saave's theory that 4.7 is a distilled Mythos Preview,  and caught Claude Code silently farming work to Haiku sub-agents. Learn Kyle's three-model workflow for squeezing more intelligence out of fewer tokens, and watch out for the long-context regression nobody's talking about. 

**🎧 Watch the replay on:****[ YouTube](https://www.youtube.com/live/v3UJKcoD2Qk)**** |**[** LinkedIn**](https://www.linkedin.com/feed/update/urn:li:activity:7450576650863349761)** | **[**Read the blog companion here**](https://theneuron.ai/explainer-articles/opus-47-live-test-the-vision-upgrade-the-long-context-drop-and-why-the-mythos-theory-keeps-adding-up/)**.**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/31dbfaac-0721-4c34-b8e5-557c4a7cb3ca/image.png?t=1765839671)
Caption: 

# 🍪 Treats to Try 

_*Asterisk = from our partners (only the first one!). _[_Advertise to 700K+ readers here_](https://info.technologyadvice.com/advertise-with-the-neuron)_!_

1. [Nous Portal's Tool Gateway](https://x.com/NousResearch/status/2044878344592699744) bundles 300+ models plus web scraping, browser automation, image generation, cloud terminal, and text-to-speech into one subscription with no separate API keys —paid only (Nous Portal subscription; trial available).

2. [Mozilla Thunderbolt](https://www.phoronix.com/news/Mozilla-Thunderbolt) is an open-source, self-hosted enterprise AI client letting organizations chat, search, research, and automate workflows across any models or data pipelines with full sovereignty, on web plus native apps —free and open source.

3. [QuiverAI](https://app.quiver.ai/) lets you sketch, prompt, or describe a design and get editable vector output back (SVGs you can actually modify, not static bitmaps) —free public beta, open signup.

4. [Sam](https://www.withsam.com/) is a voice-first AI companion that sits in a senior's home doing daily check-ins, holding smart conversations, and sending real-time alerts to family when something seems off; pitched as safety plus connection instead of another gadget —paid (check site for pricing).

5. [CodeBurn](https://github.com/AgentSeal/codeburn) is an interactive TUI cost dashboard for Claude Code, Codex, and Cursor that shows exactly where your AI coding tokens go at the task level —free, open source.

6. [MacMind](https://github.com/SeanFDZ/macmind) is a complete single-layer transformer (embeddings, positional encoding, self-attention, backpropagation, gradient descent) implemented entirely in HyperTalk, the scripting language Apple shipped with HyperCard in 1987, running on a 1989 Mac —free, open source, absurdly nostalgic.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/abf3b639-ca99-484e-992a-9cf6d8687a54/image.png?t=1765839770)
Caption: 

# 📰 Around the Horn 

* [Proximal Labs launched FrontierSWE](https://x.com/_rajanagarwal/status/2044876210098802744), an open ultra-long-horizon coding benchmark with 20-hour budgets on real tasks like optimizing video-rendering libraries; even GPT-5.4 and Opus 4.6 rarely finish in time.

* [Lucy Shi shared π0.7](https://x.com/lucy_x_shi/status/2044853335354913195), a new steerable generalist robot model showing emergent compositional generalization from diverse training data: zero-shot shirt folding on unseen UR5e arms, operating an air fryer from verbal coaching alone ([blog](https://www.pi.website/blog/pi07)).

* [Adobe data shared via TechCrunch](https://techcrunch.com/2026/04/16/ai-traffic-to-us-retailers-rose-393-in-q1-and-its-boosting-their-revenue-too/) shows AI traffic to US retail sites rose 393% in Q1 2026 (up 269% in March alone), and AI-sourced shoppers convert better and spend more than non-AI visitors.

* [Roblox's AI assistant got agentic tools](https://techcrunch.com/2026/04/16/robloxs-ai-assistant-gets-new-agentic-tools-to-plan-build-and-test-games/): Planning Mode turns prompts into editable action plans, Mesh Generation and Procedural Model Generation build assets, and self-correcting playtesting agents close the loop for end-to-end game creation.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a000e4e0-4bc0-400d-8af9-0777155f6578/image.png?t=1765839850)
Caption: 

**FROM OUR PARTNERS **

### Are you tracking agent views on your docs?

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c9470934-6719-487e-8a20-a7225256bf33/Frame_2018778052.png?t=1773434539)
Follow image link: (https://www.mintlify.com/use-cases/developer-documentation/?utm_campaign=YJ4ZPRQDHV&utm_source=beehiiv&utm_medium=newsletter&utm_content=AI%20traffic%2C%20Mar%20-%20Secondary&_bhiiv=opp_32bc2363-6398-4c33-a8b6-6bb20cca0af9_71696469&bhcl_id=ca35f0ca-b51a-457b-9dd8-d446bd0f626b_3c85c7a0-63c3-4ac6-a4e9-0f8a1c17f957_e63657e5-d3a9-4224-83cf-d530b54d0e07)
Caption: 

AI agents already outnumber human visitors to your docs — now you can track them.

[See your AI traffic!](https://www.mintlify.com/use-cases/developer-documentation/?utm_campaign=YJ4ZPRQDHV&utm_source=beehiiv&utm_medium=newsletter&utm_content=AI%20traffic%2C%20Mar%20-%20Secondary&_bhiiv=opp_32bc2363-6398-4c33-a8b6-6bb20cca0af9_71696469&bhcl_id=ca35f0ca-b51a-457b-9dd8-d446bd0f626b_3c85c7a0-63c3-4ac6-a4e9-0f8a1c17f957_e63657e5-d3a9-4224-83cf-d530b54d0e07)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c8f9d58e-efb0-48ea-a3e4-1397bafab601/image.png?t=1765839750)
Caption: 

# 🌟 Sunday Special: The Week in Five Stories

Catching up after a week of touching grass? Here's what mattered.

1. [Anthropic shipped Opus 4.7. OpenAI countered hours later.](https://www.anthropic.com/news/claude-opus-4-7) Vision jumped to 82.1%, SWE-bench Pro to 64.3%, and a hidden new tokenizer quietly raised your Claude bill up to 35%. 

2. OpenAI's[ Codex overhaul landed the same afternoon](https://openai.com/index/codex-for-almost-everything/) with Mac computer use, 111 plugins, and scheduled automations ([Full breakdown](https://www.theneuron.ai/explainer-articles/openai-just-turned-codex-into-a-desktop-superapp/)).

3. [Canva declared itself an AI platform with design tools.](https://www.capitalbrief.com/briefing/biggest-transformation-yet-canva-launches-canva-ai-20-1d30d156-ebb2-44ff-b3e9-47061541c523/) COO Cliff Obrecht said the quiet part aloud onstage: _"Until now, Canva has been a design platform with AI tools. Now we become an AI platform with design tools."_ 

4. Same day,[ Anthropic CPO Mike Krieger quit Figma's board](https://techcrunch.com/2026/04/16/anthropic-cpo-leaves-figmas-board-after-reports-he-will-offer-a-competing-product/) ahead of Anthropic shipping competing design software (more on that tomorrow).

5. [OpenAI launched GPT-Rosalind](https://openai.com/index/introducing-gpt-rosalind/), a frontier reasoning model built for biology, drug discovery, and translational medicine, deployed under trusted-access terms to Moderna, Amgen, the Allen Institute, and Thermo Fisher. _The biggest shift since OpenAI started naming models after historical figures._

[Want the rest of the top 10 of the week (Top 10 Stories & Tools), plus new stuff from this weekend? Read our weekend Around the Horn Digest here.](https://theneuron.ai/newsletter/around-the-horn-digest-everything-that-happened-in-ai-this-weekend-friday-sunday-april-17-19-2026/) 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7a022a39-ae81-44c4-8a3d-bb7b8779404f/image.png?t=1772214166)
Caption: 

# A Cat’s Commentary 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/d467d524-10c6-44f3-b5b1-c98c009b14a5/A_Cat_s_Commentary_x_2025__14_.png?t=1774367772)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4846c203-f27d-4487-99c7-60003fe4dfdc/image.png?t=1772213604)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. 




**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).  


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/two-free-3d-world-models-dropped-this-week
