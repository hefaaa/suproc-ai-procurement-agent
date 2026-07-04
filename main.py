from agent.parser import RequirementParser
from agent.executor import AgentExecutor
from agent.advisor import LLMAdvisor

print("=" * 60)
print("SUPROC LOCAL AGENT")
print("=" * 60)

print("\nAI Agent Started...\n")

request = """We are a sustainable food-packaging startup based in Bengaluru. We need three suppliers
from South India that can provide food-grade biodegradable containers, support an initial
order of 10,000 units and deliver within 30 days. Explain why each supplier is suitable,
identify any missing information and prepare an outreach message."""

# -------------------------------------------------------
# Initialize Components
# -------------------------------------------------------

parser = RequirementParser()
executor = AgentExecutor()
advisor = LLMAdvisor()

# -------------------------------------------------------
# Parse Requirement
# -------------------------------------------------------

requirement = parser.parse(request)

print("\n" + "=" * 60)
print("BUSINESS REQUIREMENT")
print("=" * 60)

print(f"Objective              : {requirement.objective}")
print(f"Entity Type           : {requirement.entity_type}")
print(f"Category              : {requirement.category}")
print(f"Locations             : {', '.join(requirement.locations)}")
print(f"Minimum Capacity      : {requirement.min_capacity:,}")
print(f"Maximum Delivery Days : {requirement.max_delivery_days}")
print(f"Requested Results     : {requirement.requested_results}")

# -------------------------------------------------------
# Execute Agent
# -------------------------------------------------------

result = executor.execute(requirement)

results = result["recommendations"]
professionals = result["professionals"]
projects = result["projects"]
history = result["history"]
opportunities = result["opportunities"]
report = result["validation_report"]
correction = result["correction_report"]

# -------------------------------------------------------
# AI Analysis (ONE LLM CALL)
# -------------------------------------------------------

analysis = advisor.generate_analysis(
    requirement,
    results
)

# -------------------------------------------------------
# Execution Plan
# -------------------------------------------------------

print("\n" + "=" * 60)
print("EXECUTION PLAN")
print("=" * 60)

for i, step in enumerate(analysis["execution_plan"], start=1):
    print(f"{i}. {step}")

# -------------------------------------------------------
# Recommendations
# -------------------------------------------------------

print("\n" + "=" * 60)
print("TOP RECOMMENDATIONS")
print("=" * 60)

for i, supplier in enumerate(results, 1):

    print("\n" + "=" * 60)
    print(f"RECOMMENDATION {i}")
    print("=" * 60)

    print(f"Supplier      : {supplier['CompanyName']}")
    print(f"Location      : {supplier['Location']}")
    print(f"Match Score   : {supplier['MatchScore']}/100")

    print("\nEvidence")

    print(f"✓ Category        : {supplier['Category']}")
    print(f"✓ Certification   : {supplier['Certification']}")
    print(f"✓ Capacity        : {supplier['Capacity']:,}")
    print(f"✓ Delivery        : {supplier['DeliveryDays']} Days")
    print(f"✓ Rating          : {supplier['Rating']}")
    print(f"✓ Availability    : {supplier['Availability']}")

    print("\nScore Breakdown")

    for k, v in supplier["Breakdown"].items():
        print(f"{k:25} {v}/")
print("\n" + "=" * 60)
print("SIMILAR PROCUREMENT REQUESTS")
print("=" * 60)

if history.empty:
    print("No similar procurement requests found.")
else:
    for _, row in history.head(3).iterrows():
        print(f"\n{row['RequestID']}")
        print(f"Business : {row['Business']}")
        print(f"Quantity : {row['Quantity']}")
        print(f"Delivery : {row['DeliveryDays']} Days")

# -------------------------------------------------------
# Validation Report
# -------------------------------------------------------

print("\n" + "=" * 60)
print("VALIDATION REPORT")
print("=" * 60)

for item in report:

    print(f"\nSupplier : {item['SupplierID']}")
    print(f"Status   : {item['Status']}")

    if item["Status"] == "FAIL":

        print("Reasons:")

        for reason in item["Reasons"]:
            print(f" - {reason}")

    elif item["Status"] == "WARNING":

        print(item["Reasons"][0])

# -------------------------------------------------------
# Validation Status
# -------------------------------------------------------

print("\n" + "=" * 60)
print("VALIDATION STATUS")
print("=" * 60)

if all(item["Status"] == "PASS" for item in report):
    print("PASS")
    print("All recommendations satisfy hard constraints.")
else:
    print("PARTIAL PASS")
    print("Some recommendations require correction.")

# -------------------------------------------------------
# Correction Report
# -------------------------------------------------------

print("\n" + "=" * 60)
print("CORRECTION REPORT")
print("=" * 60)

for item in correction:
    print(f"• {item}")

# -------------------------------------------------------
# Missing Information
# -------------------------------------------------------

print("\n" + "=" * 60)
print("MISSING INFORMATION")
print("=" * 60)

for item in analysis["missing_information"]:
    print(f"• {item}")

# -------------------------------------------------------
# Risks
# -------------------------------------------------------

print("\n" + "=" * 60)
print("RISKS")
print("=" * 60)

for risk in analysis["risks"]:
    print(f"• {risk}")
print("\n" + "=" * 60)
print("RELATED PROJECTS")
print("=" * 60)

if projects.empty:
    print("No related projects found.")
else:
    for _, row in projects.head(3).iterrows():
        print(f"\n{row['ProjectName']}")
        print(f"Budget : {row['Budget']}")
        print(f"Status : {row['Status']}")

# -------------------------------------------------------
# Recommended Next Action
# -------------------------------------------------------

print("\n" + "=" * 60)
print("RECOMMENDED NEXT ACTION")
print("=" * 60)

print("Contact the following suppliers:\n")

for supplier in results:
    print(f"• {supplier['CompanyName']}")

print("\n" + "=" * 60)
print("RECOMMENDED PROFESSIONALS")
print("=" * 60)

if professionals.empty:
    print("No professionals found.")
else:
    for _, row in professionals.head(3).iterrows():
        print(f"\n{row['Name']}")
        print(f"Skill : {row['Skill']}")
        print(f"Rating : {row['Rating']}")

# -------------------------------------------------------
# Draft Outreach
# -------------------------------------------------------

print("\n" + "=" * 60)
print("DRAFT OUTREACH")
print("=" * 60)

print(analysis["outreach"])

print("\n" + "=" * 60)
print("RELATED OPPORTUNITIES")
print("=" * 60)

if opportunities.empty:
    print("No related opportunities found.")
else:
    for _, row in opportunities.head(3).iterrows():
        print(f"\n{row['Title']}")
        print(f"Reward : ₹{row['Reward']}")

# -------------------------------------------------------
# Final Status
# -------------------------------------------------------

print("\n" + "=" * 60)
print("STATUS")
print("=" * 60)

print("Awaiting Human Approval")