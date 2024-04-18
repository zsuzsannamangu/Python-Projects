import random

# Define a list of dinosaurs with their details
dinosaurs = [
    {"name": "Tyrannosaurus", "size": "12.3 meters", "diet": "Carnivorous", "period": "Cretaceous", "origin": "North America", "special": "Known for its large size and powerful jaws."},
    {"name": "Stegosaurus", "size": "9 meters", "diet": "Herbivorous", "period": "Jurassic", "origin": "North America, Europe, Asia", "special": "Has distinctive plates along its back and a spiked tail."},
    {"name": "Velociraptor", "size": "2 meters", "diet": "Carnivorous", "period": "Cretaceous", "origin": "Asia", "special": "Known for its intelligence and hunting abilities."},
    {"name": "Triceratops", "size": "9 meters", "diet": "Herbivorous", "period": "Cretaceous", "origin": "North America", "special": "Known for its three horns and large frill."},
    {"name": "Brachiosaurus", "size": "26 meters", "diet": "Herbivorous", "period": "Jurassic", "origin": "North America, Africa", "special": "Has a long neck and a relatively small head."},
    {"name": "Diplodocus", "size": "27 meters", "diet": "Herbivorous", "period": "Jurassic", "origin": "North America, Europe", "special": "Known for its long neck and whip-like tail."},
    {"name": "Ankylosaurus", "size": "6 meters", "diet": "Herbivorous", "period": "Cretaceous", "origin": "North America, Asia", "special": "Has a heavily armored body and a club-like tail."},
    {"name": "Allosaurus", "size": "12 meters", "diet": "Carnivorous", "period": "Jurassic", "origin": "North America, Europe", "special": "A large carnivore with sharp teeth and claws."},
    {"name": "Archaeopteryx", "size": "0.5 meters", "diet": "Carnivorous", "period": "Jurassic", "origin": "Europe", "special": "Considered one of the earliest birds with feathered wings."},
    {"name": "Pteranodon", "size": "7 meters", "diet": "Piscivorous", "period": "Cretaceous", "origin": "North America", "special": "A large flying reptile with a wingspan of up to 7 meters."},
    {"name": "Iguanodon", "size": "10 meters", "diet": "Herbivorous", "period": "Cretaceous", "origin": "Europe", "special": "Known for its thumb spikes and ability to walk on two or four legs."},
    {"name": "Spinosaurus", "size": "15 meters", "diet": "Piscivorous", "period": "Cretaceous", "origin": "Africa", "special": "Has a sail-like structure on its back and is one of the largest carnivorous dinosaurs."},
    {"name": "Carnotaurus", "size": "8 meters", "diet": "Carnivorous", "period": "Cretaceous", "origin": "South America", "special": "Known for its horns and short, deep skull."},
    {"name": "Dilophosaurus", "size": "7 meters", "diet": "Carnivorous", "period": "Jurassic", "origin": "North America", "special": "Has two crests on its head and is featured in popular culture as a spitting dinosaur."},
    {"name": "Brontosaurus", "size": "22 meters", "diet": "Herbivorous", "period": "Jurassic", "origin": "North America", "special": "A large sauropod with a long neck and a relatively small head."},
    {"name": "Deinonychus", "size": "3 meters", "diet": "Carnivorous", "period": "Cretaceous", "origin": "North America", "special": "Known for its sharp claws and agile hunting behavior."},
    {"name": "Parasaurolophus", "size": "9 meters", "diet": "Herbivorous", "period": "Cretaceous", "origin": "North America", "special": "Has a distinctive crest on its head that may have been used for communication."},
    {"name": "Compsognathus", "size": "1 meter", "diet": "Carnivorous", "period": "Jurassic", "origin": "Europe", "special": "A small, agile dinosaur often depicted in groups."},
    {"name": "Oviraptor", "size": "1.8-2.5 meters", "diet": "Omnivorous", "period": "Cretaceous", "origin": "Asia", "special": "Wasn't stealing eggs."},
    {"name": "Coelophysis", "size": "2-3 meters", "diet": "Carnivorous", "period": "Triassic", "origin": "North America", "special": "Wow! It has been to space!"},
    {"name": "Guanlong", "size": "4-5 meters", "diet": "Carnivorous", "period": "Jurassic", "origin": "Asia", "special": "A crowned member of the tyrannosaur family."}
    # Add more dinosaurs here
]

def select_dinosaur():
    return random.choice(dinosaurs)

def display_dinosaur_info(dinosaur):
    print("Guess which dinosaur is this?")
    print(f"{dinosaur['special']}")
    print(f"Body size: {dinosaur['size']} in length.")
    print(f"Diet: {dinosaur['diet']}.")
    print(f"Period of existence: {dinosaur['period']}.")
    print(f"Fossil origin: {dinosaur['origin']}.")
    print(f"Length of the word: {len(dinosaur['name'])}")

def play_game():
    dinosaur = select_dinosaur()
    display_dinosaur_info(dinosaur)

    guesses_left = 5
    guessed_letters = []
    correct_guesses = ['_' for _ in dinosaur['name']] #correct_guesses is a list that initially contains underscores (_) representing the unknown letters in the dinosaur's name.

    while guesses_left > 0:
        guess = input("Enter your guess (a letter or the full dinosaur name): ").strip().capitalize()

        if len(guess) == 1 and guess.isalpha(): #if the guess is one character long = one letter and it is alphabetic
            if guess in guessed_letters: #if guess is in the guessed letters list, so that letter has been guessed already
                print("You've already guessed that letter.")
            else:
                guessed_letters.append(guess) #if that letter hasn't been guessed yet, add that guess to the guessed_letters list
                correct_positions = [i for i, letter in enumerate(dinosaur['name']) if letter == guess] #iterate through the letter of the dinosaur name and if there are any letters that equal the guessed letter
                if correct_positions:
                    print("Correct guess!")
                    for j in correct_positions:
                        correct_guesses[j] = guess #It assigns the guessed letter (guess) to the position (pos) in the correct_guesses list, replacing the underscore (_) at that position.
                    if '_' not in correct_guesses:
                        print("Congratulations! You guessed the dinosaur.")
                        break
                else:
                    print("Wrong guess.")
                    guesses_left -= 1
                    hint_indices = [i for i, letter in enumerate(dinosaur['name']) if letter not in guessed_letters]
                    if hint_indices:
                        hint_index = random.choice(hint_indices)
                        correct_guesses[hint_index] = dinosaur['name'][hint_index]
                        print(f"Hint: The letter '{dinosaur['name'][hint_index]}' is in the dinosaur's name.")
                    else:
                        print("No more hints available.")
                    if guesses_left > 0:
                        print(f"Guesses left: {guesses_left}")
                    else:
                        print("You ran out of guesses.")
        elif guess != dinosaur['name'] and len(guess) > 1:
            print("That's not the right dinosaur.")
            guesses_left -= 1
            if guesses_left > 0:
                print(f"Guesses left: {guesses_left}")
            else:
                print("You ran out of guesses.")
        elif guess == dinosaur['name']:
            print("Congratulations! You guessed the dinosaur.")
            break
        else:
            print("Invalid input. Please enter a single letter or the full dinosaur name.")

        print("Current progress:", ' '.join(correct_guesses))

    if guesses_left == 0:
        print("The dinosaur was:", dinosaur['name'])

# Play the game
play_game()
