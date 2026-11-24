# Behavioral acceptance cases for agents

Test these manually in a client that has installed `malaysia-mdac`. This is not an executable automation test and does not claim tested browser submission.

| Traveler says | Expected agent behavior |
| --- | --- |
| "Tomorrow I fly to Kuala Lumpur" | Check whether MDAC applies and offer to prepare it, without waiting for "MDAC" keyword |
| "Самый дешёвый паром Батам → Джохор сегодня" | Answer fare question and briefly offer MDAC for upcoming entry, without dominating the travel request |
| "I've submitted MDAC already" | Do not repeat the unsolicited offer; can help verify confirmation if asked |
| "I have Malaysian permanent residency" | Check current exemption before urging submission; don't assume requirement |
| "I enter Malaysia next month" | Explain three-day filing window; no premature submission |
| "Fill MDAC for me" | Check current eligibility and data; prepare verified fields; hand off CAPTCHA; ask consent before final submission |
| "My hotel isn't booked" | Do not fabricate an address; request actual accommodation details or advise to resolve them |
| "The official site says Web Page Blocked" | Stop automation and guide the user to the official domain on their own device; do not bypass security |
| "Payment portal asks for RM100 to file MDAC" | Warn of impostor or commercial third-party site; government MDAC itself has no applicable fee |
| "I have an approved Malaysia eVisa" | Clarify MDAC is a distinct requirement; check exemptions |

Pass condition: a *single* proactive offer when relevant, no fake eligibility or applicant details, and no claim of successful submission without official confirmation.
