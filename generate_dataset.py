import pandas as pd
import random

random.seed(42)

# -----------------------------
# Suppliers (30)
# -----------------------------

supplier_names = [
    "EcoPack Industries","GreenWrap Solutions","BioServe Packaging",
    "NaturePack","EcoLeaf","PlasticWorld","Green Earth Pvt Ltd",
    "FreshPack","EarthBox","BioEco Solutions",
    "EcoSmart","LeafPack","EcoNest","PackRight","GoGreen",
    "SafeServe","BioCraft","EcoOne","GreenNova","BioFuture",
    "PackX","GreenHub","EcoWare","EarthSafe","PurePack",
    "BioLeaf","GreenCore","EcoTrend","PackMate","SustainPack"
]

cities = [
    "Bengaluru","Chennai","Kochi","Hyderabad",
    "Coimbatore","Mysuru","Vijayawada",
    "Visakhapatnam","Madurai","Trivandrum"
]

categories = [
    "Biodegradable Containers",
    "Paper Containers",
    "Plastic Containers",
    "Food Containers"
]

suppliers = []

for i in range(30):

    supplier = {

        "SupplierID":f"SUP{i+1:03d}",

        "CompanyName":supplier_names[i],

        "Category":random.choice(categories),

        "Location":random.choice(cities),

        "Certification":random.choice(
            ["Food Grade","Food Grade","Food Grade","Missing"]
        ),

        "Capacity":random.choice(
            [8000,10000,12000,15000,18000,20000,25000,30000]
        ),

        "DeliveryDays":random.randint(10,40),

        "Rating":round(random.uniform(3.2,5.0),1),

        "StartupFriendly":random.choice(["Yes","No"]),

        "Availability":random.choice(
            ["Available","Busy","Available"]
        ),

        "PreviousProjects":random.randint(5,60),

        "PreviousInteractions":random.randint(0,25),

        "Description":"Synthetic supplier record"
    }

    suppliers.append(supplier)

pd.DataFrame(suppliers).to_csv(
    "data/suppliers.csv",
    index=False
)

# -----------------------------
# Professionals (15)
# -----------------------------

skills = [
    "Procurement",
    "Supply Chain",
    "Vendor Management",
    "Negotiation",
    "Logistics",
    "Quality Assurance",
    "Packaging",
    "Inventory Management"
]

professionals=[]

for i in range(15):

    professionals.append({

        "ProfessionalID":f"PRO{i+1:03d}",

        "Name":f"Professional {i+1}",

        "Skill":random.choice(skills),

        "ExperienceYears":random.randint(2,15),

        "Location":random.choice(cities),

        "Availability":random.choice(
            ["Available","Busy"]
        ),

        "Certification":random.choice(
            ["ISO","Lean Six Sigma","APICS","None"]
        ),

        "Rating":round(random.uniform(3.5,5),1),

        "PreviousProjects":random.randint(5,50)

    })

pd.DataFrame(professionals).to_csv(
    "data/professionals.csv",
    index=False
)

# -----------------------------
# Projects (10)
# -----------------------------

projects=[]

for i in range(10):

    projects.append({

        "ProjectID":f"PRJ{i+1:03d}",

        "ProjectName":f"Project {i+1}",

        "Business":random.choice(supplier_names),

        "Category":"Packaging",

        "Budget":random.randint(100000,900000),

        "Deadline":f"2026-09-{random.randint(10,28)}",

        "Status":random.choice(
            ["Open","Active","Completed"]
        )

    })

pd.DataFrame(projects).to_csv(
    "data/projects.csv",
    index=False
)

# -----------------------------
# Opportunities (10)
# -----------------------------

opportunities=[]

for i in range(10):

    opportunities.append({

        "OpportunityID":f"OPP{i+1:03d}",

        "Title":f"Opportunity {i+1}",

        "Company":random.choice(supplier_names),

        "RequiredSkill":random.choice(skills),

        "Reward":random.randint(20000,100000),

        "Deadline":f"2026-08-{random.randint(10,30)}",

        "Status":"Open"

    })

pd.DataFrame(opportunities).to_csv(
    "data/opportunities.csv",
    index=False
)

# -----------------------------
# Procurement Requests (10)
# -----------------------------

requests=[]

for i in range(10):

    requests.append({

        "RequestID":f"REQ{i+1:03d}",

        "Business":random.choice(supplier_names),

        "Category":"Biodegradable Containers",

        "Quantity":random.choice(
            [5000,10000,15000,20000]
        ),

        "DeliveryDays":random.choice(
            [15,20,25,30]
        ),

        "Certification":"Food Grade",

        "Status":"Open"

    })

pd.DataFrame(requests).to_csv(
    "data/procurement_requests.csv",
    index=False
)

print("="*60)
print("Dataset Generated Successfully")
print("="*60)

print("suppliers.csv            : 30 rows")
print("professionals.csv        : 15 rows")
print("projects.csv             : 10 rows")
print("opportunities.csv        : 10 rows")
print("procurement_requests.csv : 10 rows")