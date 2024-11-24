# Cyber Security Base course project 1

## Purpose

A very insecure web app for the University of Helsinki Cyber Security Base -course.
The point is to demonstrate common cyber security problems and their fixes.

## Description of vulnerabilities

> **_NOTE:_** More detailed description of problems coming soon.

I am using the 2021 OWASP Top Ten list.

LINK: https://github.com/VSinerva/csb-project-1

I am using the basic Django template, so no instructions are included.

FLAW 1:

Broken Access Control (Can delete another user's notes)

FLAW 2:

Cryptographic Failure (Weak/No password hashing)

FLAW 3:

SQL Injection (Unsanitized SQL query for search)

FLAW 4:

Identification and Authentication Failure (No password strength checks)

FLAW 5:

CSRF (No CSRF token for Delete)
