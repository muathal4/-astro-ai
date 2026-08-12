"""أوامر ASTRO الأساسية."""

from datetime import datetime
import ast
import operator


# العمليات الحسابية المسموحة فقط
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
}


def calculate(expression: str):
    """يحسب عملية رياضية بسيطة وآمنة."""
    try:
        tree = ast.parse(expression, mode="eval")
        return _evaluate(tree.body)
    except (ValueError, TypeError, ZeroDivisionError, SyntaxError):
        return None


def _evaluate(node):
    """تقييم العمليات الرياضية المسموحة فقط."""
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.UnaryOp) and type(node.op) in OPERATORS:
        return OPERATORS[type(node.op)](_evaluate(node.operand))

    if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
        left = _evaluate(node.left)
        right = _evaluate(node.right)
        return OPERATORS[type(node.op)](left, right)

    raise ValueError("عملية غير مسموحة")


def get_time() -> str:
    """إرجاع الوقت الحالي."""
    return datetime.now().strftime("%H:%M:%S")


def get_date() -> str:
    """إرجاع التاريخ الحالي."""
    return datetime.now().strftime("%Y-%m-%d")


def process_command(command: str) -> str:
    """معالجة أوامر ASTRO."""
    text = command.strip().lower()

    # الوقت
    if "الوقت" in text or "الساعة" in text:
        return f"الوقت الآن: {get_time()} ⏰"

    # التاريخ
    if "التاريخ" in text or "اليوم" in text:
        return f"تاريخ اليوم: {get_date()} 📅"

    # معلومات عن استرو
    if "من أنت" in text or "وش أنت" in text or "ما أنت" in text:
        return "أنا ASTRO 🤖، روبوت رقمي يتم تطويره باستخدام Python."

    # تحية
    if text in {"هلا", "مرحبا", "السلام عليكم", "أهلين"}:
        return "أهلًا! أنا استرو 🤖 كيف أقدر أساعدك؟"

    # حساب
    if text.startswith("احسب "):
        expression = text[5:].strip()
        result = calculate(expression)

        if result is None:
            return "ما قدرت أحسبها 🤔 تأكد أن العملية مثل: احسب 5 + 3"

        return f"الناتج = {result} 🧮"

    # خروج
    if text in {"خروج", "انهاء", "إنهاء", "exit", "quit"}:
        return "__EXIT__"

    return "ما فهمت الأمر 🤔 جرب: الوقت، التاريخ، من أنت، أو احسب 5 + 3"


if __name__ == "__main__":
    print("ASTRO Commands Module 🤖")
    print("الوحدة جاهزة للعمل.")