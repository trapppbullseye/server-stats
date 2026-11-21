#!/usr/bin/env python3
"""Discord server stats display bot"""
import argparse
def main():
 p=argparse.ArgumentParser(description="Discord server stats display bot")
 p.add_argument("--version",action="store_true")
 args=p.parse_args()
 if args.version:print("server-stats v0.1.0");return
 print(f"[22:56] server-stats ready")
if __name__=="__main__":main()
