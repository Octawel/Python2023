def construieste_element_xml(tag, content, **atribute):
    xml = f"<{tag}"

    for cheie, valoare in atribute.items():
        xml += f' {cheie}="{valoare}"'

    xml += f">{content}"

    xml += f"</{tag}>"

    return xml

eticheta = "a"
continut = "Hello there"
atribute = {
    "href": "http://python.org",
    "_class": "my-link",
    "id": "someid"
}

rezultat = construieste_element_xml(eticheta, continut, **atribute)
print(rezultat)
