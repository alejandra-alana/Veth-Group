EXCL_IND=['Administration of Justice','Armed Forces','Cosmetology and Barber Schools','E-Learning Providers','Education','Education Administration Programs','Fine Arts Schools','Government Administration','Higher Education','Language Schools','Law Enforcement','Legislative Offices','Libraries','Military and International Affairs','Primary and Secondary Education','Public Policy Offices','Public Safety','Secretarial Schools','Political Organizations','International Affairs']
ROLES={
 "Finance leadership":dict(job_titles=["Chief Financial Officer","CFO","VP Finance","Vice President of Finance","Vice President, Finance","VP of Finance","Head of Finance"],seniority=["c-level","vp"]),
 "FP&A / Controller":dict(job_titles=["Financial Planning","FP&A","Corporate Controller","Controller"],seniority=["vp","director","manager"]),
 "Procurement":dict(job_titles=["Chief Procurement Officer","Procurement","Purchasing","Strategic Sourcing","Sourcing"],seniority=["c-level","vp","director"]),
}
EXCL_TITLES=["Assistant","Intern","Analyst","Coordinator","Specialist","Associate","Buyer","Clerk","Student","Retired","Former","Consultant","Fractional","Advisor"]
def base(min_e=250,max_e=2000):
    return dict(countries=["United States"],company_size_min=min_e,company_size_max=max_e,exclude_industries=EXCL_IND,exclude_job_titles=EXCL_TITLES,email_status=["VALID"],require_email=True)
