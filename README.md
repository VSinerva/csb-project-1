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
> ADD EXACT SOURCE LINK

(Broken Access Control) Right now, the notes are identified and deleted with a simple sequential ID.
This makes it trivial for a logged in user to delete notes from other users.
The malicious user simply needs to edit the client-side URL of their POST request.

The issue can easily be fixed by adding the commented out ownership check before deleting a note.
The check compares the logged in user to the owner of the note, and only deletes the note if they match.
This should never cause a problem for a normal user, but it makes sure that the note being deleted
belongs to the logged in user.

FLAW 2:
> ADD EXACT SOURCE LINK

Cryptographic Failure (Weak/No password hashing)

FLAW 3:
> ADD EXACT SOURCE LINK

SQL Injection (Unsanitized SQL query for search)

FLAW 4:
> ADD EXACT SOURCE LINK

(Identification and Authentication Failures) As is, the application performs no checks for weak passwords.
This makes users more vulnerable to attacks based on trying common and weak passwords, escpecially if the password database gets leaked (See also flaws 2 and 3).

The fix for this issue is to perform server-side validation on new passwords, and checking that they are reasonable.
Django includes a simple built-in validator which checks that the password has a minimum length (default 8, in this app 10), is not too similar to the username, is not a common password (20000 password list) and is not purely numeric.
These checks are implemented in the commented out code, and would significantly improve the situation.

FLAW 5:
> ADD EXACT SOURCE LINK

CSRF (No CSRF token for Delete)
