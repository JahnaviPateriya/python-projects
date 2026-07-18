import os

def clear():
    input("\nPress ENTER to begin investigation...")
    if os.name == "nt" :
        os.system("cls") #Windows
    else:
        os.system("clear") #macOS & Linux

print("═"*55)
print("        🕵️  THE LAST ALIBI 📜")
print("     Criminal Investigation Unit (CIU)")
print("═"*55)
clear()
print()
print()
print("📂 Loading Case Files...")
print("█████████████████████████████████████ 100%")
print()
print("🔐 Establishing Secure Connection...")
print("✅ Connection Successful")
print()
name = input("Your name :").strip().title()
print("👤 Detective :" , name)

print(""" 
      📁 Case ID      : #404
      📍 Location     : Blackwood Manor
      🧑 Victim       : Edward Blackwood
      🚨 Case Status  : OPEN
      ⚠️  Priority     : HIGH """)
print()
print("═"*55)
print()
print("🩸 INCIDENT REPORT")
print()
print(""" 
      At exactly 10:35 PM ,
      Edward Blackwood was found dead inside 
      his private library .""")
print()
print(""" 
      🚪 No forced entry.
      🩸 One fatal stab wound.
      🕰️ Clock stopped at 10:35 PM.""")
print()
print("Only FOUR people were inside the mansion.")
print()
print("One of them is lying.")
print()
print("Can you solve the mystery?")
print()
print("═"*55)
print()
clear()

def menu() :
    print()
    print("▣"*25)
    print("🕵️ INVESTIGATION MENU")
    print("▣"*25)
    print()
    print("""
      1️⃣  🔎 Examine Crime Scene
      2️⃣  👤 Suspect Database 🖥️🗂️
      3️⃣  📂 View Evidence Locker
      4️⃣  📜 Read Autopsy Report
      5️⃣  📖 Detective Notebook
      6️⃣  ⚖️ Accuse the Killer
      7️⃣  🚪 Exit Investigation """)

def next_page():
    input("\nPress Enter To Return Back to Menu...")
    if os.name == "nt" :
        os.system("cls") #Windows
    else:
        os.system("clear") #macOS & Linux

def innocent():
     print("""
❌ WRONG ACCUSATION

🚨 The real killer escaped.

⚠️ Evidence was insufficient.

📂 Case Status :
UNSOLVED

Better luck next time,
Detective.""")

