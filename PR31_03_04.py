class FileUtils:
    @staticmethod
    def count_lines(file_path):
        try:
            with open(file_path, 'r') as file:
                line_count = sum(1 for line in file)
            return line_count
        except FileNotFoundError:
            print("No file")
            return None
        except Exception as e:
            print("Error", e)
            return None

file_path = "text.txt"
count_lines = FileUtils.count_lines(file_path)

print("Lines: ", count_lines)

