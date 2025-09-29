import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/yaul149/bike-dashboard/main/gabungan_bike_sharing.csv"
df = pd.read_csv(url)


df['dteday'] = pd.to_datetime(df['dteday'])


st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Start Date", df['dteday'].min())
end_date = st.sidebar.date_input("End Date", df['dteday'].max())

filtered_df = df[(df['dteday'] >= str(start_date)) & (df['dteday'] <= str(end_date))]


tab1, tab2, tab3, tab4 = st.tabs(["📊 Customers", "📦 Orders", "💰 Sales", "🏷️ Products"])


with tab1:
    st.subheader("Customers Overview")
    st.write("Data Customers (Casual & Registered)")
    st.line_chart(filtered_df[['dteday','casual','registered']].set_index('dteday'))

    st.metric("Total Casual", filtered_df['casual'].sum())
    st.metric("Total Registered", filtered_df['registered'].sum())

with tab2:
    st.subheader("Orders Overview")
    st.write("Jumlah order total (Casual + Registered)")
    filtered_df['total_orders'] = filtered_df['casual'] + filtered_df['registered']
    st.area_chart(filtered_df[['dteday','total_orders']].set_index('dteday'))

with tab3:
    st.subheader("Sales Overview")
    st.write("Total Sales Harian")
    st.line_chart(filtered_df[['dteday','cnt_sales']].set_index('dteday'))
    st.metric("Total Sales", int(filtered_df['cnt_sales'].sum()))

with tab4:
    st.subheader("Product View")
    st.write("Karena dataset tidak ada detail produk, bagian ini bisa dikembangkan.")
    st.write("Contoh: kita bisa lihat tren penjualan per musim dari data yang ada.")

   
    filtered_df['season'] = pd.cut(
        filtered_df['dteday'].dt.month,
        bins=[0,3,6,9,12],  
        labels=['Winter','Spring','Summer','Fall'],
        right=True,
        include_lowest=True
    )

   
    season_sales = filtered_df.groupby('season')['cnt_sales'].sum().reset_index()

  
    fig, ax = plt.subplots()
    ax.bar(season_sales['season'], season_sales['cnt_sales'], color="skyblue")
    ax.set_ylabel("Total Sales")
    ax.set_title("Sales by Season")
    st.pyplot(fig)
