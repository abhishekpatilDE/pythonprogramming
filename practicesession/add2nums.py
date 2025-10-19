#Add two numbers
#!/usr/bin/env python3
"""practicesessions.py

Simple utility to add two numbers. Supports three modes:
- Demo mode: `--demo` shows example additions
- CLI mode: pass two numbers as positional arguments
- Interactive mode: prompts the user for two numbers

The script accepts integers or floats.
"""

from __future__ import annotations
import argparse
import sys


def add(a: float, b: float) -> float:
      return a + b


def demo() -> None:
      cases = [
            (1, 2),
            (3.5, 2.2),
            (-5, 10),
            (0, 0),
      ]
      print("Demo additions:")
      for x, y in cases:
            print(f"  {x} + {y} = {add(x, y)}")


def parse_num(s: str) -> float:
      """Parse a string as int or float. Raise argparse.ArgumentTypeError on failure."""
      s = s.strip()
      try:
            return int(s)
      except ValueError:
            try:
                  return float(s)
            except ValueError:
                  raise argparse.ArgumentTypeError(f"not a number: {s!r}")


def interactive_prompt() -> tuple[float, float]:
      while True:
            try:
                  a = input("Enter first number: ").strip()
                  b = input("Enter second number: ").strip()
                  return parse_num(a), parse_num(b)
            except (KeyboardInterrupt, EOFError):
                  print("\nInput cancelled.")
                  sys.exit(1)
            except Exception as exc:
                  print("Invalid input:", exc)
                  print("Please try again.\n")


def main(argv: list[str] | None = None) -> int:
      parser = argparse.ArgumentParser(
            prog="practicesessions.py",
            description="Add two numbers (interactive, CLI args, or --demo)",
      )
      parser.add_argument("numbers", nargs="*", type=parse_num, help="Two numbers to add")
      parser.add_argument("--demo", action="store_true", help="Run demo cases")
      args = parser.parse_args(argv)

      if args.demo:
            demo()
            return 0

      if len(args.numbers) == 2:
            a, b = args.numbers
            print(f"The sum is: {add(a, b)}")
            return 0

      # Fallback to interactive mode
      a, b = interactive_prompt()
      print("The sum is:", add(a, b))
      return 0


if __name__ == "__main__":
      raise SystemExit(main())