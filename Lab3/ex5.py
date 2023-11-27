def validate_dict(rules, dictionar):
    for cheie, prefix, middle, suffix in rules:
        if cheie in dictionar:
            valoare = dictionar[cheie]
            if (prefix == "" or valoare.startswith(prefix)) and (suffix == "" or valoare.endswith(suffix)):
                index_middle = valoare.find(middle)
                if index_middle != -1 and index_middle > len(prefix) and index_middle < len(valoare) - len(suffix) - 1:
                    continue 
                else:
                    return False
            else:
                return False
    return True

reguli = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
dictionar = {
    "key1": "come inside, it's too cold out",
    "key3": "this is not valid"
}

rezultat = validate_dict(reguli, dictionar)
print(rezultat)
