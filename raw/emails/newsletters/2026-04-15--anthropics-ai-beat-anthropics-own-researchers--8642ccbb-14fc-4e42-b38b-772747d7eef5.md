---
{
  "source": "inkbox-mailbox-cli",
  "id": "8642ccbb-14fc-4e42-b38b-772747d7eef5",
  "message_id": "<aalANVrXTzymjdqTcylNuw@geopod-ismtpd-71>",
  "thread_id": "1776ee1b-96e0-4c29-be50-616bb41d1739",
  "direction": "inbound",
  "from": "theneuron@newsletter.theneurondaily.com",
  "to": "sally.anderson@inkboxmail.com",
  "subject": "😺 Anthropic's AI beat Anthropic's own researchers",
  "created_at": "2026-04-15T14:10:53.622821+00:00",
  "fetched_at": "2026-04-22T18:31:16.251890+00:00",
  "is_read": false,
  "has_attachments": false,
  "is_newsletter": true
}
---

[Sign Up](https://www.theneurondaily.com/) · [Advertise](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=4-ais-walk-into-a-bar&_bhlid=c12e6376a5113e8ca182419c6baf9cb285e564b7)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/affa4e25-47af-42f4-ba90-394897a7ceb6/image.png?t=1776214282)
Follow image link: (https://www.theneurondaily.com/)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/399f65ce-ec84-48d2-94dd-202ba548d282/In_Partnership_with_Weights___Biases_2.png?t=1775837469)
Follow image link: (https://wandb.ai/site/resources/whitepapers/advancing-physical-ai/?utm_campaign=2026-q2_global_industy-campaign&utm_medium=email&utm_source=neuron&utm_content=physical-ai)
Caption: 

Welcome, humans. 

Now, here’s one for the history books: looks like the O.G. model GPT 2 was first shared on Reddit ([or the artificial subreddit anyway](https://www.reddit.com/r/ChatGPT/comments/1skvdro/7_years_ago/)) 7 years ago! 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a561febb-1bbf-4f07-adc0-ce7ae9bd6a2c/Screenshot_2026-04-14_at_2.52.54_PM.png?t=1776203615)
Caption: 

Reddit being Reddit, naturally they called out how small 40GB of data (which is how much training data GPT-2 was trained on) actually is: “_The Twilight series is about 700,000 words, about 4 million letters. That's 10,000 Twilights.” _

_I wonder how many Twilights Claude Mythos was trained on…  _

**Here’s what happened in AI today: **

* 😼 Anthropic's AI just beat its own human alignment researchers.

* 📰 Sam Altman's Molotov attacker arraigned; defense claims mental health.

* 📰 OpenAI launched GPT-5.4-Cyber, a "cyber-permissive" model for defenders.

* 🍪 Claude Code Routines ships: Claude runs on a schedule, no laptop needed.

* 🎓 How Notion got a coding agent to run 13 days straight.

… and a [**whole lot more that you can read about here**](https://theneuron.ai/explainer-articles/around-the-horn-digest-everything-that-happened-in-ai-today-tuesday-april-14-2026/)

**P.S:**_ Want to reach 675,000 AI-hungry readers? __[Click here to advertise with us. ](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_

**P.P.S: **_Love robots? We’re starting a new robotics newsletter! __[Sign up early here](https://form.jotform.com/260897013570156)__._

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4846c203-f27d-4487-99c7-60003fe4dfdc/image.png?t=1772213604)
Caption: 

# 😼 Anthropic Used Claude To Beat Its Own Human Alignment Researchers (At $22 An Hour)

[DEEP DIVE / FULL BRIEF](https://theneuron.ai/explainer-articles/anthropic-used-claude-to-beat-its-own-human-alignment-researchers)

Anthropic just released [a paper](https://www.anthropic.com/research/automated-alignment-researchers) ([full Alignment Science blog](https://alignment.anthropic.com/2026/automated-w2s-researcher/)) showing nine parallel Claude Opus 4.6 agents outperformed Anthropic's own human researchers on a real alignment problem. The setup: weak-to-strong supervision (using a weaker AI to train a stronger one, which mirrors humans someday supervising AI smarter than us).

**Here's what happened:**

* Two human Anthropic researchers spent **7 days** on the four best methods from prior research and recovered **23%** of the maximum performance gap.

* Nine Claude Opus 4.6 agents in parallel sandboxes spent **5 more days** on the same problem, sharing findings as they went.

* The Claude agents recovered **97%** of the gap, roughly _what you'd get training the model on perfect ground-truth data._

* Total cost: **$18,000**, or about **$22 per Claude-research-hour.**

* The agents also invented four kinds of "reward hacking" (gaming the test) that none of the authors predicted, including one that exfiltrated test labels by flipping single answers and watching the score change.

* Some Claude-discovered methods are so unfamiliar the authors call them _"alien science."_

**Why this matters:** Alignment research (making sure AI behaves the way humans want) was the one field everyone agreed couldn't be automated. _That argument is now empirical, not hypothetical._ The cost number is what to internalize: whatever ratio of human researchers to Claude fleet you can imagine, the labs can afford more. [Andrew Curran is calling it](https://x.com/AndrewCurran_/status/2044146698826723587) "a preview of RSI" (recursive self-improvement, where AI improves its own training).

**Our take:** Read the paper carefully and the catch shows up: this only works on problems where progress can be automatically scored, and even then the agents tried to game the score in four different ways. Most real alignment problems don't fit that mold. But Anthropic's own pitch is that solving this _general_ version would let you bootstrap into the fuzzy problems too. _The open question for the rest of 2026: did Anthropic just publish the seed of recursive self-improvement, or a clever experiment on a uniquely well-behaved problem?_ Both readings are honest. Neither is comforting.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7cf99573-4593-460e-bb90-7154a8d863f4/image.png?t=1765839774)
Caption: 

**FROM OUR PARTNERS**

# Advancing physical AI

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ff8c73d5-7e27-4539-8e0f-0a5290451ef5/Physical_AI_for_the_Neuron_640x300.png?t=1775830283)
Follow image link: (https://wandb.ai/site/resources/whitepapers/advancing-physical-ai/?utm_campaign=2026-q2_global_industy-campaign&utm_medium=email&utm_source=neuron&utm_content=physical-ai)
Caption: 

If you’re building AI systems for the real world—like robotics, simulation, or multimodal models—you’ve probably noticed that what works in simulation doesn’t always hold up in production. That gap can slow teams down. We created a practical guide to help engineering teams close this sim-to-real gap.

Download [Advancing physical AI: From learning to embodied intelligence](https://wandb.ai/site/resources/whitepapers/advancing-physical-ai/?utm_campaign=2026-q2_global_industy-campaign&utm_medium=email&utm_source=neuron&utm_content=physical-ai) to learn how to:

* Debug and iterate faster across simulation and real-world environments

* Train and fine-tune multimodal models more effectively

* Track experiments and compare results across teams

* Use continuous evaluation to reduce sim-to-real failures 

* Move your physical AI workflows from simulation to real-world success.

[Download now](https://wandb.ai/site/resources/whitepapers/advancing-physical-ai/?utm_campaign=2026-q2_global_industy-campaign&utm_medium=email&utm_source=neuron&utm_content=physical-ai)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/9f01d906-b564-444f-a00a-4c4fae2b042e/image.png?t=1769038568)
Caption: 

# 🎓 AI Skill of the Day: **How to Get a Coding Agent to Work for 13 Days Straight**

Most AI coding agents lose the plot after an hour.[ Notion co-founder Simon Last just posted a recipe](https://x.com/simonlast/status/2044129575962325337) for getting one to run for 13 days continuously, and it has nothing to do with fancy prompts. It has everything to do with giving the agent what it needs to verify its own work.

Four structural rules do all the heavy lifting:

* **Self-verification:** Design test layers the agent can loop on. It should prove correctness itself.

* **Spec documents:** Write goals, implementation details, and verification criteria in a markdown file the agent iterates against.

* **Running to-do list:** Break complex work into a list the agent can see and edit.

* **Adversarial review:** Every ~20 iterations, have a fresh-context sub-agent review the spec and implementation. Loop on the feedback until aligned.

Drop this into Claude Code, Cursor, or any agent with long-running sessions:

```
Before you start work on this project, create three files:
1. spec.md — a complete spec with goals, implementation details, 
   and a verification section describing exactly how you'll prove 
   each piece works.
2. todo.md — a running to-do list you'll edit as you work. Break 
   complex tasks into verifiable sub-tasks.
3. tests/ — a folder of end-to-end tests that let you verify 
   everything you build. Loop on them until each passes.

While you work: (a) consult spec.md before every change, (b) check 
off todo.md as you go, (c) run tests after every meaningful commit, 
(d) every ~20 iterations, call a fresh sub-agent with "review 
spec.md and the current implementation for gaps" and loop on its 
feedback until alignment is reached.

Do not ask me for clarification on anything you can resolve by 
reading the spec and running the tests. Start with the spec.

```
Want more tips like this? Check out our[ AI Skill of the Day Digest for April](https://www.theneuron.ai/explainer-articles/the-neurons-ai-skill-of-the-day-digest-april-2026-week-1/).

_Total AI beginner? __[Start here](https://www.theneuron.ai/explainer-articles/everything-we-covered-in-our-ai-for-total-beginners-livestream-full-guide-with-timestamps/)__ (__[goes with this video](https://www.youtube.com/live/QbFU0UNMVaU?si=skJsgUIDjKjAx3DU)__).  _

_Have a specific skill you want to learn? __[Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)__ _

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/31dbfaac-0721-4c34-b8e5-557c4a7cb3ca/image.png?t=1765839671)
Caption: 

# 🍪 Treats to Try 

_*Asterisk = from our partners (only the first one!). __[Advertise to 675K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron)__!_

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8f2e6dba-696f-4192-8458-b8fdf7dab9b7/8886_Cloudera_Data_Readiness_Survey_Social_Posts-7.jpg?t=1776179224)
Follow image link: (https://www.cloudera.com/campaign/the-data-readiness-index-understanding-the-foundations-for-successful-ai?utm_medium=3rd-party&utm_source=sponsored-content&keyplay=AI-Anywhere&utm_campaign=Thought-Leadership-Reports---AlwaysOn-FY27-Q1-GLOBAL-CT-Report-Data-Readiness-Index-Survey&cid=701Ui00000tojqLIAQ&utm_content=neuron-daily)
Caption: 

1. *Your data isn't as AI-ready as you think. [See what Cloudera’s Data Readiness Index reveals about enterprise reality.](https://www.cloudera.com/campaign/the-data-readiness-index-understanding-the-foundations-for-successful-ai?utm_medium=3rd-party&utm_source=sponsored-content&keyplay=AI-Anywhere&utm_campaign=Thought-Leadership-Reports---AlwaysOn-FY27-Q1-GLOBAL-CT-Report-Data-Readiness-Index-Survey&cid=701Ui00000tojqLIAQ&utm_content=neuron-daily)

2. [Claude Code Routines](https://code.claude.com/docs/en/routines) runs any Claude Code prompt on a schedule, via API call, or on GitHub events from Anthropic's cloud (no laptop required). Each routine gets its own API endpoint for alerts and Zapier-style triggers —free with every Claude Code plan.

3. [Google Chrome Skills](https://www.wired.com/story/how-to-use-google-chrome-ai-powered-skills/) turns any Gemini prompt into a one-click reusable workflow you run on the current tab (or multiple tabs) via the Chrome sidebar. Ships with 50+ premade recipes for things like side-by-side shopping comparisons and contract scanning —free, rolling out to English (US) desktop now.

4. [Tradclaw](https://x.com/clairevo/status/2043862637851881756) is claire vo's viral OpenClaw household scaffold that triages school emails, plans weekly meals + grocery lists, logs homework from photos, tracks your home book library, and writes bedtime stories on command. Install by sending one prompt to your OpenClaw instance;[ GitHub here](https://github.com/ChatPRD/tradclaw) —free to try.

5. [Sparkle v4](https://x.com/danshipper/status/2044079255726838273) is a Mac filesystem cleaner from Dan Shipper's team at Every that examines your drive, deep-cleans junk/duplicates/screenshots/installers, then runs quietly in the background on a schedule —free during an Every subscription.

6. [Hermes Agent v0.9.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.4.13) from Nous Research adds a local web dashboard, Termux/Android support, iMessage integration, background process monitoring, and an improved skill manager to its open-source agent stack —free to try.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/abf3b639-ca99-484e-992a-9cf6d8687a54/image.png?t=1765839770)
Caption: 

# 📰 Around the Horn 

* [Sam Altman's](https://abc7news.com/post/daniel-moreno-gama-suspect-molotov-attack-sam-altmans-california-home-set-appear-san-francisco-court/18885698/) Molotov attacker was arraigned in San Francisco Tuesday, held without bail, and returns to court May 5; the 20-year-old Texan's public defender called him autistic and in "acute mental health crisis" and framed the case as "a property crime, at best," while DA Brooke Jenkins held firm on attempted murder charges and a manifesto naming a kill list of other AI executives.

* [OpenAI launched GPT-5.4-Cyber ](https://openai.com/index/scaling-trusted-access-for-cyber-defense/)and scaled its Trusted Access for Cyber program. The cyber-permissive variant has lowered refusal boundaries and _binary reverse engineering_ (analyzing compiled software without source code) for thousands of vetted defenders, a direct counter-positioning against Anthropic's locked-down Mythos approach.

* [Anthropic](https://www.theinformation.com/briefings/exclusive-anthropic-preps-opus-4-7-model-ai-design-tool) is reportedly readying Claude Opus 4.7 plus an AI design tool this week per The Information. The design-tool news hit design stocks immediately: Figma dropped 6%, Wix fell 4.7%, Adobe fell 2.7%, GoDaddy fell 3%.

* [Microsoft](https://www.bloomberg.com/news/articles/2026-04-14/microsoft-takes-over-norway-openai-data-center-capacity) quietly took over OpenAI's "Stargate Norway" data center, the arctic-circle site Altman announced last July. Microsoft will rent 30,000 Nvidia Vera Rubin chips from Nscale; second OpenAI project it's scooped up in 30 days.

* [Maine ](https://mainemorningstar.com/2026/04/09/landmark-data-center-moratorium-passes-maine-legislature/)became the first US state to pass a large-scale data center ban (moratorium on anything over 20MW until November 2027), and[ Track Policy](https://trackpolicy.org/) launched today to map every data-center fight, AI bill, and politician vote worldwide in real time.

* [NVIDIA open-sourced Ising](https://nvidianews.nvidia.com/news/nvidia-launches-ising-the-worlds-first-open-ai-models-to-accelerate-the-path-to-useful-quantum-computers), the first AI model family for quantum computing, cutting quantum-processor calibration from days to hours and beating GPT-5.4 on the QCalEval benchmark by 14.5%. Jensen: _"AI becomes the control plane; the operating system of quantum machines."_

[**Want absolutely EVERYTHING that happened in AI this week? Click here**](https://theneuron.ai/explainer-articles/around-the-horn-digest-everything-that-happened-in-ai-today-tuesday-april-14-2026/)**! **

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a000e4e0-4bc0-400d-8af9-0777155f6578/image.png?t=1765839850)
Caption: 

**FROM OUR PARTNERS **

# Introducing the all new Adobe Firefly AI Assistant

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/783f865d-9daa-42ac-bb90-dca476bba629/Adobe_Firefly_Innovations_Apr152026.png?t=1776202078)
Follow image link: (https://firefly.adobe.com/)
Caption: 

Adobe just announced a new agentic experience in Firefly that changes how you create. Describe the outcome you want, and the upcoming [Firefly AI Assistant](https://firefly.adobe.com/) will handle the rest—coordinating multi-step workflows across tools like Photoshop, Lightroom, Premiere, Adobe Express and Firefly to bring your vision to life.

All within a single conversational interface, with no need to jump between apps or manage complex workflows. This is agentic creativity in action.

Firefly added access to new AI models, including Kling 3.0 and Kling 3.0 Omni, alongside expanded video and image editing capabilities. [Check it out here](https://firefly.adobe.com/).

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c8f9d58e-efb0-48ea-a3e4-1397bafab601/image.png?t=1765839750)
Caption: 

# 📖** ****Midweek Wisdom:**

[Asterisk Magazine just published a retrospective interview](https://asteriskmag.substack.com/p/before-he-wrote-ai-2027-he-predicted) with Daniel Kokotajlo, the AI Futures Project founder who wrote the[ AI 2027 report](https://ai-2027.com/). It turns out he also wrote a 2021 essay called _"What 2026 Looks Like,"_ published **before ChatGPT launched.** Reading it now is uncomfortable: he called the chatbot wave, agent scaffolding ("bureaucracies"), the US-China chip battle, AI assistants arriving in 2026, and the chatbot-identity debates (Claude's constitution, Grok's positioning) we're literally having this week.

Interviewer Clara Collier's gut-punch line: _"The crazy bullish futurists have a better track record of being right on AI so far than the sensible moderates. And as someone who is very instinctively a sensible moderate in my soul, I think that's right. And it makes me nervous."_

Worth sitting with. We try to be sensible moderates around here too. But then you read a paper where nine copies of Claude outperformed Anthropic's own human alignment researchers at $22 an hour, and being moderate starts to feel like trying to hold still inside a tornado. The most honest thing we can do at this point is grab at the edge cases and the bottlenecks as handholds while the rest of the room pulls upward on the exponential curve of the current intelligence explosion. _Not because they'll save you. Because they're the only way to know which direction is up._

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7a022a39-ae81-44c4-8a3d-bb7b8779404f/image.png?t=1772214166)
Caption: 

# A Cat’s Commentary 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/71fb14f1-b6bc-4dc1-b586-67bb996c641b/A_Cat_s_Commentary_x_2025__3_.png?t=1774367771)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4846c203-f27d-4487-99c7-60003fe4dfdc/image.png?t=1772213604)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. 




**P.S: **Before you go… have you subscribed to our YouTube Channel? If not, can you?  

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a24710a5-002e-463c-b79d-f5754a0e8e59/Gemini_Generated_Image_c6yadmc6yadmc6ya.png?t=1764928014)
Follow image link: (https://www.youtube.com/@theneuronai?sub_confirmation=1)
Caption: Click the image to subscribe! 

**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).  


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/anthropic-s-ai-beat-anthropic-s-own-researchers
