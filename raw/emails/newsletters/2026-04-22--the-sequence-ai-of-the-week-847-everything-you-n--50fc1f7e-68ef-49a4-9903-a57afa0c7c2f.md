---
{
  "source": "inkbox-mailbox-cli",
  "id": "50fc1f7e-68ef-49a4-9903-a57afa0c7c2f",
  "message_id": "<20260422110006.3.2c29b58f5fc7fa1f@mg-d0.substack.com>",
  "thread_id": "cb3f8ba4-90b2-4c79-a0cd-05122cb0ab98",
  "direction": "inbound",
  "from": "thesequence@substack.com",
  "to": "sally.anderson@inkboxmail.com",
  "subject": "The Sequence AI of the Week #847: Everything You Need to Know About Claude Opus 4.7",
  "created_at": "2026-04-22T11:02:58.412475+00:00",
  "fetched_at": "2026-04-22T18:31:07.310061+00:00",
  "is_read": false,
  "has_attachments": false,
  "is_newsletter": false,
  "in_reply_to": "<post-195018628@substack.com>"
}
---

View this post on the web at https://thesequence.substack.com/p/the-sequence-ai-of-the-week-847-everything

Claude Opus 4.7 shipped last week. The benchmarks are what you’d expect from a two-month incremental release — SWE-bench Verified 87.6%, SWE-bench Pro 64.3%, MCP-Atlas +14.6pp, state-of-the-art on GDPval-AA for economically valuable knowledge work, XBOW visual-acuity 54.5% → 98.5%, finance and document reasoning up, BrowseComp and long-context multi-needle retrieval down. Fine. Worth skimming. But the raw numbers undersell what actually changed.
The easier way in is to look at what got removed from the API, because the release is as much about the contract between you and the model as it is about the weights.
If you migrate a 4.6 harness to 4.7 and it still sets temperature, top_p, top_k, or thinking.budget_tokens, you get a 400. Not deprecated with a warning — gone. The only supported thinking mode is adaptive. In their place: an effort enum (low, medium, high, xhigh, max) and task_budget, a soft token ceiling the model can actually see. Every one of the removed parameters was a sampling-level control — you were reaching into the decoding loop and fiddling with token probabilities. What replaces them are semantic controls. You’re no longer tuning the softmax; you’re telling the model how hard to think and how much runway it has.
That’s basically the release in one sentence. The inference-time interface has shifted from stochastic sampling knobs to self-paced budgets, and the model has been trained to sit inside that interface responsibly. Everything else — self-verification, the literal instruction following, 1:1 pixel mapping, file-system memory, differential capability shaping — is downstream of this posture. Let me walk through what the new contract actually buys you.
Self-verification as a trained behavior, not a prompt trick...

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly90aGVzZXF1ZW5jZS5zdWJzdGFjay5jb20vYWN0aW9uL2Rpc2FibGVfZW1haWw_dG9rZW49ZXlKMWMyVnlYMmxrSWpvME9UWTNOVGN5TnpFc0luQnZjM1JmYVdRaU9qRTVOVEF4T0RZeU9Dd2lhV0YwSWpveE56YzJPRFUxTnpjeUxDSmxlSEFpT2pFNE1EZ3pPVEUzTnpJc0ltbHpjeUk2SW5CMVlpMDFORE13T1NJc0luTjFZaUk2SW1ScGMyRmliR1ZmWlcxaGFXd2lmUS5ZTWVhbVlYYk9qNmVodlNFeE13UEoyTXdUNXE3WW9xbW5WQnJ6b1dlQ2swIiwicCI6MTk1MDE4NjI4LCJzIjo1NDMwOSwiZiI6dHJ1ZSwidSI6NDk2NzU3MjcxLCJpYXQiOjE3NzY4NTU3NzIsImV4cCI6MjA5MjQzMTc3MiwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.gfkNfmb2Qs8l02aA6Pgc7ork_PTwu5gmm-Ch_sgfGnY?
