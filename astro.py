"""ASTRO - الروبوت الرقمي."""

from commands import process_command


def main():
    print("=" * 40)
    print("ASTRO 🤖 | الروبوت الرقمي")
    print("اكتب 'خروج' لإنهاء البرنامج")
    print("=" * 40)

    while True:
        command = input("أنت: ")

        reply = process_command(command)

        if reply == "__EXIT__":
            print("استرو: إلى اللقاء! 👋")
            break

        print(f"استرو: {reply}")


if __name__ == "__main__":
    main()