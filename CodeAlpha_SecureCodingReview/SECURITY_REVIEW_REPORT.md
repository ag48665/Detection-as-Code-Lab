# Security Review Report

## Project Information

**Project:** Secure Coding Review  
**Language:** Python  
**Database:** SQLite  
**Reviewer:** Agata Gabara  
**Internship:** CodeAlpha Cyber Security Internship

---

# Executive Summary

This report presents the results of a security review performed on a vulnerable Python login application.

Several security vulnerabilities were identified, including SQL Injection, insecure password storage, missing input validation, and lack of brute-force protection.

The secure version of the application demonstrates recommended secure coding practices.

---

# Security Findings

## 1. SQL Injection

**Risk:** High

### Description
The application builds SQL queries using string formatting.

```python
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
```

### Impact

An attacker can manipulate the SQL query to bypass authentication or access sensitive data.

### Recommendation

Use parameterized SQL queries.

---

## 2. Plain Text Password Storage

**Risk:** High

### Description

Passwords are compared directly without encryption.

### Impact

If the database is compromised, all user passwords become immediately accessible.

### Recommendation

Store password hashes instead of plain-text passwords.

---

## 3. Missing Password Hashing

**Risk:** High

### Description

The application does not hash passwords before verification.

### Recommendation

Use SHA-256, bcrypt, Argon2, or PBKDF2.

---

## 4. Missing Input Validation

**Risk:** Medium

### Description

User input is accepted without validation.

### Recommendation

Validate username length and allowed characters before processing.

---

## 5. Poor Error Handling

**Risk:** Medium

### Description

The application does not handle database exceptions.

### Recommendation

Use try-except blocks and log errors securely.

---

## 6. Missing Authentication Protection

**Risk:** Medium

### Description

Unlimited login attempts are allowed.

### Recommendation

Implement account lockout or rate limiting.

---

## 7. Missing Security Logging

**Risk:** Low

### Description

Login attempts are not logged.

### Recommendation

Log failed login attempts for security monitoring.

---

# Overall Risk Assessment

| Vulnerability | Risk |
|---------------|------|
| SQL Injection | High |
| Plain Text Passwords | High |
| Missing Password Hashing | High |
| Input Validation | Medium |
| Error Handling | Medium |
| Authentication Protection | Medium |
| Security Logging | Low |

---

# Secure Coding Improvements

The secure version introduces:

- Parameterized SQL queries
- Password hashing (SHA-256)
- Hidden password input
- Input sanitization
- Improved code readability
- Better authentication process

---

# Conclusion

The vulnerable application contains several common security weaknesses that could lead to unauthorized access or data compromise.

The secure implementation follows secure coding principles and significantly reduces the attack surface by using parameterized queries, password hashing, and improved authentication practices.