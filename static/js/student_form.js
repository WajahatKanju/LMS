document.addEventListener('DOMContentLoaded', () => {
    const schoolField = document.querySelector('#id_student-school');
    const gradeField = document.querySelector('#id_student-grade');
    const genderField = document.querySelector('#id_student-gender');
    const rollNo = document.getElementById("id_student-roll_no");
    const admissionNo = document.getElementById("id_student-admission_no");
    const studentCnic = document.getElementById("id_student-student_cnic");
    const fatherCnic = document.getElementById("id_student-father_cnic")
    const mobile = document.getElementById("id_student-mobile")

    studentCnic.value = '15604-'
    fatherCnic.value = '15604-'
    mobile.value = '0333-'


    // add event listener to roll_no field
    rollNo.addEventListener("input", function () {
        // check if the input value is less than or equal to 0
        if (this.value <= 0) {
            this.value = 1; // clear the input value
        }
    });

    // add event listener to admission_no field
    admissionNo.addEventListener("input", function () {
        // check if the input value is less than or equal to 0
        if (this.value <= 0) {
            this.value = 1; // clear the input value

        }
    });

    function numericStringMask(str, mask) {
        if (!mask) return str;

        const numeric = str.replaceAll(/[^\d]/g, '');

        let idx = 0;

        const formated = mask.split('').map(el => {
            if (el === '#') {
                el = numeric[idx];
                idx++;
            }
            return el;
        });

        return formated.join('');
    }

    const cnicFields = [studentCnic, fatherCnic];
    cnicFields.forEach(function (inputField) {
        inputField.addEventListener("input", function (event) {
            // Get the current value of the input field
            const actualValue = inputField.value.replaceAll('-', '');
            if (actualValue.length === 5) {
                inputField.value = numericStringMask(inputField.value, '#####-')
            } else if (actualValue.length === 13) {

                inputField.value = numericStringMask(inputField.value, '#####-#######-#');
            }
            if (actualValue.length >= 11) {
                if (inputField.classList.contains("is-invalid")) {
                    // If it does, remove the class 'is-invalid'
                    inputField.classList.remove("is-invalid");
                }
            }

        });
        inputField.addEventListener('focusout', function () {
            const warning = 'Warning: Less than 13';
            const warningElem = inputField.nextElementSibling;

            if (inputField.value.replaceAll('-', '').length !== 13) {
                if (!warningElem || !warningElem.classList.contains('text-warning')) {
                    // insert a new warning
                    const newWarningElem = document.createElement('span');
                    newWarningElem.className = 'text-warning';
                    newWarningElem.innerHTML = '<strong><small>' + warning + '</small></strong>';
                    inputField.parentNode.insertBefore(newWarningElem, inputField.nextSibling);
                }
            } else {
                if (warningElem && warningElem.classList.contains('text-warning')) {
                    inputField.parentNode.removeChild(warningElem);
                }
            }
        });
    });


    mobile.addEventListener('input', function () {
        mobile.value = numericStringMask(mobile.value, '####-#######')
    })

    mobile.addEventListener('focusout', function () {
        const warning = 'Warning: Less than 11';
        const warningElem = mobile.nextElementSibling;

        if (mobile.value.replaceAll('-', '').length < 11) {
            if (!warningElem || !warningElem.classList.contains('text-warning')) {
                // insert a new warning
                const newWarningElem = document.createElement('span');
                newWarningElem.className = 'text-warning';
                newWarningElem.innerHTML = '<strong><small>' + warning + '</small></strong>';
                mobile.parentNode.insertBefore(newWarningElem, mobile.nextSibling);
            }
        } else {
            if (warningElem && warningElem.classList.contains('text-warning')) {
                mobile.parentNode.removeChild(warningElem);
            }
        }
    });


    rollNo.addEventListener("input", function () {
        admissionNo.value = rollNo.value;
    });

    schoolField.addEventListener('change', () => {
        const schoolId = schoolField.value;
        if (schoolId) {
            const xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function () {
                if (this.readyState === 4 && this.status === 200) {
                    const grades = JSON.parse(this.responseText);
                    gradeField.innerHTML = '';
                    for (const key in grades) {
                        if (grades.hasOwnProperty(key)) {
                            const option = document.createElement('option');
                            option.text = grades[key].name;
                            option.value = key;
                            gradeField.add(option);
                        }
                    }
                }
            };
            xhr.open('GET', `/get-grades/${schoolId}/`, true);
            xhr.send();
        }
    });

    function saveFilters(schoolId, classId, gender) {
        localStorage.setItem('schoolId', schoolId);
        localStorage.setItem('classId', classId);
        localStorage.setItem('gender', gender);
    }

// Load school and class filters from local storage
    function loadFilters() {
        const schoolId = localStorage.getItem('schoolId');
        const classId = localStorage.getItem('classId');
        const gender = localStorage.getItem('gender');

        if (schoolId) {
            document.querySelector('#id_student-school').value = schoolId;
        }
        if (classId) {
            document.querySelector('#id_student-grade').value = classId;
        }
        if (gender) {
            document.querySelector('#id_student-gender').value = gender;
        }
    }


// Attach event listener to school and class filters
    const Filters = [schoolField, gradeField, genderField];

    Filters.forEach((filter) => {
        filter.addEventListener('change', function () {
            const schoolId = document.querySelector('#id_student-school').value;
            const classId = document.querySelector('#id_student-grade').value;
            const gender = document.querySelector('#id_student-gender').value;
            saveFilters(schoolId, classId, gender);
        });
    });

    document.querySelector('#id_student-grade').addEventListener('change', function () {
        const schoolId = document.querySelector('#id_student-school').value;
        const classId = this.value;
        const gender = document.querySelector('#id_student-gender').value;
        saveFilters(schoolId, classId, gender);
    });

    loadFilters();


// Retrieve previously submitted values from local storage
    const storedRollNo = localStorage.getItem("rollNo");
    const storedAdmissionNo = localStorage.getItem("admissionNo");

// If the values exist in local storage, set the form field values to them
    if (storedRollNo) {
        rollNo.value = storedRollNo;
    }
    if (storedAdmissionNo) {
        admissionNo.value = storedAdmissionNo;
    }

// Add an event listener to the form for submission
    const form = document.querySelector("form");

    form.addEventListener("submit", function (event) {
        // Prevent the default form submission behavior

        // Get the form field values
        const rollNoValue = rollNo.value;
        const admissionNoValue = admissionNo.value;

        // Store the form field values in local storage
        localStorage.setItem("rollNo", rollNoValue);
        localStorage.setItem("admissionNo", admissionNoValue);

        // Create a span element to show the previously submitted values
        const storedRollNo = localStorage.getItem("rollNo");
        const storedAdmissionNo = localStorage.getItem("admissionNo");

        // Add a span element to show the previously submitted rollNo value
        const rollNoSpan = document.createElement("span");
        rollNoSpan.innerText = `Previously submitted Roll No: ${storedRollNo}`;

        // Remove any existing span element before adding the new one
        const existingRollNoSpan = rollNo.parentElement.querySelector("span");
        if (existingRollNoSpan) {
            existingRollNoSpan.remove();
        }

        rollNo.parentElement.insertBefore(rollNoSpan, rollNo);

        // Add a span element to show the previously submitted admissionNo value
        const admissionNoSpan = document.createElement("span");
        admissionNoSpan.innerText = `Previously submitted Admission No: ${storedAdmissionNo}`;

        // Remove any existing span element before adding the new one
        const existingAdmissionNoSpan = admissionNo.parentElement.querySelector("span");
        if (existingAdmissionNoSpan) {
            existingAdmissionNoSpan.remove();
        }

        admissionNo.parentElement.insertBefore(admissionNoSpan, admissionNo);
        form.submit()
    });


});


// Load filters on page load
