# Cyber Security Base course project 1

## Purpose

A very insecure web app for the University of Helsinki Cyber Security Base -course.
The point is to demonstrate common cyber security problems and their fixes.

## Description of vulnerabilities

> **_NOTE:_** More detailed description of problems coming soon.

I am using the 2021 OWASP Top Ten list.

LINK: https://github.com/VSinerva/csb-project-1

I am using the basic Django template, so no instructions are included.
The user accounts `test1:test1` and `test2:test2` have been added to the database for testing purposes.

FLAW 1:
> ADD EXACT SOURCE LINK

(Broken Access Control) Right now, the notes are identified and deleted with a simple sequential ID, with no ownership or permission checks.
This makes it trivial for any logged in user to delete notes from other users.
The malicious user simply needs to edit the client-side URL of their POST request.

The issue can easily be fixed by adding the commented out ownership check before deleting a note.
The check compares the logged in user to the owner of the note, and only deletes the note if they match.
This should never cause a problem for a normal user, but it makes sure that the note being deleted
belongs to the logged in user.


FLAW 2:
> ADD EXACT SOURCE LINK

(Cryptographic Failures) The current settings for the application has unsalted MD5 as the password hashing algorithm.
This in insecure for several reasons.
MD5 is considered broken for cryptographic purposes, and has been for years, because modern hardware can check guessed passwords too quickly.
This is made worse by the lack of a salt (a unique random string added to each users password before hashing), because all users with the same password will have the same hash.
With these settings, the hashing is so broken that you can type the hash for a weak password (See also flaws 3 and 4) into a search engine and get the password!

The fix is to use a secure hashing algorithm, like PBKDF2 or Argon2 (both with the appropriate parameters).
This will make the hashes much harder to break for any reasonably strong password.
The algorithms mentioned above have been commented out in the code.
If users already exist with weakly hashed passwords, a more complicated migration (re-hash on login or storing hashes of the MD5 hashes) is needed.

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

(Security Misconfiguration) The current project settings set debug features to always be on, and contains the Django secret key in the public repository.
Django in debug mode shows detailed stack traces etc. when errors occur, which could reveal internal information.
The secret key is crucial for e.g. session security, so should absolutely never be posted publicly, as it has been here.

The solution to both of these problems is to load the values from environment variables at runtime.
This, in combination with e.g. a .env file, helps to make sure that the correct settings and keys are in use in development and in production.
This fix is implemented in the commented out code.
