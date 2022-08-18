"""
    - Language:
        Python 3.X
    
    - Creators:
        This program has beeen created by Mr.Guerziz,
        and implemanted in Python 3 by Jim Pavan.

    - Goal:
        Test if a number is only composed by the same characters.
        (Actually it's not supports floating numbers and negative numbers).
"""


from json import dump
from time import time


class Main:
    def get_number(self, number):
        """Receive the number to test"""

        self.number = number

    def run(self):
        """Evaluate the number.

        if the loop is over and the value is equal to the number
        then the number is a rep_unit."""

        if self.number >= 0:
            set_num = set(str(self.number))
            
            if len(set_num) == 1:
                digit, *other_elements = set_num
                return {"Number": self.number, "Digit": digit}


def data_to_json_file(path, file_name, datas):
    """Create a json file with file datas."""

    file_path = "./" + path + "/" + file_name + ".json"

    with open(file_path, "w") as file:
        dump(
            {
                "start": number_start,
                "range": number_range + 1,
                "step": number_step,
                "exec time": runtime,
                "number of rep unit": number_of_rep_unit,
            },
            file,
            indent=4,
        )
        dump(datas, file, indent=4)


if __name__ == "__main__":
    obj_main = Main()

    rep_unit_list = []
    number_start = 0
    number_range = 1000000
    number_step = 1

    start_time = time()

    for i in range(number_start, number_range, number_step):
        obj_main.get_number(int(i))
        answer = obj_main.run()

        if answer is not None:
            rep_unit_list.append(answer)

    end_time = time()
    runtime = end_time - start_time

    number_of_rep_unit = len(rep_unit_list)

    data_to_json_file("", "Results", rep_unit_list)

    print("-- > The program has finished < --")
