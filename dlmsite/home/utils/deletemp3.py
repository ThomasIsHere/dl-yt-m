import os
import after_response

@after_response.enable
def deleteMp3File(filePath):
    os.remove(filePath)