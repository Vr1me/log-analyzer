class LogAnalyzer:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def read_logs(self) -> list[str]:
        with open(self.filepath, "r") as file:
            return file.readlines()

    def count_errors(self) -> int:
        logs = self.read_logs()
        return sum("ERROR" in line for line in logs)

    def count_warnings(self) -> int:
        logs = self.read_logs()
        return sum("WARNING" in line for line in logs)
