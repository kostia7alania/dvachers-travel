# Workflow evidence and official references

Evidence reviewed during the 24 October 2026 client session, which crossed into 25 October in western Indonesia, the 26 October office follow-up, and verified issuance on 30 October. Recheck the live portal and responsible office before reuse.

## Current evidence boundary

An extension application was created and paid through GoPay on 25 October 2026. eVisa showed Paid, a payment date and NTPN, with `Biometric enrollment at Immigration Office`; these were payment and processing evidence. The notification required an office photo within three working days, without a specific appointment slot.

On 26 October, the user reported arriving at the office and receiving instructions to supply one combined PDF through `UPDATE PENDING`. After the authorized Save, the supporting-document link changed. The application later showed `Waiting Confirmation` with an end date but no new permit number or `Valid From`; that intermediate state was not issuance.

On 30 October, an official approval email and its attached one-page new e-ITK confirmed issuance. The PDF was matched against the applicant's name, passport number, birth date and passport expiry. A refreshed application independently showed a new Permit Number, an actual e-stay-permit PDF link, `Valid From 2026-10-30` and `Valid Until 2026-11-24`. The final expiry was 24 November, thirty days beyond the original 25 October expiry. The portal's `Valid From` was the issue date, not a basis to add another thirty days.

The saved passport issue date was still incorrect; the owner had reported case-specific oral officer acceptance, not a data correction. The exact photo/interview steps were not independently confirmed. No further hotel booking or general exemption from accommodation evidence was established. Keep application identifiers, receipt contents, mailbox evidence and personal documents in the private case, outside this package.

The user confirmed the successful payment was made through the PNG with the white border. The user also found a service named Penerimaan Negara in GoPay search. That menu's presence was observed in that user's app; it was not the payment route used in this case.

## Official requirements and accommodation

