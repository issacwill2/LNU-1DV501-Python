class MultiDisplay:

    def included(alph_num):
        alph_num.message = ' '
        alph_num.count = 0

    def set_message(alph_num, string):
        alph_num.message = string

    def set_count(alph_num, count):
        alph_num.count = count

    def display(alph_num):
        for i in range(alph_num.count):
            print(alph_num.message)

    def set_display(alph_num, message, count):
        alph_num.message = message
        alph_num.count = count
        for i in range(alph_num.count):
            print(alph_num.message)

    def to_string(alph_num):
        return ("Message: " + alph_num.message + ", " + "Count: "
                + str(alph_num.count))

    def get_message(alph_num):
        return alph_num.message
