# problem link: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem


# my solution:
def designerPdfViewer(h, word):
    height = 0
    for letter in word:
        ind = ord(letter) - ord('a')
        current_height = h[ind]
        if current_height > height:
            height = current_height
    return height * len(word) * 1
