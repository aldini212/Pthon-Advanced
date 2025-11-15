contact_info = {
    "Alice": "045-211-231",
    "Bob": "042-412-212"
}

alice_phone =contact_info["Alice"]
print(alice_phone)

contact_info["Alice"] = "046-212-213"
print(contact_info)

contact_info["Eva"] = "045-123-124"
print(contact_info)

del contact_info["Bob"]
print(contact_info)

keys = contact_info.keys()
print(keys)

values = contact_info.values()
print(values)

items = contact_info.items()
print(items)



contact_infromation = {

    "Alice" : {
        "phone_number" : "123-555",
        "email": "alice@gmail.com",
        "birthday": "20/11/2000"
    },

    "bob" : {
        "phone_number" : "122-555",
        "email": "bob@gmail.com",
        "birthday": "21/11/2000"
    }
}
print(contact_infromation)
print(contact_infromation["Bob"])