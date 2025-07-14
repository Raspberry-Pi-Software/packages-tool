#!/usr/bin/env python3

#
## PI (S)O(FT)(W)ARE
# An official fork.

import os
import sys

def print_welcome_message():
    """Print the welcome message for PiSftw Daemon."""
    print("Welcome to PiSftw Daemon, the fast Raspberry dragon.")

def main():
    """Main entry point for the PiSftw daemon."""
    if len(sys.argv) > 1:
        if sys.argv[1] == "print-wlcm-msg":
            print_welcome_message()
        else:
            print(f"Unknown command: {sys.argv[1]}")
            print("Available commands:")
            print("  print-wlcm-msg    Print welcome message")
    else:
        print("PiSftw Daemon - Raspberry Pi Software Tool Helper")
        print("Usage: python3 pisftw.py <command>")

if __name__ == "__main__":
    main()
