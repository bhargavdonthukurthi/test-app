import streamlit as st
from streamlit_option_menu import option_menu

from action_on_transaction import (
    get_transactions_data,
    display_total_debit,
    display_total_credit,
    display_total_debit_opex,
    display_total_credit_income,
    display_total_credit_investment,
    display_pareto_chart,
    display_debit_trend_with_classification_selection,
    display_credit_trend_income,display_net_profit_or_loss,display_transaction_trends
)
# from action_on_daily_menu import display_daily_menu, display_top_runners
# from action_on_procurement import display_procurement
# from action_on_time_entry import editable_employee_grid
# from action_on_stalls_daily_sales import stalls_daily_sales, plot_trend_of_sold_and_leftover_price
# from action_on_whautomate import send_menu_to_contact
# from action_on_bill import bill_entry_by_user
# from action_on_gmail import read_bank_statement
from action_on_recipe import get_recipe
# from action_on_chat_tab import display_chat_tab

st.set_page_config(
    page_title="UKC",
    page_icon="./ukc_logo.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": """
         This website was designed by UKC Backend for the purpose of accessing and analyzing data effectively and conveniently.
        """,
    },
)

# Apply custom CSS for dark theme
st.markdown(
    """
    <style>
        /* Background for the app */
        .block-container {
            background-color: #1e1e1e;
            color: white;
        }

        /* Customize sidebar menu */
        .css-17eq0hr {
            background-color: #000000 !important;  /* Black background */
            color: white !important;
        }

        /* Sidebar navigation link styles */
        .css-1v3fvcr a {
            color: white !important;
        }
        .css-1v3fvcr a:hover {
            background-color: #333333 !important;
        }

        /* Selected menu style */
        .css-1v3fvcr .css-10trblm {
            background-color: #444444 !important;  /* Dark gray for selected */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create a dark-themed icon-based sidebar menu
with st.sidebar:
    tab = option_menu(
        "Navigation",
        ["Home", "Transaction", "Procurement", "Time entry", "Daily Menu", 
         "Stalls Daily Sales", "Menu Message", "Upload bill", 
         "Bank Statement", "Recipe", "Chat"],
        icons=[
            "house", "wallet2", "cart", "clock", "menu-app", 
            "shop", "chat", "cloud-upload", "bank", "book","chat",
        ],
        menu_icon="list",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#000000"},  # Black background
            "icon": {"color": "#00c0f1", "font-size": "20px"},  # Cool blue for icons
            "nav-link": {
                "font-size": "12px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#333333",
                "color": "white",  # White text
            },
            "nav-link-selected": {"background-color": "#444444"},  # Dark gray for selected tab
        },
    )

# Streamlit app title
st.title("UKC Hygiene Foods")

# Handle navigation
if tab == "Transaction":
    get_transactions_data()

elif tab == "Home":
    st.title("P&L")

    # Display total debit and total credit in one row
    col1, col2 = st.columns(2)
    with col1:
        display_total_debit()
    with col2:
        display_total_credit()

    # Line separator
    st.write("---")

    # Display income and OPEX in one row
    col3, col4 = st.columns(2)
    with col3:
        display_total_debit_opex()
    with col4:
        display_total_credit_income()

    # Line separator
    st.write("---")

    # Display investment and PL in one row
    col5, col6 = st.columns(2)
    with col5:
        display_total_credit_investment()
    with col6:
        display_net_profit_or_loss()

    

    # Display additional charts and trends
    st.write("---")
    display_transaction_trends()
    display_pareto_chart()
    display_debit_trend_with_classification_selection()
    display_credit_trend_income()

elif tab == "Procurement":
    display_procurement()

elif tab == "Time entry":
    editable_employee_grid()

elif tab == "Stalls Daily Sales":
    plot_trend_of_sold_and_leftover_price()
    stalls_daily_sales()

elif tab == "Menu Message":
    send_menu_to_contact()

elif tab == "Upload bill":
    bill_entry_by_user()

elif tab == "Daily Menu":
    display_daily_menu()
    display_top_runners()



elif tab == "Recipe":
    get_recipe()


