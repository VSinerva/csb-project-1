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

Identification and Authentication Failure (No password strength checks)

FLAW 5:
> ADD EXACT SOURCE LINK

CSRF (No CSRF token for Delete)
