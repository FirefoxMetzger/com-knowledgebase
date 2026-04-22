---
{
  "source": "inkbox-mailbox-cli",
  "id": "d3e2b1f3-8c50-4d9b-a670-8635b42bf223",
  "message_id": "<20260415094558.3.705ae8e4c00e4d6f@mg-d1.substack.com>",
  "thread_id": "8f1e3214-f05b-4e05-b8ca-1d76cc9199ed",
  "direction": "inbound",
  "from": "exponentialview@substack.com",
  "to": "sally.anderson@inkboxmail.com",
  "subject": "🔮 The classified frontier",
  "created_at": "2026-04-15T09:50:48.563053+00:00",
  "fetched_at": "2026-04-22T18:31:17.451272+00:00",
  "is_read": false,
  "has_attachments": false,
  "is_newsletter": false,
  "in_reply_to": "<post-194198231@substack.com>"
}
---

View this post on the web at https://www.exponentialview.co/p/the-classified-frontier

In May 2025, an OpenAI representative arrived at Los Alamos National Laboratory bearing locked metal briefcases. They were accompanied by armed security officers. Inside the cases were the model weights for ChatGPT o3 – at the time, OpenAI’s leading reasoning model. The weights were physically transported because the destination, the Venado supercomputer [ https://substack.com/redirect/bbd42921-2dcb-413d-9f25-b16ff15bebc3?j=eyJ1IjoiODdyOGQzIn0.y42enNAzGlO-pLEFmj9sFi4SGWTKor_6ime9GAwNnG8 ], operates on a classified, air-gapped network. You cannot download a frontier AI model onto a classified government system – you have to walk it in.
We talk about models as if they float in the cloud, weightless and ambient, but AI is physical. Model weights are arrays of billions of numbers stored as tensors in files distributed across racks of GPUs in a data center. When you use Claude or ChatGPT through an API, the weights never leave those servers – you send text in, get text back, but the intelligence stays on someone else’s hardware. In a briefcase, they are a hard drive. In both cases, a physical arrangement of matter encoding a capability.
Last week, Anthropic’s Mythos Preview [ https://substack.com/redirect/f2bb47cf-88ee-4d34-a17a-18409a001a58?j=eyJ1IjoiODdyOGQzIn0.y42enNAzGlO-pLEFmj9sFi4SGWTKor_6ime9GAwNnG8 ] demonstrated what that capability now means. The model found thousands of vulnerabilities across every major operating system and browser. As I argued on Friday [ https://substack.com/redirect/09aa9347-fca1-4ffa-a40f-044d13ea5615?j=eyJ1IjoiODdyOGQzIn0.y42enNAzGlO-pLEFmj9sFi4SGWTKor_6ime9GAwNnG8 ], AI models like Mythos have permanently collapsed the distinction between capability and danger. Who controls the weights of that model – and how – is now the central question in AI governance.
The viscosity mismatch
Some technologies diffuse quickly – published papers, vaccines, drones. Others are viscous: they require specific infrastructure, tacit knowledge, or resources that slow their spread. Nuclear weapons are the canonical example. The knowledge has been public for decades; the ability to build one remains confined to a handful of states because the materials and engineering are highly viscous.
Frontier AI has an uncomfortable asymmetry. The creation of frontier weights is viscous. Training runs cost billions of dollars in compute – hundreds of thousands of GPUs running for months. They require proprietary data pipelines and deep engineering talent. Only a handful of labs can do it, nearly all based in the United States. China, the closest rival, remains constrained by chip export controls that limit its access to the most advanced hardware. That makes the capability concentrated and, in principle, seizable.
But the spread of weights is not viscous at all. They are files, and in some cases, even books (Ethan Mollick  printed GPT-1’s weights as a book [ https://substack.com/redirect/9c6cba7e-2325-46b8-b5d7-0f879f2efe04?j=eyJ1IjoiODdyOGQzIn0.y42enNAzGlO-pLEFmj9sFi4SGWTKor_6ime9GAwNnG8 ]). Today, I can download to my laptop an open-weight model that would have been frontier six months ago. And the use of frontier capability is even less viscous: anyone with an API key can access the capability without possessing the weights at all.
Creation viscosity is high. Spread and use viscosity are low. That asymmetry creates a closing door – you no longer need the weights to capture much of the value. Synthetic data and distillation – the process of training a weaker model on a stronger model’s outputs – allow labs to approximate reasoning and training signals from stronger systems. Chinese labs DeepSeek, Moonshot, and MiniMax were caught by Anthropic generating over 16 million conversations with Claude [ https://substack.com/redirect/a6d260c1-57f8-48f1-9276-75cb8cc89d66?j=eyJ1IjoiODdyOGQzIn0.y42enNAzGlO-pLEFmj9sFi4SGWTKor_6ime9GAwNnG8 ] between them to use as training data for their own systems.
If adversaries can get close to frontier capability by reverse engineering through use, then securing API access becomes essential. And so far, access controls have been systematically circumvented. It’s hard to slay a hydra of fake accounts. Any sufficiently motivated actor can query these models millions of times via normal API access, and use those responses to teach their own model – no briefcase required.
Containment is no longer feasible...

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cuZXhwb25lbnRpYWx2aWV3LmNvL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqbzBPVFkzTlRjeU56RXNJbkJ2YzNSZmFXUWlPakU1TkRFNU9ESXpNU3dpYVdGMElqb3hOemMyTWpRMk5qUXlMQ0psZUhBaU9qRTRNRGMzT0RJMk5ESXNJbWx6Y3lJNkluQjFZaTB5TWpVeUlpd2ljM1ZpSWpvaVpHbHpZV0pzWlY5bGJXRnBiQ0o5LmtxX1NJbzRuODBZTUVUSUNVeW4yZ2pqckxoUFpmUy15YlNTa1p0Vkc1NVUiLCJwIjoxOTQxOTgyMzEsInMiOjIyNTIsImYiOnRydWUsInUiOjQ5Njc1NzI3MSwiaWF0IjoxNzc2MjQ2NjQyLCJleHAiOjIwOTE4MjI2NDIsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.ofjwR4oSIUw4pJw3-eCy9yrHvbVm98zZj5Eo_-WnYAI?
