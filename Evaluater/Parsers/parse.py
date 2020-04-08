import yaml


class Parser:

    def parse_yaml(self, file_path):
        with open(file_path, 'r') as stream:
            try:
                data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        print(data)
        return data

    def io_fetcher(self, dic):
        input_dic = dic["inputs"]
        output_dic = dic["outputs"]
        inputs = []
        outputs = []

        for (key1, val1), (key2, val2) in zip(input_dic.items(), output_dic.items()):
            inputs.append(val1)
            outputs.append(val2)
        result_dic = {
            "inputs": inputs,
            "outputs": outputs
        }
        return result_dic



