from CustomErrors import NotAllowedNumberError, NotInDictError, NotInRangeError


def input_number(prompt, _range=None):
    while True:
        try:
            value = int(input(prompt))
            if _range:
                if value not in _range:
                    raise NotInRangeError
                return value
            # if value < 10 or value >= 100:
            #     raise NotAllowedNumberError
            return value
        except NotInRangeError:
            print("NOT WITHIN THE RANGE\n"
                  f"HINT: your input should be within {_range}")
        except ValueError:
            print("Wrong type\n"
                  "HINT: An integer type of number must be entered")
        except NotAllowedNumberError:
            print("Input is not allowed \n"
                  "HINT: Input value mus be within [10-100) boundary")


def display_options(_dict, question):
    print(question)
    for key, value in _dict.items():
        print(f"{key}: {value}")


def choose_value(_dict):
    while True:
        try:
            value = int(input("-> "))
            if value not in _dict.keys():
                raise NotInDictError
            return value
        except NotInDictError:
            print("Chosen value is not available \n"
                  "HINT: Choose from the displayed options")
        except ValueError:
            print("Wrong type\n"
                  "HINT: An integer type of number must be entered")
