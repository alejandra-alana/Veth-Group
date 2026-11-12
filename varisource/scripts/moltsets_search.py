"""Pull Varisource ICP prospects from Moltsets search_people (emails + risk grade included).
Usage: python3 moltsets_search.py <raw_out.jsonl> [records_per_role_band]"""
import os,sys,json,time,requests
from concurrent.futures import ThreadPoolExecutor
H={"Authorization":"Bearer "+os.environ["MOLTSETS_API_KEY"],"Content-Type":"application/json"}
URL="https://api.moltsets.com/api/v1/tools/search_people"
out=sys.argv[1]; per=int(sys.argv[2]) if len(sys.argv)>2 else 1000
EXCL_IND=["Education","Government and Public Administration"]
ROLES={
 "Finance leadership":dict(title=["Chief Financial Officer","CFO","VP Finance","Vice President Finance","Head of Finance"],seniority=["C Suite","VP","Head"]),
 "FP&A / Controller":dict(title=["Financial Planning","FP&A","Controller"],seniority=["Manager","Director","VP","Head"]),
 "Procurement":dict(title=["Procurement","Purchasing","Strategic Sourcing"],seniority=["C Suite","VP","Head","Director"]),
}
BANDS=["201-500","501-1000","1001-5000"]
def page(role,band,off):
    body={**ROLES[role],"country":"United States","employee_range":band,"exclude_industry":EXCL_IND,"limit":25,"offset":off}
    for i in range(6):
        try:
            r=requests.post(URL,headers=H,json=body,timeout=90)
            if r.status_code==429: time.sleep(int(r.headers.get("Retry-After",2))+1); continue
            j=r.json(); res=(j.get("results") or {}).get("results") or []
            for x in res: x["_role"]=role; x["_band"]=band
            return res,(j.get("metadata") or {}).get("fair_use")
        except Exception as e: time.sleep(3)
    return [],None
jobs=[(r,b,o) for r in ROLES for b in BANDS for o in range(0,per,25)]
n=0
with open(out,"w") as f, ThreadPoolExecutor(4) as p:
    for res,fu in p.map(lambda a:page(*a),jobs):
        for x in res: f.write(json.dumps(x)+"\n"); n+=1
print("raw records",n,"fair_use",fu)
