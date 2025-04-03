# Password Strength Checker

A simple Python-based password strength checker using **regular expressions (regex)** to validate password security based on industry standards.

## Features
- **Password Strength Analysis**: Checks for length, uppercase, lowercase, numbers, and special characters.
- **Real-time Validation**: Provides immediate feedback on password strength.
- **Easy to Use**: Works via command-line input.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-strength-checker.git
   cd password-strength-checker
   ```

2. No additional dependencies required! Just ensure you have Python installed.

## Usage

Run the script and enter a password to check its strength:

```bash
python password_strength_checker.py
```

### Example

```
Enter your password: Password@123
Password Strength: Strong 💪
```

## Password Strength Criteria
- **Weak** ❌: Fails multiple checks (e.g., too short, missing special characters, etc.).
- **Medium** ⚡: Passes at least 3 of 5 checks.
- **Strong** 💪: Meets all security criteria.

## Security Notes
- Passwords are **not stored or logged**.
- All processing happens **locally**.


