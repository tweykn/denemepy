import random

def guess_the_number():
    while True:
        number_to_guess = random.randint(1, 100)
        print("\n1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin?")
        
        guess_count = 0

        while True:
            try:
                user_guess = int(input("Tahmininiz: "))
                guess_count += 1
                if user_guess < number_to_guess:
                    print("Daha büyük bir sayı dene.")
                elif user_guess > number_to_guess:
                    print("Daha küçük bir sayı dene.")
                else:
                    print(f"Tebrikler! {guess_count} denemede doğru tahmin ettiniz! 🎉")
                    break
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")

        play_again = input("Tekrar oynamak ister misin? (E/H): ").strip().lower()
        if play_again != 'e':
            print("Görüşmek üzere! 👋")
            break

if __name__ == "__main__":
    guess_the_number()
