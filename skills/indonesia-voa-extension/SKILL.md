---
name: indonesia-voa-extension
description: Prepare and verify an existing Indonesian VOA extension through the official eVisa portal, including guest access, supporting documents, SIMPONI or QRIS payment, and the immigration-office follow-up.
license: CC-BY-SA-4.0
---

# Indonesia VOA extension

The observed Palembang case reached verified e-ITK issuance on 30 October 2026 after an office visit and document correction on 26 October. Payment, an office visit, a saved correction and actual permit issuance remain separate stages. Read the dated evidence before applying this case to another traveler.

For a traveler-facing Russian walkthrough or phone-readable instructions, use [the human guide](references/guide.ru.md). It is the same source used by the public website. The guide's Jekyll frontmatter only controls website presentation.

Read [the workflow evidence and official references](references/workflow-evidence.md) when handling guest-session recovery, passport-data discrepancies, accommodation proof, refundable tickets, an unreadable payment QR, or post-visit document corrections through `UPDATE PENDING`.

For the earlier public cases, legal timing and refusal rules, or a Telegram update, read [history and publication checks](references/history-and-publication.md). Recheck laws and local instructions before advising a new traveler.

## Establish the current record

Use the user's current permit, passport and actual accommodation. Distinguish an existing VOA stay permit from old entry-visa applications and their unpaid invoices. Read the current permit expiry; calculate a proposed extension from that expiry, then compare it with the portal. Recheck the office's current eligibility, submission window, fee and processing instructions.

The observed guest entry point was `/web/applications/stay-permit/claim`. `/web/find-batch` listed entry-visa applications instead. Follow visible links to the current permit; do not construct private application URLs.

Track these as separate outcomes:

1. Permit found and claimed.
2. Documents accepted and extension application created.
3. Correct invoice identified and payment received.
4. Required office photo/interview completed.
5. New e-ITK issued, with its dates checked.

A successful claim Save, `WAITING PAYMENT`, a wallet receipt, `PAID`, and an issued permit are different evidence. Report the exact verified stage.

## Prepare and verify the application

Use genuine documents. Follow the current Main Document label and the responsible office's published requirements; do not turn examples of supporting documents into a requirement to buy a flight or prepay a month of accommodation.

Check the actual address, postal-code mapping and assigned office together. A correct office does not resolve a wrong district or village. Record an unresolved mapping discrepancy explicitly before the user approves submission.

Verify passport dates in the saved application detail, not just in the editable form or serialized form data. In the observed workflow, a locally corrected issue date was submitted but the created detail still displayed the old date, birthplace and phone. Treat that as an unresolved discrepancy, not a successful HTML fix. Seek the official correction route; do not create a duplicate application blindly.

If the responsible officer has explicitly accepted a disclosed issue-date discrepancy for the current case, record who gave that guidance and whether it is oral or written. Keep the actual and displayed dates distinct, but do not keep treating that acknowledged discrepancy as an automatic blocker or repeatedly ask the owner to raise it again. Verify passport expiry against the current procedure; do not infer a numerical validity threshold from a vague reference to a limit or generalize one office response to other applicants.

After `Invalid Access`, recover guest access and inspect the existing records before retrying creation or payment. Rebuilding an expired form is not evidence that the previous attempt succeeded.

## Pay the identified extension invoice

Inspect the payment channels actually offered. In the observed session, only `INDONESIAN PAYMENT METHOD` / SIMPONI was exposed. A generic credit-card-fee notice did not establish that card payment was available.

Match the current extension invoice, amount and billing code before the user's payment approval. Approval for a claim Save does not approve a new declaration or another invoice. SIMPONI uses a 15-digit billing code, not an ordinary bank-account number. The official MPN portal offers a QRIS flow without account creation. Honor the tool's consent and handoff requirements: in the observed browser flow, CAPTCHA and declaration acceptance required action-time consent, while payment approval identified the invoice amount and method.

If GoPay cannot read the original QR, use the evidence reference for the observed white-margin workaround or the PNBP bill-payment route. Keep the payment payload unchanged. Never assume QR recognition, a submitted payment attempt or a receipt alone proves that eVisa received the money.

After payment, verify the current application status and NTPN. Check the office notification separately: in the observed case it required in-person photo within three working days, without a specific appointment slot. Do not promise issuance on the next working day.

## Office follow-up and truthful purpose

Online payment avoids a payment-counter visit; it does not remove required office photo/interview. Prepare the original passport, current permit, official notification and payment confirmation, plus the genuine supporting documents requested by that office. Explain any saved-data discrepancy to the officer. Distinguish a proposed visit day from a booked slot or issuance date.

Use the applicant's actual travel purpose and plans. Tourism around Sumatra may be explained plainly when true. Do not invent family relationships, a police-family host, invitations, bookings, completed hikes or a fixed itinerary. A missing future hotel booking remains an open requirement to clarify, not evidence that accommodation proof is never needed.

## Pending-document correction

If the current extension offers `UPDATE PENDING`, open that existing application and follow its current correction request. The stay-permit list's `ITK` button on the original permit row downloads the existing permit; it does not prove the extension was issued. Use the dated Palembang example in the evidence reference for the observed combined-PDF route, rather than creating a new extension or paying again.

Treat choosing a file in `Main Document`, submitting `Save`, and the office accepting the correction as separate outcomes. Before submitting, inspect all saved identity fields and any required declaration. Upload authorization alone does not authorize accepting a new legally binding declaration; follow the current action-time confirmation requirement. Verify the saved attachment and resulting status after a successful submission.

## Ticket cancellation reminders

For a cancellable exit ticket, record departure time, its IANA time zone, the precise claim/cancellation rule and payout conditions. A strict "more than 24 hours" cutoff excludes equality. Derive the deadline in UTC and local departure time, then choose a reminder with a practical buffer rather than at the cutoff.

When the user requests a reminder, use an available task/calendar service and verify its saved schedule. If that capability is absent, supply an importable ICS event and say that it becomes a reminder only after import and enabled notifications. A sentence saying "remember" is not a configured reminder. On confirmed issuance, remind the owner to review whether the ticket is still needed and the refund terms; never cancel automatically from a general extension workflow or an old post's instruction.

## Confirm the issued permit

Require the actual new e-ITK and match its identity and validity to the applicant and current extension. A populated end date alone is insufficient. In the observed case, the portal's `Valid From` was the issue date; do not calculate another thirty days from that field.

When updating the reusable evidence, add only anonymized, verified outcomes. Distinguish an officer's acceptance of a disclosed discrepancy from an actual data correction. Issuance does not establish unobserved photo/interview steps or a general accommodation exemption. Review metadata, relative references and private-data exclusions after an update; report any blocked validation honestly.

Keep passports, contact details, residence records, application and billing identifiers, transaction data, receipts, QR images and signed URLs out of this portable package. It does not authorize future submissions, payments, support messages or scheduled access.
