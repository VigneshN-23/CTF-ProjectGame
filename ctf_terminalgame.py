#!/usr/bin/env python3
import csv
import random
import os
import time

# ---------- Terminal Colors ----------
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ---------- Globals ----------
score = 0  # MCQ Score
ctf_score = 0  # CTF Score

# ---------- LEVEL 1: MCQ ----------
def load_questions(filename):
    questions = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            questions.append({
                "question": row["question"],
                "options": {
                    'a': row["option_a"],
                    'b': row["option_b"],
                    'c': row["option_c"],
                    'd': row["option_d"],
                },
                "answer": row["answer"].strip().lower()
            })
    return questions

def ask_mcq(q):
    global score
    print(f"\n{CYAN}{q['question']}{RESET}")
    for key, val in q["options"].items():
        print(f" {key}) {val}")
    choice = input(f"{YELLOW}Your answer (a/b/c/d): {RESET}").strip().lower()
    if choice == q["answer"]:
        print(f"{GREEN}✅ Correct!{RESET}")
        score += 10
    else:
        print(f"{RED}❌ Incorrect!{RESET}")
        print(f"The correct answer was: {q['answer']}) {q['options'][q['answer']]}\n")

def level1_mcq():
    print(f"{CYAN}🎮 Welcome to CyberQuest - Learn Cybersecurity! 🎮{RESET}")
    print("-------------------------------------------------------------")
    questions = load_questions("questions.csv")
    random.shuffle(questions)
    for q in questions[:5]:
        ask_mcq(q)

    print("-------------------------------------------------------------")
    print(f"🏆 Your MCQ score: {score} / 50")
    if score >= 30:
        print(f"{GREEN}🔓 You unlocked Level 2 - Recon CTF!{RESET}")
        return True
    else:
        print(f"{RED}🔒 Level 2 Locked. Keep practicing!{RESET}")
        return False

# ---------- LEVEL 2: RECON CTF ----------
def hint(msg): print(f"{YELLOW}[Hint] {msg}{RESET}")
def success(flag):
    global ctf_score
    print(f"{GREEN}Correct! {flag}{RESET}\n")
    ctf_score += 1
def fail(): print(f"{RED}Incorrect. Try again.{RESET}\n")
def wait(): time.sleep(1)

def ctf1():
    print(f"{CYAN}CTF 1: WHOIS Recon{RESET}")
    print("Find the registrar name of 'example.com'")
    choice = input(f"{YELLOW}Answer or type 'hint': {RESET}")
    if choice.strip().lower() == 'hint':
        hint("Try: whois example.com | grep Registrar")
        choice = input(f"{YELLOW}Answer: {RESET}")
    if "icann" in choice.lower() or "reserved" in choice.lower():
        success("FLAG{whois_detective}")
    else:
        fail()

def ctf2():
    print(f"{CYAN}CTF 2: DNS A Record Lookup{RESET}")
    print("Find the IP address of shopify.com")
    choice = input(f"{YELLOW}Answer or type 'hint': {RESET}")
    if choice.strip().lower() == 'hint':
        hint("Try: dig shopify.com +short")
        choice = input(f"{YELLOW}Answer: {RESET}")
    if any(choice.startswith(ip) for ip in ["23.227.", "151.101."]):
        success("FLAG{dns_lookup}")
    else:
        fail()

def ctf3():
    print(f"{CYAN}CTF 3: Email Harvesting{RESET}")
    print("Find an email belonging to tryhackme.com")
    choice = input(f"{YELLOW}Email or type 'hint': {RESET}")
    if choice.strip().lower() == 'hint':
        hint("Use: theHarvester -d tryhackme.com -b all")
        choice = input(f"{YELLOW}Email: {RESET}")
    if "@tryhackme.com" in choice.lower():
        success("FLAG{email_harvest}")
    else:
        fail()

def ctf4():
    print(f"{CYAN}CTF 4: Port Scan{RESET}")
    print("Find one open port on scanme.nmap.org")
    choice = input(f"{YELLOW}Enter open port or type 'hint': {RESET}")
    if choice.strip().lower() == 'hint':
        hint("Use: nmap scanme.nmap.org")
        choice = input(f"{YELLOW}Port: {RESET}")
    if choice.strip() in ["22", "80"]:
        success("FLAG{open_port}")
    else:
        fail()

def ctf5():
    print(f"{CYAN}CTF 5: NS Records{RESET}")
    print("Give one name server of python.org")
    choice = input(f"{YELLOW}NS record or 'hint': {RESET}")
    if choice.strip().lower() == 'hint':
        hint("Use: nslookup -type=ns python.org")
        choice = input(f"{YELLOW}NS: {RESET}")
    if "ns" in choice.lower() and ".org" in choice.lower():
        success("FLAG{ns_lookup}")
    else:
        fail()

def level2_ctf():
    print(f"\n{CYAN}============= LEVEL 2: RECON CTF ============={RESET}")
    for ctf in [ctf1, ctf2, ctf3, ctf4, ctf5]:
        ctf()
        wait()

    print(f"\n{GREEN}Recon CTF Score: {ctf_score}/5{RESET}")
    print(f"{CYAN}======== 🧠 What You Learned ========{RESET}")
    print(f"{YELLOW}WHOIS:{RESET} Used to find domain registrar info")
    print(f"{YELLOW}DNS Lookup:{RESET} Helps identify infrastructure IPs")
    print(f"{YELLOW}Email Harvesting:{RESET} Can expose employees to phishing")
    print(f"{YELLOW}Port Scanning:{RESET} Reveals services like SSH, HTTP")
    print(f"{YELLOW}NS Records:{RESET} Useful for DNS mapping & hijacking")
    print(f"{CYAN}====================================={RESET}")
    print(f"{GREEN}💡 These are real recon steps used in red teaming & bug bounty!{RESET}")

# ---------- Main ----------
if __name__ == "__main__":
    os.system("clear")
    passed_mcq = level1_mcq()
    if passed_mcq:
        level2_ctf()
