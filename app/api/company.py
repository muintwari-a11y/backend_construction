from fastapi import APIRouter
from typing import List, Dict, Any

router = APIRouter()

# Company info data
company_info = {
    "name": "GO Construction Company Ltd",
    "address": "GBC House, Gikondo, Kigali",
    "email": "info@goconstructioltd.com",
    "phone": "0789889108",
    "established": "6th August 2024",
    "registeredWith": "Rwanda Development Board (RDB)",
}

mission = "Our mission is to provide professional engineering, real estate, and project consultancy services that meet the highest standards of quality, safety, and integrity ensuring client satisfaction and long-term partnerships."

vision = "To become a leading and trusted provider of innovative engineering solutions, sustainable real-estate developments, and high-quality project studies that shape modern, resilient, and thriving communities."

core_values = [
    {"id": 1, "title": "Integrity & Ethics", "icon": "Shield"},
    {"id": 2, "title": "Quality & Excellence", "icon": "Award"},
    {"id": 3, "title": "Safety & Environmental Responsibility", "icon": "Leaf"},
    {"id": 4, "title": "Innovation & Continuous Improvement", "icon": "Lightbulb"},
    {"id": 5, "title": "Client Focus & Satisfaction", "icon": "Users"},
    {"id": 6, "title": "Teamwork & Collaboration", "icon": "Handshake"},
    {"id": 7, "title": "Professionalism & Reliability", "icon": "CheckCircle"},
]

services = [
    {
        "id": 1,
        "category": "Engineering Services & Technical Consultancy",
        "items": [
            "Architecture and structural design",
            "Geotechnical Studies",
            "Construction work",
            "Project planning and supervision",
            "Environmental and feasibility studies",
            "Wastewater management and treatment",
        ],
    },
    {
        "id": 2,
        "category": "Real Estate Development & Property Management",
        "items": [
            "Development of residential, commercial, and institutional properties",
            "Property investment, sales, and leasing",
            "Property and facility management",
            "Asset maintenance and upgrade services",
        ],
    },
]

achievements = [
    {
        "id": 1,
        "title": "RDB Registration",
        "description": "Successfully registered with Rwanda Development Board (RDB) as a professional construction company.",
        "date": "2024",
        "icon": "Award",
        "category": "Certification"
    },
    {
        "id": 2,
        "title": "Engineering Excellence",
        "description": "Over 37 years of combined engineering experience from founding team members.",
        "date": "2024",
        "icon": "Shield",
        "category": "Experience"
    },
    {
        "id": 3,
        "title": "Professional Team",
        "description": "Assembled a qualified team of engineers, architects, and project managers.",
        "date": "2024",
        "icon": "Users",
        "category": "Team"
    },
    {
        "id": 4,
        "title": "Quality Standards",
        "description": "Committed to delivering projects with the highest standards of quality and safety.",
        "date": "2024",
        "icon": "CheckCircle",
        "category": "Quality"
    },
    {
        "id": 5,
        "title": "Sustainable Development",
        "description": "Focus on environmentally responsible construction practices and sustainable development.",
        "date": "2024",
        "icon": "Leaf",
        "category": "Sustainability"
    },
    {
        "id": 6,
        "title": "Client Satisfaction",
        "description": "Building long-term partnerships through integrity, reliability, and client-focused services.",
        "date": "2024",
        "icon": "Handshake",
        "category": "Service"
    },
]

