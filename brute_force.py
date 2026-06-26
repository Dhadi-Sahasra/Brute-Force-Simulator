import itertools
import string
import time

def brute_force(target_password):

    characters = string.ascii_lowercase + string.digits

    attempts = 0

    start_time = time.time()

    for length in range(1, len(target_password) + 1):

        for guess in itertools.product(characters, repeat=length):

            attempts += 1

            guess = ''.join(guess)

            if guess == target_password:

                end_time = time.time()

                return {
                    "password": guess,
                    "attempts": attempts,
                    "time_taken": round(end_time - start_time, 3)
                }

    return {
        "password": "Not Found",
        "attempts": attempts,
        "time_taken": round(time.time() - start_time, 3)
    }