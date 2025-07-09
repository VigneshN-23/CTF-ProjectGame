#!/usr/bin/env python3
import os
import time

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def banner():
    os.system("clear")
    print(f"{CYAN}========== CTF: TOOL-BASED RECON CHALLENGE =========={RESET}")
    print(f"{YELLOW}Use real cybersecurity tools on Linux to solve each level.{RESET}")
    print("Type your answers carefully. Flags follow this format: FLAG{something}\n")

def hint(msg):
    print(f"{YELLOW}[Hint] {msg}{RESET}")

def success(flag):
    print(f"{GREEN}Correct! {flag}{RESET}\n")

def fail():
    print(f"{RED}Incorrect. Check your tool output and try again.{RESET}\n")

def wait(): time.sleep(1)

# ------------------- CHALLENGES -------------------

def level1():
    print(f"{CYAN}Level 1: WHOIS Recon{RESET}")
    print("Find the registrar name of the domain 'example.com'.")
    choice = input(f"{YELLOW}Enter your answer (or type 'hint'): {RESET}")

    if choice.lower().strip() == 'hint':
        hint("Use: whois example.com | grep Registrar")
        choice = input(f"{YELLOW}Enter your answer: {RESET}")

    if "icann" in choice.lower() or "reserved" in choice.lower():
        success("FLAG{whois_detective}")
        return True
    else:
        fail()
        return False

def level2():
    print(f"{CYAN}Level 2: DNS Subdomain Discovery{RESET}")
    print("What is the IP address of the subdomain 'shopify.com'?")

    choice = input(f"{YELLOW}Enter the A record IP of 'shopify.com' (or type 'hint'): {RESET}")
    if choice.lower().strip() == "hint":
        hint("Use: dig shopify.com +short OR host shopify.com")
        choice = input(f"{YELLOW}Enter IP: {RESET}")

    valid_prefixes = ["23.227.", "151.101."]
    if any(choice.startswith(ip) for ip in valid_prefixes):
        success("FLAG{dns_resolver}")
        return True
    else:
        fail()
        return False

def level3():
    print(f"{CYAN}Level 3: Email Harvesting{RESET}")
    print("Find a publicly available email related to 'tryhackme.com'.")
    choice = input(f"{YELLOW}Enter the email (or type 'hint'): {RESET}")

    if choice.lower().strip() == "hint":
        hint("Try: theHarvester -d tryhackme.com -b all")
        choice = input(f"{YELLOW}Enter email found: {RESET}")

    if "@tryhackme.com" in choice.lower():
        success("FLAG{email_sniper}")
        return True
    else:
        fail()
        return False

def level4():
    print(f"{CYAN}Level 4: Nmap Basic Recon{RESET}")
    print("Find one open port on 'scanme.nmap.org'")
    choice = input(f"{YELLOW}Enter the port number (or type 'hint'): {RESET}")

    if choice.lower().strip() == "hint":
        hint("Use: nmap scanme.nmap.org")
        choice = input(f"{YELLOW}Enter open port: {RESET}")

    valid_ports = ["22", "80"]
    if choice.strip() in valid_ports:
        success("FLAG{port_probe}")
        return True
    else:
        fail()
        return False

def level5():
    print(f"{CYAN}Level 5: NS Lookup Madness{RESET}")
    print("What are the name servers of 'python.org'?")
    choice = input(f"{YELLOW}Enter one NS record (or type 'hint'): {RESET}")

    if choice.lower().strip() == "hint":
        hint("Use: nslookup -type=ns python.org")
        choice = input(f"{YELLOW}Enter NS record: {RESET}")

    if "ns" in choice.lower() and ".org" in choice.lower():
        success("FLAG{ns_lookup_master}")
        return True
    else:
        fail()
        return False

# ------------------- GAME FLOW -------------------

def main():
    banner()
    score = 0
    levels = [level1, level2, level3, level4, level5]

    for i, level in enumerate(levels, 1):
        print(f"{CYAN}--- Challenge {i} ---{RESET}")
        if level():
            score += 1
        wait()

    print(f"\n{GREEN}You solved {score}/{len(levels)} real-world recon challenges!{RESET}")
    if score == len(levels):
        print(f"{GREEN}🏁 You are a true Recon Operator! 🏁{RESET}")
    else:
        print(f"{YELLOW}Practice more with recon tools and try again!{RESET}")

    print(f"\n{CYAN}======== 🧠 What You Learned ========{RESET}")
    print(f"{YELLOW}Level 1 - WHOIS Recon:{RESET} You learned how attackers identify registrar, admin contact, and expiration info — often used in social engineering or takeover attempts.\n")
    print(f"{YELLOW}Level 2 - DNS Discovery:{RESET} DNS lookups help identify subdomains and infrastructure IPs. Used for asset mapping in red teaming.\n")
    print(f"{YELLOW}Level 3 - Email Harvesting:{RESET} Tools like theHarvester automate finding exposed emails that may be used for phishing or brute-force attacks.\n")
    print(f"{YELLOW}Level 4 - Nmap Scanning:{RESET} Port scanning is foundational to finding exposed services and entry points like SSH, HTTP, or databases.\n")
    print(f"{YELLOW}Level 5 - NS Lookup:{RESET} Enumerating nameservers helps understand DNS hosting, which is useful in DNS hijacking or misconfiguration discovery.\n")
    print(f"{CYAN}======================================={RESET}")
    print(f"{GREEN}💡 Tip: Every recon activity you've done mirrors real steps used in bug bounty, red teaming, or cyber threat hunting.{RESET}")

if __name__ == "__main__":
    main()