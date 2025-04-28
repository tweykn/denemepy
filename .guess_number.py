import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    print("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin?")
    
    while True:
        try:
            user_guess = int(input("Tahmininiz: "))
            if user_guess < number_to_guess:
                print("Daha büyük bir sayı dene.")
            elif user_guess > number_to_guess:
                print("Daha küçük bir sayı dene.")
            else:
                print("Tebrikler! Doğru tahmin ettiniz.")
                break
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

if __name__ == "__main__":
    guess_the_number()