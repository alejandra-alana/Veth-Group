"""Build the active-client milestone list for Desiree's homework.

Source: Monday.com (pulled 2026-11-05)
  - Client CRM (active "Clients" group, 112 items) -> client list + monthly $ by service
  - Shipping Board "Target Post Date"               -> next LinkedIn post date (real date)
  - Podcasts subitems "Target Live Date"           -> next episode date (real date)
  - New Campaign Launches (group = stage)          -> campaign milestone (no date column -> proposed)
  - Non-Launch Tasks (open)                        -> one-off milestone (no due date -> proposed)

Writes active_clients_milestones.csv and .md next to this file.
"""
import csv
import os
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))

# Proposed target dates for items Monday has no date for (based on the stage they sit in today).
STAGE = {
    "copy":     ("Copy/creative sent to client", "2026-11-13"),
    "approval": ("Client approves campaign copy", "2026-11-10"),
    "warmup":   ("Campaign launches (domains warmed up)", "2026-11-16"),
    "build":    ("Campaign built and ready for QA", "2026-11-12"),
    "dnc":      ("DNC / exclusions confirmed", "2026-11-09"),
    "qa":       ("Campaign QA'd and live", "2026-11-09"),
    "revision": ("Revisions delivered", "2026-11-10"),
    "stuck":    ("Unblock campaign build", "2026-11-12"),
    "task":     (None, "2026-11-12"),
}

M, P = "Monday", "Proposed"


def post(d, who=""):
    label = "Next LinkedIn post goes live" + (f" ({who})" if who else "")
    return (label, d, M)


def camp(stage, name):
    label, d = STAGE[stage]
    return (f"{label}: {name}", d, P)


def task(name, d="2026-11-12"):
    return (f"Task done: {name}", d, P)


GAP = "GAP"