staff_members = [
    {
        "id": "chairman",
        "name": "Eng. Nkurunziza Gilbert",
        "title": "Chairman",
        "role": "chairman",
        "department": "management",
        "level": 1,
        "image": "/placeholder.svg",
        "bio": "Founder and visionary leader of GO Construction Company Ltd, Eng. Nkurunziza Gilbert possesses over 37 years of distinguished experience in civil engineering and construction management. He has spearheaded major infrastructure developments, commercial projects, and government contracts, establishing the company as a trusted partner in Rwanda's construction industry.",
        "experience": "37+ years",
        "qualifications": ["Civil Engineering", "Project Management", "Business Administration"],
        "projects": ["Major infrastructure projects", "Commercial developments", "Government contracts"]
    },
    {
        "id": "md",
        "name": "Eng. Nsengimana Olivier",
        "title": "Managing Director",
        "role": "admin",
        "department": "management",
        "email": "info@goconstructioltd.com",
        "phone": "+250789889108",
        "reportsTo": "chairman",
        "level": 2,
        "image": "/img/md.jpg",
        "bio": "As Managing Director, Eng. Nsengimana Olivier is responsible for the overall company operations, strategic planning, and building strong client relationships. With 15+ years of experience in civil engineering and project management, he oversees the execution of key projects including residential complexes, commercial buildings, and infrastructure developments, ensuring they meet the highest standards of quality and timeliness.",
        "experience": "15+ years",
        "qualifications": ["Civil Engineering", "MBA", "Project Management Professional"],
        "projects": ["Residential Complex Phase 1", "Commercial Building", "Infrastructure Development"]
    },
    {
        "id": "td",
        "name": "Eng. Izere Aime Bruce",
        "title": "Technical Director",
        "role": "admin",
        "department": "technical",
        "reportsTo": "md",
        "level": 3,
        "image": "/img/td.jpg",
        "bio": "As Technical Director, Eng. Izere Aime Bruce leads the engineering and construction operations, bringing 12+ years of expertise in structural design, project execution, and team management. He ensures all projects adhere to the highest standards of safety, quality, and innovation, overseeing multi-story buildings, bridge construction, and road infrastructure developments.",
        "experience": "12+ years",
        "qualifications": ["Civil Engineering", "Structural Engineering", "Construction Management"],
        "projects": ["Multi-story buildings", "Bridge construction", "Road infrastructure"]
    },
    {
        "id": "ad",
        "name": "Nkurikiyintwari Donath",
        "title": "Financial Director",
        "role": "financial",
        "department": "finance",
        "reportsTo": "md",
        "level": 3,
        "image": "/placeholder.svg",
        "bio": "As Financial Director, Nkurikiyintwari Donath oversees all financial operations, including budgeting, financial planning, and compliance. With 10+ years of experience in accounting and finance, he ensures the company's financial health, manages budgets for major projects, and optimizes tax strategies to support sustainable growth.",
        "experience": "10+ years",
        "qualifications": ["Accounting", "Finance", "Business Administration"],
        "projects": ["Financial planning for major projects", "Budget management", "Tax optimization"]
    },
    {
        "id": "accountant",
        "name": "Tuyishimire Divine",
        "title": "Accountant",
        "role": "financial",
        "department": "finance",
        "reportsTo": "ad",
        "level": 4,
        "image": "/img/accountant.jpg",
        "bio": "Tuyishimire Divine serves as the Senior Accountant, managing financial transactions, preparing reports, and ensuring compliance with financial regulations for all construction projects. With 8+ years of experience, she handles project costing, audit preparations, and financial reporting to support the company's financial integrity.",
        "experience": "8+ years",
        "qualifications": ["Accounting", "Finance", "CPA"],
        "projects": ["Financial reporting", "Project costing", "Audit preparation"]
    },
    {
        "id": "qe",
        "name": "Eng. Mbarushimana Tharcisse",
        "title": "Quality Engineer",
        "role": "staff",
        "department": "technical",
        "reportsTo": "td",
        "level": 4,
        "image": "/img/qe.jpg",
        "bio": "Eng. Mbarushimana Tharcisse is the Quality Engineer responsible for ensuring all construction work meets international standards and client specifications. With 10+ years of experience, he conducts quality assurance for residential complexes, material testing, and compliance audits to maintain the highest levels of safety and quality.",
        "experience": "10+ years",
        "qualifications": ["Civil Engineering", "Quality Management", "ISO Standards"],
        "projects": ["Quality assurance for residential complexes", "Material testing", "Compliance audits"]
    },
    {
        "id": "pm",
        "name": "Eng. Manzi Bizimungu Aubin",
        "title": "Project Manager",
        "role": "staff",
        "department": "technical",
        "reportsTo": "md",
        "level": 3,
        "image": "/img/pm.jpg",
        "bio": "Eng. Manzi Bizimungu Aubin serves as the Project Manager, coordinating construction activities, managing timelines, and allocating resources for multiple projects. With 9+ years of experience in civil engineering and project management, he oversees residential complex phases, commercial buildings, and infrastructure projects to ensure successful delivery.",
        "experience": "9+ years",
        "qualifications": ["Civil Engineering", "Project Management", "Construction Supervision"],
        "projects": ["Residential Complex Phase 1", "Commercial Building", "Infrastructure projects"]
    },
    {
        "id": "arch",
        "name": "Eng. Niyonsenga Roger",
        "title": "Quantity Surveyor",
        "role": "staff",
        "department": "technical",
        "reportsTo": "qe",
        "level": 5,
        "image": "/img/arch.jpg",
        "bio": "Eng. Niyonsenga Roger is the Quantity Surveyor responsible for managing project costs, procurement, and contract administration. With 7+ years of experience, he handles cost estimation, contract negotiations, and procurement management to optimize project budgets and ensure financial efficiency.",
        "experience": "7+ years",
        "qualifications": ["Quantity Surveying", "Cost Engineering", "Contract Management"],
        "projects": ["Cost estimation", "Contract negotiation", "Procurement management"]
    },
    {
        "id": "qs",
        "name": "Eng. Ineza Robert",
        "title": "Topographical Surveyor",
        "role": "staff",
        "department": "technical",
        "reportsTo": "qe",
        "level": 5,
        "image": "/img/qs.jpg",
        "bio": "Eng. Ineza Robert is the Topographical Surveyor specializing in land surveys, mapping, and site analysis. With 6+ years of experience in surveying and GIS, he conducts land surveying, site mapping, and topographical analysis to provide accurate data for construction planning.",
        "experience": "6+ years",
        "qualifications": ["Topographical Surveying", "Land Surveying", "GIS", "AutoCAD"],
        "projects": ["Land surveying", "Site mapping", "Topographical analysis"]
    },
    {
        "id": "water",
        "name": "Eng. Tuyizere Alexandre",
        "title": "Water Engineer",
        "role": "staff",
        "department": "technical",
        "reportsTo": "pm",
        "level": 5,
        "image": "/img/water.jpg",
        "bio": "Eng. Tuyizere Alexandre is the Water Engineer specializing in water supply systems, wastewater treatment, and hydraulic design. With 8+ years of experience in water engineering and hydraulics, he designs and oversees water supply systems, wastewater treatment facilities, and drainage systems for sustainable infrastructure.",
        "experience": "8+ years",
        "qualifications": ["Water Engineering", "Hydraulics", "Environmental Engineering"],
        "projects": ["Water supply systems", "Wastewater treatment", "Drainage systems"]
    },
    {
        "id": "geo",
        "name": "Eng. Nshimyimana Aime Valantin",
        "title": "Geotechnical Engineer",
        "role": "staff",
        "department": "technical",
        "reportsTo": "pm",
        "level": 5,
        "image": "/img/geo.jpg",
        "bio": "Eng. Nshimyimana Aime Valantin is the Geotechnical Engineer conducting soil investigations and foundation design. With 7+ years of experience in geotechnical engineering and soil mechanics, he performs soil testing, foundation design, and slope stability analysis to ensure safe and stable construction.",
        "experience": "7+ years",
        "qualifications": ["Geotechnical Engineering", "Soil Mechanics", "Foundation Design"],
        "projects": ["Soil testing", "Foundation design", "Slope stability analysis"]
    },
    {
        "id": "env",
        "name": "Eng. Manzi Malyse",
        "title": "M.Sc. Environmental Engineer",
        "role": "staff",
        "department": "technical",
        "reportsTo": "pm",
        "level": 5,
        "image": "/placeholder.svg",
        "bio": "Eng. Manzi Malyse is the M.Sc. Environmental Engineer specializing in environmental impact assessments, sustainability, and compliance. With 7+ years of experience, she conducts EIAs, promotes sustainable development projects, and ensures environmental compliance to minimize ecological impact.",
        "experience": "7+ years",
        "qualifications": ["Environmental Engineering", "EIA", "Sustainability"],
        "projects": ["Environmental impact assessments", "Sustainable development projects", "Environmental compliance"]
    },
    {
        "id": "ele",
        "name": "Maitre Eng. Mugemana Miguel",
        "title": "Electrical Engineer",
        "role": "staff",
        "department": "technical",
        "reportsTo": "pm",
        "level": 5,
        "image": "/img/ele.jpg",
        "bio": "Maitre Eng. Mugemana Miguel is the Electrical Engineer designing and overseeing electrical systems. With 7+ years of experience in electrical engineering and power systems, he handles electrical design for buildings, power distribution, and lighting systems.",
        "experience": "7+ years",
        "qualifications": ["Electrical Engineering", "Power Systems", "Building Automation"],
        "projects": ["Electrical design for buildings", "Power distribution", "Lighting systems"]
    },
    {
        "id": "it1",
        "name": "IT. Mugenga Ntwari Olivier",
        "title": "IT Director",
        "role": "admin",
        "email": "it@goconstructioltd.com",
        "phone": "+250788839820",
        "department": "management",
        "reportsTo": "md",
        "level": 3,
        "image": "/img/it1.jpg",
        "bio": "IT. Mugenga Ntwari Olivier is the IT Director managing the company's information technology infrastructure, software development, and digital solutions. With 7+ years of experience in IT and software development, he oversees IT infrastructure setup, software development projects, and digital solutions to enhance operational efficiency.",
        "experience": "7+ years",
        "qualifications": ["Information Technology", "Software Development", "System Administration"],
        "projects": ["IT infrastructure setup", "Software development", "Digital solutions"]
    },
    {
        "id": "media",
        "name": "IT. Nayituriki Olivier",
        "title": "Media Specialist",
        "role": "staff",
        "department": "management",
        "reportsTo": "it1",
        "level": 4,
        "image": "/img/media.jpg",
        "bio": "IT. Nayituriki Olivier is the Media Specialist handling company media content, marketing materials, and digital presence. With 7+ years of experience in media production and digital marketing, he creates media content, campaigns, and manages brand presence to promote the company's services.",
        "experience": "7+ years",
        "qualifications": ["Media Production", "Graphic Design", "Digital Marketing"],
        "projects": ["Media content creation", "Marketing campaigns", "Brand management"]
    },
    {
        "id": "eng1",
        "name": "Eng. Ndatimana Regis",
        "title": "Environmental Engineer",
        "role": "staff",
        "department": "technical",
        "reportsTo": "td",
        "level": 5,
        "image": "/img/eng1.jpg",
        "bio": "Eng. Ndatimana Regis is the Environmental Engineer conducting environmental impact assessments and ensuring compliance. With 8+ years of experience, he performs EIAs, promotes sustainable projects, and ensures environmental compliance to support eco-friendly construction.",
        "experience": "8+ years",
        "qualifications": ["Environmental Engineering", "EIA", "Sustainability", "Environmental Compliance"],
        "projects": ["Environmental impact assessments", "Sustainable projects", "Environmental compliance"]
    },
    {
        "id": "eng2",
        "name": "Eng. Dukundane Anselme",
        "title": "Architectural and Structural Engineer",
        "role": "staff",
        "department": "technical",
        "reportsTo": "td",
        "level": 5,
        "image": "/img/eng2.jpg",
        "bio": "Eng. Dukundane Anselme is the Architectural and Structural Engineer designing buildings and analyzing structural integrity. With 9+ years of experience in architecture and structural engineering, he handles architectural design, structural analysis, and building construction to ensure safe and efficient structures.",
        "experience": "9+ years",
        "qualifications": ["Architecture", "Structural Engineering", "Building Design", "Structural Analysis"],
        "projects": ["Architectural design", "Structural analysis", "Building construction"]
    },
    {
        "id": "eng3",
        "name": "Eng. Impano Aime Fiacre",
        "title": "Senior Quantity Surveyor",
        "role": "staff",
        "department": "technical",
        "reportsTo": "pm",
        "level": 5,
        "image": "/img/eng3.jpg",
        "bio": "Eng. Impano Aime Fiacre is the Senior Quantity Surveyor specializing in cost planning, estimation, and financial management. With 7+ years of experience, he manages cost planning, project estimation, and financial management to ensure economic efficiency in construction projects.",
        "experience": "7+ years",
        "qualifications": ["Quantity Surveying", "Cost Management", "Project Finance"],
        "projects": ["Cost planning", "Project estimation", "Financial management"]
    },
    {
        "id": "eng4",
        "name": "Eng. Kandangira Hubert",
        "title": "Architect",
        "role": "staff",
        "department": "technical",
        "reportsTo": "td",
        "level": 5,
        "image": "/img/eng4.jpg",
        "bio": "Eng. Kandangira Hubert is the Architect designing innovative and functional building structures. With 6+ years of experience in architecture and building design, he focuses on architectural design, building planning, and interior design to create aesthetically pleasing and functional spaces.",
        "experience": "6+ years",
        "qualifications": ["Architecture", "Building Design", "AutoCAD", "SketchUp"],
        "projects": ["Architectural design", "Building planning", "Interior design"]
    },
    {
        "id": "eng5",
        "name": "Maitre Eng. Mukamisha Barbara",
        "title": "Maitre Eng. Mukamisha Barbara",
        "role": "staff",
        "department": "technical",
        "reportsTo": "td",
        "level": 4,
        "image": "/img/eng5.jpg",
        "bio": "Maitre Eng. Mukamisha Barbara is the Master Project Management Engineer overseeing the project lifecycle. With 10+ years of experience, she ensures timely delivery, budget control, and quality standards through project management, quality control, and budget management.",
        "experience": "10+ years",
        "qualifications": ["Project Management", "Engineering", "PMP", "Project Planning"],
        "projects": ["Project management", "Quality control", "Budget management"]
    },
    {
        "id": "eng6",
        "name": "Eng. Nyabyenda Paulin",
        "title": "Head Advisor Engineer",
        "role": "staff",
        "department": "technical",
        "reportsTo": "td",
        "level": 3,
        "image": "/img/eng6.jpg",
        "bio": "Eng. Nyabyenda Paulin is the Head Advisor Engineer providing expert advisory services, technical guidance, and strategic planning. With 10+ years of experience in civil engineering and advisory, he offers engineering advisory, technical guidance, and project strategy to support complex engineering endeavors.",
        "experience": "10+ years",
        "qualifications": ["Civil Engineering", "Engineering Advisory", "Strategic Planning"],
        "projects": ["Engineering advisory", "Technical guidance", "Project strategy"]
    }
]

@router.get("/info")
async def get_company_info():
    return company_info

@router.get("/mission")
async def get_mission():
    return {"mission": mission}

@router.get("/vision")
async def get_vision():
    return {"vision": vision}

@router.get("/values")
async def get_values():
    return {"values": core_values}

@router.get("/services")
async def get_services():
    return {"services": services}

@router.get("/achievements")
async def get_achievements():
    return {"achievements": achievements}

@router.get("/staff")
async def get_staff():
    return {"staff": staff_members}