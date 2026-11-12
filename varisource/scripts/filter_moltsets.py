"""Filter Moltsets raw search output into a send-ready Varisource list.
Usage: python3 filter_moltsets.py raw.jsonl sample_enriched.csv out.csv"""
import sys,json,csv,re,collections
raw,sample,out=sys.argv[1:4]
TITLE={
 "Finance leadership":re.compile(r"(?i)\b(chief financial officer|cfo|(vp|vice president|svp|evp|head)\b.{0,15}\bfinance)\b"),
 "FP&A / Controller":re.compile(r"(?i)(financial planning|fp ?& ?a|\bcontroller\b)"),
 "Procurement":re.compile(r"(?i)(procurement|purchasing|sourcing|supply management)"),
}
BADT=re.compile(r"(?i)\b(assistant|intern|analyst|coordinator|specialist|associate|buyer|clerk|student|retired|former|consultant|fractional|advisor|interim|accountant|payable|receivable|payroll)\b")
BADIND=re.compile(r"(?i)educat|school|universit|college|government|armed forces|military|law enforcement|legislat|public policy|public safety|administration of justice|libraries|political")
FREE={"gmail.com","yahoo.com","hotmail.com","outlook.com","aol.com","icloud.com","me.com","live.com","msn.com","comcast.net"}
seen={r["Email"].strip().lower() for r in csv.DictReader(open(sample)) if r.get("Email")}
seenli={r["LinkedIn"].rstrip("/").lower() for r in csv.DictReader(open(sample))}
why=collections.Counter(); dom=collections.Counter(); rows=[]
for line in open(raw):
    x=json.loads(line); c=x.get("company") or {}
    e=(x.get("business_email") or "").strip().lower(); t=x.get("title") or ""
    try: size=int(float(c.get("size") or 0))
    except: size=0
    inds=" ".join([x.get("current_industry") or "",c.get("industry") or ""]+(c.get("linkedin_industry") or []))
    if not e or "@" not in e: why["no email"]+=1; continue
    if x.get("business_email_risk_score") not in ("A","B"): why["grade not A/B"]+=1; continue
    if e.split("@")[1] in FREE: why["free mail"]+=1; continue
    if e in seen or (x.get("linkedin_url") or "").rstrip("/").lower() in seenli: why["duplicate"]+=1; continue
    if not TITLE[x["_role"]].search(t) or BADT.search(t): why["title off-ICP"]+=1; continue
    if not 250<=size<=5000: why["size outside 250-5000"]+=1; continue
    if BADIND.search(inds): why["school/gov"]+=1; continue
    d=e.split("@")[1]
    if dom[d]>=3: why["4th+ at company"]+=1; continue
    dom[d]+=1; seen.add(e)
    fn=x.get("first_name") or ""; fn=fn.title() if fn.isupper() or fn.islower() else fn
    ln=re.split(r",",x.get("last_name") or "")[0].strip(); ln=ln.title() if ln.isupper() or ln.islower() else ln
    rows.append({"Role Group":x["_role"],"First Name":fn,"Last Name":ln,"Title":t,"Seniority":x.get("seniority"),"Company":c.get("name"),
      "Website":c.get("domain") or c.get("website_url"),"Employees":size,"Industry":(c.get("linkedin_industry") or [c.get("industry")])[0],
      "City":x.get("city"),"State":x.get("state"),"LinkedIn":x.get("linkedin_url"),"Email":e,"Email_Source":"moltsets_search",
      "Risk_Score":x.get("business_email_risk_score"),"Email_Validated":x.get("business_email_validated_at"),
      "Wave":"Wave 1 (250-2000)" if size<=2000 else "Wave 2 (2001-5000)"})
w=csv.DictWriter(open(out,"w",newline=""),fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print("kept",len(rows)); print("dropped",dict(why))
print(collections.Counter(r["Wave"] for r in rows)); print(collections.Counter((r["Wave"][:6],r["Role Group"]) for r in rows))
print("companies",len(dom)); print(collections.Counter(r["Industry"] for r in rows).most_common(12))
