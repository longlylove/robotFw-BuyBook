# robotFw-BuyBook

This is a demo project that uses a combination of robot framework \ web driver \ python to drive UI test on a website.

The basic test flow:
- navigate to https://www.bookdepository.com
- search for a book title
- verify that the search result is returned

Basic setup and running instructions (applicable for Linux \ Windows)

Prerequisites:
- install python 3.x 
- install pip
- via pip, install robotframework (verify that after installation robot library is available under /Python3x/Lib/site-packages)
- via pip, install selenium (verify that after installation SeleniumLibrary \ Selenium2Library packages is available under /Python3x/Lib/site-packages)

How-to:
- clone this repo to your local folder (ie. C:\Dev\robotFw-BuyBook)
- from your command line (ie. powershell or PS), go to your local folder
- check your pythonpath ie. on PS, run python -c "import sys; print(sys.path)"
- export your local path to pythonpath ie. on PS, run $env:PYTHONPATH = "C:\Dev\robotFw-Demo\"
- to execute the test with active internet connection, run 'robot .' or 'robot <your local folder>'
- verify chrome is open and test is executed and test shown as PASS

Troubleshoot test run:
- Once robot tests are run, log file and test reports are available in your local folder. Hence look for following files
  + output.xml
  + log.html
  + report.html

Note:
- Python complied files (.pyc) are generated automatically under each folder where .py files are stored


