from fastapi import FastAPI
from starlette.responses import JSONResponse

from app import generate_password

app = FastAPI()

app.include_router(generate_password.router)


@app.get("/", tags=["root"])
def get_personal_details():
    """
    Get my personal details in JSON format.

    Returns:
    - JSONResponse: JSON response containing personal details.
    """
    personal_details = {
        "name": "Kartikeya P Malimath",
        "email": "kartikeyapm.uk@gmail.com",
        "linkedin": "linkedin.com/in/kartikeya-malimath",
        "github": "github.com/KartikeyaMalimath",
        "phone": "+44 (0) 744 373 4121",
        "location": "Leeds, United Kingdom",
        "education": [
            {
                "university": "University of Leeds",
                "degree": "MSc. in Advanced Computer Science",
                "grade": "7.14/10.00 (Distinction)",
                "completion_date": "September 2023",
                "related_courses": [
                    "Algorithms",
                    "Cloud Computing",
                    "Bio Inspired Computing",
                    "Advanced Software Engineering",
                    "Data Science",
                    "Deep Learning",
                    "Data mining & Text Analysis"
                ],
                "project": "Frame Interpolation Using AI-Model (FILM) for Low Bitrate Video Enhancement",
                "technologies_used": ["Convolutional Neural Network", "Python", "FastAPI", "HTML5", "CSS3"]
            },
            {
                "university": "Visvesvaraya Technological University",
                "degree": "B.E. in Computer Science & Engineering",
                "cgpa": "8.05/10.00 (Distinction)",
                "completion_date": "August 2020",
                "awards": ["Smart India Hackathon 2018 - Best Innovation Award",
                           "Onload National level Hackathon - Winner"],
                "organizations": ["Open Source Labs", "Apple Innovation Lab", "Google Developer student Clubs",
                                  "Google AI - ML ambassador"]
            }
        ],
        "skills": {
            "programming_languages": ["Python", "Golang", "Java", "HTML5", "CSS3", "PhP", "Javascript"],
            "operating_systems": ["Linux Ubuntu", "Windows"],
            "technologies": ["FastAPI", "Git", "AWS", "GCP", "CI/CD", "Docker", "Redis", "Kubernetes"]
        },
        "experience": [
            {
                "company": "Chatterbug Limited",
                "position": "Python Developer",
                "duration": "Sep/2023 - Present",
                "responsibilities": [
                    "Leading subscription-based SAAS product development using FastAPI, PostgreSQL, Redis, HTML5, CSS3, and JavaScript on GCP.",
                    "Spearheading end-to-end Patient Management System development, balancing frontend and backend roles.",
                    "Implementing Dockerization for streamlined deployment and consistency across diverse environments.",
                    "Operating in an agile environment, adapting to evolving requirements, and delivering iterative releases.",
                    "Driving revenue impact through a subscription-based model."
                ]
            },
            {
                "company": "Amagi Media Labs Pvt. Ltd.",
                "position": "Application Engineer - Python Developer",
                "duration": "Feb/2022 - Aug/2022",
                "responsibilities": [
                    "Designed and Developed SAAS internal product for the Media Ingestion Team using Python, AWS, FastAPI, Docker, Git & GitHub, and Circle CI.",
                    "Led the team in creating a scalable media ingestion solution, successfully onboarded 10+ customers for alpha and beta testing."
                ]
            },
            {
                "company": "Tata Consultancy Services",
                "position": "Assistant System Engineer - R&D",
                "duration": "Nov/2020 - Feb/2022",
                "responsibilities": [
                    "Worked on L2-L3 network layer feature integration for Cisco routers using Python scripts in an Agile team environment."
                ]
            },
            {
                "company": "Fusion Minds technologies",
                "position": "Full Stack Developer Intern",
                "duration": "Jan/2020 - Mar/2020",
                "responsibilities": [
                    "Full stack development experience using HTML5, CSS3, JS, Ajax, Bootstrap, PHP, Apache, and SQL in an Agile environment.",
                    "Developed and delivered a B2B SAAS product for ticketing and parking systems using QR code scanners."
                ]
            }
        ],
        "publications": [
            {
                "title": "Citizen Unique ID Based Real-Time Face Recognition for Surveillance and National Security",
                "journal": "IJRTE",
                "publication_date": "March 2020"
            },
            {
                "title": "Implementation of Aadhaar Verified, face Recognition based Security Surveillance",
                "journal": "IJITEE",
                "publication_date": "July 2020"
            }
        ],
        "projects": [
            "Image Recognition and Image Captioning: Python Project",
            "Face Recognition for Surveillance: Aadhaar based face detection - Python Application",
            "Easy Transit: public transport real-time booking system with sentimental analysis - Web Application",
            "On-Call Medical Assistant: AI-based medical assistant on-call for primary health care - Python/Tensorflow"
        ]
    }
    test = "test"
    return JSONResponse(personal_details)
