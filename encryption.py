import string
import random

class Encryption:
    def __init__(self, seed):
        # set a random seed
        random.seed(seed)
        self.seed = seed

        # Create an empty string attribute to hold the encrypted phrase
        self.encrypted_phrase = ""

        # Create correct attribute and another suffle attribute
        self.true_alphabet = list(string.ascii_lowercase)
        self.random_alphabet = random.sample(
            self.true_alphabet, len(self.true_alphabet)
        )

    def encryption(self, message):
        output = ""

        # Replace every other letter with a random number
        for i in range(len(message)):
            output += message[i]
            # it grabs 1 letter from true_alphabet, since random() returns a list, grab element at index 0
            output += random.sample(self.true_alphabet, 1)[0]

        # Reverse the string
        self.encrypted_phrase = output[::-1]

        # Use the random shuffled alphabet  for a Ceaser Cipher
        encryption_phase_two = list(range(len(self.encrypted_phrase)))

        for i, letter in enumerate(self.encrypted_phrase.lower()):
            if letter in self.true_alphabet:
                index = self.true_alphabet.index(letter)
                encryption_phase_two[i] = self.random_alphabet[index]
            else:
                # Grabs spaces and other letters
                encryption_phase_two[i] = letter

        self.encrypted_phrase = "".join(encryption_phase_two)

        return self.encrypted_phrase

    def decryption(self, message, seed):
        random.seed(seed)

        session_rand_alphabet = random.sample(
            self.true_alphabet, len(self.true_alphabet)
        )
        decrypted_message = list(range(len(message)))

        for i, letter in enumerate(message.lower()):
            if letter in self.true_alphabet:
                index = session_rand_alphabet.index(letter)
                decrypted_message[i] = self.true_alphabet[index]
            else:
                decrypted_message[i] = letter

        decrypted_message = "".join(decrypted_message)[::-1]  # Reverse the string

        return decrypted_message[::2]  # grab the letter at every other position


encrypt = Encryption(20)

encrypted_msg = encrypt.encryption("hello world")
print("encrypted message:", encrypted_msg)

original_msg = encrypt.decryption(encrypted_msg, 20)
print("original message after decryption:", original_msg)

