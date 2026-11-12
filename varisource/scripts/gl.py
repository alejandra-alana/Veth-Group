import os,sys,json,requests
EP="https://app.getleads.io/api/mcp"
H={"Authorization":"Bearer "+os.environ["GETLEADS_API_KEY"],"Content-Type":"application/json","Accept":"application/json, text/event-stream"}
sid=None;rid=[1]
def parse(t):
    t=t.strip()
    if not t: return {}
    if t.startswith("data:") or "\ndata:" in t:
        L=[l[5:].strip() for l in t.splitlines() if l.startswith("data:")]
        L=[l for l in L if l and l!="[DONE]"]; return json.loads(L[-1]) if L else {}
    return json.loads(t)
def post(p,exp=True):
    global sid
    h=dict(H); 
    if sid: h["mcp-session-id"]=sid
    r=requests.post(EP,headers=h,json=p,timeout=300)
    sid=r.headers.get("mcp-session-id") or sid
    if not exp: return None
    j=parse(r.text)
    if "error" in j: raise Exception(j["error"])
    return j.get("result")
def init():
    post({"jsonrpc":"2.0","id":0,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"lb","version":"1"}}})
    post({"jsonrpc":"2.0","method":"notifications/initialized"},False)
def call(name,args):
    rid[0]+=1
    r=post({"jsonrpc":"2.0","id":rid[0],"method":"tools/call","params":{"name":name,"arguments":args}})
    t=(r or {}).get("content",[{}])[0].get("text")
    if t is None: return r
    try: return json.loads(t)
    except: return t
if __name__=="__main__" or True: init()
if __name__=="__main__":
    if sys.argv[1]=="list":
        r=post({"jsonrpc":"2.0","id":9,"method":"tools/list","params":{}})
        print(json.dumps(r,indent=1))
    else:
        print(json.dumps(call(sys.argv[1],json.loads(sys.argv[2])),indent=1))
