## Assistant Behavior Design

The assistant is intentionally designed to ask clarifying questions before giving advice.
Career decisions are highly context-dependent, and premature recommendations can be misleading.

This design choice prioritizes responsible guidance and mirrors how human mentors reason
before advising on high-stakes decisions.



The assistant provides advice using a structured decision framework
(summary, factors, pros, cons, risks, recommendation).
This ensures responses are explainable and aligned with real-world
decision-making rather than generic suggestions.


During testing, overly strict clarification-first behavior delayed useful advice.
The prompt was refined to allow conditional recommendations with explicit assumptions,
balancing responsibility with practical usefulness.


The assistant reports a confidence level and suggests alternatives when uncertainty is high,
encouraging informed decision-making rather than overconfident advice.
