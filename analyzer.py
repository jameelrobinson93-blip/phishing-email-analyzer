import re

# Read the sample email
with open("sample_email.txt", "r") as file:
    email = file.read()

print("=" * 40)
print("PHISHING EMAIL ANALYZER")
print("=" * 40)

score = 0

# Detect urgent language
urgent_words = ["urgent", "immediately", "verify", "suspended", "compromised"]

for word in urgent_words:
    if word in email.lower():
        print(f"Urgent keyword detected: {word}")
        score += 1

# Detect suspicious links
links = re.findall(r'http[s]?://\S+', email)

if links:
    print("\nSuspicious Links:")
    for link in links:
        print("-", link)
        score += 1

# Detect executable attachments
if ".exe" in email.lower():
    print("\nExecutable attachment detected")
    score += 1

# Display sender
sender = re.search(r'From:\s*(.*)', email)

if sender:
    print("\nSender:")
    print(sender.group(1))

print("\nRisk Score:", score)

if score >= 3:
    print("HIGH RISK PHISHING EMAIL")
elif score == 2:
    print("MEDIUM RISK")
else:
    print("LOW RISK")