# client -> (services, milestones[, suggested milestone if gap])
C = {
    "RJS Logistics": [camp("qa", "RJS Logistics Email Campaign"), camp("dnc", "RJS DNC"), post("2026-11-05", "Massimo Pittari")],
    "Saga": [post("2026-11-05", "Hansen Qian"), camp("copy", "Hansen Qian Saga AI Email Campaign")],
    "Aspen Funds": [post("2026-11-06", "Ellis Hammond"), camp("approval", "School Golf Polo Email + Pilots DM")],
    "Brad McCormick": [post("2026-11-06"), camp("stuck", "White Paper, Interview, Book")],
    "John Wetmore": [camp("build", "Annuity Partner Email Campaign"), task("Set up Postwatch for VAs + schedule VA training")],
    "Una": [post("2026-11-05", "Jeff / Luke Livers"), camp("copy", "New ad campaigns (4 options)"), task("Won-deal titles, enrichment, blacklist on Una 1 & 2")],
    "CloudX": [task("Add Ken Brownlow to Positives Tracker")],
    "One2One": [GAP, "Next LinkedIn post scheduled (Nick Paulukow, 2/week target)"],
    "Adler Advisors": [post("2026-11-05", "Dustin Riedel")],
    "Thinkbridge": [post("2026-11-05", "Anand Krishnan"), task("Edit Meaningful Tech interview MP4 + clips")],
    "Bing Consulting Group": [post("2026-11-05", "Lisa Bing")],
    "CoAction": [post("2026-11-06", "Corporate page")],
    "Newave Solutions": [post("2026-11-05", "Kellen Cowan"), camp("copy", "Kellen Email Campaign"), camp("dnc", "Kellen DNC")],
    "EmotionTrac": [post("2026-11-06", "Jonathan Brickman")],
    "Adam Levy": [camp("qa", "Tatum Phoenix Email Campaign")],
    "Tiger Presentations": [post("2026-11-05"), task("Add Flybridge trade-show owners to campaign")],
    "Brandor": [post("2026-11-05", "Delano Bartolomei"), camp("build", "Brandor (Delano) Cold Email Campaign")],
    "McDermott + Bull": [GAP, "Next consulting deliverable / strategy call"],
    "V2 Jets": [GAP, "Next LinkedIn post (Alex Simkovitz) + reply to open email"],
    "Kinective": [post("2026-11-05", "Stephen Baker / Michael Ball")],
    "Lexigate": [camp("build", "Stephanie Varone Email Campaign")],
    "Schoolfundr": [GAP, "Next LinkedIn post scheduled"],
    "NCC Data": [post("2026-11-05", "James McClendon")],
    "Predikly": [post("2026-11-06", "Sunil Ranka")],
    "New Heritage Capital": [post("2026-11-05")],
    "HISMI": [GAP, "Next consulting session + post scheduled"],
    "Brewer Digital": [post("2026-11-05", "Joel Brewer"), ("Podcast episode live (Valentine Reed-Johnson)", "2026-11-09", M)],
    "Rektio": [GAP, "Next newsletter + post (Rex Biggs, 5/week target)"],
    "TRG Datacenters": [post("2026-11-05", "Chris Hinkle")],
    "Reboot": [post("2026-11-05", "Christopher Zvirbulis"), camp("approval", "Chris Zvirbulis Oct/Nov cold email")],
    "VitalStorm": [post("2026-11-05", "Josh Moran")],
    "RTS Labs": [post("2026-11-06", "Jyot Singh")],
    "True North IT": [GAP, "Next LinkedIn post (Matt Murren, 5/week target)"],
    "Steele Consulting": [post("2026-11-06", "Greg")],
    "Datamax": [GAP, "Next outbound campaign refresh / report"],
    "Infinity CTI": [post("2026-11-05", "Frank / Mike")],
    "Dave Golding": [task("Business Black Belts: review guest docs & logos, send LinkedIn credentials")],
    "Choyce Industries": [post("2026-11-06", "Matt Choyce")],
    "Liongard": [task("Get BDR names; Nathan adds them as senders (waiting on client)")],
    "Fortress Financial Partners": [post("2026-11-05", "Chris Gure")],
    "Life Care Plan": [post("2026-11-06", "Sarah Smola")],
    "Taggr Solutions": [post("2026-11-05"), camp("approval", "Parking Enforcement Email Campaign")],
    "Big Red M": [camp("copy", "Big Red M Cold Email Campaign")],
    "Cyber Solutions": [post("2026-11-05", "Company page / Kylan Cleveland")],
    "Synchronet": [post("2026-11-05", "Jerry Sheehan")],
    "Profound Hope Industries": [task("Retarget LinkedIn to CSR + nonprofit EDs, DMs back to 10/day")],
    "Datamam": [post("2026-11-05")],
    "Dale Carnegie": [post("2026-11-06", "Brian Williamson"), task("Load Nora's LinkedIn connections into PostWatch")],
    "DiMassimo Goldstein": [post("2026-11-05", "Lee Goldstein")],
    "BearPeak": [GAP, "Next LinkedIn post scheduled"],
    "ICUC Social": [GAP, "Next outbound campaign refresh / report"],
    "Honeydew Consulting": [post("2026-11-06")],
    "s90 TechOps": [post("2026-11-05", "Sean Crowley")],
    "Lumen21": [post("2026-11-06", "Ed Don")],
    "Lydonia": [task("Send rep's 2 drafted emails via Lydonia Woodpecker")],
    "HyreDay": [post("2026-11-05")],
    "Valuebase": [post("2026-11-05", "Will Jarvis"), task("Remove San Diego County from list")],
    "AMD Communications": [post("2026-11-05", "Kyle Bowden")],
    "Fueled": [GAP, "Next outbound campaign refresh / report"],
    "Small Biz Controller": [post("2026-11-05", "Jose Santana")],
    "IMMIX Bio": [post("2026-11-05")],
    "Sentant": [GAP, "Next outbound campaign refresh / post"],
    "AT-NET": [camp("approval", "New creative for Jeffrey King Email Campaign")],
    "SisAdmin": [post("2026-11-05", "Mary"), task("SisAdmin clips")],
    "Leadership Trainer": [GAP, "Next post / podcast episode (Jonathan Kroll)"],
    "Image Supply Service": [GAP, "Next LinkedIn post (Andrew Wiese)"],
    "Tagg Education": [GAP, "Next outbound campaign refresh / post"],
    "Endsight": [GAP, "Next outbound campaign refresh / post"],
    "20 Mile Consulting": [post("2026-11-05", "Charles Rushman")],
    "Lucky Marketing": [post("2026-11-06", "Carson")],
    "Actor Inside": [post("2026-11-06", "Andy Laithwaite")],
    "SFP": [GAP, "Next LinkedIn post scheduled"],
    "Insight R + D": [post("2026-11-05"), task("Route LinkedIn + email leads to Steven's team")],
    "Archetype Consulting": [post("2026-11-05", "Oliver (video)"), task("Send Oliver the second list")],
    "Punches Advisory Group": [GAP, "Next LinkedIn post (Matthew Punches)"],
    "Gov Transfer": [post("2026-11-05", "Joe Puuri"), camp("approval", "GovTransfer Email Campaign")],
    "ePIC Services": [GAP, "Next LinkedIn post (Carter / Christina Wilcoxson)"],
    "Integreon": [post("2026-11-06", "Brendan"), camp("approval", "Fellow IU Grad Email Campaign")],
    "Fully Promoted": [post("2026-11-06", "Chad South")],
    "Craddock Recruiting": [post("2026-11-06", "Ginger Craddock"), task("Check PostWatch list still has names")],
    "My HR Counsel": [post("2026-11-05", "Kevin Rohrer"), camp("approval", "Franchise + Broker Email Campaigns")],
    "Bill Fanter": [post("2026-11-06", "video")],
    "1wire": [post("2026-11-05", "1Wire / Adam Sessions")],
    "Arc Technologies": [post("2026-11-05", "Jason McKinley")],
    "eCircular": [post("2026-11-06")],
    "Voltage Media": [post("2026-11-05", "Mark Brown"), camp("approval", "Voltage Media Email Campaign")],
    "Hett Painting Group": [post("2026-11-06")],
    "Complete": [GAP, "Next LinkedIn post (Anthony Garofalo / Jeremy Wanamaker)"],
    "Brunson Sales Consulting": [post("2026-11-05", "Stephen Brunson")],
    "Performance Building Services": [post("2026-11-05", "Ron Matthews")],
    "Tetheree": [post("2026-11-05", "Logistics page")],
    "InfoTech": [post("2026-11-05", "Hayden Bruns"), camp("approval", "Hayden Packages"), camp("build", "Hayden PostWatch")],
    "American Business Copiers": [post("2026-11-05", "Erik Manger"), camp("approval", "Erik Manger Cold Email Campaign")],
    "Intero": [post("2026-11-05", "Raymond Jones"), task("Recurring import of daily blacklist")],
    "Rebel Media": [GAP, "Next LinkedIn post (Nahrahel Louis, 5/week, marked ASAP)"],
    "Allegiant Generator Services": [post("2026-11-06", "John Alford")],
    "Saterman Connect": [post("2026-11-05", "Michael / Josh Saterman")],
    "C3S": [post("2026-11-06", "Pete Donovan")],
    "Optimize Cyber": [post("2026-11-05", "Matt Quammen")],
    "AC.Styles": [post("2026-11-06", "Ashley Capps")],
    "Sertis": [GAP, "Next LinkedIn DM ad results review (Donna)"],
    "JST Consulting": [post("2026-11-05"), camp("warmup", "JST Consulting (Joey) Email Campaign")],
    "ShadowHQ": [GAP, "Next outbound campaign refresh / report"],
    "Catalytics": [GAP, "Next LinkedIn post scheduled"],
    "Grant Edwards": [post("2026-11-05", "GrantTheCFO")],
    "Secure Cloud Innovations": [post("2026-11-05"), camp("qa", "Email Campaign for venture-funded start-ups")],
    "Congruent Connections": [camp("approval", "Desiree Kansas City Email Campaign")],
    "Filejet": [GAP, "Next outbound campaign refresh / report"],
    "Quantile": [camp("approval", "Quantile Email Campaign")],
    "Varisource": [camp("copy", "Varisource Cold Email Campaign")],
    "Entrepreneurial Capital": [camp("copy", "Peter Cold Email Campaign")],
    "POSITIVES": [GAP, "Next outbound campaign refresh / report"],
}

