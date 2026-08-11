
class WordGrid:

    def __init__(self, setAI, setBI):
        self.setA = setAI
        self.setB = setBI

    def generate(self):
        wordsA = self.generate_cells(sorted(self.setA, key=len))
        wordsB = self.generate_cells(sorted(self.setB, key=len))
        return self.html_template(wordsA, wordsB)

    def generate_cells(self, words):
        # Build 9 cells; each cell contains 3 words stacked vertically.
        # The 9 cells will later be formatted as 3 columns of 3 rows.
        result = []
        for j in range(9):
            col_words = words[3*j:3*j+3]  # 3 words in this cell
            col_html = [f"      <div class='word'>{w}</div>" for w in col_words]
            result.append(
                "    <div class='cell'>\n" +
                "\n".join(col_html) +
                "\n    </div>"
            )
        return "\n".join(result)

    def html_template(self, insert1, insert2):
        return f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>3x3x3 Word Grid</title>
  <style>
    .flow {{
      background: #eeeeee;
      border: 1px solid #ccc;
      display: grid;
      grid-template-columns: repeat(2, 1fr);
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(3, max-content);
      gap: 10px;
      width: fit-content;
      margin: 24px auto;
    }}
    .cell {{
      border: 1px solid #ccc;
      padding: 12px;
      background: #fafafa;
      display: flex;
      flex-direction: column; /* stack 3 words vertically */
      justify-content: center;
      min-height: 120px;
      text-align: center;
      font: 18px/1.3 system-ui, sans-serif;
      align-items: stretch;
    }}
    .word {{
      padding: 4px 0;
    }}
  </style>
</head>
<body>
  <main class=flow>
    <div class="grid">
{insert1}
    </div>
    <div class="grid">
{insert2}
    </div>
  </main>
</body>
</html>
"""


