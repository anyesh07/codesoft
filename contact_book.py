#!/usr/bin/env python3
import json
import os

DATA_FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []

def save_contacts(contacts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2)

def add_contact(contacts):
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()
    if not name:
        print("Name required.")
        return
    next_id = max((c.get("id", 0) for c in contacts), default=0) + 1
    contacts.append({"id": next_id, "name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    print("Saved.")

def list_contacts(contacts):
    if not contacts:
        print("No contacts.")
        return
    for c in contacts:
        print(f"{c['id']}: {c['name']} - {c.get('phone','')}")

def find_contacts(contacts):
    q = input("Search name or phone: ").strip().lower()
    res = [c for c in contacts if q in c.get("name","").lower() or q in c.get("phone","")]
    if not res:
        print("No results.")
        return
    for c in res:
        print(json.dumps(c, indent=2))

def update_contact(contacts):
    list_contacts(contacts)
    try:
        cid = int(input("Enter id to update: ").strip())
    except:
        print("Invalid id.")
        return
    for c in contacts:
        if c["id"] == cid:
            name = input(f"Name [{c['name']}]: ").strip() or c['name']
            phone = input(f"Phone [{c.get('phone','')}]: ").strip() or c.get('phone','')
            email = input(f"Email [{c.get('email','')}]: ").strip() or c.get('email','')
            address = input(f"Address [{c.get('address','')}]: ").strip() or c.get('address','')
            c.update({"name": name, "phone": phone, "email": email, "address": address})
            save_contacts(contacts)
            print("Updated.")
            return
    print("Not found.")

def delete_contact(contacts):
    list_contacts(contacts)
    try:
        cid = int(input("Enter id to delete: ").strip())
    except:
        print("Invalid id.")
        return contacts
    new = [c for c in contacts if c["id"] != cid]
    if len(new) == len(contacts):
        print("Not found.")
    else:
        save_contacts(new)
        print("Deleted.")
    return new

def menu():
    while True:
        contacts = load_contacts()
        print("\n1) Add  2) List  3) Search  4) Update  5) Delete  6) Exit")
        c = input("> ").strip()
        if c == "1":
            add_contact(contacts)
        elif c == "2":
            list_contacts(contacts)
        elif c == "3":
            find_contacts(contacts)
        elif c == "4":
            update_contact(contacts)
        elif c == "5":
            _ = delete_contact(contacts)
        elif c == "6":
            break
        else:
            print("Unknown choice.")

if __name__ == "__main__":
    menu()
