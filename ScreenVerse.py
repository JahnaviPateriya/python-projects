print()
print("✪✪" * 30)
print()
print("       🎬 SCREENVERSE 🍿")
print("     Movies • Web Series ")
print()
print("✪✪" * 30)
print()

print("👋 Welcome to ScreenVerse!")
print("=" * 30)

your_name = input("Enter your name: ").title().strip()

print("\n📂 Choose a Category")
entertainments = [
    "🎥 Movies",
    "📺 Web Series"
]

print("=" * 30)
print("1.", entertainments[0])
print("2.", entertainments[1])

choice = int(input("Enter your choice (1/2): "))

# ---------------- MOVIES ----------------

if choice == 1:

    print("=" * 30)
    print("\n🎥 MOVIES")

    movies = [
        "12 Angry Men",
        "The Man from Earth",
        "Interstellar",
        "Leave the World Behind",
        "Carry-On"
    ]

    print("1.", movies[0])
    print("2.", movies[1])
    print("3.", movies[2])
    print("4.", movies[3])
    print("5.", movies[4])

    print("=" * 30)

    movie_choice = int(input("Choose a movie (1-5): "))

    selected_movie = movies[movie_choice - 1]

    print("-" * 30)
    print("🍿 Excellent Choice!")
    print("You selected:", selected_movie)
    print("-" * 30)

    num_tickets = int(input("How many tickets would you like? 🎟 "))

    print("🔍 Checking availability...")
    print("💺 Reserving your seats...")
    print("🎟 Printing your ticket...")

    print()
    print("════════════════════════════════════════════════════")
    print("                 ✨ SCREENVERSE ✨")
    print("════════════════════════════════════════════════════")
    print(f"👤 Customer : {your_name}")
    print(f"🎬 Movie    : {selected_movie}")
    print(f"🎟 Tickets  : {num_tickets}")
    print("════════════════════════════════════════════════════")
    print("🍿 Sit Back • Relax • Enjoy the Show 🍿")
    print("════════════════════════════════════════════════════")

# ---------------- WEB SERIES ----------------

elif choice == 2:

    print("=" * 30)
    print("\n📺 WEB SERIES")

    series = [
        "AGGGTM",
        "I Will Find You",
        "Safe",
        "The Stranger",
        "The Watcher",
        "Fool Me Once"
    ]

    print("1.", series[0])
    print("2.", series[1])
    print("3.", series[2])
    print("4.", series[3])
    print("5.", series[4])
    print("6.", series[5])

    print("=" * 30)

    series_choice = int(input("Choose a web series (1-6): "))

    selected_series = series[series_choice - 1]

    print("-" * 30)
    print("🍿 Excellent Choice!")
    print("You selected:", selected_series)
    print("-" * 30)

    num_tickets = int(input("How many tickets would you like? 🎟 "))

    print("🔍 Checking availability...")
    print("💺 Reserving your seats...")
    print("🎟 Printing your ticket...")

    print()
    print("════════════════════════════════════════════════════")
    print("                 ✨ SCREENVERSE ✨")
    print("════════════════════════════════════════════════════")
    print(f"👤 Customer : {your_name}")
    print(f"📺 Series   : {selected_series}")
    print(f"🎟 Tickets  : {num_tickets}")
    print("════════════════════════════════════════════════════")
    print("🍿 Happy Binge Watching! 📺")
    print("════════════════════════════════════════════════════")

# ---------------- INVALID CHOICE ----------------

else:
    print("❌ Invalid choice. Please restart the program.")