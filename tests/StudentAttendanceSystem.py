import datetime

class AttendanceSystem:
    def __init__(self):
        self.students = set()
        self.attendance_records = {}

    def add_student(self, student_name):
        if not student_name.strip():
            print("\n[Error] Student name cannot be empty.")
            return
            
        if student_name in self.students:
            print(f"\n[Info] Student '{student_name}' already exists.")
        else:
            self.students.add(student_name)
            print(f"\n[Success] Student '{student_name}' added successfully.")

    def mark_attendance(self, date_str, student_name, status):
        if student_name not in self.students:
            print(f"\n[Error] Student '{student_name}' not found. Please add the student first.")
            return

        status = status.upper()
        if status not in ['P', 'A']:
            print("\n[Error] Invalid status. Please use 'P' for Present or 'A' for Absent.")
            return

        if date_str not in self.attendance_records:
            self.attendance_records[date_str] = {}

        self.attendance_records[date_str][student_name] = status

    def view_student_attendance(self, student_name):
        if student_name not in self.students:
            print(f"\n[Error] Student '{student_name}' not found.")
            return

        print(f"\n--- Attendance Record for {student_name} ---")
        found_records = False
        for date, records in sorted(self.attendance_records.items()):
            if student_name in records:
                status = "Present" if records[student_name] == 'P' else "Absent"
                print(f"  Date: {date}   |   Status: {status}")
                found_records = True

        if not found_records:
            print(f"  No attendance records found for '{student_name}'.")
        print("------------------------------------------")

    def view_daily_attendance(self, date_str):
        if date_str not in self.attendance_records:
            print(f"\n[Info] No attendance records found for the date: {date_str}")
            return

        print(f"\n--- Daily Attendance for {date_str} ---")
        records = self.attendance_records[date_str]
        for student, status in sorted(records.items()):
            status_text = "Present" if status == 'P' else "Absent"
            print(f"  Student: {student:<20} | Status
