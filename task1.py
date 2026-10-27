INPUT:
    applicants
    aggregate_min
    subject_min
    attendance_min
    income_max
    scholarship_slots

eligible = []
rejected = []

FOR each applicant IN applicants:
    IF application data is invalid:
        record rejection: "Invalid or incomplete data"

    ELSE IF aggregate < aggregate_min:
        record rejection: "Aggregate below minimum"

    ELSE IF any subject score < subject_min:
        record rejection: "Subject minimum not met"

    ELSE IF attendance < attendance_min:
        record rejection: "Attendance below minimum"

    ELSE IF family_income > income_max:
        record rejection: "Income exceeds limit"

    ELSE:
        add applicant to eligible

SORT eligible BY:
    aggregate DESCENDING,
    attendance DESCENDING,
    lowest_subject_score DESCENDING,
    family_income ASCENDING,
    verified_application_id ASCENDING

FOR each applicant IN eligible:
    assign rank

    IF rank <= scholarship_slots:
        status = "Selected"
    ELSE:
        status = "Waitlisted"

OUTPUT:
    selected applicants
    waitlisted applicants
    rejected applicants with reasons
    ranking and audit report
