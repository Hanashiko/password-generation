from random import choice

def generate_password(length: int = 8) -> str:
  symbols: str = "abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ0123456789!@#$%^&*()-_=+{}[]|\\;:'\",.<>/?"
  password: str = ""
  for _ in range(length):
    password += choice(symbols)
  return password

def main() -> None:
	length: int = int(input("Введіть довжину пароля: "))
	password: str = generate_password(length)
	print(f"Згенерований пароль: {password}")

if __name__ == "__main__":
	main()
