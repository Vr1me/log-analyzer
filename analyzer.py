class LogAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path

    def count_errors(self):
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()

            error_count = sum(1 for line in lines if "ERROR" in line)
            warning_count = sum(1 for line in lines if "WARNING" in line)

            return error_count, warning_count

        except FileNotFoundError:
            print("Log file not found.")
            return 0, 0