# Main Game Loop
game_running = True
while game_running:
    menu()
    choice = input("Enter choice :").strip() # Kept as string to prevent crashes on letters

    if choice == "1":
        print("◆"*30)
        print("🔎 CRIME SCENE REPORT")
        print("◆"*30)
        print ("""
📍 Location :
Private Library

🩸 Blood found near fireplace.
               
👞 Muddy footprints lead towards the garden door.

📷 Security camera disconnected exactly at 10:28 PM.

🗡️ Murder weapon missing.

📄 Torn family photograph.

🕰️ Clock stopped at 10:35 PM. """)
        print()
        print("◆"*30)
        next_page()
        
    elif choice == "2":
        print("◆"*30)
        print("👤 Suspect Database 🖥️🗂️")
        print("◆"*30)
        print()
        print("""
1️⃣ Amelia Blackwood
────────────────────────
👩 Relationship :
Victim's Wife

💰 Motive :
Standing to inherit the entire family estate.

📜 Alibi :
"I was reading upstairs."
              
🔍 Evidence:
Her fingerprints are found only upstairs.

⚠️ Suspicion :
HIGH """)
        print()
        print("◆"*30)
        print()
        print("""
2️⃣ Victor Hayes
────────────────────────
👨 Relationship :
Business Partner

💼 Motive :
Financial dispute

📞 Alibi:
"I was outside talking on my phone."

⚠ Witness:
No one saw him outside.
              
📵 Phone records:
No outgoing calls between 10:20–10:45 PM.

⚠️ Suspicion :
MEDIUM """)
        print()
        print("◆"*30)
        print()
        print("""
3️⃣ Olivia Carter
────────────────────────
👩 Relationship :
Housekeeper

🍽️ Alibi :
Preparing dinner.
              
🔍 Evidence:
Kitchen staff confirms it.

⚠️ Suspicion :
LOW""")
        print()
        print("◆"*30)
        print()
        print("""
4️⃣ Daniel Blackwood
────────────────────────
👨 Relationship :
Victim's Son
              
🎰 Motive  :
Ongoing gambling debts.
              
📺 Alibi :
Watching television.
              
🔍 Evidence:
TV was still ON.

⚠️ Suspicion :
MEDIUM""")
        print()
        print("◆"*30)
        next_page()

    elif choice == "3":
        print("Verifying your identity...")
        user_id = input("Enter the first 3 letters of your name:")
        print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 100%")
        print(f"✔ Verified: Clear for Agent {user_id.upper()}")
        print()
        print("◆"*30)
        print("📂 EVIDENCE LOCKER 🔑 ")
        print("◆"*30)
        print()
        print("""
🗡️ Blood-Stained Letter Opener
✅ Collected

────────────────────────────

📷 Broken Security Camera
⚠️ Damaged

────────────────────────────

📱 Victim's Phone
🔓 Decrypted Message:
"Victor... We need to talk. Tonight."

────────────────────────────

🧬 Fingerprints
Victim ✔ | Victor ✔ | Unknown ❌

────────────────────────────

📄 Torn Photograph
📌 Important Evidence

────────────────────────────

🔑 Rusty Key
❓ Unknown Purpose """)
        print()
        print("◆"*30)
        next_page()

    elif choice == "4":
         print("◆"*30)
         print("📜 AUTOPSY REPORT ")
         print("◆"*30)
         print()
         print()
         print("""
👤 Victim :
Edward Blackwood

🎂 Age :
58

🩸 Cause of Death :
Single stab wound.

🕰️ Estimated Time :
10:35 PM

🧪 Toxicology :
Negative

🛡️ Defensive Wounds :
None
               
☕ Victim had coffee 5 minutes before death.

📌 Conclusion :
Victim most likely knew his attacker.""")
         print()
         print("◆"*30)
         next_page()

    elif choice == "5":
         print("◆"*30)
         print("📖 DETECTIVE NOTEBOOK")
         print("◆"*30)
         print()
         print("""
✔ Victim knew killer.

✔ No forced entry.

✔ Murder weapon missing.

✔ Fingerprints recovered.

✔ Victor's alibi cannot be verified.

✔ Phone records contradict Victor's statement.
""")
         print()
         print("◆"*30)
         next_page()
         
    elif choice == "6":
         print("◆"*30)
         print("⚖️ FINAL DECISION")
         print("◆"*30)
         print()
         print("WHO DO YOU BELIEVE IS THE KILLER?")
         print("""
1️⃣ Amelia Blackwood

2️⃣ Victor Hayes

3️⃣ Olivia Carter

4️⃣ Daniel Blackwood""")
         killer = input("Enter Choice(1/2/3/4) :").strip()
         print()
         
         case_result = "UNSOLVED"
         case_accuracy = "Investigation Failed"

         if killer == "1":
              innocent()
         elif killer == "3":
              innocent()
         elif killer == "4":
              innocent()
         elif killer == "2":
              case_result = "CASE SOLVED"
              case_accuracy = "100%"
              print("""
══════════════════════════════════════════

🧬 Cross-checking DNA...
██████████████████ 100%

🔍 Matching Fingerprints...
██████████████████ 100%

📜 Verifying Statements...
██████████████████ 100%

══════════════════════════════════════════

🎉 CASE CLOSED

🏆 Congratulations Detective!

👮 Victor Hayes has been arrested.

💰 Motive :
To hide a $12 Million fraud.

🗡️ Murder Weapon :
Recovered.

⚖️ Justice Served.
🎉 CASE CLOSED!

══════════════════════════════════════════""")
         
         print()
         input("Press Enter to view INVESTIGATION SUMMARY...")
         print()
         print()
         print("""
+++++++++++++++++++++++++++++++++++++++++++    
      📊 INVESTIGATION SUMMARY     
+++++++++++++++++++++++++++++++++++++++++++  
""")
         print()
         print()
         print("👤 Detective :" , name)
         print(f"""
📁 Case ID   : #404
🏆 Result    : {case_result}
⭐ Accuracy  : {case_accuracy}
""")
         print("+" * 45)
         print()
         print("🔄 Play Again?")
         print("""
1️⃣ Yes
2️⃣ No""")
         play = input("⟹ Your choice (1/2) : ")
         if play == "1" :
              clear()
         elif play == "2" :
              print("\n👋 Thank you for playing THE LAST ALIBI!")
              print("Stay sharp, Detective.")
              game_running = False

    elif choice == "7":
        print("\n👋 Thank you for playing THE LAST ALIBI!")
        print("Stay sharp, Detective.")
        game_running = False
        
    else:
        print("❌ Invalid Choice! Please choose an option from 1 to 7.")