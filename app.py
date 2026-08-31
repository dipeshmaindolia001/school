"""
Chalkframe School Outreach Script
----------------------------------
Sends a personalized email (via Gmail SMTP) and/or WhatsApp message
(via WhatsApp Web, using pywhatkit) to each school in SCHOOLS.

SETUP (one-time):
    pip install pywhatkit

    Gmail:
      1. Turn on 2-Step Verification on your Gmail account.
      2. Create an "App Password": https://myaccount.google.com/apppasswords
      3. Put that 16-char password (not your normal password) in GMAIL_APP_PASSWORD below.

    WhatsApp:
      1. Log into web.whatsapp.com on your DEFAULT browser (must stay logged in).
      2. pywhatkit opens a browser tab and sends the message automatically.
      3. Keep your PC/laptop screen unlocked while the script runs.

USAGE:
    python send_outreach.py --dry-run          # preview messages, sends nothing
    python send_outreach.py --email-only        # only send emails
    python send_outreach.py --whatsapp-only      # only send WhatsApp
    python send_outreach.py                      # send both
"""

import argparse
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ============ CONFIG — EDIT THESE ============
GMAIL_ADDRESS = "youremail@gmail.com"
GMAIL_APP_PASSWORD = "your16charapppassword"   # NOT your normal Gmail password
YOUR_NAME = "Dipesh Maindolia"
YOUR_WHATSAPP_NUMBER = "+917017982390"
WEBSITE_LINK = "https://chalkframe.vercel.app/index.html"
SECONDS_BETWEEN_WHATSAPP_MSGS = 25   # keep >=20s so the WhatsApp tab has time to load/send
# ==============================================

# ============ SCHOOL LIST ============
# phones: list of numbers in +91XXXXXXXXXX format (first one is used for WhatsApp)
# email: set to None if not publicly listed
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
     "phones": [],  # landline 05947-357284 — not a WhatsApp number, skip
     "email": None},

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


def email_body(school_name: str) -> str:
    return f"""Dear Sir/Ma'am,

We are Chalkframe, a digital agency helping schools in Ramnagar, Kashipur & Haldwani with professional Instagram reels, admission graphics, and modern websites — fully managed remotely over WhatsApp, without hiring any in-house staff.

We came across {school_name} and would love to help boost your admissions online.

What we offer:
- Social Media Management (Reels, Posts, Admissions Creatives) — Rs 10,000/month
- School Website Development — Rs 15,000 one-time
- Website Maintenance — Rs 3,000/month

You can check our work and pricing here: {WEBSITE_LINK}

We'd love to offer your school a free digital audit — a quick 5-point report on your current online presence.

Feel free to reply here or WhatsApp us at {YOUR_WHATSAPP_NUMBER}.

Regards,
{YOUR_NAME}
Chalkframe
"""


EMAIL_SUBJECT = "Boost Your School's Admissions with Professional Social Media & Website"


def whatsapp_message(school_name: str) -> str:
    # Shorter, WhatsApp-native version of the same pitch
    return (
        f"Namaste 🙏, this is {YOUR_NAME} from *Chalkframe*.\n\n"
        f"We help schools like *{school_name}* get more admissions through professional "
        f"Instagram reels, admission creatives & modern websites — fully managed remotely, "
        f"no in-house staff needed.\n\n"
        f"📱 Social Media Management — ₹10,000/month\n"
        f"🌐 Website Development — ₹15,000 one-time\n"
        f"🔧 Website Maintenance — ₹3,000/month\n\n"
        f"See our work: {WEBSITE_LINK}\n\n"
        f"We'd love to send you a *free 5-point digital audit* of your school's current online presence — "
        f"would you like us to send it over?"
    )


def send_email(to_email: str, school_name: str) -> bool:
    msg = MIMEMultipart()
    msg["From"] = GMAIL_ADDRESS
    msg["To"] = to_email
    msg["Subject"] = EMAIL_SUBJECT
    msg.attach(MIMEText(email_body(school_name), "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
            server.sendmail(GMAIL_ADDRESS, to_email, msg.as_string())
        return True
    except Exception as e:
        print(f"  [EMAIL FAILED] {to_email}: {e}")
        return False


def send_whatsapp(phone: str, school_name: str) -> bool:
    try:
        import pywhatkit
    except ImportError:
        print("  [WHATSAPP FAILED] pywhatkit not installed. Run: pip install pywhatkit")
        return False

    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no=phone,
            message=whatsapp_message(school_name),
            wait_time=15,
            tab_close=True,
        )
        return True
    except Exception as e:
        print(f"  [WHATSAPP FAILED] {phone}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Preview only, send nothing")
    parser.add_argument("--email-only", action="store_true")
    parser.add_argument("--whatsapp-only", action="store_true")
    args = parser.parse_args()

    do_email = not args.whatsapp_only
    do_whatsapp = not args.email_only

    results = []

    for school in SCHOOLS:
        name = school["name"]
        print(f"\n=== {name} ===")

        # EMAIL
        if do_email:
            if school["email"]:
                if args.dry_run:
                    print(f"  [DRY-RUN] Would email: {school['email']}")
                    print(f"  Subject: {EMAIL_SUBJECT}")
                else:
                    ok = send_email(school["email"], name)
                    print(f"  Email -> {school['email']}: {'sent' if ok else 'FAILED'}")
                    results.append((name, "email", school["email"], ok))
            else:
                print("  No public email listed — skipped.")

        # WHATSAPP
        if do_whatsapp:
            if school["phones"]:
                phone = school["phones"][0]  # primary number
                if args.dry_run:
                    print(f"  [DRY-RUN] Would WhatsApp: {phone}")
                else:
                    ok = send_whatsapp(phone, name)
                    print(f"  WhatsApp -> {phone}: {'sent' if ok else 'FAILED'}")
                    results.append((name, "whatsapp", phone, ok))
                    time.sleep(SECONDS_BETWEEN_WHATSAPP_MSGS)
            else:
                print("  No mobile number listed — skipped.")

    if not args.dry_run and results:
        print("\n\n=== SUMMARY ===")
        for name, channel, target, ok in results:
            print(f"{'✔' if ok else '✘'} {name} [{channel}] -> {target}")


if __name__ == "__main__":
    main()