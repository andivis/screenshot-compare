# pip packages
import imgcompare

class Images:
    def differencePercentage(self, file1, file2):
        return imgcompare.image_diff_percent(file1, file2)