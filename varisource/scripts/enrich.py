import csv,os,sys,json,requests,time
from concurrent.futures import ThreadPoolExecutor
src,out=sys.argv[1],sys.argv[2]
rows=list(csv.DictReader(open(src)))
MH={"Authorization":"Bearer "+os.environ["MOLTSETS_API_KEY"],"Content-Type":"application/json"}
QH={"Authorization":"Bearer "+os.environ["QUICKENRICH_API_KEY"],"Accept":"application/json"}
MV=os.environ["MILLIONVERIFIER_API_KEY"]
FREE={"gmail.com","yahoo.com","hotmail.com","outlook.com","aol.com","icloud.com","me.com","live.com","msn.com","comcast.net"}
def molt(x):
    try:
        j=requests.post("https://api.moltsets.com/api/v1/tools/linkedin_to_business_email",headers=MH,json={"linkedin_url":x["LinkedIn"]},timeout=60).json()
        r=j.get("results") or {}
        if r.get("email") and r.get("type")!="personal": return r["email"],"moltsets",r.get("risk_score")
    except Exception as e: pass
    return None
def qe(x):
    try:
        j=requests.get("https://app.quickenrich.io/api/employees/search",headers=QH,params={"linkedin_url":x["LinkedIn"],"company_url":x["Website"],"first_name":x["First Name"],"last_name":x["Last Name"]},timeout=60).json()
        d=j.get("data")
        if isinstance(d,dict) and d.get("email"): return d["email"],"quickenrich",""
    except Exception: pass
    return None
def mv(e):
    for i in range(3):
        try:
            j=requests.get("https://api.millionverifier.com/api/v3/",params={"api":MV,"email":e,"timeout":20},timeout=40).json()
            return j.get("result"),j.get("subresult")
        except Exception: time.sleep(2)
    return "error",""
def work(x):
    f=molt(x) or qe(x)
    x=dict(x); x.update(Email="",Email_Source="",Risk_Score="",MV_Result="",MV_Sub="")
    if f:
        e,s,rs=f
        if e.split("@")[-1].lower() in FREE: return x
        x.update(Email=e.lower(),Email_Source=s,Risk_Score=rs or "")
        x["MV_Result"],x["MV_Sub"]=mv(e)
    return x
with ThreadPoolExecutor(6) as p: res=list(p.map(work,rows))
w=csv.DictWriter(open(out,"w",newline=""),fieldnames=list(res[0].keys())); w.writeheader(); w.writerows(res)
import collections
print("found",sum(1 for r in res if r["Email"]),"/",len(res))
print(collections.Counter(r["Email_Source"] for r in res)); print(collections.Counter(r["MV_Result"] for r in res))
