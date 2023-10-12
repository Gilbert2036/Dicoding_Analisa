import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
sns.set(style='dark')

def workingday_df(df):
    workingday = df.groupby(by='workingday').cnt.sum().reset_index()
    workingday.rename(columns={'cnt':'sum'}, inplace=True)

    return workingday.sort_values(by='sum', ascending=False)


def weathersit_df(df):
    weathers = df.groupby(by='weathersit').cnt.sum().reset_index()
    weathers.rename(columns={'cnt':'sum'}, inplace=True)

    return weathers.sort_values(by='sum', ascending=False)


def hour_df(df):
    hours = df.groupby(by='hr').cnt.sum().reset_index()
    hours.rename(columns={'cnt':'sum'}, inplace=True) 

    return hours.sort_values(by='sum', ascending=False)

def sidebar(df):
    df['dteday'] = pd.to_datetime(df['dteday'])
    min = df['dteday'].min()
    max = df['dteday'].max()

    with st.sidebar:
        st.image('https://static.vecteezy.com/system/resources/previews/000/421/581/original/vector-bicycle-icon.jpg')
        def on_change():
            st.session_state.date = date

        date = st.date_input(
            label="Pilih Rentang Waktu",
            min_value=min,
            max_value=max,
            value=[min, max],
            on_change=on_change
        )
    return date

def workingday_chart(df):
    st.subheader('Penggunaan Bike-Sharing berdasarkan Working Day')
    df['sum'] = df['sum'] / 1000
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
        x='workingday',
        y='sum',
        data = df,
        ax=ax
    )
    ax.set_title("Nuber of Bike-Sharing by Working Day \n in thousand", loc="center", fontsize=30)
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    ax.tick_params(axis="x", labelsize=35)
    ax.tick_params(axis="y", labelsize=30)
    st.pyplot(fig)


def weathersit_chart(df):
    st.subheader('Penggunaan Bike-Sharing berdasarkan Weathersit')
    df['sum'] = df['sum'] / 1000
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
        x='sum',
        y='weathersit',
        data = df,
        ax=ax
    )
    ax.set_title("Nuber of Bike-Sharing by Weathersit \n in thousand", loc="center", fontsize=30)
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    ax.tick_params(axis="x", labelsize=35)
    ax.tick_params(axis="y", labelsize=30)
    st.pyplot(fig)


def hour_chart(df):
    st.subheader('Penggunaan Bike-Sharing berdasarkan Hour')
    df['sum'] = df['sum'] / 1000
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
        x='hr',
        y='sum',
        data = df,
        ax=ax
    )
    ax.set_title("Nuber of Bike-Sharing by hour \n in thousand", loc="center", fontsize=30)
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    ax.tick_params(axis="x", labelsize=35)
    ax.tick_params(axis="y", labelsize=30)
    st.pyplot(fig)

df = pd.read_csv('all_data.csv')

date = sidebar(df)

if(len(date) == 2):
    main_df = df[(df["dteday"] >= str(date[0])) & (df["dteday"] <= str(date[1]))]
else:
    main_df = df[(df["dteday"] >= str(st.session_state.date[0])) & (df["dteday"] <= str(st.session_state.date[1]))]

st.header(':sparkles: Dashboard Bike-Sharing :sparkles:')

working_day_df = workingday_df(main_df)
workingday_chart(working_day_df)

weathersits_df = weathersit_df(main_df)
weathersit_chart(weathersits_df)

hour_df = hour_df(main_df)
hour_chart(hour_df)