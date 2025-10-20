# AccuKnox User Management Tests

This project automates the **User Management E2E flow** in [OrangeHRM Demo App](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login) using **Playwright (Python)**.

---

## Test Scenarios Covered
1. Verify Admin module navigation  
2. Verify validation messages when saving without input  
3. Verify Admin can add a new user  
4. Verify Admin can search the newly created user  
5. Verify Admin cannot search with invalid data  
6. Verify Admin can edit user details  

---

## Project Setup

### 1- Clone the repository
```bash
git clone https://github.com/mdntarif/AccuKnox-user-management-tests.git
cd AccuKnox-user-management-tests
```

### 2- Install dependencies
```bash
pip install -r requirements.txt
```

### 3- Install Playwright browsers
```bash
playwright install
```

### 4- Run the Tests

To execute all test cases:
```bash
pytest test_user_management.py
```

Or run a single test:
```bash
pytest -k "test_add_new_user"
```

### Playwright Version

Playwright Python v1.42.0

### Folder Structure

```sql
AccuKnox-user-management-tests/
│
├── admin_page.py
├── login_page.py
├── test_user_management.py
├── requirements.txt
└── README.md
```

### Author

Md Tarif
<br>
Automation QA | Python + Playwright


