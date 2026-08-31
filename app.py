"""
Chalkframe School Outreach — Email via Browser (Gmail Compose)
-----------------------------------------------------------------
No SMTP, no app password. Opens a pre-filled Gmail compose window
in your browser for each school (subject + body already typed in) —
you just review and hit Send yourself.

USAGE:
    python app.py                 # opens one compose tab per school, pausing between each
    python app.py --no-pause      # opens all tabs back to back, no pausing
"""

import argparse
import time
import webbrowser
from urllib.parse import quote

# ============ CONFIG — EDIT THESE ============
YOUR_NAME = "Dipesh Maindolia"
YOUR_WHATSAPP_NUMBER = "+917017982390"
WEBSITE_LINK = "https://chalkframe.vercel.app/index.html"
# ==============================================

# ============ SCHOOL LIST ============
SCHOOLS = [
    {"name": "The Touchwood School", "area": "Near New Dhela Bridge, Beljuri, Kashipur",
     "phones": ["+918477867776", "+919756515547"], "email": "thetouchwoodschool@gmail.com"},

    {"name": "Little Scholars School", "area": "Bhalla Farm, Pratappur, Kashipur",
     "phones": ["+919105666371"], "email": "littlescholars.kashipur@gmail.com"},

    {"name": "The Gurukul Foundation School", "area": "Jaitpur Road, Kashipur",
     "phones": ["+918193030303", "+919917481556", "+919837092182"], "email": "contactus@thegurukulfoundation.school"},

    {"name": "Kids Increase Convent School", "area": "Kachnalgaji, Kashipur",
     "phones": ["+919473835675"], "email": None},

    {"name": "Krishna Public Collegiate", "area": "Tanda Ujjain, Kashipur",
     "phones": ["+919719321450"], "email": None},

    {"name": "Vision Valley School", "area": "Kuan Khera, Kundeshwari Road, Kashipur",
     "phones": [], "email": None},

    {"name": "Shri Sai Public School", "area": "Jaspur Khurd / Vaishali Colony",
     "phones": ["+917534010191"], "email": None},

    {"name": "Roots Public School", "area": "NH-121, Kashipur",
     "phones": ["+919837736322"], "email": None},

    {"name": "Jagriti Public School", "area": "Teacher's Colony, Kashipur",
     "phones": ["+918218172798"], "email": None},

    {"name": "Aman Public School (APS)", "area": "Laxmipur, Kashipur",
     "phones": ["+918126465330"], "email": None},
]
# ======================================

EMAIL_SUBJECT = "Boost Your School's Admissions with Professional Social Media & Website"


def email_body(school_name: str) -> str:
    return f"""Dear Sir/Ma'am,

We are Chalkframe, a digital agency helping schools in Ramnagar, Kashipur & Haldwani with professional Instagram reels, admission graphics, and modern websites — fully managed remotely over WhatsApp, without hiring any in-house staff.

We came across {school_name} and would love to help boost your admissions online.

What we offer:
- Social Media Management (Reels, Posts, Admissions Creatives) - Rs 10,000/month
- School Website Development - Rs 15,000 one-time
- Website Maintenance - Rs 3,000/month

You can check our work and pricing here: {WEBSITE_LINK}

We'd love to offer your school a free digital audit - a quick 5-point report on your current online presence.

Feel free to reply here or WhatsApp us at {YOUR_WHATSAPP_NUMBER}.

Regards,
{YOUR_NAME}
Chalkframe
"""


def gmail_compose_url(to_email: str, subject: str, body: str) -> str:
    return (
        "https://mail.google.com/mail/?view=cm&fs=1"
        f"&to={quote(to_email)}"
        f"&su={quote(subject)}"
        f"&body={quote(body)}"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-pause", action="store_true",
                         help="Open all compose tabs back-to-back without waiting for Enter between each")
    args = parser.parse_args()

    schools_with_email = [s for s in SCHOOLS if s["email"]]

    if not schools_with_email:
        print("No schools with a public email in the list.")
        return

    print(f"Opening Gmail compose for {len(schools_with_email)} school(s)...\n")

    for school in schools_with_email:
        name = school["name"]
        email = school["email"]
        url = gmail_compose_url(email, EMAIL_SUBJECT, email_body(name))

        print(f"=== {name} ===")
        print(f"  -> {email}")
        webbrowser.open(url)

        if not args.no_pause:
            input("  Review & hit Send in the browser, then press Enter here to open the next one...")
        else:
            time.sleep(2)  # small gap so tabs don't all fire at once

    print("\nDone. Every compose window is pre-filled — just review and click Send in each tab.")


if __name__ == "__main__":
    main()