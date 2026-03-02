# System Architecture

Raw student data is entered in Google Sheets.

Apps Script automation:
- validates scores
- cleans data
- moves valid data to CleanData sheet

Dashboard:
- calculates KPIs
- displays performance metrics

Python pipeline:
- reads dataset
- generates analytics report
- creates visualization

Flow:
RawData → CleanData → Dashboard → Python Analytics
