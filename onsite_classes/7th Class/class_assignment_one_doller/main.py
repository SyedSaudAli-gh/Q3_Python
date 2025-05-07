import streamlit as st
import random
import json
import os

# -------------------- Account Class --------------------
class Account:
    def __init__(self, acc_number, name, password, balance=0.0):
        self.acc_number = acc_number
        self.name = name
        self.__password = password
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}"

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient balance."
        self.__balance -= amount
        return f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}"

    def check_balance(self, password):
        if password == self.__password:
            return f"Current balance: ${self.__balance:.2f}"
        else:
            return "Incorrect password."

    def transfer(self, target_account, amount, password):
        if password != self.__password:
            return "Incorrect password."
        if amount > self.__balance:
            return "Insufficient funds."
        self.__balance -= amount
        target_account.__balance += amount
        return f"Transferred ${amount:.2f} to {target_account.name} (Acc#: {target_account.acc_number})"

    def to_dict(self):
        return {
            "acc_number": self.acc_number,
            "name": self.name,
            "password": self.__password,
            "balance": self.__balance
        }

    @staticmethod
    def from_dict(data):
        return Account(
            acc_number=data["acc_number"],
            name=data["name"],
            password=data["password"],
            balance=data["balance"]
        )


# -------------------- Data Persistence --------------------
DATA_FILE = "accounts.json"

def save_data(accounts):
    data = {str(acc.acc_number): acc.to_dict() for acc in accounts.values()}
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
                valid_data = {}
                for k, v in data.items():
                    if all(key in v for key in ["acc_number", "name", "password", "balance"]):
                        valid_data[int(k)] = Account.from_dict(v)
                return valid_data
            except json.JSONDecodeError:
                st.error("Failed to load accounts.json — it might be corrupted.")
    return {}



# -------------------- Bank Class --------------------
class Bank:
    def __init__(self):
        self.accounts = load_data()

    def create_account(self, name, password, deposit):
        for acc in self.accounts.values():
            if acc.name.lower() == name.lower():
                return None, acc.acc_number
        acc_number = random.randint(10000, 99999)
        while acc_number in self.accounts:
            acc_number = random.randint(10000, 99999)
        self.accounts[acc_number] = Account(acc_number, name, password, deposit)
        save_data(self.accounts)
        return acc_number, None

    def get_account(self, acc_number):
        return self.accounts.get(acc_number)


# -------------------- Streamlit App --------------------
if 'bank' not in st.session_state:
    st.session_state.bank = Bank()

if 'is_logged_in' not in st.session_state:
    st.session_state.is_logged_in = False

if 'logged_in_user' not in st.session_state:
    st.session_state.logged_in_user = None

if 'created_acc_number' not in st.session_state:
    st.session_state.created_acc_number = None

st.title("\U0001F3E6 SSD Banking System")

# -------------------- Sidebar Login/Logout --------------------
if not st.session_state.is_logged_in:
    st.sidebar.subheader("🔐 Login")
    name = st.sidebar.text_input("Name")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        for acc in st.session_state.bank.accounts.values():
            if acc.name.lower() == name.lower() and acc._Account__password == password:
                st.session_state.is_logged_in = True
                st.session_state.logged_in_user = acc
                st.sidebar.success(f"Welcome back, {acc.name}!")
                break
        else:
            st.sidebar.error("Invalid username or password.")
else:
    st.sidebar.success(f"Logged in as: {st.session_state.logged_in_user.name}")
    if st.sidebar.button("Logout"):
        st.session_state.is_logged_in = False
        st.session_state.logged_in_user = None
        st.experimental_rerun()

# -------------------- Main Area --------------------
if not st.session_state.is_logged_in:
    st.subheader("Don't have an account? Create one below:")
    new_name = st.text_input("Enter your name")
    new_pass = st.text_input("Set a password", type="password")
    new_dep = st.number_input("Initial deposit", min_value=0.00)
    if st.button("Create Account"):
        if new_name and new_pass:
            acc_no, existing = st.session_state.bank.create_account(new_name, new_pass, new_dep)
            if existing:
                st.warning(f"User already exists. Account Number: `{existing}`")
                st.session_state.created_acc_number = existing
            else:
                st.success(f"Account created! Your account number is: `{acc_no}`")
                st.session_state.created_acc_number = acc_no
        else:
            st.warning("Please fill in all fields.")
else:
    acc = st.session_state.logged_in_user
    st.subheader(f"Hello, {acc.name} (Acc#: {acc.acc_number})")
    option = st.radio("Choose an option", ["Check Balance", "Deposit", "Withdraw", "Transfer"])

    if option == "Check Balance":
        st.info(acc.check_balance(acc._Account__password))

    elif option == "Deposit":
        amount = st.number_input("Amount to deposit", min_value=10.0)
        if st.button("Deposit"):
            st.success(acc.deposit(amount))
            save_data(st.session_state.bank.accounts)

    elif option == "Withdraw":
        amount = st.number_input("Amount to withdraw", min_value=10.0)
        if st.button("Withdraw"):
            st.success(acc.withdraw(amount))
            save_data(st.session_state.bank.accounts)

    elif option == "Transfer":
        target = st.number_input("Recipient account number", step=1)
        amount = st.number_input("Amount to transfer", min_value=10.0)
        if st.button("Transfer"):
            recipient = st.session_state.bank.get_account(target)
            if recipient:
                st.success(acc.transfer(recipient, amount, acc._Account__password))
                save_data(st.session_state.bank.accounts)
            else:
                st.error("Recipient account not found.")

st.markdown("---")
st.markdown("📌 **Built with ❤️ using Streamlit** | Developed by SYED SAUD ALI")