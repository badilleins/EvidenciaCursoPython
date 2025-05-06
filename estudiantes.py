class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    pass

class FileEmpty(StudentsDataException):
    pass

def read_and_process_file(filename):
    student_data = {}

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            if not lines:  
                raise FileEmpty("The file is empty.")

            for line in lines:
                line = line.strip()
                if not line: 
                    continue

                parts = line.split()
                
                if len(parts) != 3:  
                    raise BadLine(f"Bad line format: {line}")

                first_name, last_name, points_str = parts

                try:
                    points = float(points_str)
                except ValueError:
                    raise BadLine(f"Invalid points value: {points_str} in line: {line}")

                full_name = f"{first_name} {last_name}"

                if full_name not in student_data:
                    student_data[full_name] = 0
                student_data[full_name] += points

    except FileNotFoundError:
        print("The file does not exist.")
        return None
    except FileEmpty as e:
        print(e)
        return None
    except BadLine as e:
        print(e)
        return None

    return student_data

def print_report(student_data):
    if student_data:
        sorted_data = sorted(student_data.items())

        for full_name, total_points in sorted_data:
            print(f"{full_name}    {total_points:.1f}")

def main():
    filename = input("Enter the name of the file: ")
    student_data = read_and_process_file(filename)

    if student_data:
        print_report(student_data)

if __name__ == "__main__":
    main()
