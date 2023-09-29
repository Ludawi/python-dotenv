import os
class GetEnv():
    def __init__(self, key:str):
        self.key = key

        lines = []
        filename = '/.env'

        def get_dir(filename):
            path = os.path.dirname(os.path.realpath(__file__))
            filepath = path
            filepath = str(filepath)
            filepath = filepath + filename
            return filepath


        with open(get_dir(filename), "r") as file:
            for line in file:
                line = line.rstrip()
                lines.append(line)


        def create_lookup(env_arr):
            lookup_table = {}
            for item in env_arr:
                separator = item.index('=')
                var = item[:separator]
                value = item[separator+1:]
                value = value.replace("'",'')

                lookup_table[var] = value
            return lookup_table

        self.lib= create_lookup(lines)

    def __str__(self):
        return self.lib[self.key]

print(GetEnv('HOST'))
