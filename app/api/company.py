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
        "bio": "Founder and visionary leader of GO Construction Company Ltd...",
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
        "level": 2,
        "bio": "As Managing Director, Eng. Nsengimana Olivier is responsible for the overall company operations...",
        "experience": "15+ years",
        "qualifications": ["Civil Engineering", "MBA", "Project Management Professional"],
        "projects": ["Residential Complex Phase 1", "Commercial Building", "Infrastructure Development"]
    },
    # Add more staff members as needed
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