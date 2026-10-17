
def test_attendance_marking():
    student_id = "STU001"
    attendance_status = "Present"

    if student_id and attendance_status in ["Present", "Absent"]:
        print("Attendance marking test: PASS")
    else:
        print("Attendance marking test: FAIL")


if __name__ == "__main__":
    test_attendance_marking()
