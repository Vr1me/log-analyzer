# --- Functions practice ---

def get_even_numbers(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n % 2 == 0]


def greet(name: str) -> str:
    return f"Hello, {name}"


def calculate_total(price: float, tax: float = 0.19) -> float:
    return price * (1 + tax)


# --- Dict practice ---

user = {"name": "Alex", "age": 20}
user["city"] = "Berlin"

if "email" not in user:
    user["email"] = "not_provided"

print(user)

# --- File practice ---

def count_lines(filepath: str) -> int:
    with open(filepath, "r") as f:
        return len(f.readlines())
    
def count_lines(filepath: str) -> int:
    with open(filepath, "r") as f:
        return len(f.readlines())