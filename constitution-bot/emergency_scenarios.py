"""
emergency_scenarios.py

Structured content for Ordo Juris's "I need help right now" Emergency Mode.

NOTE: This is general legal information, not legal advice. Laws and procedures
can vary by state and change over time — always verify with a lawyer or the
official helplines listed under "get_help" for anything urgent or high-stakes.
"""

EMERGENCY_SCENARIOS_EN = {

    "police_stopped": {
        "title": "Police stopped me",
        "what_to_know": [
            "Police can stop and question you, but they must identify themselves if asked.",
            "Being stopped is not the same as being arrested — you are not automatically in custody.",
            "You do not have to answer questions beyond identifying yourself, in most situations.",
        ],
        "what_you_can_do": [
            "Calmly ask the officer for their name, rank, and station (ID card / badge number).",
            "Ask clearly: 'Am I being detained, or am I free to go?'",
            "If a search is being conducted, ask for it to be done as per procedure (e.g., in the presence of a witness where applicable).",
            "Note the time, place, and officer details as soon as you can — mentally or by writing it down.",
        ],
        "what_not_to_do": [
            "Don't argue, run, or physically resist — this can be used against you regardless of who is at fault.",
            "Don't sign any document you don't fully understand.",
            "Don't hand over your phone or let it be searched without a clear legal basis — ask them to state the basis.",
        ],
        "your_rights": [
            {"article": "Article 21", "desc": "Right to life and personal liberty — protects against arbitrary or unlawful treatment."},
            {"article": "Article 22", "desc": "Protections that apply if the stop escalates into arrest (see 'I've been arrested')."},
        ],
        "get_help": [
            {"name": "Police Control Room", "contact": "112 (All-India Emergency Number)"},
            {"name": "National Legal Services Authority (NALSA)", "contact": "15100 / nalsa.gov.in"},
        ],
    },

    "arrested": {
        "title": "I've been arrested",
        "what_to_know": [
            "You have the right to know the grounds of your arrest as soon as possible.",
            "You have the right to consult and be defended by a lawyer of your choice — including at the time of arrest, not just later.",
            "You must be produced before a magistrate within 24 hours of arrest (excluding travel time).",
            "Offences are either 'bailable' or 'non-bailable'. For a bailable offence, bail is a right — the police or court generally must grant it. For a non-bailable offence, bail is at the court's discretion.",
            "A woman generally cannot be arrested after sunset and before sunrise except in exceptional circumstances, and only with prior permission and by a woman police officer where possible.",
            "If the person arrested is a minor (under 18), they must be treated under the Juvenile Justice Act — produced before a Juvenile Justice Board, not a regular criminal court, and generally not handcuffed.",
        ],
        "what_you_can_do": [
            "Ask clearly and calmly: 'What is the reason for my arrest, and is this a bailable offence?'",
            "Ask to inform a family member, friend, or lawyer of your arrest and location — this is a right, not a favour.",
            "Request access to a lawyer immediately — you don't have to wait until questioning starts.",
            "If you cannot afford a lawyer, ask for free legal aid (this is a constitutional guarantee) — say clearly: 'I want a legal aid lawyer.'",
            "If your lawyer isn't reachable: stay calm, state that you wish to remain silent until you have legal representation, and repeat your request to contact the Legal Services Authority (15100).",
            "Ask for a copy of the arrest memo (a written record of the arrest, witnessed and signed) — this is a legal requirement.",
            "If you're taken for a medical exam, you're entitled to one, and it should be documented — this protects you if there's ever a dispute about your treatment in custody.",
        ],
        "what_not_to_do": [
            "Don't sign any confession or statement without your lawyer present.",
            "Don't resist physically, even if you believe the arrest is wrongful — challenge it legally afterward.",
            "Don't assume you must answer every question — you have the right against self-incrimination.",
            "Don't panic if bail isn't immediate — ask specifically whether the offence is bailable, since that changes the process significantly.",
        ],
        "your_rights": [
            {"article": "Article 22(1)", "desc": "Right to be informed of grounds of arrest and to consult a lawyer of your choice."},
            {"article": "Article 22(2)", "desc": "Right to be produced before a magistrate within 24 hours of arrest."},
            {"article": "Article 20(3)", "desc": "Protection against being compelled to be a witness against yourself."},
            {"article": "Article 39A", "desc": "State's duty to provide free legal aid to those who cannot afford it."},
            {"article": "D.K. Basu v. State of West Bengal (1997)", "desc": "Supreme Court guidelines requiring an arrest memo, medical exam, and the right to inform a relative/friend at the time of arrest."},
        ],
        "get_help": [
            {"name": "NALSA Free Legal Aid Helpline", "contact": "15100"},
            {"name": "District Legal Services Authority (DLSA)", "contact": "Search 'DLSA + your district'"},
            {"name": "Police Control Room", "contact": "112"},
        ],
    },

    "house_search": {
        "title": "Police want to search my house",
        "what_to_know": [
            "In most cases, police need a search warrant issued by a magistrate to search your home.",
            "Searches without a warrant are only allowed in specific, limited circumstances (e.g., in hot pursuit, or to prevent evidence destruction).",
            "A search should generally be conducted in the presence of independent witnesses.",
        ],
        "what_you_can_do": [
            "Politely ask to see the search warrant and read it — note the name of the issuing authority and date.",
            "Ask for the names and addresses of the witnesses (panchas) present during the search.",
            "Request a copy of the seizure list (panchnama) if anything is taken, and ensure you and the witnesses sign only what accurately reflects what was found.",
        ],
        "what_not_to_do": [
            "Don't obstruct the police physically, even if you dispute the warrant's validity — raise objections through legal channels later.",
            "Don't sign a blank or incomplete seizure list.",
            "Don't let the search happen without at least trying to have independent witnesses present.",
        ],
        "your_rights": [
            {"article": "Article 21", "desc": "Right to life and personal liberty, which includes protection of your dignity during a search."},
            {"article": "Article 19(1)(d)/(e)", "desc": "Broader freedoms that inform how state action in your home must be lawful and proportionate."},
        ],
        "get_help": [
            {"name": "NALSA Free Legal Aid Helpline", "contact": "15100"},
            {"name": "Local Bar Association", "contact": "Search '[your district] bar association'"},
        ],
    },

    "money_demand": {
        "title": "Someone is demanding money (bribery / extortion)",
        "what_to_know": [
            "Demanding a bribe from a public servant is a criminal offence under anti-corruption law.",
            "Extortion by threat of harm is also a criminal offence, regardless of who is demanding it.",
            "You are generally protected, and in many cases encouraged, to report bribery demands.",
        ],
        "what_you_can_do": [
            "If safe to do so, note the date, time, place, and identity of the person demanding money.",
            "Report to the Anti-Corruption Bureau (ACB) in your state, or the Central Vigilance Commission for central government matters.",
            "For extortion/threats, file a police complaint (FIR) at the nearest station.",
        ],
        "what_not_to_do": [
            "Don't pay the bribe if you can avoid it — it can complicate any later complaint.",
            "Don't confront the person aggressively if you fear for your safety — report through official channels instead.",
        ],
        "your_rights": [
            {"article": "Article 14", "desc": "Equality before law — public servants are not above the law."},
            {"article": "Prevention of Corruption Act, 1988", "desc": "Criminalises demanding or accepting bribes by public servants."},
        ],
        "get_help": [
            {"name": "Central Vigilance Commission", "contact": "cvc.gov.in / 1964"},
            {"name": "State Anti-Corruption Bureau", "contact": "Search '[your state] ACB helpline'"},
            {"name": "Police / FIR", "contact": "112"},
        ],
    },

    "employer_not_paying": {
        "title": "Employer isn't paying me",
        "what_to_know": [
            "Non-payment or delayed payment of wages is addressed under labour laws such as the Payment of Wages Act and the Code on Wages.",
            "You generally have the right to timely payment for work done, regardless of employment type.",
            "You can approach a Labour Court or the Labour Commissioner's office for unpaid wages.",
        ],
        "what_you_can_do": [
            "Keep records: appointment letter, payslips, attendance, messages about pay promised.",
            "First, request payment formally in writing (email/letter) and keep a copy.",
            "If unresolved, file a complaint with the local Labour Commissioner's office.",
            "For larger or organised-sector disputes, you can approach the Labour Court.",
        ],
        "what_not_to_do": [
            "Don't rely only on verbal assurances — get things in writing where possible.",
            "Don't sign a resignation or 'full and final settlement' you don't agree with, just to get paid faster.",
        ],
        "your_rights": [
            {"article": "Article 39(a)", "desc": "State's directive to secure an adequate means of livelihood for citizens."},
            {"article": "Article 23", "desc": "Prohibits forced labour — this can be relevant if you're being made to work without fair pay."},
            {"article": "Payment of Wages Act, 1936 / Code on Wages, 2019", "desc": "Statutory right to timely and full payment of wages."},
        ],
        "get_help": [
            {"name": "Labour Commissioner's Office", "contact": "Search '[your state] labour commissioner'"},
            {"name": "Shram Suvidha Portal", "contact": "shramsuvidha.gov.in"},
            {"name": "NALSA Free Legal Aid", "contact": "15100"},
        ],
    },

    "child_labour": {
        "title": "Child labour",
        "what_to_know": [
            "Employing a child below 14 years in any occupation is prohibited.",
            "Employing adolescents (14–18) in hazardous occupations is also prohibited.",
            "This is both a constitutional protection and a criminal offence under the Child Labour (Prohibition and Regulation) Act.",
        ],
        "what_you_can_do": [
            "Report the case to Childline (a free, 24x7 national helpline) or the local police.",
            "You can also inform the Labour Department or the local Child Welfare Committee.",
            "If safe, note the location, employer details, and approximate age of the child.",
        ],
        "what_not_to_do": [
            "Don't confront the employer directly if it could put you or the child at risk — report to authorities instead.",
            "Don't assume it's 'not your place to report' — child labour reporting is actively encouraged and can be done anonymously in many cases.",
        ],
        "your_rights": [
            {"article": "Article 24", "desc": "No child below 14 years shall be employed in any factory, mine, or hazardous employment."},
            {"article": "Article 21A", "desc": "Right to free and compulsory education for children aged 6–14."},
            {"article": "Article 39(e)/(f)", "desc": "State's duty to protect children from abuse and ensure healthy development."},
        ],
        "get_help": [
            {"name": "Childline India", "contact": "1098"},
            {"name": "Police", "contact": "112"},
            {"name": "Child Welfare Committee (CWC)", "contact": "Search '[your district] CWC'"},
        ],
    },

    "court_notice": {
        "title": "Court / legal notice received",
        "what_to_know": [
            "A legal notice or court summons is a formal document — ignoring it can lead to consequences like an ex-parte order against you.",
            "You usually have a specific window of time to respond or appear.",
            "Not every notice means you're guilty of something — many are procedural or the start of a dispute resolution process.",
        ],
        "what_you_can_do": [
            "Read the notice carefully — note the deadline, the issuing court/authority, and what is being asked of you.",
            "Consult a lawyer as soon as possible, especially if there's a response deadline.",
            "If you can't afford a lawyer, approach the Legal Services Authority for free legal aid.",
            "Keep the original notice and any envelope/proof of delivery safe.",
        ],
        "what_not_to_do": [
            "Don't ignore it — deadlines in legal matters are often strict.",
            "Don't respond directly (especially in writing) without legal advice, as it can affect your position later.",
        ],
        "your_rights": [
            {"article": "Article 39A", "desc": "State's duty to ensure free legal aid so that justice is not denied due to economic hardship."},
            {"article": "Article 21", "desc": "Right to a fair procedure — includes the right to be properly heard."},
        ],
        "get_help": [
            {"name": "NALSA Free Legal Aid Helpline", "contact": "15100"},
            {"name": "District Legal Services Authority (DLSA)", "contact": "Search 'DLSA + your district'"},
        ],
    },

    "hospital_legal": {
        "title": "Hospital / medical legal issue",
        "what_to_know": [
            "Hospitals cannot refuse emergency treatment on the grounds of inability to pay upfront.",
            "You generally have the right to informed consent before any procedure.",
            "You have the right to access your own medical records.",
        ],
        "what_you_can_do": [
            "In a medical emergency, insist on treatment first — payment/formalities can follow.",
            "Ask for a written explanation of any procedure before consenting.",
            "For disputes (e.g., negligence, billing issues), you can approach the Consumer Forum or the State Medical Council.",
        ],
        "what_not_to_do": [
            "Don't sign consent forms you don't understand — ask for clarification or a translation.",
            "Don't let a hospital delay emergency care over payment — this can be reported.",
        ],
        "your_rights": [
            {"article": "Article 21", "desc": "Right to life includes the right to emergency medical treatment."},
            {"article": "Consumer Protection Act, 2019", "desc": "Covers medical negligence and deficiency of service as consumer disputes."},
        ],
        "get_help": [
            {"name": "National Consumer Helpline", "contact": "1915"},
            {"name": "State Medical Council", "contact": "Search '[your state] medical council'"},
            {"name": "Ambulance / Emergency", "contact": "108 / 112"},
        ],
    },

    "domestic_violence": {
        "title": "Domestic violence",
        "what_to_know": [
            "Domestic violence includes physical, emotional, sexual, verbal, and economic abuse — not just physical harm.",
            "You have the right to reside in the shared household, regardless of whose name it's registered in.",
            "Protection orders, monetary relief, custody orders, and residence orders can all be obtained through the Protection of Women from Domestic Violence Act, 2005 (PWDVA) — this is a civil remedy, separate from filing a criminal case.",
            "You can pursue a PWDVA case and a criminal complaint (e.g., under cruelty provisions) at the same time — they aren't mutually exclusive.",
            "A Protection Officer's job is specifically to help you file a Domestic Incident Report and connect you to shelter, medical aid, and legal aid — you don't need a lawyer to make first contact with one.",
        ],
        "what_you_can_do": [
            "If you're in immediate danger, call 112 or go to the nearest police station — you can also ask the police to accompany you to safety.",
            "Contact a Protection Officer (appointed under the DV Act) in your district — they can help you file a Domestic Incident Report (DIR), which is often the first formal step.",
            "Reach out to the Women's Helpline (181) for guidance, shelter information, and counseling — available 24x7 and confidential.",
            "Keep evidence where safe to do so — messages, photos, medical records, witness contacts. If it's not safe to keep evidence at home, consider storing it with a trusted person or in cloud storage.",
            "Consider reaching out to a One Stop Centre (Sakhi) — these provide medical aid, police assistance, legal aid, and shelter all in one place, run by the state.",
            "If children are involved, you can request interim custody as part of the same DV Act proceedings.",
        ],
        "what_not_to_do": [
            "Don't feel you have to resolve it alone or that it's a 'private matter' — support structures exist specifically for this.",
            "Don't sign any agreement (including a settlement or a document 'to keep the peace') under pressure without understanding your rights first.",
            "Don't wait for a single 'serious enough' incident — a pattern of escalating behaviour is valid grounds to seek a protection order.",
        ],
        "your_rights": [
            {"article": "Article 21", "desc": "Right to life with dignity — the foundation for protection from domestic violence."},
            {"article": "Article 15(3)", "desc": "Allows the State to make special provisions for women — the legal basis for laws like the DV Act."},
            {"article": "Protection of Women from Domestic Violence Act, 2005", "desc": "Provides protection orders, residence rights, monetary relief, and custody orders through a civil process."},
        ],
        "get_help": [
            {"name": "Women's Helpline", "contact": "181"},
            {"name": "Police", "contact": "112"},
            {"name": "One Stop Centre (Sakhi)", "contact": "Search 'One Stop Centre + your district'"},
            {"name": "National Commission for Women", "contact": "ncw.nic.in"},
        ],
    },

    "online_harassment": {
        "title": "Online harassment / fraud",
        "what_to_know": [
            "Cyberbullying, stalking, and online fraud are criminal offences under the IT Act and the Bharatiya Nyaya Sanhita.",
            "You can report cybercrime online, from anywhere in India, through the National Cyber Crime Reporting Portal, without needing to visit a police station first.",
            "For financial fraud, speed matters — many banks and payment platforms can freeze or reverse a transaction if reported within the first few hours ('Golden Hour').",
            "Sextortion and non-consensual sharing of intimate images are specifically criminalised — you are not at fault, and reporting is strongly encouraged even if you feel embarrassed.",
            "Evidence (screenshots, links, transaction IDs, sender details) significantly helps investigation — but the portal and police can still act even with partial evidence.",
        ],
        "what_you_can_do": [
            "For financial fraud: call the Cyber Crime Helpline (1930) immediately — this is specifically for fast-tracking bank/UPI transaction freezes.",
            "Take screenshots of the harassment/fraud, including usernames, timestamps, URLs, and any transaction IDs — do this before blocking the person.",
            "Report on the National Cyber Crime Reporting Portal (cybercrime.gov.in) — you can file anonymously for certain categories, including women/child-related crimes.",
            "Block/report the account on the platform itself, in addition to filing an official complaint — these are independent, do both.",
            "If it involves a minor, or non-consensual images of anyone, report immediately — these are treated as priority cases.",
            "Save your bank/payment app's fraud reporting number in advance — most major banks have a dedicated 24x7 fraud line separate from customer care.",
        ],
        "what_not_to_do": [
            "Don't delete evidence, even if it's distressing — preserve it first, then report or block.",
            "Don't engage or negotiate directly with a scammer/blackmailer, and don't pay a sextortion demand — it rarely stops the threats and can escalate them.",
            "Don't assume nothing can be done because the person is anonymous or 'untraceable' — cyber cells can often trace accounts through platform cooperation.",
            "Don't wait to 'gather more proof' before reporting financial fraud — every hour reduces the chance of recovering funds.",
        ],
        "your_rights": [
            {"article": "Article 21", "desc": "Right to privacy and dignity, recognised as part of the right to life (K.S. Puttaswamy v. Union of India, 2017)."},
            {"article": "Information Technology Act, 2000", "desc": "Covers cyberstalking, identity theft, obscene content, and online fraud."},
            {"article": "Bharatiya Nyaya Sanhita, 2023", "desc": "Covers stalking, defamation, and related offences alongside the IT Act."},
        ],
        "get_help": [
            {"name": "National Cyber Crime Helpline (fraud/reporting)", "contact": "1930"},
            {"name": "Cyber Crime Reporting Portal", "contact": "cybercrime.gov.in"},
            {"name": "Police", "contact": "112"},
        ],
    },

    "workplace_harassment": {
        "title": "Sexual harassment at work",
        "what_to_know": [
            "Every workplace with 10+ employees is legally required to have an Internal Complaints Committee (ICC) under the POSH Act.",
            "Sexual harassment includes unwelcome physical contact, sexual remarks, showing pornography, or any unwelcome sexual conduct — verbal or non-verbal.",
            "You have the right to complain without fear of retaliation, and the law requires the complaint to be handled confidentially.",
            "If your workplace has no ICC (e.g., small business, unorganised sector), you can approach the Local Complaints Committee set up by the district.",
        ],
        "what_you_can_do": [
            "Write down what happened as soon as possible — date, time, place, what was said/done, and any witnesses.",
            "File a written complaint with the Internal Complaints Committee (ICC) — this can typically be done within 3 months of the incident (extendable).",
            "If there's no ICC or you're unsure who to approach, contact the Local Complaints Committee (LCC) for your district.",
            "Keep copies of any messages, emails, or documents related to the incident.",
        ],
        "what_not_to_do": [
            "Don't assume you have to resolve it informally or 'let it go' to protect your job — retaliation for a good-faith complaint is itself prohibited.",
            "Don't delete relevant messages or evidence, even if you're unsure whether to file a complaint yet.",
        ],
        "your_rights": [
            {"article": "Article 14 / 15", "desc": "Equality and non-discrimination, including on the basis of sex, at the workplace."},
            {"article": "Article 21", "desc": "Right to life with dignity — includes the right to a safe working environment."},
            {"article": "Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013 (POSH Act)", "desc": "Mandates an Internal Complaints Committee and a defined redressal process."},
            {"article": "Vishaka v. State of Rajasthan (1997)", "desc": "The Supreme Court judgment that first laid down workplace sexual harassment guidelines, later codified into the POSH Act."},
        ],
        "get_help": [
            {"name": "Women's Helpline", "contact": "181"},
            {"name": "National Commission for Women", "contact": "ncw.nic.in"},
            {"name": "SHe-Box (online POSH complaint portal)", "contact": "shebox.wcd.gov.in"},
        ],
    },

    "landlord_tenant": {
        "title": "Landlord / tenant dispute or illegal eviction",
        "what_to_know": [
            "A landlord generally cannot evict a tenant without following due legal process, even if there's no formal written agreement.",
            "'Self-help' eviction — such as changing locks, cutting off water/electricity, or removing your belongings without a court order — is not legal, even if rent is unpaid.",
            "Security deposit rules, notice periods, and eviction grounds vary by state's Rent Control Act.",
        ],
        "what_you_can_do": [
            "Keep proof of tenancy — rent receipts, bank transfers, any written or messaged agreement, utility bills in your name.",
            "If you're threatened with illegal eviction, you can approach the local police to prevent a breach of peace, and simultaneously consult a lawyer about an injunction.",
            "For rent/deposit disputes, you can approach the Rent Control Court or Civil Court in your area, depending on your state's law.",
            "Document any harassment (calls, messages, visits) with timestamps.",
        ],
        "what_not_to_do": [
            "Don't vacate immediately just because you've been verbally told to leave — ask for the legal basis and timeline in writing.",
            "Don't sign any document (like a 'voluntary vacate' letter) under pressure.",
        ],
        "your_rights": [
            {"article": "Article 21", "desc": "Right to life and personal liberty — courts have read the right to shelter into this."},
            {"article": "State Rent Control Acts", "desc": "Govern eviction procedure, notice periods, and rent disputes — these vary by state."},
        ],
        "get_help": [
            {"name": "NALSA Free Legal Aid Helpline", "contact": "15100"},
            {"name": "Local Rent Control Office / Civil Court", "contact": "Search '[your state] rent control act'"},
            {"name": "Police (to prevent illegal 'self-help' eviction)", "contact": "112"},
        ],
    },

    "dowry_harassment": {
        "title": "Dowry harassment",
        "what_to_know": [
            "Demanding, giving, or taking dowry is illegal under the Dowry Prohibition Act, 1961.",
            "Harassment for dowry — including cruelty, threats, or violence connected to dowry demands — is a criminal offence.",
            "This can be pursued alongside a domestic violence case (PWDVA) if the harassment is happening within the marital home.",
        ],
        "what_you_can_do": [
            "If you're in immediate danger, call 112.",
            "Contact the Women's Helpline (181) for guidance and connection to a Protection Officer or One Stop Centre.",
            "File a complaint with the police — dowry harassment and related cruelty are criminal offences that can be reported directly.",
            "Preserve any evidence — messages, witnesses, financial records of dowry demands or transfers.",
        ],
        "what_not_to_do": [
            "Don't treat it as a private family matter that must be resolved silently — the law treats this as a criminal issue, not just a domestic one.",
            "Don't sign any document under pressure from your marital family, including anything related to property or 'settlement'.",
        ],
        "your_rights": [
            {"article": "Article 21", "desc": "Right to life with dignity."},
            {"article": "Article 15(3)", "desc": "Basis for special protective laws for women."},
            {"article": "Dowry Prohibition Act, 1961", "desc": "Criminalises the giving, taking, and demanding of dowry."},
            {"article": "Protection of Women from Domestic Violence Act, 2005", "desc": "Can apply where dowry harassment overlaps with domestic abuse."},
        ],
        "get_help": [
            {"name": "Women's Helpline", "contact": "181"},
            {"name": "Police", "contact": "112"},
            {"name": "One Stop Centre (Sakhi)", "contact": "Search 'One Stop Centre + your district'"},
        ],
    },

    "senior_citizen_abuse": {
        "title": "Senior citizen neglect or abuse",
        "what_to_know": [
            "Senior citizens have a legal right to be maintained by their children or legal heirs under the Maintenance and Welfare of Parents and Senior Citizens Act, 2007.",
            "This law also allows a Tribunal to order children/relatives to pay maintenance, and even allows cancellation of a property transfer if it was made on the condition of being cared for and that condition wasn't honoured.",
            "Abandonment of a senior citizen is a criminal offence under this Act.",
        ],
        "what_you_can_do": [
            "Approach the Maintenance Tribunal set up under the Senior Citizens Act in your district — the process is designed to be simple and fast, and doesn't require a lawyer.",
            "If there's immediate danger or abandonment, contact the police or the Senior Citizens' Helpline.",
            "If property was transferred on a promise of care that isn't being honoured, you can apply to have that transfer declared void through the Tribunal.",
        ],
        "what_not_to_do": [
            "Don't assume nothing can be done because it involves family — the law specifically anticipates and addresses this situation.",
            "Don't sign away property or assets under pressure, even from close family.",
        ],
        "your_rights": [
            {"article": "Article 21", "desc": "Right to life with dignity, which the Supreme Court has extended to include a dignified old age."},
            {"article": "Article 41", "desc": "Directive Principle requiring the State to make provisions for public assistance in old age."},
            {"article": "Maintenance and Welfare of Parents and Senior Citizens Act, 2007", "desc": "Provides for maintenance, protection of property, and welfare of senior citizens."},
        ],
        "get_help": [
            {"name": "Elderline (Senior Citizens' Helpline)", "contact": "14567"},
            {"name": "Maintenance Tribunal", "contact": "Search '[your district] senior citizen tribunal'"},
            {"name": "Police", "contact": "112"},
        ],
    },

    "consumer_fraud": {
        "title": "Consumer fraud (products, services, e-commerce)",
        "what_to_know": [
            "You have the right to safety, information, choice, and redressal as a consumer under the Consumer Protection Act, 2019.",
            "This covers defective products, deficient services, misleading advertisements, and unfair trade practices — including online purchases and digital services.",
            "There's no need for a lawyer to file a basic consumer complaint — Consumer Commissions are designed to be accessible without one.",
        ],
        "what_you_can_do": [
            "Keep all proof: order confirmation, payment receipt, chat/email with the seller, photos of the defective product.",
            "First, try to resolve it with the seller/platform in writing — this creates a paper trail even if it doesn't resolve.",
            "Call the National Consumer Helpline (1915) for free guidance on next steps.",
            "File a complaint on the e-Daakhil portal (the online consumer complaint filing system) if the seller doesn't resolve it.",
        ],
        "what_not_to_do": [
            "Don't rely only on phone calls with the seller — get responses in writing/email/chat wherever possible.",
            "Don't let the seller pressure you into 'store credit' if you're entitled to a refund and want one.",
        ],
        "your_rights": [
            {"article": "Article 21", "desc": "Right to life, extended by courts in ways relevant to consumer safety and wellbeing."},
            {"article": "Consumer Protection Act, 2019", "desc": "Grants the right to safety, information, choice, redressal, and covers e-commerce specifically."},
        ],
        "get_help": [
            {"name": "National Consumer Helpline", "contact": "1915"},
            {"name": "e-Daakhil (online complaint portal)", "contact": "edaakhil.nic.in"},
        ],
    },
}

