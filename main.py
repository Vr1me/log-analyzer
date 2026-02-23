from analyzer import LogAnalyzer
from pathlib import Path

log_path = Path(__file__).parent / "sample.log"

analyzer = LogAnalyzer(log_path)
errors, warnings = analyzer.count_errors()

print(f"Errors: {errors}")
print(f"Warnings: {warnings}")