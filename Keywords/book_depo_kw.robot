*** Settings ***
Library  ../Model/BookDepoHome.py  Chrome
Library  ../Model/SearchResults.py  Chrome

*** Keywords ***
Open BookDepoHome Page
    Open

Close Pages
    Close

Search Books
    [Arguments]  ${bookTitle}
    enter book name  ${bookTitle}
    search book

Books are found
     [Arguments]  ${bookTitle}
     ${found}=  Get found books  ${bookTitle}
     Should Be True  ${found}