EMERGENCY_SCENARIOS_HI = {

    "police_stopped": {
        "title": "पुलिस ने मुझे रोका",
        "what_to_know": [
            "पुलिस आपको रोक कर पूछताछ कर सकती है, लेकिन पूछने पर उन्हें अपनी पहचान बतानी होगी।",
            "रोका जाना गिरफ्तारी के समान नहीं है — आप स्वतः हिरासत में नहीं आ जाते।",
            "ज्यादातर स्थितियों में आपको अपनी पहचान बताने के अलावा और सवालों के जवाब देने की जरूरत नहीं है।",
        ],
        "what_you_can_do": [
            "शांति से अधिकारी से उनका नाम, पद और थाना (आईडी कार्ड / बैज नंबर) पूछें।",
            "स्पष्ट रूप से पूछें: 'क्या मुझे हिरासत में लिया जा रहा है, या मैं जा सकता/सकती हूं?'",
            "अगर तलाशी ली जा रही है, तो उचित प्रक्रिया के अनुसार (जैसे, गवाह की उपस्थिति में जहां लागू हो) करने को कहें।",
            "समय, स्थान और अधिकारी का विवरण जल्द से जल्द याद रखें या लिख लें।",
        ],
        "what_not_to_do": [
            "बहस न करें, भागें नहीं, या शारीरिक रूप से विरोध न करें — इसका इस्तेमाल गलती किसकी भी हो, आपके खिलाफ हो सकता है।",
            "ऐसा कोई दस्तावेज़ न साइन करें जिसे आप पूरी तरह से नहीं समझते।",
            "बिना स्पष्ट कानूनी आधार के अपना फोन न दें या उसे तलाशी लेने न दें — आधार बताने को कहें।",
        ],
        "your_rights": [
            {"article": "अनुच्छेद 21", "desc": "जीवन और व्यक्तिगत स्वतंत्रता का अधिकार — मनमाने या गैरकानूनी व्यवहार से सुरक्षा देता है।"},
            {"article": "अनुच्छेद 22", "desc": "अगर रोकना गिरफ्तारी में बदल जाए तो लागू होने वाली सुरक्षा (देखें 'मुझे गिरफ्तार कर लिया गया है')।"},
        ],
        "get_help": [
            {"name": "पुलिस कंट्रोल रूम", "contact": "112 (अखिल भारतीय आपातकालीन नंबर)"},
            {"name": "राष्ट्रीय विधिक सेवा प्राधिकरण (NALSA)", "contact": "15100 / nalsa.gov.in"},
        ],
    },

    "arrested": {
        "title": "मुझे गिरफ्तार कर लिया गया है",
        "what_to_know": [
            "आपको जल्द से जल्द अपनी गिरफ्तारी का कारण जानने का अधिकार है।",
            "आपको अपनी पसंद के वकील से सलाह लेने और उसके द्वारा बचाव किए जाने का अधिकार है — गिरफ्तारी के समय से ही, न कि केवल बाद में।",
            "आपको गिरफ्तारी के 24 घंटे के भीतर (यात्रा का समय छोड़कर) मजिस्ट्रेट के सामने पेश किया जाना चाहिए।",
            "अपराध या तो 'जमानती' या 'गैर-जमानती' होते हैं। जमानती अपराध में जमानत आपका अधिकार है — पुलिस या अदालत को आमतौर पर इसे देना ही होता है। गैर-जमानती अपराध में जमानत अदालत के विवेक पर निर्भर करती है।",
            "एक महिला को आमतौर पर सूर्यास्त के बाद और सूर्योदय से पहले गिरफ्तार नहीं किया जा सकता, सिवाय असाधारण परिस्थितियों के, और वह भी पूर्व अनुमति के साथ और जहां संभव हो, महिला पुलिस अधिकारी द्वारा।",
            "अगर गिरफ्तार व्यक्ति नाबालिग (18 वर्ष से कम) है, तो उसके साथ किशोर न्याय अधिनियम के तहत व्यवहार किया जाना चाहिए — नियमित आपराधिक अदालत के बजाय किशोर न्याय बोर्ड के सामने पेश किया जाना चाहिए, और आमतौर पर हथकड़ी नहीं लगाई जानी चाहिए।",
        ],
        "what_you_can_do": [
            "शांति से स्पष्ट रूप से पूछें: 'मेरी गिरफ्तारी का कारण क्या है, और क्या यह जमानती अपराध है?'",
            "किसी परिवार के सदस्य, दोस्त, या वकील को अपनी गिरफ्तारी और स्थान के बारे में सूचित करने के लिए कहें — यह आपका अधिकार है, कोई एहसान नहीं।",
            "तुरंत वकील तक पहुंच का अनुरोध करें — पूछताछ शुरू होने का इंतजार करने की जरूरत नहीं है।",
            "अगर आप वकील का खर्च नहीं उठा सकते, तो मुफ्त कानूनी सहायता मांगें (यह एक संवैधानिक गारंटी है) — स्पष्ट रूप से कहें: 'मुझे कानूनी सहायता वकील चाहिए।'",
            "अगर आपका वकील उपलब्ध नहीं है: शांत रहें, कहें कि आप कानूनी प्रतिनिधित्व मिलने तक चुप रहना चाहते हैं, और विधिक सेवा प्राधिकरण (15100) से संपर्क करने का अनुरोध दोहराएं।",
            "गिरफ्तारी मेमो (गिरफ्तारी का एक लिखित रिकॉर्ड, गवाह और हस्ताक्षरित) की एक प्रति मांगें — यह एक कानूनी आवश्यकता है।",
            "अगर आपको चिकित्सा जांच के लिए ले जाया जाता है, तो आप इसके हकदार हैं, और इसे दस्तावेज़ित किया जाना चाहिए — यह हिरासत में आपके साथ व्यवहार को लेकर किसी भी विवाद की स्थिति में आपकी सुरक्षा करता है।",
        ],
        "what_not_to_do": [
            "अपने वकील की उपस्थिति के बिना कोई इकबालिया बयान या स्टेटमेंट साइन न करें।",
            "शारीरिक रूप से विरोध न करें, भले ही आपको लगे कि गिरफ्तारी गलत है — इसे बाद में कानूनी रूप से चुनौती दें।",
            "यह न मानें कि आपको हर सवाल का जवाब देना ही है — आपको खुद के खिलाफ गवाही न देने का अधिकार है।",
            "अगर जमानत तुरंत नहीं मिलती तो घबराएं नहीं — विशेष रूप से पूछें कि क्या अपराध जमानती है, क्योंकि इससे प्रक्रिया काफी बदल जाती है।",
        ],
        "your_rights": [
            {"article": "अनुच्छेद 22(1)", "desc": "गिरफ्तारी के आधार के बारे में सूचित किए जाने और अपनी पसंद के वकील से सलाह लेने का अधिकार।"},
            {"article": "अनुच्छेद 22(2)", "desc": "गिरफ्तारी के 24 घंटे के भीतर मजिस्ट्रेट के सामने पेश किए जाने का अधिकार।"},
            {"article": "अनुच्छेद 20(3)", "desc": "खुद के खिलाफ गवाह बनने के लिए मजबूर न किए जाने से सुरक्षा।"},
            {"article": "अनुच्छेद 39A", "desc": "जो लोग खर्च नहीं उठा सकते उन्हें मुफ्त कानूनी सहायता प्रदान करने का राज्य का कर्तव्य।"},
            {"article": "डी.के. बसु बनाम पश्चिम बंगाल राज्य (1997)", "desc": "सुप्रीम कोर्ट के दिशानिर्देश जिनमें गिरफ्तारी मेमो, चिकित्सा जांच, और गिरफ्तारी के समय किसी रिश्तेदार/दोस्त को सूचित करने का अधिकार शामिल है।"},
        ],
        "get_help": [
            {"name": "NALSA मुफ्त कानूनी सहायता हेल्पलाइन", "contact": "15100"},
            {"name": "जिला विधिक सेवा प्राधिकरण (DLSA)", "contact": "'DLSA + आपका जिला' खोजें"},
            {"name": "पुलिस कंट्रोल रूम", "contact": "112"},
        ],
    },

    "house_search": {
        "title": "पुलिस मेरे घर की तलाशी लेना चाहती है",
        "what_to_know": [
            "ज्यादातर मामलों में, पुलिस को आपके घर की तलाशी लेने के लिए मजिस्ट्रेट द्वारा जारी तलाशी वारंट की जरूरत होती है।",
            "बिना वारंट के तलाशी केवल विशिष्ट, सीमित परिस्थितियों में ही अनुमत है (जैसे, तुरंत पीछा करते हुए, या सबूत नष्ट होने से रोकने के लिए)।",
            "तलाशी आमतौर पर स्वतंत्र गवाहों की उपस्थिति में की जानी चाहिए।",
        ],
        "what_you_can_do": [
            "विनम्रता से तलाशी वारंट देखने और पढ़ने को कहें — जारी करने वाले प्राधिकरण का नाम और तारीख नोट करें।",
            "तलाशी के दौरान मौजूद गवाहों (पंचों) के नाम और पते मांगें।",
            "अगर कुछ जब्त किया जाता है तो जब्ती सूची (पंचनामा) की एक प्रति मांगें, और सुनिश्चित करें कि आप और गवाह केवल वही साइन करें जो सही मायने में पाया गया था।",
        ],
        "what_not_to_do": [
            "पुलिस को शारीरिक रूप से न रोकें, भले ही आप वारंट की वैधता पर विवाद करते हों — आपत्तियां बाद में कानूनी माध्यमों से उठाएं।",
            "खाली या अधूरी जब्ती सूची पर साइन न करें।",
            "स्वतंत्र गवाहों को मौजूद रखने की कोशिश किए बिना तलाशी न होने दें।",
        ],
        "your_rights": [
            {"article": "अनुच्छेद 21", "desc": "जीवन और व्यक्तिगत स्वतंत्रता का अधिकार, जिसमें तलाशी के दौरान आपकी गरिमा की सुरक्षा शामिल है।"},
            {"article": "अनुच्छेद 19(1)(d)/(e)", "desc": "व्यापक स्वतंत्रताएं जो यह तय करती हैं कि आपके घर में राज्य की कार्रवाई कानूनी और उचित होनी चाहिए।"},
        ],
        "get_help": [
            {"name": "NALSA मुफ्त कानूनी सहायता हेल्पलाइन", "contact": "15100"},
            {"name": "स्थानीय बार एसोसिएशन", "contact": "'[आपका जिला] बार एसोसिएशन' खोजें"},
        ],
    },

    "money_demand": {
        "title": "कोई पैसे की मांग कर रहा है (रिश्वत / जबरन वसूली)",
        "what_to_know": [
            "किसी सरकारी कर्मचारी द्वारा रिश्वत मांगना भ्रष्टाचार विरोधी कानून के तहत एक आपराधिक अपराध है।",
            "धमकी देकर जबरन वसूली भी एक आपराधिक अपराध है, चाहे मांग कोई भी कर रहा हो।",
            "आप आमतौर पर सुरक्षित हैं, और कई मामलों में रिश्वत की मांग की रिपोर्ट करने के लिए प्रोत्साहित किए जाते हैं।",
        ],
        "what_you_can_do": [
            "अगर सुरक्षित हो, तो पैसे की मांग करने वाले व्यक्ति की तारीख, समय, स्थान और पहचान नोट करें।",
            "अपने राज्य में भ्रष्टाचार निरोधक ब्यूरो (ACB), या केंद्र सरकार के मामलों के लिए केंद्रीय सतर्कता आयोग को रिपोर्ट करें।",
            "जबरन वसूली/धमकी के लिए, निकटतम थाने में पुलिस शिकायत (FIR) दर्ज करें।",
        ],
        "what_not_to_do": [
            "अगर बचा जा सके तो रिश्वत न दें — इससे बाद की कोई शिकायत जटिल हो सकती है।",
            "अगर आपको अपनी सुरक्षा का डर हो तो व्यक्ति का आक्रामक रूप से सामना न करें — इसके बजाय आधिकारिक माध्यमों से रिपोर्ट करें।",
        ],
        "your_rights": [
            {"article": "अनुच्छेद 14", "desc": "कानून के समक्ष समानता — सरकारी कर्मचारी कानून से ऊपर नहीं हैं।"},
            {"article": "भ्रष्टाचार निवारण अधिनियम, 1988", "desc": "सरकारी कर्मचारियों द्वारा रिश्वत मांगने या स्वीकार करने को अपराध घोषित करता है।"},
        ],
        "get_help": [
            {"name": "केंद्रीय सतर्कता आयोग", "contact": "cvc.gov.in / 1964"},
            {"name": "राज्य भ्रष्टाचार निरोधक ब्यूरो", "contact": "'[आपका राज्य] ACB हेल्पलाइन' खोजें"},
            {"name": "पुलिस / FIR", "contact": "112"},
        ],
    },

    "employer_not_paying": {
        "title": "मेरा नियोक्ता मुझे भुगतान नहीं कर रहा",
        "what_to_know": [
            "मजदूरी का भुगतान न करना या देरी से करना वेतन भुगतान अधिनियम और वेतन संहिता जैसे श्रम कानूनों के तहत आता है।",
            "आपको आमतौर पर किए गए काम के लिए समय पर भुगतान पाने का अधिकार है, चाहे रोजगार का प्रकार कोई भी हो।",
            "आप अवैतनिक मजदूरी के लिए श्रम न्यायालय या श्रम आयुक्त के कार्यालय से संपर्क कर सकते हैं।",
        ],
        "what_you_can_do": [
            "रिकॉर्ड रखें: नियुक्ति पत्र, वेतन पर्ची, उपस्थिति, वादा किए गए भुगतान के बारे में संदेश।",
            "पहले, लिखित रूप में (ईमेल/पत्र) औपचारिक रूप से भुगतान का अनुरोध करें और एक प्रति रखें।",
            "अगर समाधान न हो, तो स्थानीय श्रम आयुक्त के कार्यालय में शिकायत दर्ज करें।",
            "बड़े या संगठित क्षेत्र के विवादों के लिए, आप श्रम न्यायालय से संपर्क कर सकते हैं।",
        ],
        "what_not_to_do": [
            "केवल मौखिक आश्वासनों पर भरोसा न करें — जहां संभव हो, चीजों को लिखित में लें।",
            "जल्दी भुगतान पाने के लिए ऐसा इस्तीफा या 'पूर्ण और अंतिम निपटान' न साइन करें जिससे आप सहमत नहीं हैं।",
        ],
        "your_rights": [
            {"article": "अनुच्छेद 39(a)", "desc": "नागरिकों के लिए आजीविका के पर्याप्त साधन सुनिश्चित करने का राज्य का निर्देश।"},
            {"article": "अनुच्छेद 23", "desc": "जबरन श्रम को प्रतिबंधित करता है — अगर आपको बिना उचित वेतन के काम करने के लिए मजबूर किया जा रहा है तो यह प्रासंगिक हो सकता है।"},
            {"article": "वेतन भुगतान अधिनियम, 1936 / वेतन संहिता, 2019", "desc": "समय पर और पूर्ण वेतन भुगतान का वैधानिक अधिकार।"},
        ],
        "get_help": [
            {"name": "श्रम आयुक्त कार्यालय", "contact": "'[आपका राज्य] श्रम आयुक्त' खोजें"},
            {"name": "श्रम सुविधा पोर्टल", "contact": "shramsuvidha.gov.in"},
            {"name": "NALSA मुफ्त कानूनी सहायता", "contact": "15100"},
        ],
    },

    "child_labour": {
        "title": "बाल श्रम",
        "what_to_know": [
            "14 वर्ष से कम उम्र के बच्चे को किसी भी व्यवसाय में नियोजित करना प्रतिबंधित है।",
            "किशोरों (14-18) को खतरनाक व्यवसायों में नियोजित करना भी प्रतिबंधित है।",
            "यह एक संवैधानिक सुरक्षा और बाल श्रम (निषेध और विनियमन) अधिनियम के तहत एक आपराधिक अपराध दोनों है।",
        ],
        "what_you_can_do": [
            "चाइल्डलाइन (एक मुफ्त, 24x7 राष्ट्रीय हेल्पलाइन) या स्थानीय पुलिस को मामले की रिपोर्ट करें।",
            "आप श्रम विभाग या स्थानीय बाल कल्याण समिति को भी सूचित कर सकते हैं।",
            "अगर सुरक्षित हो, तो स्थान, नियोक्ता का विवरण, और बच्चे की अनुमानित उम्र नोट करें।",
        ],
        "what_not_to_do": [
            "अगर इससे आपको या बच्चे को खतरा हो सकता है, तो नियोक्ता का सीधे सामना न करें — इसके बजाय अधिकारियों को रिपोर्ट करें।",
            "यह न मानें कि 'यह आपकी जगह नहीं है रिपोर्ट करना' — बाल श्रम रिपोर्टिंग को सक्रिय रूप से प्रोत्साहित किया जाता है और कई मामलों में गुमनाम रूप से भी की जा सकती है।",
        ],
        "your_rights": [
            {"article": "अनुच्छेद 24", "desc": "14 वर्ष से कम उम्र के किसी भी बच्चे को किसी कारखाने, खान, या खतरनाक रोजगार में नियोजित नहीं किया जाएगा।"},
            {"article": "अनुच्छेद 21A", "desc": "6-14 वर्ष के बच्चों के लिए मुफ्त और अनिवार्य शिक्षा का अधिकार।"},
            {"article": "अनुच्छेद 39(e)/(f)", "desc": "बच्चों को दुर्व्यवहार से बचाने और स्वस्थ विकास सुनिश्चित करने का राज्य का कर्तव्य।"},
        ],
        "get_help": [
            {"name": "चाइल्डलाइन इंडिया", "contact": "1098"},
            {"name": "पुलिस", "contact": "112"},
            {"name": "बाल कल्याण समिति (CWC)", "contact": "'[आपका जिला] CWC' खोजें"},
        ],
    },

    "court_notice": {
        "title": "अदालत / कानूनी नोटिस मिला",
        "what_to_know": [
            "कानूनी नोटिस या अदालती समन एक औपचारिक दस्तावेज़ है — इसे नज़रअंदाज़ करने से आपके खिलाफ एकतरफा आदेश जैसे परिणाम हो सकते हैं।",
            "आपके पास आमतौर पर जवाब देने या पेश होने के लिए एक विशिष्ट समय सीमा होती है।",
            "हर नोटिस का मतलब यह नहीं है कि आप किसी चीज़ के दोषी हैं — कई प्रक्रियात्मक होते हैं या विवाद समाधान प्रक्रिया की शुरुआत होते हैं।",
        ],
        "what_you_can_do": [
            "नोटिस को ध्यान से पढ़ें — समय सीमा, जारी करने वाली अदालत/प्राधिकरण, और आपसे क्या पूछा जा रहा है, नोट करें।",
            "जल्द से जल्द वकील से सलाह लें, खासकर अगर जवाब देने की समय सीमा हो।",
            "अगर आप वकील का खर्च नहीं उठा सकते, तो मुफ्त कानूनी सहायता के लिए विधिक सेवा प्राधिकरण से संपर्क करें।",
            "मूल नोटिस और डिलीवरी के किसी भी लिफाफे/प्रमाण को सुरक्षित रखें।",
        ],
        "what_not_to_do": [
            "इसे नज़रअंदाज़ न करें — कानूनी मामलों में समय सीमाएं अक्सर सख्त होती हैं।",
            "बिना कानूनी सलाह के सीधे (खासकर लिखित रूप में) जवाब न दें, क्योंकि यह बाद में आपकी स्थिति को प्रभावित कर सकता है।",
        ],
        "your_rights": [
            {"article": "अनुच्छेद 39A", "desc": "यह सुनिश्चित करने का राज्य का कर्तव्य कि आर्थिक तंगी के कारण न्याय से वंचित न हों, इसके लिए मुफ्त कानूनी सहायता।"},
            {"article": "अनुच्छेद 21", "desc": "उचित प्रक्रिया का अधिकार — इसमें ठीक से सुने जाने का अधिकार शामिल है।"},
        ],
        "get_help": [
            {"name": "NALSA मुफ्त कानूनी सहायता हेल्पलाइन", "contact": "15100"},
            {"name": "जिला विधिक सेवा प्राधिकरण (DLSA)", "contact": "'DLSA + आपका जिला' खोजें"},
        ],
    },

    "hospital_legal": {
        "title": "अस्पताल / चिकित्सा कानूनी मुद्दा",
        "what_to_know": [
            "अस्पताल पहले से भुगतान करने में असमर्थता के आधार पर आपातकालीन उपचार से इनकार नहीं कर सकते।",
            "किसी भी प्रक्रिया से पहले आपको आमतौर पर सूचित सहमति का अधिकार है।",
            "आपको अपने खुद के मेडिकल रिकॉर्ड तक पहुंचने का अधिकार है।",
        ],
        "what_you_can_do": [
            "चिकित्सा आपातकाल में, पहले उपचार पर जोर दें — भुगतान/औपचारिकताएं बाद में हो सकती हैं।",
            "सहमति देने से पहले किसी भी प्रक्रिया की लिखित व्याख्या मांगें।",
            "विवादों (जैसे, लापरवाही, बिलिंग मुद्दे) के लिए, आप उपभोक्ता फोरम या राज्य चिकित्सा परिषद से संपर्क कर सकते हैं।",
        ],
        "what_not_to_do": [
            "ऐसे सहमति फॉर्म साइन न करें जिन्हें आप नहीं समझते — स्पष्टीकरण या अनुवाद मांगें।",
            "अस्पताल को भुगतान को लेकर आपातकालीन देखभाल में देरी न करने दें — इसकी रिपोर्ट की जा सकती है।",
        ],
        "your_rights": [
            {"article": "अनुच्छेद 21", "desc": "जीवन के अधिकार में आपातकालीन चिकित्सा उपचार का अधिकार शामिल है।"},
            {"article": "उपभोक्ता संरक्षण अधिनियम, 2019", "desc": "चिकित्सा लापरवाही और सेवा में कमी को उपभोक्ता विवाद के रूप में कवर करता है।"},
        ],
        "get_help": [
            {"name": "राष्ट्रीय उपभोक्ता हेल्पलाइन", "contact": "1915"},
            {"name": "राज्य चिकित्सा परिषद", "contact": "'[आपका राज्य] मेडिकल काउंसिल' खोजें"},
            {"name": "एम्बुलेंस / आपातकाल", "contact": "108 / 112"},
        ],
    },

    "domestic_violence": {
        "title": "घरेलू हिंसा",
        "what_to_know": [
            "घरेलू हिंसा में शारीरिक, भावनात्मक, यौन, मौखिक, और आर्थिक शोषण शामिल है — केवल शारीरिक नुकसान नहीं।",
            "आपको साझा घर में रहने का अधिकार है, चाहे वह किसी के भी नाम पर पंजीकृत हो।",
            "सुरक्षा आदेश, आर्थिक राहत, हिरासत आदेश, और निवास आदेश सभी घरेलू हिंसा से महिलाओं के संरक्षण अधिनियम, 2005 (PWDVA) के माध्यम से प्राप्त किए जा सकते हैं — यह एक सिविल उपाय है, आपराधिक मामला दर्ज करने से अलग।",
            "आप एक साथ PWDVA मामला और आपराधिक शिकायत (जैसे, क्रूरता प्रावधानों के तहत) दोनों दायर कर सकते हैं — ये परस्पर अनन्य नहीं हैं।",
            "एक संरक्षण अधिकारी का काम विशेष रूप से आपको घरेलू घटना रिपोर्ट दाखिल करने में मदद करना और आपको आश्रय, चिकित्सा सहायता, और कानूनी सहायता से जोड़ना है — पहला संपर्क करने के लिए आपको वकील की जरूरत नहीं है।",
        ],
        "what_you_can_do": [
            "अगर आप तत्काल खतरे में हैं, तो 112 पर कॉल करें या नजदीकी पुलिस स्टेशन जाएं — आप पुलिस से आपको सुरक्षित स्थान तक ले जाने के लिए भी कह सकते हैं।",
            "अपने जिले में एक संरक्षण अधिकारी (DV अधिनियम के तहत नियुक्त) से संपर्क करें — वे आपको घरेलू घटना रिपोर्ट (DIR) दाखिल करने में मदद कर सकते हैं, जो अक्सर पहला औपचारिक कदम होता है।",
            "मार्गदर्शन, आश्रय जानकारी, और परामर्श के लिए महिला हेल्पलाइन (181) से संपर्क करें — 24x7 उपलब्ध और गोपनीय।",
            "जहां सुरक्षित हो वहां सबूत रखें — संदेश, फोटो, मेडिकल रिकॉर्ड, गवाहों के संपर्क। अगर घर पर सबूत रखना सुरक्षित नहीं है, तो इसे किसी विश्वसनीय व्यक्ति या क्लाउड स्टोरेज में रखने पर विचार करें।",
            "वन स्टॉप सेंटर (सखी) से संपर्क करने पर विचार करें — ये राज्य द्वारा संचालित एक ही स्थान पर चिकित्सा सहायता, पुलिस सहायता, कानूनी सहायता, और आश्रय प्रदान करते हैं।",
            "अगर बच्चे शामिल हैं, तो आप उसी DV अधिनियम कार्यवाही के हिस्से के रूप में अंतरिम हिरासत का अनुरोध कर सकते हैं।",
        ],
        "what_not_to_do": [
            "यह महसूस न करें कि आपको इसे अकेले हल करना है या यह एक 'निजी मामला' है — इसके लिए विशेष रूप से सहायता ढांचे मौजूद हैं।",
            "अपने अधिकारों को समझे बिना दबाव में कोई समझौता (जिसमें 'शांति बनाए रखने' के लिए निपटान या दस्तावेज़ शामिल है) साइन न करें।",
            "एक ही 'काफी गंभीर' घटना का इंतजार न करें — बढ़ता हुआ व्यवहार का पैटर्न संरक्षण आदेश मांगने के लिए वैध आधार है।",
        ],
        "your_rights": [
            {"article": "अनुच्छेद 21", "desc": "गरिमा के साथ जीवन का अधिकार — घरेलू हिंसा से सुरक्षा का आधार।"},
            {"article": "अनुच्छेद 15(3)", "desc": "राज्य को महिलाओं के लिए विशेष प्रावधान बनाने की अनुमति देता है — DV अधिनियम जैसे कानूनों का कानूनी आधार।"},
            {"article": "घरेलू हिंसा से महिलाओं के संरक्षण अधिनियम, 2005", "desc": "एक सिविल प्रक्रिया के माध्यम से सुरक्षा आदेश, निवास अधिकार, आर्थिक राहत, और हिरासत आदेश प्रदान करता है।"},
        ],
        "get_help": [
            {"name": "महिला हेल्पलाइन", "contact": "181"},
            {"name": "पुलिस", "contact": "112"},
            {"name": "वन स्टॉप सेंटर (सखी)", "contact": "'वन स्टॉप सेंटर + आपका जिला' खोजें"},
            {"name": "राष्ट्रीय महिला आयोग", "contact": "ncw.nic.in"},
        ],
    },

    "online_harassment": {
        "title": "ऑनलाइन उत्पीड़न / धोखाधड़ी",
        "what_to_know": [
            "साइबरबुलिंग, स्टॉकिंग, और ऑनलाइन धोखाधड़ी IT अधिनियम और भारतीय न्याय संहिता के तहत आपराधिक अपराध हैं।",
            "आप पहले पुलिस स्टेशन जाने की जरूरत के बिना, भारत में कहीं से भी राष्ट्रीय साइबर अपराध रिपोर्टिंग पोर्टल के माध्यम से साइबर अपराध की ऑनलाइन रिपोर्ट कर सकते हैं।",
            "वित्तीय धोखाधड़ी के लिए, गति मायने रखती है — कई बैंक और भुगतान प्लेटफॉर्म पहले कुछ घंटों में रिपोर्ट करने पर लेनदेन को रोक या उलट सकते हैं ('गोल्डन आवर')।",
            "सेक्सटॉर्शन और अंतरंग तस्वीरों को बिना सहमति के साझा करना विशेष रूप से अपराधीकृत है — गलती आपकी नहीं है, और शर्मिंदगी महसूस होने पर भी रिपोर्ट करने के लिए दृढ़ता से प्रोत्साहित किया जाता है।",
            "सबूत (स्क्रीनशॉट, लिंक, लेनदेन आईडी, प्रेषक विवरण) जांच में काफी मदद करते हैं — लेकिन पोर्टल और पुलिस आंशिक सबूत के साथ भी कार्रवाई कर सकते हैं।",
        ],
        "what_you_can_do": [
            "वित्तीय धोखाधड़ी के लिए: तुरंत साइबर क्राइम हेल्पलाइन (1930) पर कॉल करें — यह विशेष रूप से बैंक/UPI लेनदेन को तेजी से रोकने के लिए है।",
            "उत्पीड़न/धोखाधड़ी के स्क्रीनशॉट लें, जिसमें यूज़रनेम, टाइमस्टैम्प, URL, और कोई भी लेनदेन आईडी शामिल हो — व्यक्ति को ब्लॉक करने से पहले ऐसा करें।",
            "राष्ट्रीय साइबर अपराध रिपोर्टिंग पोर्टल (cybercrime.gov.in) पर रिपोर्ट करें — आप कुछ श्रेणियों के लिए गुमनाम रूप से फाइल कर सकते हैं, जिसमें महिला/बाल संबंधित अपराध शामिल हैं।",
            "आधिकारिक शिकायत दर्ज करने के अलावा, प्लेटफॉर्म पर ही खाते को ब्लॉक/रिपोर्ट करें — ये स्वतंत्र हैं, दोनों करें।",
            "अगर इसमें कोई नाबालिग शामिल है, या किसी की भी गैर-सहमति वाली तस्वीरें हैं, तो तुरंत रिपोर्ट करें — इन्हें प्राथमिकता मामलों के रूप में माना जाता है।",
            "अपने बैंक/भुगतान ऐप का धोखाधड़ी रिपोर्टिंग नंबर पहले से सेव करें — ज्यादातर प्रमुख बैंकों की ग्राहक सेवा से अलग एक समर्पित 24x7 धोखाधड़ी लाइन होती है।",
        ],
        "what_not_to_do": [
            "सबूत न मिटाएं, भले ही यह परेशान करने वाला हो — पहले इसे सुरक्षित रखें, फिर रिपोर्ट करें या ब्लॉक करें।",
            "किसी धोखेबाज़/ब्लैकमेलर के साथ सीधे बातचीत या मोलभाव न करें, और सेक्सटॉर्शन की मांग का भुगतान न करें — इससे शायद ही कभी धमकियां रुकती हैं और यह बढ़ भी सकता है।",
            "यह न मानें कि व्यक्ति गुमनाम या 'अनट्रेसेबल' होने के कारण कुछ नहीं किया जा सकता — साइबर सेल अक्सर प्लेटफॉर्म सहयोग के माध्यम से खातों का पता लगा सकते हैं।",
            "वित्तीय धोखाधड़ी की रिपोर्ट करने से पहले 'अधिक सबूत जुटाने' का इंतजार न करें — हर घंटा धन वापस पाने की संभावना को कम करता है।",
        ],
        "your_rights": [
            {"article": "अनुच्छेद 21", "desc": "गोपनीयता और गरिमा का अधिकार, जीवन के अधिकार के हिस्से के रूप में मान्यता प्राप्त (के.एस. पुट्टास्वामी बनाम भारत संघ, 2017)।"},
            {"article": "सूचना प्रौद्योगिकी अधिनियम, 2000", "desc": "साइबरस्टॉकिंग, पहचान की चोरी, अश्लील सामग्री, और ऑनलाइन धोखाधड़ी को कवर करता है।"},
            {"article": "भारतीय न्याय संहिता, 2023", "desc": "IT अधिनियम के साथ-साथ स्टॉकिंग, मानहानि, और संबंधित अपराधों को कवर करता है।"},
        ],
        "get_help": [
            {"name": "राष्ट्रीय साइबर क्राइम हेल्पलाइन (धोखाधड़ी/रिपोर्टिंग)", "contact": "1930"},
            {"name": "साइबर क्राइम रिपोर्टिंग पोर्टल", "contact": "cybercrime.gov.in"},
            {"name": "पुलिस", "contact": "112"},
        ],
    },

    "workplace_harassment": {
        "title": "कार्यस्थल पर यौन उत्पीड़न",
        "what_to_know": [
            "10+ कर्मचारियों वाले हर कार्यस्थल में POSH अधिनियम के तहत एक आंतरिक शिकायत समिति (ICC) होना कानूनी रूप से आवश्यक है।",
            "यौन उत्पीड़न में अवांछित शारीरिक संपर्क, यौन टिप्पणियां, अश्लील सामग्री दिखाना, या कोई भी अवांछित यौन व्यवहार शामिल है — मौखिक या गैर-मौखिक।",
            "आपको प्रतिशोध के डर के बिना शिकायत करने का अधिकार है, और कानून के अनुसार शिकायत को गोपनीय रूप से संभाला जाना चाहिए।",
            "अगर आपके कार्यस्थल पर कोई ICC नहीं है (जैसे, छोटा व्यवसाय, असंगठित क्षेत्र), तो आप जिले द्वारा स्थापित स्थानीय शिकायत समिति से संपर्क कर सकते हैं।",
        ],
        "what_you_can_do": [
            "जो हुआ उसे जल्द से जल्द लिख लें — तारीख, समय, स्थान, क्या कहा/किया गया, और कोई भी गवाह।",
            "आंतरिक शिकायत समिति (ICC) के पास लिखित शिकायत दर्ज करें — यह आमतौर पर घटना के 3 महीने के भीतर की जा सकती है (बढ़ाई जा सकती है)।",
            "अगर कोई ICC नहीं है या आप निश्चित नहीं हैं कि किससे संपर्क करें, तो अपने जिले के लिए स्थानीय शिकायत समिति (LCC) से संपर्क करें।",
            "घटना से संबंधित किसी भी संदेश, ईमेल, या दस्तावेज़ की प्रतियां रखें।",
        ],
        "what_not_to_do": [
            "यह न मानें कि आपको अपनी नौकरी बचाने के लिए इसे अनौपचारिक रूप से हल करना है या 'छोड़ देना' है — सद्भावनापूर्ण शिकायत के लिए प्रतिशोध खुद ही प्रतिबंधित है।",
            "प्रासंगिक संदेश या सबूत न मिटाएं, भले ही आप निश्चित न हों कि शिकायत दर्ज करनी है या नहीं।",
        ],
        "your_rights": [
            {"article": "अनुच्छेद 14 / 15", "desc": "कार्यस्थल पर लिंग के आधार पर सहित समानता और गैर-भेदभाव।"},
            {"article": "अनुच्छेद 21", "desc": "गरिमा के साथ जीवन का अधिकार — इसमें सुरक्षित कार्य वातावरण का अधिकार शामिल है।"},
            {"article": "कार्यस्थल पर महिलाओं का यौन उत्पीड़न (निवारण, निषेध और निवारण) अधिनियम, 2013 (POSH अधिनियम)", "desc": "एक आंतरिक शिकायत समिति और एक परिभाषित निवारण प्रक्रिया अनिवार्य करता है।"},
            {"article": "विशाखा बनाम राजस्थान राज्य (1997)", "desc": "सुप्रीम कोर्ट का वह निर्णय जिसने पहली बार कार्यस्थल यौन उत्पीड़न दिशानिर्देश निर्धारित किए, जो बाद में POSH अधिनियम में संहिताबद्ध हुए।"},
        ],
        "get_help": [
            {"name": "महिला हेल्पलाइन", "contact": "181"},
            {"name": "राष्ट्रीय महिला आयोग", "contact": "ncw.nic.in"},
            {"name": "SHe-Box (ऑनलाइन POSH शिकायत पोर्टल)", "contact": "shebox.wcd.gov.in"},
        ],
    },

    "landlord_tenant": {
        "title": "मकान मालिक / किरायेदार विवाद या अवैध बेदखली",
        "what_to_know": [
            "मकान मालिक आमतौर पर उचित कानूनी प्रक्रिया का पालन किए बिना किरायेदार को बेदखल नहीं कर सकता, भले ही कोई औपचारिक लिखित समझौता न हो।",
            "'सेल्फ-हेल्प' बेदखली — जैसे ताले बदलना, पानी/बिजली काटना, या अदालत के आदेश के बिना आपका सामान हटाना — कानूनी नहीं है, भले ही किराया बकाया हो।",
            "सुरक्षा जमा नियम, नोटिस अवधि, और बेदखली के आधार राज्य के किराया नियंत्रण अधिनियम के अनुसार अलग-अलग होते हैं।",
        ],
        "what_you_can_do": [
            "किरायेदारी का प्रमाण रखें — किराया रसीदें, बैंक ट्रांसफर, कोई भी लिखित या संदेश में समझौता, आपके नाम पर उपयोगिता बिल।",
            "अगर आपको अवैध बेदखली की धमकी दी जाती है, तो शांति भंग को रोकने के लिए स्थानीय पुलिस से संपर्क करें, और साथ ही निषेधाज्ञा के बारे में वकील से सलाह लें।",
            "किराया/जमा विवादों के लिए, आप अपने राज्य के कानून के आधार पर अपने क्षेत्र में किराया नियंत्रण न्यायालय या सिविल न्यायालय से संपर्क कर सकते हैं।",
            "किसी भी उत्पीड़न (कॉल, संदेश, विज़िट) को टाइमस्टैम्प के साथ दस्तावेज़ित करें।",
        ],
        "what_not_to_do": [
            "केवल इसलिए तुरंत घर खाली न करें क्योंकि आपको मौखिक रूप से जाने के लिए कहा गया है — लिखित में कानूनी आधार और समय सीमा मांगें।",
            "दबाव में कोई दस्तावेज़ (जैसे 'स्वैच्छिक रूप से खाली करने' का पत्र) साइन न करें।",
        ],
        "your_rights": [
            {"article": "अनुच्छेद 21", "desc": "जीवन और व्यक्तिगत स्वतंत्रता का अधिकार — अदालतों ने इसमें आश्रय के अधिकार को शामिल माना है।"},
            {"article": "राज्य किराया नियंत्रण अधिनियम", "desc": "बेदखली प्रक्रिया, नोटिस अवधि, और किराया विवादों को नियंत्रित करते हैं — ये राज्य के अनुसार भिन्न होते हैं।"},
        ],
        "get_help": [
            {"name": "NALSA मुफ्त कानूनी सहायता हेल्पलाइन", "contact": "15100"},
            {"name": "स्थानीय किराया नियंत्रण कार्यालय / सिविल न्यायालय", "contact": "'[आपका राज्य] किराया नियंत्रण अधिनियम' खोजें"},
            {"name": "पुलिस (अवैध 'सेल्फ-हेल्प' बेदखली को रोकने के लिए)", "contact": "112"},
        ],
    },

    "dowry_harassment": {
        "title": "दहेज उत्पीड़न",
        "what_to_know": [
            "दहेज मांगना, देना, या लेना दहेज निषेध अधिनियम, 1961 के तहत गैरकानूनी है।",
            "दहेज के लिए उत्पीड़न — जिसमें क्रूरता, धमकियां, या दहेज मांगों से जुड़ी हिंसा शामिल है — एक आपराधिक अपराध है।",
            "अगर उत्पीड़न वैवाहिक घर में हो रहा है तो इसे घरेलू हिंसा मामले (PWDVA) के साथ आगे बढ़ाया जा सकता है।",
        ],
        "what_you_can_do": [
            "अगर आप तत्काल खतरे में हैं, तो 112 पर कॉल करें।",
            "मार्गदर्शन और संरक्षण अधिकारी या वन स्टॉप सेंटर से जुड़ने के लिए महिला हेल्पलाइन (181) से संपर्क करें।",
            "पुलिस के पास शिकायत दर्ज करें — दहेज उत्पीड़न और संबंधित क्रूरता आपराधिक अपराध हैं जिनकी सीधे रिपोर्ट की जा सकती है।",
            "किसी भी सबूत को सुरक्षित रखें — संदेश, गवाह, दहेज मांगों या स्थानांतरण के वित्तीय रिकॉर्ड।",
        ],
        "what_not_to_do": [
            "इसे एक निजी पारिवारिक मामला न मानें जिसे चुपचाप सुलझाना है — कानून इसे केवल घरेलू मामले के रूप में नहीं, बल्कि एक आपराधिक मुद्दे के रूप में मानता है।",
            "अपने ससुराल वालों के दबाव में कोई दस्तावेज़ साइन न करें, जिसमें संपत्ति या 'निपटान' से संबंधित कुछ भी शामिल हो।",
        ],
        "your_rights": [
            {"article": "अनुच्छेद 21", "desc": "गरिमा के साथ जीवन का अधिकार।"},
            {"article": "अनुच्छेद 15(3)", "desc": "महिलाओं के लिए विशेष सुरक्षात्मक कानूनों का आधार।"},
            {"article": "दहेज निषेध अधिनियम, 1961", "desc": "दहेज देने, लेने, और मांगने को अपराध घोषित करता है।"},
            {"article": "घरेलू हिंसा से महिलाओं के संरक्षण अधिनियम, 2005", "desc": "जब दहेज उत्पीड़न घरेलू शोषण के साथ मेल खाता है तो लागू हो सकता है।"},
        ],
        "get_help": [
            {"name": "महिला हेल्पलाइन", "contact": "181"},
            {"name": "पुलिस", "contact": "112"},
            {"name": "वन स्टॉप सेंटर (सखी)", "contact": "'वन स्टॉप सेंटर + आपका जिला' खोजें"},
        ],
    },

    "senior_citizen_abuse": {
        "title": "वरिष्ठ नागरिक उपेक्षा या दुर्व्यवहार",
        "what_to_know": [
            "माता-पिता और वरिष्ठ नागरिकों के भरण-पोषण और कल्याण अधिनियम, 2007 के तहत वरिष्ठ नागरिकों को अपने बच्चों या कानूनी उत्तराधिकारियों द्वारा भरण-पोषण किए जाने का कानूनी अधिकार है।",
            "यह कानून एक न्यायाधिकरण को बच्चों/रिश्तेदारों को भरण-पोषण देने का आदेश देने की अनुमति भी देता है, और यहां तक कि अगर संपत्ति हस्तांतरण देखभाल की शर्त पर किया गया था और वह शर्त पूरी नहीं हुई तो उसे रद्द करने की भी अनुमति देता है।",
            "किसी वरिष्ठ नागरिक को छोड़ना इस अधिनियम के तहत एक आपराधिक अपराध है।",
        ],
        "what_you_can_do": [
            "अपने जिले में वरिष्ठ नागरिक अधिनियम के तहत स्थापित भरण-पोषण न्यायाधिकरण से संपर्क करें — प्रक्रिया सरल और तेज़ होने के लिए डिज़ाइन की गई है, और इसके लिए वकील की जरूरत नहीं है।",
            "अगर तत्काल खतरा या परित्याग है, तो पुलिस या वरिष्ठ नागरिक हेल्पलाइन से संपर्क करें।",
            "अगर संपत्ति देखभाल के वादे पर हस्तांतरित की गई थी जिसका सम्मान नहीं किया जा रहा है, तो आप न्यायाधिकरण के माध्यम से उस हस्तांतरण को शून्य घोषित करने के लिए आवेदन कर सकते हैं।",
        ],
        "what_not_to_do": [
            "यह न मानें कि परिवार से जुड़ा होने के कारण कुछ नहीं किया जा सकता — कानून विशेष रूप से इस स्थिति की अपेक्षा और संबोधन करता है।",
            "करीबी परिवार के दबाव में भी संपत्ति या संपत्ति न छोड़ें।",
        ],
        "your_rights": [
            {"article": "अनुच्छेद 21", "desc": "गरिमा के साथ जीवन का अधिकार, जिसे सुप्रीम कोर्ट ने एक गरिमापूर्ण बुढ़ापे को शामिल करने के लिए विस्तारित किया है।"},
            {"article": "अनुच्छेद 41", "desc": "राज्य को वृद्धावस्था में सार्वजनिक सहायता के प्रावधान बनाने की आवश्यकता वाला निर्देशक सिद्धांत।"},
            {"article": "माता-पिता और वरिष्ठ नागरिकों के भरण-पोषण और कल्याण अधिनियम, 2007", "desc": "वरिष्ठ नागरिकों के भरण-पोषण, संपत्ति की सुरक्षा, और कल्याण का प्रावधान करता है।"},
        ],
        "get_help": [
            {"name": "एल्डरलाइन (वरिष्ठ नागरिक हेल्पलाइन)", "contact": "14567"},
            {"name": "भरण-पोषण न्यायाधिकरण", "contact": "'[आपका जिला] वरिष्ठ नागरिक न्यायाधिकरण' खोजें"},
            {"name": "पुलिस", "contact": "112"},
        ],
    },

    "consumer_fraud": {
        "title": "उपभोक्ता धोखाधड़ी (उत्पाद, सेवाएं, ई-कॉमर्स)",
        "what_to_know": [
            "उपभोक्ता संरक्षण अधिनियम, 2019 के तहत एक उपभोक्ता के रूप में आपको सुरक्षा, जानकारी, पसंद, और निवारण का अधिकार है।",
            "यह दोषपूर्ण उत्पादों, कमी वाली सेवाओं, भ्रामक विज्ञापनों, और अनुचित व्यापार प्रथाओं को कवर करता है — जिसमें ऑनलाइन खरीदारी और डिजिटल सेवाएं शामिल हैं।",
            "एक बुनियादी उपभोक्ता शिकायत दर्ज करने के लिए वकील की जरूरत नहीं है — उपभोक्ता आयोग बिना वकील के सुलभ होने के लिए डिज़ाइन किए गए हैं।",
        ],
        "what_you_can_do": [
            "सभी प्रमाण रखें: ऑर्डर पुष्टिकरण, भुगतान रसीद, विक्रेता के साथ चैट/ईमेल, दोषपूर्ण उत्पाद की तस्वीरें।",
            "पहले, विक्रेता/प्लेटफॉर्म के साथ लिखित रूप में समाधान करने की कोशिश करें — यह हल न होने पर भी एक कागजी ट्रेल बनाता है।",
            "अगले चरणों के लिए मुफ्त मार्गदर्शन के लिए राष्ट्रीय उपभोक्ता हेल्पलाइन (1915) पर कॉल करें।",
            "अगर विक्रेता समाधान नहीं करता है तो e-Daakhil पोर्टल (ऑनलाइन उपभोक्ता शिकायत दाखिल प्रणाली) पर शिकायत दर्ज करें।",
        ],
        "what_not_to_do": [
            "केवल विक्रेता के साथ फोन कॉल पर भरोसा न करें — जहां भी संभव हो लिखित/ईमेल/चैट में जवाब लें।",
            "अगर आप रिफंड के हकदार हैं और चाहते हैं, तो विक्रेता को आपको 'स्टोर क्रेडिट' के लिए दबाव न बनाने दें।",
        ],
        "your_rights": [
            {"article": "अनुच्छेद 21", "desc": "जीवन का अधिकार, जिसे अदालतों ने उपभोक्ता सुरक्षा और कल्याण से संबंधित तरीकों से विस्तारित किया है।"},
            {"article": "उपभोक्ता संरक्षण अधिनियम, 2019", "desc": "सुरक्षा, जानकारी, पसंद, निवारण का अधिकार देता है, और विशेष रूप से ई-कॉमर्स को कवर करता है।"},
        ],
        "get_help": [
            {"name": "राष्ट्रीय उपभोक्ता हेल्पलाइन", "contact": "1915"},
            {"name": "e-Daakhil (ऑनलाइन शिकायत पोर्टल)", "contact": "edaakhil.nic.in"},
        ],
    },
}

EMERGENCY_SCENARIOS_BY_LANG = {
    "English": EMERGENCY_SCENARIOS_EN,
    "Hindi": EMERGENCY_SCENARIOS_HI,
}
