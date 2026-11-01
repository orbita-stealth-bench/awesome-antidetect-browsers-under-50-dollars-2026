#!/usr/bin/env python3
"""Awesome Antidetect Fleet TCO Calculator 2026 (GoLogin vs AdsPower vs MoreLogin vs Multilogin)."""
import argparse

BENCHMARK_FLEET = {
    "gologin": {"profiles": 100, "annual_monthly": 24.50, "seats": 1},
    "adspower": {"profiles": 100, "annual_monthly": 40.00, "seats": 1},
    "morelogin": {"profiles": 100, "annual_monthly": 40.00, "seats": 2},
    "multilogin": {"profiles": 100, "annual_monthly": 99.00, "seats": 1}
}

def calculate():
    print("=" * 70)
    print("Awesome Antidetect Fleet TCO Matrix (100 Profiles / Annual Plans)")
    print("=" * 70)
    print(f"{'Provider':<15} {'Profiles':<10} {'Monthly Equiv':<15} {'Annual TCO':<15} {'Rank'}")
    print("-" * 70)
    sorted_items = sorted(BENCHMARK_FLEET.items(), key=lambda x: x[1]["annual_monthly"])
    for rank, (name, data) in enumerate(sorted_items, start=1):
        rate = data["annual_monthly"]
        annual = rate * 12.0
        print(f"{name.capitalize():<15} {data['profiles']:<10} ${rate:.2f}/mo{'':<7} ${annual:.2f}/yr{'':<6} #{rank}")
    print("=" * 70)
    return sorted_items

if __name__ == "__main__":
    calculate()