# Monthly $ from Client CRM (outbound, content, consulting) - pasted from the board pull.
CRM = """RJS Logistics|2000||
Saga|800||700
Aspen Funds||800|800
Brad McCormick||800|
John Wetmore||1000|
Una|1200|1200|2000
CloudX|999|500|
One2One||600|
Adler Advisors|800|500|500
Thinkbridge||500|
Bing Consulting Group||600|
CoAction|999|500|
Newave Solutions||500|
EmotionTrac|1750||
Adam Levy||600|
Tiger Presentations|600||
Brandor|1600|2750|
McDermott + Bull|||2000
V2 Jets||500|
Kinective||2000|
Lexigate|3200||500
Schoolfundr||600|
NCC Data|1000|750|
Predikly|600|500|
New Heritage Capital||2000|
HISMI||300|300
Brewer Digital||700|
Rektio|600|1500|
TRG Datacenters||1000|
Reboot|1400|1500|375
VitalStorm||1000|
RTS Labs||500|
True North IT||1000|
Steele Consulting|2000||
Datamax|1000||500
Infinity CTI|1000||500
Dave Golding|999||
Choyce Industries||600|
Liongard|1000||
Fortress Financial Partners||800|
Life Care Plan||800|
Taggr Solutions||1200|
Big Red M||1500|
Cyber Solutions|1500||
Synchronet|900||600
Profound Hope Industries||400|
Datamam||800|
Dale Carnegie|300|900|
DiMassimo Goldstein||1000|
BearPeak||1000|
ICUC Social|5200||
Honeydew Consulting||600|
s90 TechOps||1200|
Lumen21||600|
Lydonia|2000||
HyreDay||800|
Valuebase||1000|2000
AMD Communications|1800||
Fueled|3500||
Small Biz Controller|300||600
IMMIX Bio||500|
Sentant|1000||
AT-NET|1000||
SisAdmin|500|800|
Leadership Trainer||800|
Image Supply Service||300|
Tagg Education|1500||
Endsight|1500||
20 Mile Consulting||400|
Lucky Marketing||600|
Actor Inside|||500
SFP||800|
Insight R + D|1000|500|
Archetype Consulting||800|
Punches Advisory Group||400|
Gov Transfer||400|
ePIC Services||1000|
Integreon|3000||
Fully Promoted|999||
Craddock Recruiting||750|
My HR Counsel|||1000
Bill Fanter||600|
1wire|||800
Arc Technologies||800|
eCircular||600|
Voltage Media||800|
Hett Painting Group||800|
Complete||800|
Brunson Sales Consulting||300|
Performance Building Services|||800
Tetheree||800|
InfoTech||800|400
American Business Copiers||800|
Intero|5000||
Rebel Media||1000|
Allegiant Generator Services|800||800
Saterman Connect||800|500
C3S|800||
Optimize Cyber||1200|
AC.Styles||800|
Sertis||800|
JST Consulting||600|
ShadowHQ|999||
Catalytics||600|
Grant Edwards|||800
Secure Cloud Innovations||800|
Congruent Connections||800|
Filejet|1000||
Quantile|800||
Varisource|800||
Entrepreneurial Capital|||500
POSITIVES|2000||"""


