# Domain Expert Interview Guide

## Principle
Human interviews are an evidence source, not a ceremonial final review.

Interview when artifacts cannot reliably establish:
- business intent or terminology
- why a flow or status exists
- real operational sequence
- exceptional/manual handling
- historical design rationale
- what “success” or “stuck” means operationally
- ownership across teams/modules

## Ask focused questions
Ask one question at a time. Prefer questions that close a specific knowledge gap discovered during investigation.

Good:
- “Code shows records move from RECEIVED to READY before posting. What business condition does READY represent?”
- “The outward flow invokes Transaction Posting after validation. What does Outward expect back before it can continue?”

Avoid:
- “Explain the whole module.”
- long questionnaires sent all at once
- leading questions that embed an unverified conclusion

## Interview loop
1. State the evidence already found briefly.
2. Ask one precise question.
3. Record the answer as `USER_CONFIRMED` with person/role/date when practical.
4. Compare it with code/document evidence.
5. If it conflicts, mark `CONFLICT` and ask a resolving question.
6. Update the provisional flow model.
7. Ask the next highest-value question.

## Distinguish unknown types
- **SEARCH_GAP**: likely answerable from artifacts; investigate first.
- **DOMAIN_GAP**: meaning/intent likely requires a person; interview.
- **CONFLICT**: sources disagree; explicitly resolve.
- **UNAVAILABLE**: cannot currently verify; preserve as `UNKNOWN`.

## Interview completion
Stop when unresolved questions no longer block a truthful explanation of the current bounded flow. Do not force every historical detail to be known.
