*** Settings ***
Resource   ../Keywords/book_depo_kw.robot

*** Test Cases ***
The user can search for a book
    Search Books  the fast 800
    Books are found  The Fast 800