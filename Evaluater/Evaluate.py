import subprocess
import pathlib
from Parsers.parse import Parser
from globals.EvaluaterGlobals import LANGUAGES
import os

my_obj = Parser()
path = os.path.dirname(os.getcwd())
io_yaml_abs_path = str(path) + '/yaml_files/IO.yaml'


class Evaluater:

    def evaluate(self):
        io_yaml_parsed_dic = my_obj.parse_yaml(io_yaml_abs_path)
        io_dic = my_obj.io_fetcher(io_yaml_parsed_dic)
        language_dic = my_obj.parse_yaml("code/lang.yaml")
        language = language_dic["language"]
        inputs = io_dic["inputs"]
        outputs = io_dic["outputs"]
        if language:
            if str(language) in LANGUAGES:
                to_check_extension = LANGUAGES[language]
                if language == "python3":
                    file_extension = pathlib.Path('code/program.py').suffix
                    if file_extension == to_check_extension:
                        case = 1
                        for inp, outp in zip(inputs, outputs):
                            data, temp = os.pipe()
                            os.write(temp, bytes(str(inp)+"\n", "utf-8"))
                            os.close(temp)
                            output = subprocess.check_output(["python3", "code/program.py"], stdin = data)
                            output = output.decode("utf-8")
                            output = output.strip('\n')

                            print(output == str(outp))
                            if output == str(outp):
                                print("Test Case " + str(case) + ": Passed")
                                case = case + 1
                            else:
                                case = case + 1
                                raise Exception(
                                    "Test Case " + str(case) + ": Failed"
                                )
                    else:
                        raise Exception(
                            "language in lang.yaml and program file doesnt match"
                        )
                elif language == "cpp":
                    file_extension = pathlib.Path('code/program.cpp').suffix
                    if file_extension == to_check_extension:
                        subprocess.call(["g++", "-o", "code/program", "code/program.cpp"])
                        case = 1
                        for inp, outp in zip(inputs, outputs):
                            data, temp = os.pipe()
                            os.write(temp, bytes(str(inp)+"\n", "utf-8"))
                            os.close(temp)
                            output = subprocess.check_output(["code/program"], stdin=data)
                            output = output.decode("utf-8")
                            output = output.strip('\n')
                            if output == str(outp):
                                print("Test Case " + str(case) + ": Passed")
                                case = case + 1
                            else:
                                case = case + 1
                                raise Exception(
                                    "Test Case " + str(case) + ": Failed"
                                )
                    else:
                        raise Exception(
                            "language in lang.yaml and program file doesnt match"
                        )
                elif language == "c":
                    file_extension = pathlib.Path('code/program.c').suffix
                    if file_extension == to_check_extension:
                        subprocess.call(["gcc", "-o", "code/program", "code/program.c"])
                        case = 1
                        for inp, outp in zip(inputs, outputs):
                            data, temp = os.pipe()
                            os.write(temp, bytes(str(inp)+"\n", "utf-8"))
                            os.close(temp)
                            output = subprocess.check_output(["code/program"], stdin=data)
                            output = output.decode("utf-8")
                            output = output.strip('\n')
                            if output == str(outp):
                                print("Test Case " + str(case) + ": Passed")
                                case = case + 1
                            else:
                                case = case + 1
                                raise Exception(
                                    "Test Case " + str(case) + ": Failed"
                                )
                    else:
                        raise Exception(
                            "language in lang.yaml and program file doesnt match"
                        )
                elif language == "java":
                    file_extension = pathlib.Path('code/Program.java').suffix
                    if file_extension == to_check_extension:
                        subprocess.call(["javac", "code/Program.java"])
                        case = 0
                        for inp, outp in zip(inputs, outputs):
                            data, temp = os.pipe()
                            os.write(temp, bytes(str(inp)+"\n", "utf-8"))
                            os.close(temp)
                            output = subprocess.check_output(["java", "code.Program"], stdin=data)
                            output = output.decode("utf-8")
                            output = output.strip('\n')
                            if output == str(outp):
                                print("Test Case " + str(case) + ": Passed")
                                case = case + 1
                            else:
                                case = case + 1
                                raise Exception(
                                    "Test Case " + str(case) + ": Failed"
                                )
                    else:
                        raise Exception(
                            "language in lang.yaml and program file doesnt match"
                        )
                else:
                    raise Exception(
                        "Not supported language in lang.yaml"
                    )

            else:
                raise Exception(
                    "Not supported language in lang.yaml"
                )
        else:
            raise Exception(
                "lang.yaml not found"
            )
if __name__ == '__main__':
    eval_obj = Evaluater()
    eval_obj.evaluate()