def fmt_date(d):
    return date.fromisoformat(d).strftime("%a %b %-d")


def services(o, c, k):
    parts = []
    for label, v in (("Outbound", o), ("Content", c), ("Consulting", k)):
        if v:
            parts.append(f"{label} ${int(v):,}")
    return " · ".join(parts)


rows = []
for line in CRM.splitlines():
    name, o, c, k = line.split("|")
    ms = C[name]
    svc = services(o, c, k)
    total = sum(int(x) for x in (o, c, k) if x)
    if ms[0] == GAP:
        rows.append(dict(client=name, services=svc, mrr=total, milestone=f"NO MILESTONE IN MONDAY. Suggested: {ms[1]}",
                         target="2026-11-13", source="Proposed (gap)", other=""))
        continue
    ms_sorted = sorted(ms, key=lambda m: m[1])
    first = ms_sorted[0]
    other = "; ".join(f"{m[0]} ({fmt_date(m[1])}, {m[2].lower()})" for m in ms_sorted[1:])
    rows.append(dict(client=name, services=svc, mrr=total, milestone=first[0], target=first[1], source=first[2], other=other))

assert len(rows) == 112, len(rows)
rows.sort(key=lambda r: (r["source"] == "Proposed (gap)", r["target"], -r["mrr"]))

