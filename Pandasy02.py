# Pandasy02.py
# Maciej Kuśnierz
# Julian Kwiatkowski
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import argparse


def generate_time_series(n, periods, start_date="1/1/2020"):
    """Generuje i zwraca serię czasową."""
    ts = pd.Series(np.random.randn(n), index=pd.date_range(start_date, periods=periods))
    return ts.cumsum()


def generate_dataframe(n, periods, columns, start_date="1/1/2020"):
    """Generuje i zwraca DataFrame z losowymi danymi."""
    df = pd.DataFrame(np.random.randn(n, len(columns)),
                      index=pd.date_range(start_date, periods=periods),
                      columns=columns)
    return df.cumsum()


def plot_verbose(fig, title, verbose_level, min_level=1, save_path=None):
    """Wyświetla wykres w zależności od poziomu szczegółowości."""
    if verbose_level >= min_level:
        plt.title(title)
        plt.show()
    if save_path:
        plt.savefig(save_path)
    plt.close()


def analyze_and_plot(n, periods, verbose_level=1):
    """Tworzy i wyświetla wykresy zależnie od parametrów."""
    # 1. Seria czasowa
    ts = generate_time_series(n, periods)
    plt.figure()
    ts.plot()
    plot_verbose(plt, "Seria czasowa (cumsum)", verbose_level, 1, "ts_plot.png")

    # 2. DataFrame z 4 kolumnami (A, B, C, D)
    df = generate_dataframe(n, periods, list("ABCD"))
    plt.figure()
    df.plot()
    plot_verbose(plt, "DataFrame A, B, C, D (cumsum)", verbose_level, 2, "df_plot.png")

    # 3. DataFrame z A (indeks) i B, C
    df3 = pd.DataFrame(np.random.randn(n, 2), columns=["B", "C"]).cumsum()
    df3["A"] = pd.Series(list(range(n)))
    plt.figure()
    df3.plot(x="A", y="B")
    plot_verbose(plt, "Wykres B względem A", verbose_level, 2, "df3_plot.png")

    # 4. Wykres słupkowy (11. wiersz)
    plt.figure()
    df.iloc[10].plot(kind="bar")
    plot_verbose(plt, "Wykres słupkowy (wiersz 11)", verbose_level, 3, "bar_plot.png")

    # 5. Wykres kołowy (11. wiersz z nieujemnych danych)
    df_pie = pd.DataFrame(np.random.rand(n, 4), columns=list("ABCD")).cumsum()
    plt.figure()
    df_pie.iloc[10].plot(kind="pie")
    plot_verbose(plt, "Wykres kołowy (wiersz 11)", verbose_level, 3, "pie_plot.png")


if __name__ == "__main__":
    # Konfiguracja argparse
    parser = argparse.ArgumentParser(description="Generowanie i wizualizacja losowych danych z Pandas")
    parser.add_argument("-n", type=int, default=1000, help="Liczba punktów danych (np. 1000)")
    parser.add_argument("-p", "--periods", type=int, default=1000, help="Liczba okresów dla dat (np. 1000)")
    parser.add_argument("-v", "--verbose", action="count", default=1,
                        help="Poziom szczegółowości (więcej 'v' = więcej wykresów)")

    args = parser.parse_args()

    # Wykonanie analizy i wizualizacji
    analyze_and_plot(args.n, args.periods, args.verbose)