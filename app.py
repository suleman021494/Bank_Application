import streamlit as st
import pandas as pd

from bank import *

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Smart Banking System",
    page_icon="🏦",
    layout="wide"
)

# ==========================================
# Session State
# ==========================================

if "accounts" not in st.session_state:
    st.session_state.accounts = []

accounts = st.session_state.accounts

# ==========================================
# Title
# ==========================================

st.title("🏦 Smart Banking Management System")

st.write(
    "Manage customer accounts using a simple Streamlit application."
)

# ==========================================
# Sidebar Menu
# ==========================================

menu = st.sidebar.selectbox(

    "Select Operation",

    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "View Account",
        "Calculate Interest",
        "Display All Accounts"
    ]

)

# ==========================================
# Create Account
# ==========================================

if menu == "Create Account":

    st.header("Create New Account")

    account_type = st.selectbox(

        "Account Type",

        [
            "Savings",
            "Current"
        ]

    )

    account_number = st.text_input(
        "Account Number"
    )

    customer_name = st.text_input(
        "Customer Name"
    )

    balance = st.number_input(
        "Opening Balance",
        min_value=0.0
    )

    if account_type == "Savings":

        interest_rate = st.number_input(

            "Interest Rate (%)",

            min_value=0.0

        )

    else:

        overdraft_limit = st.number_input(

            "Overdraft Limit",

            min_value=0.0

        )

    if st.button("Create Account"):

        if account_number == "" or customer_name == "":

            st.error("Please fill all fields.")

        else:

            if search_account(accounts, account_number):

                st.error("Account Number already exists.")

            else:

                if account_type == "Savings":

                    message = create_savings_account(

                        accounts,

                        account_number,

                        customer_name,

                        balance,

                        interest_rate

                    )

                else:

                    message = create_current_account(

                        accounts,

                        account_number,

                        customer_name,

                        balance,

                        overdraft_limit

                    )

                st.success(message)

# ==========================================
# Deposit Money
# ==========================================

elif menu == "Deposit Money":

    st.header("Deposit Money")

    account_number = st.text_input(
        "Account Number"
    )

    amount = st.number_input(

        "Deposit Amount",

        min_value=0.0

    )

    if st.button("Deposit"):

        account = search_account(

            accounts,

            account_number

        )

        if account:

            success, message = account.deposit(amount)

            if success:

                st.success(message)

                st.info(
                    f"Current Balance : ₹{account.get_balance()}"
                )

            else:

                st.error(message)

        else:

            st.error("Account Not Found.")

# ==========================================
# Withdraw Money
# ==========================================

elif menu == "Withdraw Money":

    st.header("Withdraw Money")

    account_number = st.text_input(
        "Account Number"
    )

    amount = st.number_input(

        "Withdrawal Amount",

        min_value=0.0

    )

    if st.button("Withdraw"):

        account = search_account(

            accounts,

            account_number

        )

        if account:

            success, message = account.withdraw(amount)

            if success:

                st.success(message)

                st.info(
                    f"Current Balance : ₹{account.get_balance()}"
                )

            else:

                st.error(message)

        else:

            st.error("Account Not Found.")
            
# ==========================================
# View Account
# ==========================================

elif menu == "View Account":

    st.header("View Account Details")

    account_number = st.text_input(
        "Enter Account Number"
    )

    if st.button("Search"):

        account = search_account(
            accounts,
            account_number
        )

        if account:

            details = account.display_details()

            st.success("Account Found")

            col1, col2 = st.columns(2)

            with col1:

                st.write("### Account Information")

                st.write(
                    f"**Account Number :** {details['Account Number']}"
                )

                st.write(
                    f"**Customer Name :** {details['Customer Name']}"
                )

                st.write(
                    f"**Balance :** ₹{details['Balance']}"
                )

            with col2:

                st.write(
                    f"**Account Type :** {details['Account Type']}"
                )

                if details["Account Type"] == "Savings":

                    st.write(
                        f"**Interest Rate :** {details['Interest Rate']}"
                    )

                else:

                    st.write(
                        f"**Overdraft Limit :** ₹{details['Overdraft Limit']}"
                    )

        else:

            st.error("Account Not Found.")
# ==========================================
# Calculate Interest
# ==========================================

elif menu == "Calculate Interest":

    st.header("Calculate Interest")

    account_number = st.text_input(
        "Enter Account Number"
    )

    if st.button("Calculate"):

        account = search_account(
            accounts,
            account_number
        )

        if account:

            result = account.calculate_interest()

            if isinstance(result, str):

                st.warning(result)

            else:

                st.success(
                    f"Interest Earned : ₹{result}"
                )

        else:

            st.error("Account Not Found.")
# ==========================================
# Display All Accounts
# ==========================================

elif menu == "Display All Accounts":

    st.header("All Customer Accounts")

    all_accounts = get_all_accounts(
        accounts
    )

    if len(all_accounts) == 0:

        st.warning(
            "No Accounts Available."
        )

    else:

        df = pd.DataFrame(
            all_accounts
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        st.success(
            f"Total Accounts : {len(df)}"
        )
