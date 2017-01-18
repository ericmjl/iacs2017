pweave -f pandoc report.mdw
pandoc -s --mathjax report.md -o report.html -c style.css
