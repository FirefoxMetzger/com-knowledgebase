---
{
  "source": "inkbox-mailbox-cli",
  "id": "f53e7063-691c-4de1-a105-82c7c19d2863",
  "message_id": "<20260419022543.3.3d91dcdb100ff945@mg2.substack.com>",
  "thread_id": "9762ae04-32c2-4bbd-9ac4-bbf6b360b8d3",
  "direction": "inbound",
  "from": "exponentialview@substack.com",
  "to": "sally.anderson@inkboxmail.com",
  "subject": "🔮 Exponential View #570: Inside Jensen Huang’s worldview",
  "created_at": "2026-04-19T03:28:52.282644+00:00",
  "fetched_at": "2026-04-22T18:31:12.197540+00:00",
  "is_read": false,
  "has_attachments": false,
  "is_newsletter": false,
  "in_reply_to": "<post-194522719@substack.com>"
}
---

View this post on the web at https://www.exponentialview.co/p/ev-570

Hi,
Welcome to the Sunday edition of Exponential View. We’re trying something new in public today. 
First, you’ll get my human read on Jensen Huang’s ‘token factory’ worldview and what it means for Nvidia’s moat and US-China tech strategy. Then you’ll see the same week through a different lens – my AI Swarm View arguing through Iran scenarios. And finally, a selection of short morsels that surface the weak signals and second‑order effects we’d otherwise miss in the noise.
This is a minimally viable test. Tell us what lands (and what doesn’t) in the comments or the short survey at the end.
Thanks! 🙏🏽
Azeem’s view 
Jensen Huang and the age of the token factory
This week, Jensen’s mental model snapped into focus when he told Dwarkesh Patel  in an interview: “The input is electrons, the output is tokens. In the middle is Nvidia.” The interview was really about who controls that middle and where Jensen thinks the threats are.
Nvidia doesn’t own the middle outright. The fabs, memory, clouds and models all sit elsewhere. But Nvidia runs the orchestration. Jensen personally meets the CEOs of the chip supply chain: ASML, whose lithography machines etch the chips; TSMC, which fabricates them; Micron and SK Hynix, which make the high-bandwidth memory Nvidia’s GPUs need, and Lumentum and Coherent, which supply the optical components that wire Nvidia’s systems together. He is effectively underwriting suppliers’ long-term investments and creating demand for their products years ahead. 
The forecast becomes self-fulfilling. Suppliers build to it, and by building to it, they make it true. That translates into roughly $100 billion in explicit purchase commitments and perhaps $250 billion implicit. Critics call it circular investment; in a world of compute shortages [ https://substack.com/redirect/d7a4e54f-f396-4238-b92f-d45ec4414dd3?j=eyJ1IjoiODdyOGQzIn0.y42enNAzGlO-pLEFmj9sFi4SGWTKor_6ime9GAwNnG8 ], it looks more like foresight.​
Jensen waved off the competitive threats inside the US. His view is that custom silicon – Google TPU, AWS Trainium – leans on a single customer: 
Without Anthropic, why would there be any TPU growth at all? It’s 100% Anthropic. 
His read is that Anthropic picked those platforms because Google and AWS wrote the equity checks when no one else would. Neither has consistently used the public scorecards that chipmakers use to prove performance. Jensen doesn’t mention AMD barely features in the conversation.
You can copy the chip, but you can’t copy the system around it. Twenty years of CUDA, Nvidia’s software platform, means a generation of AI researchers has grown up coding on Nvidia – the habits, the tooling, and the muscle memory are deep. On top of that, there’s an army of Nvidia engineers embedded with customers who pull two or three times more performance out of the same silicon. And a new chip design every year – Blackwell, then Vera Rubin, then Feynman – resets the bar before rivals can catch up. The moat is in these three elements compounding.
Where Jensen is less relaxed is about China, specifically Huawei Ascend. Not because it’s directly competitive today, but because it doesn’t need to be. It’s a parallel ecosystem in which Huawei sits between electrons and tokens [ https://substack.com/redirect/84ce13a7-bac9-4887-adb6-ba22d97b109d?j=eyJ1IjoiODdyOGQzIn0.y42enNAzGlO-pLEFmj9sFi4SGWTKor_6ime9GAwNnG8 ], insulated from Nvidia by design.
This is textbook adjacent-market disruption. A constraint – US export controls – forced a standard that doesn’t have to beat CUDA. It only has to be good enough for the developers who can’t use it. “Fifty percent of AI developers are in China,” Jensen says. If those developers build on Huawei Ascend rather than CUDA, America loses the platform standard permanently. And with it, the data flows, the weights, the APIs, the default surfaces every non-Chinese enterprise uses to reach Chinese customers.
There’s a coherence to his argument, but it’s also self-serving: don’t worry about competitor ASICs – worry about cutting off Nvidia sales to China. It may well be exactly that, but underneath the special pleading is a real question, and one of the defining debates of this moment [ https://substack.com/redirect/b4d3c32e-e689-4ec2-bb69-3423cbd7fdc6?j=eyJ1IjoiODdyOGQzIn0.y42enNAzGlO-pLEFmj9sFi4SGWTKor_6ime9GAwNnG8 ]. What is better for the US: preventing access to Nvidia’s cutting-edge chips, which slows Chinese model development but accelerates China’s own chip industry? Or selling them chips and maintaining primary control of the platform that runs everyone’s AI?
Even selling chips to China might not stop the second ecosystem from forming. DeepSeek is already adapting its upcoming V4 to run on Huawei silicon, and that’s just the beginning. Beijing has shown its hand: it will intervene whenever Huawei’s trajectory is at risk.
It may not be too late to keep the platform standard in American hands. But it would take an effort on a gargantuan scale – one Washington has not yet shown the appetite for.
Swarm view 
Mapping scenario probabilities in Iran
Over the past few months, I’ve been testing a new way to think  [ https://substack.com/redirect/92e5a338-3604-4111-985a-c4feefce864d?j=eyJ1IjoiODdyOGQzIn0.y42enNAzGlO-pLEFmj9sFi4SGWTKor_6ime9GAwNnG8 ]with AI. When I hit a hard, messy question, I throw it to a panel of simulated expert agents and let them argue it out. I call it my Swarm View. I’m publishing a Swarm View for the first time as a live experiment today, after months of privately tuning the agents to think alongside me, argue and create new views I’d not have considered before.
What follows is output from one such run. RMA, my OpenClaw agent, did the work on Tuesday, 14th April. We’ve lightly edited the output. The right format, the right cadence, how to weight the confidence of the verdicts – all of this is still being worked on. Treat it as a tool for stress-testing scenarios, not a forecast to bet the farm on. I’d welcome your reaction.
This week’s question: Will the US and Israel strike Iran after the ceasefire expires on 22 April?
The synthetic panel: 
A CENTCOM operational planner, 
an Iranian strategic analyst, 
a Pakistan/ISI specialist, 
a PLA/China analyst, 
and a nuclear deterrence expert.​
The panel’s verdict: A 60-70% probability of a strike before 22 April...

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cuZXhwb25lbnRpYWx2aWV3LmNvL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqbzBPVFkzTlRjeU56RXNJbkJ2YzNSZmFXUWlPakU1TkRVeU1qY3hPU3dpYVdGMElqb3hOemMyTlRZNU16STBMQ0psZUhBaU9qRTRNRGd4TURVek1qUXNJbWx6Y3lJNkluQjFZaTB5TWpVeUlpd2ljM1ZpSWpvaVpHbHpZV0pzWlY5bGJXRnBiQ0o5LmxLZW13SE1vaE10dWg2LVUwUmkzWU5JSldNemV5anRJNFJGdlBQQTkzcUkiLCJwIjoxOTQ1MjI3MTksInMiOjIyNTIsImYiOnRydWUsInUiOjQ5Njc1NzI3MSwiaWF0IjoxNzc2NTY5MzI0LCJleHAiOjIwOTIxNDUzMjQsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.ZHZkHyrlDMhalCzPf9SdswjM8kQuDNCXX0vd4hb7cAc?
