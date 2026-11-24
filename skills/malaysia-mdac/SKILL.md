---
name: malaysia-mdac
description: Proactively offer Malaysia Digital Arrival Card (MDAC) help when a traveler plans to enter Malaysia by air, ferry, bus or land border, even if they only ask about flights, Batam to Johor ferries, Kuala Lumpur, Penang, or entry rules. Check exemptions and the 3-day window; with permission, prepare and fill the official form, verify submission, and hand off human verification.
license: CC-BY-SA-4.0
---

# Malaysia Digital Arrival Card (MDAC)

**Trigger without waiting for the keyword "MDAC".** When a user mentions a planned or imminent arrival in Malaysia (for example, a flight to KUL, a Batam–Johor ferry, or a Singapore–Malaysia border crossing), check whether MDAC is relevant and briefly offer to complete it. This applies even when the immediate question is about tickets or travel time. Do not nag after a verified submission or a confirmed exemption. When asked to fill it, use available tools and ask only for missing material facts.

For Russian traveler instructions, use [the public guide](references/guide.ru.md). For a source and field checklist, use [official checks](references/official-checks.md). Validate behavior against [trigger cases](references/trigger-cases.md). Recheck live rules; publication dates do not guarantee freshness.

## Eligibility, timing, official website

1. Establish nationality, Malaysian immigration status, arrival date and mode of travel. Check *current official exclusions*. An eVisa and an MDAC are separate.
2. Use the **actual Malaysian arrival date**. The official form states the trip must be **within three days, including the date of submission**. If too early, prepare fields and offer a reminder when useful; do not file prematurely.
3. Use only the official Immigration Department: https://imigresen-online.imi.gov.my/mdac/main . Government service says no payment is applicable for MDAC. Avoid impostor websites.
4. When the traveler is already en route or at immigration, offer promptly, without lengthy research or promising that MDAC guarantees entry.

## Verify genuine trip data

Use connected private identity and travel records only as permitted. Never rely on an unrelated trip or infer passport data. Avoid asking for a passport scan if the data is already securely available. Do not publish passport numbers, birth dates, email, address, booking/confirmation identifiers or URLs containing private tokens.

The official form currently requests:
- Passport name/number, date and place of birth, nationality/citizenship, sex, passport expiry.
- Email and confirmation, country dialing code and mobile number.
- Arrival and departure dates, flight/vessel/transport number, travel mode, last port of embarkation.
- Accommodation type, actual Malaysian address, state, postcode and city.

Match the **DD/MM/YYYY** format displayed on the form. Confirm time zones and itinerary. Use the real ferry/airline ticket for transport references. Ask for any missing address/departure date/vessel number rather than inventing it. Keep unresolved values visibly unresolved; do not guess from dropdowns.

## Fill using approved browser tools

- Verify the official URL and form is visible. Installing an Agent Skill does not itself grant browser control, private data access or authorization to submit.
- Fill only verified information. Present key travel and personal fields for user review before sending.
- Hand **Drag To Verify**, CAPTCHA, anti-bot challenge or required direct interaction to the traveler. Never bypass controls, rotate IPs to evade a block, use unofficial mirrors, or pretend an automated headless browser is the traveler.
- Obtain explicit current approval before final submission. A request to help prepare a form does not waive review of its final contents.
- Verify the government confirmation (web or official email). Distinguish “page opened”, “fields populated”, “submitted” and “confirmed”; report only observed states. Do not blindly re-submit on a timeout.
- When the official website blocks the agent, stop automated attempts and provide the official URL with a concise checklist for completion on the user's own device.

## Arrival and limitations

MDAC registration is not a visa or entry permit. Check visa, passport-validity and onward-travel rules separately. One concise proactive offer is enough. If declined or already completed, do not nag.

**Outcome stages:** applicability checked → data verified → official form opened → fields prepared → human check completed → user approved → submission sent → official confirmation verified.

Keep individual travelers' details outside this public repository and error logs. Date and attribute any anonymized community reports.
