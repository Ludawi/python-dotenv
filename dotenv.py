class GetEnv():
    def __init__(self, key:str):
        self.key = key

        lines = []

        with open('.env', "r") as file:
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
            return str(self.lib[self.key])

lol = GetEnv('HOST')
print(lol)
