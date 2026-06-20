# CodeAlpha_SecureCodingReview
Security Analysis Report
Project: Secure Coding Review  
1. Code Reviewed: login_vulnerable.py
2. Identified Vulnerabilities:  
Hardcoded Credentials: Username and password are directly written in the code, which is a significant security risk.
Plain Text Passwords: Passwords are compared in plain text instead of using secure hashing algorithms.
Lack of Rate Limiting: There is no mechanism to prevent brute-force attacks by limiting login attempts.
3. Remediation Recommendations:
Remove hardcoded credentials and use secure environment variables.
Implement password hashing using libraries like bcrypt.
Add account lockout policies after multiple failed login attempts