- [Palembang: Perpanjangan ITK](https://palembang.imigrasi.go.id/web/izin-tinggal-keimigrasian/1DKlHi0TLEx9ygcs85_IKaGc7DQ-AmuBx-Yjz6XPGx4) describes the VOA extension, passport and purpose-of-stay statement, local jurisdiction, fee, application timing and processing after payment. It ties avoiding overstay to payment before the existing ITK ends. Read the current version instead of assuming that merely submitting an application stops the clock.
- [Ngurah Rai: foreign-national services](https://ngurahrai.imigrasi.go.id/layanan-wna/) lists an onward or return ticket for VOA extension and asks for the actual accommodation address for the next five days. That is not a statement that every office requires five prepaid hotel nights or thirty nights of bookings. Follow the responsible office and the current form.
- The same Ngurah Rai page describes office photo/interview and notification steps. Its separate EPO procedure lists a departure-ticket payment receipt. Do not apply that EPO requirement as permission to replace a VOA-extension ticket with an ordinary payment receipt.
- On the 31 October source check, that page also gave conflicting filing instructions: an opening window fourteen days before expiry and a deadline seven days before expiry. Start early and resolve local timing with the responsible office. The legal filed-and-paid-before-expiry protection does not establish that every office accepts last-day filing as its normal procedure.

In the observed Palembang case, a hotel operator's published postcode mapped to a different district/village in eVisa; an independently supported postcode was not found by the portal. The full street address and the assigned office were checked separately. This is evidence of one unresolved mapping problem, not a reusable instruction to select a nearby postcode.

## Dated Palembang example: one PDF through UPDATE PENDING

On 26 October 2026, the user reported the following instructions from the office. These are a case-specific document correction, not a universal rule for every VOA extension or office.

1. Open the stay-permit list at `/web/applications/stay-permit`. The `ITK` action on the original permit row downloads that existing e-ITK. Verify its permit number and validity: an original permit can remain downloadable after expiry and is not the newly issued extension.
2. Prepare one PDF in the office-requested order: first page of the downloaded e-ITK, first page of the issued onward e-ticket, and the full supplied photograph of the current visa/stay-permit page. In this case no separate isolated copy of the sticker was requested. The assembled example was three pages, approximately 1.38 MB, and was checked for legibility. Omit extra pages only when the office instruction and the actual content support doing so; do not remove essential identity, validity or travel information.
3. In the list, open the current extension by its register-number link. Match the record, not merely the first row's position. Click `UPDATE PENDING` near the top right of its detail page.
4. In the correction form, select that combined PDF in `Main Document`. Recheck the current file-type and size limits. A selected filename does not establish that the document has been saved on the server.
5. Inspect any declaration before `Save`; follow the applicable consent requirement. After submission, verify the success message, the saved attachment and current status. Office acceptance and the eventual issued e-ITK require separate evidence.

After the user explicitly confirmed the declaration and Save, the form redirected to the sign-in screen. Reopening the existing detail showed a changed supporting-document link and the status `Biometric enrollment at Immigration Office` instead of `UPDATE PENDING`. This confirms the correction was saved for further processing; it is not office approval or permit issuance. Inspect the existing record before retrying a Save after a redirect.

## Officer response reported on 26 October

The owner reported that the Palembang officers said the passport issue-date discrepancy did not require correction in this application; their concern was sufficient remaining passport validity. This is an attributed oral response for this case, not a written rule or evidence that the incorrect portal date was changed. The owner did not provide a numerical validity threshold. Do not invent one, advise ignoring inaccurate data generally, or keep treating this disclosed issue-date discrepancy as an automatic blocker after this response. Passport expiry and final permit issuance still require their own checks.

## Fragile portal behavior

- Guest claim Save linked the existing permit; it did not create or pay an extension.
- The portal could navigate successfully even when the browser operation reported a detached page or timeout. Observe the resulting page before repeating a consequential action.
- A long-lived form later returned `Invalid Access`. Recovery through the stay-permit claim entry point located the current permit again. Inspect existing rows before retrying, so an old visa invoice or duplicate extension is not paid accidentally.
- A disabled passport issue-date field displayed an incorrect value. An authorized local DOM correction made the intended date appear in the form and in `FormData`; after creation, the detail page again showed the incorrect date. The phone and birthplace also reverted in that detail. The page did not establish whether these were application fields or shared passport-profile fields. No self-service correction path was verified in that guest view.
- [Yogyakarta's article about errors in a submitted eVOA](https://jogja.imigrasi.go.id/what-to-do-if-you-accidentally-filled-out-the-wrong-information-in-the-electronic-visa-form-and-it-was-submitted/) discusses some identity mistakes, but does not establish the remedy for this issue-date discrepancy in an unpaid extension. Do not infer automatic refusal or a mandatory new entry visa from it.
- [Batam's technical-status guidance](https://www.batam.imigrasi.go.id/category/berita-utama/begini-cara-mengecek-status-permohonan-visa-dan-izin-tinggal-indonesia-cepat-dan-mudah) describes collecting the error evidence and application identifiers for official helpdesk assistance. Prepare a concrete correction request before seeking permission to send it.

## SIMPONI, MPN and GoPay

The observed extension offered only SIMPONI. It generated a government billing code and a fee of IDR 500,000. Verify both on the current extension record; do not reuse a code from another application.

[DJPb's official payment instructions](https://djpb.kemenkeu.go.id/kppn/penerimaan/id/profil/315-layanan/layanan-mpn/pembayaran-billing-mpn.html) link to [MPN](https://mpn.kemenkeu.go.id/). The observed flow was billing code, CAPTCHA, then `Bayar via QRIS`. The resulting QR is a payment request, not evidence of payment. Its displayed expiry is separate from the permit's legal deadline.

An ordinary GoPay bank transfer requires a bank-account destination. Do not treat a 15-digit MPN billing code as that account. An alternative is the PNBP payment service or a bank's government-payment menu:

- [Official BMKG instructions](https://ptsp.bmkg.go.id/upload/file_menu/20260225103019.pdf): Gojek, GoTagihan & Pulsa, Penerimaan Negara, Penerimaan Negara Bukan Pajak (PNBP), then the billing code. Confirm the actual menu and fee in the user's version.
- [myBCA instructions](https://www.bca.co.id/id/informasi/Edukatips/2024/11/26/04/14/Pembayaran-MPN-Bisa-Dilakukan-di-BCA-Ini-Cara-Bayarnya): Bayar & Isi Ulang, MPN, funding account and billing code.
- [BNI instructions](https://www.bni.co.id/id-id/beranda/kabar-bni/tips-edukasi/articleid/25794): wondr, Bayar & Beli, Pajak, Penerimaan Negara.

### Unreadable QR: verified session workaround

MPN rendered a dense 57 by 57 module QR as a 200 by 200 SVG, with the QR touching the image boundary against a dark surrounding page. The user reported no recognition by the GoPay camera and rejection of an uploaded photo. Increasing browser zoom alone was not verified as a solution.

The original rendered vector was converted to the same binary module matrix. A 520 by 520 PNG preserved all modules and added four white modules of quiet zone on every side, at eight pixels per module. No payment data was intentionally changed. The user confirmed this PNG was recognized and the payment completed; the resulting eVisa Paid status and NTPN were checked separately.

This is one verified interoperability workaround, not proof that all GoPay QR payments require an added border, or that GoPay rather than the source generator caused the problem. The successful export changed the quiet zone, image format and raster resolution together, so the margin was not isolated in a controlled test. [DENSO WAVE specifies a four-module quiet zone](https://www.qrcode.com/en/howto/code.html/index.html) for standard QR codes; this supports checking the source renderer before attributing the issue solely to the wallet. The payment payload, embedded amount, merchant and CRC were not independently decoded during the local conversion. Confirm the amount and merchant in the wallet before PIN. Never generate a replacement payment QR from guessed or retyped payment data.

[GoPay supports uploading a QR from the gallery](https://gopay.co.id/blog/fitur-qris-upload-gopay). Its [unrecognized-QR help](https://gopay.co.id/bantuan/bayar-via-kode-qr/pembayaran-dengan-scan-qr-tidak-dikenali) does not establish the cause of this particular failure.

## Optional outbound-ticket purchase

Use an issued genuine e-ticket or a confirmation that satisfies the responsible office. A retailer's payment receipt alone does not prove airline ticket issuance, and an absent delay label does not promise instant issuance. Booking-specific issuance deadlines take precedence over a retailer's general help article.

For Traveloka's optional cancellation protection, verify the exact offer, claim deadline, eligibility, payout destination and excluded premiums or fees. A refundable-fare badge does not establish that every part of the purchase will be returned. [Product conditions](https://www.traveloka.com/id-id/buyback) and the saved booking's policy are relevant; the original payment method alone does not establish the insurance payout method.

## Dated Traveloka example: merchant refund completion on 31 October

On 31 October 2026, the owner authorized a refund request through the existing Traveloka web booking. The selected passenger and `Personal Reason` / `Self-cancellation (change of plan)` were reviewed, and the owner explicitly confirmed acceptance of the displayed Refund Policy before submission. The web result and an independent official Traveloka email confirmed that the request was submitted. The review specified the original payment card as the refund destination. This observed destination is specific to this booking; inspect the current review rather than assuming a bank-account-only payout from generic product terms.

A fresh reload on 31 October showed `Refund Process Completed`, four minutes after the recorded submission. Traveloka displayed a refund to the original payment card and the selected method marked `Done`. This verifies merchant-side completion for this case, not a universal four-minute refund promise. The interface instructed the owner to contact the payment provider if the amount was not reflected after 14 working days. The bank statement was not inspected, so actual card credit remains unverified; final airline cancellation was not independently checked. Keep submitted requests, merchant completion, airline records and credited funds distinct. Keep the booking, refund and payment identifiers and private confirmation links outside this package.
