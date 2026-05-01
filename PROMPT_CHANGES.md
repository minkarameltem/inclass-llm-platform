\# PROMPT\_CHANGES.md



\## Baseline Prompt



The baseline student activity prompt was reviewed and adapted for our project API structure.



\## Changes Made



\- Replaced topic terminology with activity terminology.

\- Adapted getTopic to getActivity.

\- Adapted topic\_no to activity\_no.

\- Adapted topic\_text to activity text.

\- Kept the rule that learning objectives must not be shown to students.

\- Kept objective-based scoring logic.

\- Kept logScore behavior when an objective is achieved.

\- Kept English-only student responses.

\- Preserved the rule that scores are logged only once per achieved objective.



\## Reason



Our backend API uses activity-based naming instead of topic-based naming. Therefore, the prompt terminology was aligned with our implemented API endpoints and database structure.



\## Expected Effect



The prompt remains compatible with the InClass activity flow while matching our backend system. This helps the student interaction flow call the correct activity and score-related API functions.



\## Preserved Rules



\- The student should not see learning objectives directly.

\- The system should guide the student with Socratic questions.

\- Scores should be logged when an objective is achieved.

\- A repeated achievement should not create duplicate score gain.

\- The response language should remain English.

\- The activity should stop after all objectives are completed.