with open(os.path.join(HERE, "active_clients_milestones.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Client", "Services (monthly)", "Monthly total", "Next milestone", "Target date", "Date source", "Other upcoming milestones"])
    for r in rows:
        w.writerow([r["client"], r["services"], r["mrr"], r["milestone"], r["target"], r["source"], r["other"]])

n_gap = sum(r["source"] == "Proposed (gap)" for r in rows)
n_mon = sum(r["source"] == M for r in rows)
gap_mrr = sum(r["mrr"] for r in rows if r["source"] == "Proposed (gap)")
md = [
    "# Active clients and their next milestone",
    "",
    "Pulled from Monday.com on Thu Nov 5, 2026. Every active client in the **Client CRM** board (Clients group, 112) is listed with at least one upcoming milestone.",
    "",
    "**How to read the date source:**",
    "",
    "- **Monday**: the date is in Monday (Shipping Board *Target Post Date* or Podcasts *Target Live Date*).",
    "- **Proposed**: Monday tracks the work but has **no date field**, so I proposed a target date based on the stage it's in today (campaign launches) or a 1-week turnaround (open tasks).",
    "- **Proposed (gap)**: nothing upcoming for this client anywhere in Monday. I suggested a milestone; these are the ones to confirm with Miles first.",
    "",
    "## Summary",
    "",
    f"- **{n_mon}** clients have a real dated milestone in Monday (almost all are the next LinkedIn post).",
    f"- **{112 - n_mon - n_gap}** clients only have campaign or task work, which has no due dates in Monday.",
    f"- **{n_gap}** clients (about **${gap_mrr:,}/month**) have **no upcoming milestone at all** in Monday.",
    "- Monday has no due-date column on the Client CRM, New Campaign Launches or Non-Launch Tasks boards. Adding one would turn most \"Proposed\" dates into real ones.",
    "- Risk flag: most posts dated Nov 5–6 were still in the Shipping Board group \"November 2 Needs Ideation From Miles\" on Nov 5, so many of those dates will likely slip.",
    "- Clients were matched across boards by name (for example, Shipping Board \"Kellen Cowan\" goes to CRM \"Newave Solutions\"). A few matches may need a quick check.",
    "",
    "## Client list",
    "",
    "| # | Client | Services (monthly) | Next milestone | Target date | Source | Other upcoming |",
    "|---|---|---|---|---|---|---|",
]
for i, r in enumerate(rows, 1):
    md.append(f"| {i} | {r['client']} | {r['services']} | {r['milestone']} | {fmt_date(r['target'])} | {r['source']} | {r['other']} |")
md += [
    "",
    "### Proposed dates used for campaign stages (New Campaign Launches board)",
    "",
    "| Stage in Monday | Milestone | Proposed target |",
    "|---|---|---|",
]
for key, label in (("dnc", "Confirm Exclusions"), ("qa", "QA & Launch"), ("approval", "Get Client Approval"),
                   ("revision", "Revisions"), ("build", "Build Out Campaign"), ("stuck", "Build Out (Stuck)"),
                   ("copy", "Make Copy or Creative"), ("warmup", "Tech is warming up")):
    m, d = STAGE[key]
    md.append(f"| {label} | {m} | {fmt_date(d)} |")
with open(os.path.join(HERE, "active_clients_milestones.md"), "w") as f:
    f.write("\n".join(md) + "\n")
print(f"rows={len(rows)} monday={n_mon} gaps={n_gap} gap_mrr={gap_mrr}")
