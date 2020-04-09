import subprocess
import pathlib
from Evaluater.Parsers.parse import Parser
from Evaluater.globals.EvaluaterGlobals import LANGUAGES
import os
import re

my_obj = Parser()

io_yaml_abs_path = '/strivio/yaml_files/IO.yaml'


class Evaluater:

    def evaluate(self):
        io_yaml_parsed_dic = my_obj.parse_yaml(io_yaml_abs_path)
        io_dic = my_obj.io_fetcher(io_yaml_parsed_dic)
        language_dic = my_obj.parse_yaml("lang.yaml")
        language = language_dic["language"]
        inputs = io_dic["inputs"]
        outputs = io_dic["outputs"]
        if language:
            if str(language) in LANGUAGES:
                to_check_extension = LANGUAGES[language]
                if language == "python3":
                    file_extension = pathlib.Path(
                        os.path.abspath(
                            "program.py"
                        )
                    ).suffix
                    if file_extension == to_check_extension:
                        case = 1
                        for inp, outp in zip(inputs, outputs):
                            data, temp = os.pipe()
                            os.write(temp, bytes(str(inp), "utf-8"))
                            os.close(temp)
                            output = subprocess.check_output(
                                [
                                    "python3",
                                 os.path.abspath(
                                     "program.py"
                                 )
                                ],
                                stdin=data
                            )
                            output = output.decode("utf-8")
                            output = re.sub('\s+', '', output)
                            outp = re.sub('\s+', '', str(outp))                        
                            if output == outp:
                                print("Test Case " + str(case) + ": Passed")
                                case = case + 1
                            else:
                                raise Exception(
                                    "Test Case " + str(case) + ": Failed"
                                )

                    else:
                        raise Exception(
                            "language in lang.yaml and program file doesnt match"
                        )
                elif language == "cpp":
                    file_extension = pathlib.Path(
                        os.path.abspath(
                            "program.cpp"
                        )
                    ).suffix
                    if file_extension == to_check_extension:
                        subprocess.call(
                            [
                                "g++",
                                "-o",
                                os.path.abspath(
                                    "program"
                                ),
                                os.path.abspath(
                                    "program.cpp"
                                )
                            ]
                        )
                        case = 1
                        for inp, outp in zip(inputs, outputs):
                            data, temp = os.pipe()
                            os.write(temp, bytes(str(inp), "utf-8"))
                            os.close(temp)
                            output = subprocess.check_output(
                                [
                                    os.path.abspath(
                                        "program"
                                    )
                                ],
                                stdin=data
                            )
                            output = output.decode("utf-8")
                            output = re.sub('\s+', '', output)
                            outp = re.sub('\s+', '', str(outp))
                            if output == str(outp):
                                print("Test Case " + str(case) + ": Passed")
                                case = case + 1
                            else:
                                raise Exception(
                                    "Test Case " + str(case) + ": Failed"
                                )

                    else:
                        raise Exception(
                            "language in lang.yaml and program file doesnt match"
                        )
                elif language == "c":
                    file_extension = pathlib.Path(
                        os.path.abspath(
                            "program.c"
                        )
                    ).suffix
                    if file_extension == to_check_extension:
                        subprocess.call(
                            [
                                "gcc",
                                "-o",
                                os.path.abspath(
                                    "program"
                                ),
                                os.path.abspath(
                                    "program.c"
                                )
                            ]
                        )
                        case = 1
                        for inp, outp in zip(inputs, outputs):
                            data, temp = os.pipe()
                            os.write(temp, bytes(str(inp), "utf-8"))
                            os.close(temp)
                            output = subprocess.check_output(
                                [
                                    os.path.abspath("program")
                                ],
                                stdin=data
                            )
                            output = output.decode("utf-8")
                            output = re.sub('\s+', '', output)
                            outp = re.sub('\s+', '', str(outp))
                            if output == str(outp):
                                print("Test Case " + str(case) + ": Passed")
                                case = case + 1
                            else:
                                raise Exception(
                                    "Test Case " + str(case) + ": Failed"
                                )

                    else:
                        raise Exception(
                            "language in lang.yaml and program file doesnt match"
                        )
                elif language == "java":
                    file_extension = pathlib.Path(
                            "program.java"
                    ).suffix
                    if file_extension == to_check_extension:
                        subprocess.call(
                            [
                                "javac",
                                 os.path.abspath("program.java")
                            ]
                        )
                        case = 0
                        for inp, outp in zip(inputs, outputs):
                            data, temp = os.pipe()
                            os.write(temp, bytes(str(inp), "utf-8"))
                            os.close(temp)
                            output = subprocess.check_output(
                                [
                                    "java",
                                    "Main"
                                ],
                                stdin=data
                            )
                            output = output.decode("utf-8")
                            output = re.sub('\s+', '', output)
                            outp = re.sub('\s+', '', str(outp))
                            if output == str(outp):
                                print("Test Case " + str(case) + ": Passed")
                                case = case + 1
                            else:
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
