import csv
import sys

filename = sys.argv[1]
mode = sys.argv[2]

start_a = "<div class=\"article\">"
start_p = "<div class=\"poster\">"
end = """</div>
"""

main = """  <a link=\"IWQC_paper_{paper_num}\">
  <span class=\"authors\">
    {authors}
  </span><br/>
  <span class=\"title\">
    {title}
  </span></br>"""

abstract="""  <div class=\"abstract\">
    <b>Abstract:</b>
    {abstract}
  </div>"""

links = """  <div class=\"links\">
    [<a href=\"papers/IWQC2024_paper_{paper_num}.pdf\">Paper PDF</a>]
    <!-- [<a href=\"slides/404_nofound.pdf\">Slides</a>] -->
  </div>"""

with open(filename) as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        if mode == row["Decision"] :
            if mode == "a" :
                print("<!-- record starts -->")
                print(start_a)
                print(main.format(
                    authors=row["Authors"],
                    title=row["Title"],
                    paper_num=row["Num"]
                ))
                print(abstract.format(abstract=row["Abstract"]))
                if row["paper"] == "True" :
                    print(links.format(paper_num=row["Num"]))
                print(end)
            if mode == "p" :
                print("<!-- record starts -->")
                print(start_p)
                print(main.format(
                    authors=row["Authors"],
                    title=row["Title"],
                    paper_num=row["Num"]
                ))
                print(end)
        


print("<!-- DONE -->")

