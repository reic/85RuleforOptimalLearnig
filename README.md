# 85%原則是最佳學習策略 (85% Rules for Optimal Learning)

這是一個 Python 工具，用來判斷英文文件是否符合自己的程度。本文參考的是 Nature Communication 文獻的一篇實作，文章相關的介紹可以參考 [最有效的學習策略：85%原則](https://twreic.blogspot.com/2020/07/85.html)

This is a Python Tool used to know if an English article is suitable for you. This is based the result of the aritcle [The Eighty Five Percent Rule for optimal learning](https://doi.org/10.1038/s41467-019-12552-4) published in Nature Commincation.

## 如何標記 How to mark the unknown word

本程式依據 Microsft Word 檔案不同格式做為判斷是否為不認識的單字，並會計算不認識的單字占總字數的比例，計算出意外率。當 1 - 意外率 < 85% 時，代表這一篇文章從文字的熟悉度來看，對你來說太難了。

在 Word 中，如何標記不熟悉的英文單字呢？ 本程式採用 雙重下底線，只需要選擇英文字，再透過 Ctrl-Shift-D 熱鍵，即可完成標記。

## 如何設置 How to configure

本程式為 Python 程式，需要額外安裝 nltk, python-docx 兩個模組，

- pip install nltk
- pip install python-docx

預設的 docx 檔案為 test.docx，不熟的英文單字會記錄在 wordlearn.txt 內。你也可以透過程式最下面的 options 的值，即可

```python
if __name__ == "__main__":
    #  filename 為 docx 的檔案名稱，預設為 test.docx
    #  output_filename 為輸出的檔案名稱，預設為 wordlearn.txt
    options = {'filename': "test.docx", 'output_filename': 'wordlearn.txt'}
```
