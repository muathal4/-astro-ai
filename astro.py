"""ASTRO - أول نسخة من الروبوت الرقمي."""


def respond(command: str) -> str:
    """يعطي استرو ردًا بسيطًا على بعض الأوامر العربية."""
    text = command.strip().lower()

    if text in {"مرحبا", "هلا", "السلام عليكم"}:
        return "وعليكم السلام! أنا استرو 🤖"

    if "اسمك" in text:
        return "اسمي استرو 🤖"

    if "كيف حالك" in text:
        return "بخير! وجاهز للأوامر 🚀"

    if text in {"خروج", "exit", "quit"}:
        return "__EXIT__"

    return "ما فهمت الأمر حتى الآن، لكن بنتعلم أكثر قريبًا!"


def main() -> None:
    print("=" * 40)
    print("ASTRO 🤖 | الروبوت الرقمي")
    print("اكتب 'خروج' لإنهاء البرنامج")
    print("=" * 40)

    while True:
        command = input("أنت: ")
        reply = respond(command)

        if reply == "__EXIT__":
            print("استرو: إلى اللقاء! 👋")
            break

        print(f"استرو: {reply}")


if __name__ == "__main__":
    main()