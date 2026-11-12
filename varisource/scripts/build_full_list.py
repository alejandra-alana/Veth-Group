"""Build the full Varisource ICP list from GetLeads (run after the daily fair-use cap resets, 00:00 UTC).
Usage: python3 build_full_list.py <min_emp> <max_emp> <max_rows_per_role> <out.csv>
  e.g. python3 build_full_list.py 250 2000 3000 ../lists/getleads_wave1.csv
Applies: US only, ICP titles per role group (filters.py), no schools/government, VALID emails only,
max 3 contacts per company, de-dupes against the sample list, then re-verifies with MillionVerifier."""
import sys,os,io,csv,time,requests,collections
sys.path.insert(0,os.path.dirname(__file__))
from gl import call
from filters import ROLES,base
lo,hi,cap,out=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),sys.argv[4]
seen=set()
sample=os.path.join(os.path.dirname(__file__),"..","lists","sample_enriched_all_430.csv")
if os.path.exists(sample): seen|={r["Email"].lower() for r in csv.DictReader(open(sample)) if r["Email"]}
rows=[]
for role,f in ROLES.items():
    a={**base(lo,hi),**f,"max_per_company":2}
    c=call("count_contacts",a)
    while isinstance(c,dict) and c.get("status")=="counting":
        time.sleep(c.get("retry_after_seconds",10)); c=call("check_count",{"count_id":c["count_id"]})
    print(role,"matching",c.get("total_matching"),"exportable",c.get("exportable_rows"))
    st=call("export_contacts",{**a,"max_rows":cap,"confirmed":True})
    eid=st.get("export_id") or st.get("id"); url=st.get("export_url")
    while not url:
        time.sleep(10); ck=call("check_contact_export",{"export_id":eid}); url=ck.get("export_url")
        if ck.get("job_status") in ("failed","error"): raise SystemExit(ck)
    print(role,"exported",ck.get("rows_exported"),ck.get("cap_reason"))
    for r in csv.DictReader(io.StringIO(requests.get(url,timeout=300).text)):
        r["Role Group"]=role; rows.append(r)
ek=next(k for k in rows[0] if k.lower() in ("email","work_email","email_address"))
dk=collections.Counter(); final=[]
for r in rows:
    e=(r.get(ek) or "").strip().lower()
    if not e or e in seen: continue
    d=e.split("@")[-1]
    if dk[d]>=3: continue
    seen.add(e); dk[d]+=1; r[ek]=e; final.append(r)
MV=os.environ["MILLIONVERIFIER_API_KEY"]
def mv(e):
    try: return requests.get("https://api.millionverifier.com/api/v3/",params={"api":MV,"email":e,"timeout":20},timeout=40).json().get("result")
    except Exception: return "error"
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(8) as p: res=list(p.map(mv,[r[ek] for r in final]))
for r,v in zip(final,res): r["MV_Result"]=v
keys=sorted({k for r in final for k in r})
w=csv.DictWriter(open(out,"w",newline=""),fieldnames=keys); w.writeheader(); w.writerows(final)
print("written",len(final),collections.Counter(res))
