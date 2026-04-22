---
{
  "source": "inkbox-mailbox-cli",
  "id": "66e3eb37-f958-4cf2-a3d9-1939c4b40d5f",
  "message_id": "<20260416110251.3.6ac4c3dbb975fff4@mg-d1.substack.com>",
  "thread_id": "412eb14b-b0b3-436a-aaf6-7b851a5a04a8",
  "direction": "inbound",
  "from": "thesequence@substack.com",
  "to": "sally.anderson@inkboxmail.com",
  "subject": "The Sequence Opinion #844: Harness Engineering: The Operating System for Agentic Software",
  "created_at": "2026-04-16T11:07:55.463729+00:00",
  "fetched_at": "2026-04-22T18:31:15.068473+00:00",
  "is_read": false,
  "has_attachments": false,
  "is_newsletter": false,
  "in_reply_to": "<post-194286881@substack.com>"
}
---

View this post on the web at https://thesequence.substack.com/p/the-sequence-opinion-844-harness

There is a meaningful difference between getting a model to write code and getting a model to reliably build software. The first is a neat demo. The second is a new engineering discipline. We are talking about harness engineering.
The idea is simple, but the implications are deep. Instead of treating the model as a magical coding oracle, you treat it as a powerful but imperfect operator inside a carefully designed environment. The goal is no longer to write the perfect prompt. The goal is to build the surrounding system so that good behavior becomes easy, bad behavior becomes visible, and failure becomes recoverable.
This is an important shift because most teams still think of agentic software as an interface problem. They focus on instructions, tone, and phrasing. But once an agent is doing meaningful work over long horizons, the bottleneck is rarely language alone. It is structure. It is visibility. It is memory. It is validation. It is the quality of the rails surrounding the model.
In other words, the real product is not the prompt. It is the harness.
OpenAI recently gave a useful name to a pattern  [ https://substack.com/redirect/3d8a4f17-04ac-4dd2-950b-3b5f53ce952a?j=eyJ1IjoiODdyOGQzIn0.y42enNAzGlO-pLEFmj9sFi4SGWTKor_6ime9GAwNnG8 ]many of us have been discovering the hard way: harness engineering. In its post on the subject, the company makes a strong argument that the real challenge is no longer just getting models to generate code, but building the surrounding environment—tools, constraints, plans, observability, documentation, and feedback loops—so agents can operate reliably inside production systems. That framing is exactly right, and it is a useful place to begin.
But this essay is not a restatement of OpenAI’s idea. I want to use that framing as a starting point and blend it with my own lessons from working with agentic systems in practice. The interesting part of harness engineering is not the label itself. It is the collection of non-obvious truths that appear once you move beyond one-shot demos and start asking agents to do real work over long horizons. At that point, the bottlenecks stop looking like prompt problems and start looking like engineering problems: memory, visibility, verification, architecture, process, and recovery.
And that is where the real lessons begin.
Lesson 1: When Agents Fail, the Environment Is Usually Underbuilt...

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly90aGVzZXF1ZW5jZS5zdWJzdGFjay5jb20vYWN0aW9uL2Rpc2FibGVfZW1haWw_dG9rZW49ZXlKMWMyVnlYMmxrSWpvME9UWTNOVGN5TnpFc0luQnZjM1JmYVdRaU9qRTVOREk0TmpnNE1Td2lhV0YwSWpveE56YzJNek0zTmpZekxDSmxlSEFpT2pFNE1EYzROek0yTmpNc0ltbHpjeUk2SW5CMVlpMDFORE13T1NJc0luTjFZaUk2SW1ScGMyRmliR1ZmWlcxaGFXd2lmUS5JVnhmNUtMbnBmYW00eXBYdC1aRE43d1VCbmJSYmdPWFVYeVVHUHhlUG5jIiwicCI6MTk0Mjg2ODgxLCJzIjo1NDMwOSwiZiI6dHJ1ZSwidSI6NDk2NzU3MjcxLCJpYXQiOjE3NzYzMzc2NjMsImV4cCI6MjA5MTkxMzY2MywiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.B9tiPvtXCqLYTkCbGjku-8js6M4eH3ePSTSCoD6SVms?
