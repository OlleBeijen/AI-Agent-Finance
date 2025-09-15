
import argparse
from ..config import AppConfig
from ..reporting.generate_weekly import generate_weekly_report

def main():
    parser = argparse.ArgumentParser(description="Creditnote Doctor CLI")
    parser.add_argument("--report", action="store_true", help="Genereer wekelijks rapport")
    args = parser.parse_args()
    cfg = AppConfig.load()
    if args.report:
        generate_weekly_report(cfg)

if __name__ == "__main__":
    main()
